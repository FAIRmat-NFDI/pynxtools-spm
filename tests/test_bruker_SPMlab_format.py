"""Tests for the Bruker SPMLab (.FLT) AFM format.

Covers the whole path a .FLT file takes through the reader: the ASCII header
reader and value/unit splitter of ``FltBruker``, its ``parse`` output, the
selection of that parser by ``SPMParser``, the SPMLab timestamp handling of
``BrukerFltAFM`` and the dispatch performed by ``SPMReader``.
"""

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pytest

from pynxtools_spm.parsers.bruker_flt import (
    DATA_OFFSET,
    HEADER_CHUNK_SIZE,
    FltBruker,
)


# ---------------------------------------------------------------------------
# BrukerFltAFM — conversion of a real SPMLab .FLT file
# ---------------------------------------------------------------------------

TEST_DATA_DIR = Path(__file__).parent / "data"
FLT_DATA_DIR = TEST_DATA_DIR / "bruker" / "afm" / "flt_default_config"
FLT_RAW_FILE = next(FLT_DATA_DIR.glob("*.flt"), None) or next(
    FLT_DATA_DIR.glob("*.FLT"), None
)
assert FLT_RAW_FILE is not None, f"no .flt file found in {FLT_DATA_DIR}"

ENTRY = "/ENTRY[entry]"
# Read straight from the reference file's ASCII header: ResolutionX/Y=512.
FLT_RESOLUTION = 512


# ---------------------------------------------------------------------------
# BrukerFltAFM — SPMLab timestamp parsing
# ---------------------------------------------------------------------------


class TestBrukerFltTimestamp:
    """SPMLab writes 'Mon.DD.YYYY HH:MM:SS', which is not ISO 8601."""

    RAW_PATH = "/Height/meta/CreationTime"
    END_DICT = {"raw_path": RAW_PATH}

    def _make_formatter(self, raw_value):
        from pynxtools_spm.nxformatters.bruker.bruker_flt_afm import BrukerFltAFM

        formatter = BrukerFltAFM.__new__(BrukerFltAFM)
        formatter.raw_data = {self.RAW_PATH: raw_value}
        formatter.template = {}
        return formatter

    @pytest.mark.parametrize(
        "raw_value, expected",
        [
            ("Jun.17.2026 08:03:43", "2026-06-17T08:03:43"),
            ("Jan.1.2020 00:00:00", "2020-01-01T00:00:00"),
            ("DEC.31.1999 23:59:59", "1999-12-31T23:59:59"),
            # Surrounding whitespace is tolerated.
            ("  Mar.05.2024 12:30:00  ", "2024-03-05T12:30:00"),
        ],
    )
    def test_valid_timestamps(self, raw_value, expected):
        formatter = self._make_formatter(raw_value)
        formatter._set_start_end_time(self.END_DICT, "/entry", "start_time")
        assert formatter.template["/entry/start_time"] == expected

    @pytest.mark.parametrize(
        "raw_value",
        [
            "",
            "   ",
            "not a date",
            "2026-06-17T08:03:43",  # already ISO, not the SPMLab spelling
            "Jun.17.2026",  # time missing
            "Xyz.17.2026 08:03:43",  # unknown month
            None,
            12345,
        ],
    )
    def test_unparsable_timestamps_write_nothing(self, raw_value):
        """A bad stamp is skipped rather than raising or writing a bad value."""
        formatter = self._make_formatter(raw_value)
        formatter._set_start_end_time(self.END_DICT, "/entry", "start_time")
        assert "/entry/start_time" not in formatter.template


# ---------------------------------------------------------------------------
# FltBruker — splitting 'value unit' metadata entries
# ---------------------------------------------------------------------------


class TestFltBrukerSplitValueAndUnit:
    """SPMLab appends the unit to the value, e.g. 'SetPoint=0.030000 V'.

    A '/@unit' entry must only be written when the trailing token really is a
    unit, so the splitter has to return None for everything else.
    """

    @pytest.mark.parametrize(
        "raw_value, expected",
        [
            # Plain unit tokens straight out of the reference header.
            ("1.0000 µm", ("1.0000", "µm")),
            ("0.030000 V", ("0.030000", "V")),
            ("0.0 °", ("0.0", "°")),
            # Compound units keep their solidus.
            ("1.0000 µm/s", ("1.0000", "µm/s")),
            ("0.7731 µm/V", ("0.7731", "µm/V")),
            # Sign and exponent belong to the value, not to the unit.
            ("-1.5e-3 nm", ("-1.5e-3", "nm")),
            ("+2.5E+2 nm", ("+2.5E+2", "nm")),
            (".5 nm", (".5", "nm")),
            # Surrounding whitespace is stripped before matching.
            ("  2.5 nm  ", ("2.5", "nm")),
        ],
    )
    def test_value_and_unit_are_separated(self, raw_value, expected):
        assert FltBruker._split_value_and_unit(raw_value) == expected

    @pytest.mark.parametrize(
        "raw_value, expected",
        [
            # The parenthesised constant of a PID gain is dropped, so that the
            # gain stays a number. It carries no unit either.
            ("0.800000 (1000.000000)", "0.800000"),
            ("12.000000 (1200.000000)", "12.000000"),
            ("0.000000 (1000.000000)", "0.000000"),
            # Sign, exponent and a missing space in front of the parenthesis do
            # not change which half is the gain.
            ("-1.5e-3 (1200.000000)", "-1.5e-3"),
            ("1.0(1200.0)", "1.0"),
            # An unparsable parenthesis is left alone rather than guessed at.
            ("1.0 (auto)", "1.0 (auto)"),
            ("1.0 (1000.0", "1.0 (1000.0"),
        ],
    )
    def test_gain_keeps_only_the_gain_itself(self, raw_value, expected):
        """SPMLab appends a per loop constant to every gain, e.g.
        'GainP=0.800000 (1000.000000)'.

        Its meaning is undocumented (see 'nxformatters/bruker/README.md'), while
        'K_p'/'K_i'/'K_d' are NX_NUMBER, so only the leading float is kept.
        """
        value, unit = FltBruker._split_value_and_unit(raw_value)
        assert value == expected
        assert unit is None, f"{raw_value!r} must not be read as carrying a unit"

    @pytest.mark.parametrize(
        "raw_value",
        [
            # A second bare number is not a unit.
            "1.0 2.0",
            # Free text must survive untouched.
            "1D Line Fit",
            "Peak Force Tapping",
            "Jun.17.2026 08:03:43",
            "SIG_TOPO",
            "None",
            "TRUE",
            # A number on its own carries no unit.
            "512",
            "",
            "   ",
        ],
    )
    def test_values_without_a_unit_return_none(self, raw_value):
        value, unit = FltBruker._split_value_and_unit(raw_value)
        assert value == raw_value.strip() if raw_value.strip() else True
        assert unit is None, f"{raw_value!r} must not be read as carrying a unit"

    @pytest.mark.parametrize("raw_value", ["1.0 on", "3 off", "4 On/Off", "5 off/on"])
    def test_switch_states_are_not_units(self, raw_value):
        """'on'/'off' are states listed in UNIT_TO_SKIP, so the unit is blanked.

        An empty string rather than None, because the value *was* split off the
        state token and the caller still writes a (unitless) '/@unit' entry.
        """
        value, unit = FltBruker._split_value_and_unit(raw_value)
        assert unit == ""
        assert value == raw_value.split()[0]

    @pytest.mark.parametrize("raw_value", [None, 512, 1.5, np.zeros(2)])
    def test_non_string_values_are_passed_through(self, raw_value):
        """Only strings carry a trailing unit; arrays and numbers are returned as is."""
        value, unit = FltBruker._split_value_and_unit(raw_value)
        assert unit is None
        assert value is raw_value


# ---------------------------------------------------------------------------
# FltBruker — reading the ASCII header out of the binary file
# ---------------------------------------------------------------------------
#
# One flavour describes one complete file, identified by the vendor, the
# software that wrote it and its version. Support for a further version is
# added by appending a flavour to FLT_HEADER_FLAVORS / FLT_FILE_FLAVORS below,
# not by adding test functions: every test in this section is parametrized over
# those lists.


@dataclass(frozen=True)
class FltHeaderFlavor:
    """A complete FLT header together with the dict it must parse into."""

    vendor: str
    software: str
    version: str
    # Rendered header of one file. A separate flavour, rather than a fixture
    # per feature, so that a new writer version is a single new entry.
    header: bytes
    expected: dict[str, dict[str, str]]

    @property
    def id(self) -> str:
        return f"{self.vendor}-{self.software}-{self.version}"


# 'DataOffset' is written with a fixed width, so substituting the real header
# length for the placeholder cannot change that length.
_OFFSET_WIDTH = 8
_OFFSET_PLACEHOLDER = "0" * _OFFSET_WIDTH


def _build_flt_header(sections: dict[str, list[tuple[str, str] | str]]) -> bytes:
    """Render an SPMLab style INI header, CRLF terminated and cp1252 encoded.

    A '[Data Parameters]' section carrying the correct 'DataOffset' leads the
    header, as it does in a real export: 'DataOffset' is the byte position at
    which the binary raster starts, i.e. the length of the header itself, and
    the parser only looks for it in the first chunk it reads.

    """
    lines = ["[Data Parameters]", f"DataOffset={_OFFSET_PLACEHOLDER}"]
    for name, entries in sections.items():
        lines.append(f"[{name}]")
        lines.extend(
            entry if isinstance(entry, str) else f"{entry[0]}={entry[1]}"
            for entry in entries
        )

    encoded = ("\r\n".join(lines) + "\r\n").encode("latin-1")
    return encoded.replace(
        f"DataOffset={_OFFSET_PLACEHOLDER}".encode("latin-1"),
        f"DataOffset={len(encoded):>{_OFFSET_WIDTH}d}".encode("latin-1"),
    )


# A synthetic SPMLab 1.00 header. It mirrors the layout of a real export and
# additionally exercises the lexical cases a single real file cannot contain at
# once: a key repeated across two sections, every unit spelling, a switch state,
# a gain range, a value holding '=', and blank and keyless lines.
_SPMLAB_1_00_SECTIONS: dict[str, list[tuple[str, str] | str]] = {
    "Data Version": [("Program", "SPMLab"), ("Version", "1.00")],
    "Scan": [
        "",
        "   ",
        "a line without an equals sign",
        ("ScanRangeX", "1.0000 µm"),
        ("Rotation", "0.0 °"),
        ("ScanningRate", "1.0000 µm/s"),
        ("ZTransferCoefficient", "0.7731 µm/V"),
        ("SetPoint", "-3.5e-2 V"),
        ("ResolutionX", "512"),
        ("ScanDirection", "FORWARD"),
        ("Feedback", "1.0 on"),
        ("GainP", "0.800000 (1000.000000)"),
        ("Expression", "a=b=c"),
        ("Leveling", "None"),
    ],
    "PreProcessing": [("Leveling", "1D Line Fit")],
    "Data": [],
}

_SPMLAB_1_00_HEADER = _build_flt_header(_SPMLAB_1_00_SECTIONS)

SPMLAB_1_00_SYNTHETIC = FltHeaderFlavor(
    vendor="bruker",
    software="spmlab",
    version="1.00-synthetic",
    header=_SPMLAB_1_00_HEADER,
    expected={
        # Written by _build_flt_header, and the only place 'DataOffset' lives.
        "Data Parameters": {"DataOffset": str(len(_SPMLAB_1_00_HEADER))},
        "Data Version": {"Program": "SPMLab", "Version": "1.00"},
        "Scan": {
            # 'µ' is 0xB5 and '°' is 0xB0: single bytes, so the header is cp1252
            # and decoding it as UTF-8 would raise on exactly these two.
            "ScanRangeX": "1.0000",
            "ScanRangeX/@unit": "µm",
            "Rotation": "0.0",
            "Rotation/@unit": "°",
            # Compound units keep their solidus.
            "ScanningRate": "1.0000",
            "ScanningRate/@unit": "µm/s",
            "ZTransferCoefficient": "0.7731",
            "ZTransferCoefficient/@unit": "µm/V",
            # Sign and exponent belong to the value, not to the unit.
            "SetPoint": "-3.5e-2",
            "SetPoint/@unit": "V",
            # No trailing token, so no '/@unit' companion.
            "ResolutionX": "512",
            "ScanDirection": "FORWARD",
            # 'on' is a switch state listed in UNIT_TO_SKIP, so the unit is
            # blanked rather than stored as if it were a unit.
            "Feedback": "1.0",
            "Feedback/@unit": "",
            # The parenthesised constant of a gain is dropped, so that the
            # gain stays a number.
            "GainP": "0.800000",
            # Only the first '=' separates key from value.
            "Expression": "a=b=c",
            # Same key as in '[PreProcessing]' below; sections keep them apart.
            "Leveling": "None",
        },
        "PreProcessing": {"Leveling": "1D Line Fit"},
        # A section marker with no key-value pairs, like '[Data]' in a real file.
        "Data": {},
    },
)

# The real reference export. Its expected dict is the ground truth the
# synthetic flavour above is modelled on.
SPMLAB_1_00_REFERENCE = FltHeaderFlavor(
    vendor="bruker",
    software="spmlab",
    version="1.00",
    header=FLT_RAW_FILE.read_bytes()[:957],
    expected={
        "Data Version": {"Program": "SPMLab", "Version": "1.00"},
        "Data Parameters": {
            "CreationTime": "Jun.17.2026 08:03:43",
            "DataName": "Height",
            "DataID": "SIG_TOPO",
            "DataOffset": "957",
            "ScanRangeX": "1.0000",
            "ScanRangeX/@unit": "µm",
            "ScanRangeY": "1.0000",
            "ScanRangeY/@unit": "µm",
            # 'OffsetX'/'OffsetY' are dropped by gwyddionpy, which is why the
            # header is read directly.
            "OffsetX": "1.0000",
            "OffsetX/@unit": "µm",
            "OffsetY": "1.0000",
            "OffsetY/@unit": "µm",
            "Rotation": "0.0",
            "Rotation/@unit": "°",
            "ScanningRate": "1.0000",
            "ScanningRate/@unit": "µm/s",
            "ResolutionX": "512",
            "ResolutionY": "512",
            "ScanDirection": "FORWARD",
            "ZTransferCoefficient": "0.7731",
            "ZTransferCoefficient/@unit": "µm/V",
            # Collapsed onto the '[PreProcessing]' entry by gwyddionpy.
            "Leveling": "None",
        },
        "PreProcessing": {"Leveling": "1D Line Fit"},
        "System Info": {
            # The linearization flags, likewise dropped by gwyddionpy.
            "XLinOn": "TRUE",
            "YLinOn": "TRUE",
            "Mode": "Peak Force Tapping",
            "SetPoint": "0.030000",
            "SetPoint/@unit": "V",
            # The Z feedback loop and the two linearization loops each carry
            # their own PID triplet; the per loop constant SPMLab appends to
            # every gain (1000.0 and 1200.0 here) is dropped by the parser.
            "GainP": "0.800000",
            "GainI": "0.300000",
            "GainD": "0.000000",
            "XLinGainP": "1.000000",
            "XLinGainI": "12.000000",
            "XLinGainD": "0.000000",
            "YLinGainP": "1.000000",
            "YLinGainI": "12.000000",
            "YLinGainD": "0.000000",
        },
        "Piezo Parameters": {
            "X Transfer Coefficient": "4.423937",
            "X Transfer Coefficient/@unit": "µm/V",
            "Y Transfer Coefficient": "4.856491",
            "Y Transfer Coefficient/@unit": "µm/V",
            "Z Transfer Coefficient": "0.773091",
            "Z Transfer Coefficient/@unit": "µm/V",
        },
        # '[Data]' marks the start of the raster and holds no key-value pairs.
        "Data": {},
    },
)

FLT_HEADER_FLAVORS = [SPMLAB_1_00_REFERENCE, SPMLAB_1_00_SYNTHETIC]


def _pad_header_past_chunk(header: bytes, pad_lines: int = 900) -> bytes:
    """Grow a header beyond HEADER_CHUNK_SIZE, keeping 'DataOffset' correct.

    The padding is appended as a section of its own, so that 'DataOffset' keeps
    its place inside the first chunk the parser reads and no existing section is
    split in two; only the header it announces becomes longer. Its value is
    rewritten through the same fixed width placeholder as in
    ``_build_flt_header``, because filling in the real length must not change
    that length.
    """
    padding = "\r\n".join(f"Pad{i}=ignored" for i in range(pad_lines))
    text = DATA_OFFSET.sub(
        f"DataOffset={_OFFSET_PLACEHOLDER}\r", header.decode("latin-1"), count=1
    )
    text += f"[Padding]\r\n{padding}\r\n"
    encoded = text.encode("latin-1")
    return encoded.replace(
        f"DataOffset={_OFFSET_PLACEHOLDER}".encode("latin-1"),
        f"DataOffset={len(encoded):>{_OFFSET_WIDTH}d}".encode("latin-1"),
    )


def _flt_parser_for(tmp_path: Path, content: bytes) -> FltBruker:
    """Bind a parser to a hand written FLT file without invoking gwyddionpy.

    ``_get_raw_header_dict`` only needs ``file_path``, so the instance is built
    with ``__new__``; going through ``__init__`` would require a raster that a
    real reader could decode, which these header tests do not exercise.
    """
    flt_file = tmp_path / "synthetic.FLT"
    flt_file.write_bytes(content)
    parser = FltBruker.__new__(FltBruker)
    parser.file_path = str(flt_file)
    return parser


@pytest.mark.parametrize(
    "flavor", FLT_HEADER_FLAVORS, ids=[flavor.id for flavor in FLT_HEADER_FLAVORS]
)
class TestFltBrukerHeader:
    """The header is read directly, because gwyddionpy drops and merges keys."""

    def test_whole_header_is_parsed_section_wise(self, flavor, tmp_path):
        """One complete header in, one complete dict out.

        A raster is appended so that the comparison also proves that nothing
        past 'DataOffset' is mistaken for text.
        """
        raster = bytes(range(256)) * 8
        parser = _flt_parser_for(tmp_path, flavor.header + raster)

        assert parser._get_raw_header_dict() == flavor.expected

    def test_header_is_read_past_the_first_chunk(self, flavor, tmp_path):
        """Padding the header beyond HEADER_CHUNK_SIZE must change nothing.

        It forces the seek-and-reread branch, which is otherwise unreachable
        for a header as short as a real export's.
        """
        header = _pad_header_past_chunk(flavor.header)
        assert len(header) > HEADER_CHUNK_SIZE

        parsed = _flt_parser_for(tmp_path, header)._get_raw_header_dict()

        # The padding sits well past the first chunk, so it is only present if
        # the parser re-read the file up to 'DataOffset'.
        assert parsed.pop("Padding") == {f"Pad{i}": "ignored" for i in range(900)}
        # Every section of the original header survives the re-read unchanged,
        # apart from 'DataOffset', which now measures the padded header.
        parsed["Data Parameters"]["DataOffset"] = flavor.expected["Data Parameters"][
            "DataOffset"
        ]
        assert parsed == flavor.expected

    def test_missing_data_offset_yields_an_empty_dict(self, flavor, tmp_path, caplog):
        """Without 'DataOffset' the end of the header is unknown.

        A truncated or foreign file is skipped whole, with a warning, rather
        than being guessed at.
        """
        header = DATA_OFFSET.sub("", flavor.header.decode("latin-1")).encode("latin-1")
        parser = _flt_parser_for(tmp_path, header)
        with caplog.at_level("WARNING"):
            assert parser._get_raw_header_dict() == {}
        assert "DataOffset" in caplog.text


# ---------------------------------------------------------------------------
# FltBruker — parse() against a real .FLT export
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FltFileFlavor:
    """A real .FLT export together with what parse() must return for it."""

    vendor: str
    software: str
    version: str
    path: Path
    channel: str
    shape: tuple[int, int]
    # Every scalar entry asserted for this file, keyed by its flattened path
    # relative to the channel group.
    expected: dict[str, str]

    @property
    def id(self) -> str:
        return f"{self.vendor}-{self.software}-{self.version}"


SPMLAB_1_00_FILE = FltFileFlavor(
    vendor="bruker",
    software="spmlab",
    version="1.00",
    path=FLT_RAW_FILE,
    channel="Height",
    shape=(FLT_RESOLUTION, FLT_RESOLUTION),
    expected={
        "name": "Height",
        # gwyddionpy converts to SI, so a frame of heights is in metres.
        "data/@unit": "m",
        "x_real/@unit": "m",
        "y_real/@unit": "m",
        # Channel metadata, with the units split off their values.
        "meta/CreationTime": "Jun.17.2026 08:03:43",
        "meta/DataID": "SIG_TOPO",
        "meta/Mode": "Peak Force Tapping",
        "meta/SetPoint": "0.030000",
        "meta/SetPoint/@unit": "V",
        "meta/ScanningRate": "1.0000",
        "meta/ScanningRate/@unit": "µm/s",
        "meta/Rotation": "0.0",
        "meta/Rotation/@unit": "°",
        # The per loop constant SPMLab appends to a gain is dropped, so that
        # the gain reaches the 'K_p' (NX_NUMBER) field as a number.
        "meta/GainP": "0.800000",
        # The raw header, nested below the channel it describes. These are the
        # keys gwyddionpy drops or merges, which is why it is read separately.
        "header/Data Parameters/OffsetX": "1.0000",
        "header/Data Parameters/OffsetX/@unit": "µm",
        "header/Data Parameters/OffsetY": "1.0000",
        "header/Data Parameters/ResolutionX": "512",
        "header/Data Parameters/ResolutionY": "512",
        "header/Data Parameters/ScanDirection": "FORWARD",
        "header/Data Parameters/Leveling": "None",
        "header/PreProcessing/Leveling": "1D Line Fit",
        "header/System Info/XLinOn": "TRUE",
        "header/System Info/YLinOn": "TRUE",
    },
)

FLT_FILE_FLAVORS = [SPMLAB_1_00_FILE]


@pytest.mark.parametrize(
    "flavor", FLT_FILE_FLAVORS, ids=[flavor.id for flavor in FLT_FILE_FLAVORS]
)
class TestFltBrukerParse:
    """parse() must hand the formatter a flat, slash separated dict."""

    @staticmethod
    def _parse(flavor: FltFileFlavor) -> dict:
        return FltBruker(str(flavor.path)).parse()

    def test_structure_is_flat_and_holds_one_channel(self, flavor):
        """A .FLT stores a single channel, whose name prefixes every path."""
        raw_data = self._parse(flavor)

        assert raw_data["/source_format"] == "spmlabf"
        assert all(key.startswith("/") for key in raw_data)
        assert not any(isinstance(val, dict) for val in raw_data.values())
        top_level = {key.split("/")[1] for key in raw_data}
        assert top_level == {"source_format", flavor.channel}

    def test_expected_entries_are_parsed(self, flavor):
        """Every metadata and header entry recorded for this file must match."""
        raw_data = self._parse(flavor)
        actual = {
            key: raw_data.get(f"/{flavor.channel}/{key}") for key in flavor.expected
        }

        assert actual == flavor.expected
        # A value without a trailing unit gets no '/@unit' companion.
        assert f"/{flavor.channel}/meta/GainP/@unit" not in raw_data

    def test_image_and_physical_size(self, flavor):
        raw_data = self._parse(flavor)
        image = raw_data[f"/{flavor.channel}/data"]

        assert isinstance(image, np.ndarray)
        assert image.shape == flavor.shape
        # The scan size is stored in SI metres alongside the image.
        assert raw_data[f"/{flavor.channel}/x_real"] == pytest.approx(1e-6)
        assert raw_data[f"/{flavor.channel}/y_real"] == pytest.approx(1e-6)

    def test_every_config_path_of_the_default_config_resolves(self, flavor):
        """No 'raw_path' of the shipped config may point at a missing key.

        The config addresses the channel through the '/CHANNEL/' placeholder,
        which the formatter resolves; the same substitution is applied here.
        """
        from pynxtools_spm.configs import load_default_config

        raw_data = self._parse(flavor)
        config = load_default_config(config_type="bruker_flt_afm")
        raw_paths: list[str] = []

        def collect(node):
            if isinstance(node, dict):
                if "#note" in node:
                    # Flagged as derived in code, so it need not resolve here.
                    return
                for key, val in node.items():
                    if key == "raw_path":
                        raw_paths.extend(val if isinstance(val, list) else [val])
                    else:
                        collect(val)
            elif isinstance(node, list):
                for item in node:
                    collect(item)

        collect(config)
        # '@default:' values are literals supplied by the config, not lookups.
        lookups = [
            path.replace("/CHANNEL/", f"/{flavor.channel}/")
            for path in raw_paths
            if path and not path.startswith("@default:")
        ]
        assert lookups, "the config must address the raw data somewhere"
        missing = [path for path in lookups if path not in raw_data]
        assert not missing, f"config paths absent from the parsed data: {missing}"


def test_flt_parser_rejects_a_missing_file(tmp_path):
    """SPMBase refuses a path that does not exist, like every other parser."""
    with pytest.raises(FileNotFoundError):
        FltBruker(str(tmp_path / "absent.FLT"))


# ---------------------------------------------------------------------------
# SPMParser — picking FltBruker for a .FLT file
# ---------------------------------------------------------------------------

VENDOR_KEY = "/ENTRY[entry]/INSTRUMENT[instrument]/software/vendor"
MODEL_KEY = "/ENTRY[entry]/INSTRUMENT[instrument]/software/model"


class TestFltParserSelection:
    """Selection goes through vendor and software model, with a fallback."""

    @staticmethod
    def _parsed(**kwargs) -> dict:
        from pynxtools_spm.parsers import SPMParser

        return SPMParser().get_raw_data_dict(str(FLT_RAW_FILE), **kwargs)

    @pytest.mark.parametrize(
        "model",
        [
            # The header reports 'Program=SPMLab' and 'Version=1.00', so the
            # ELN may spell the model in any of these ways.
            "SPMLab 1.00",
            "SPMLab 1.0",
            "SPMLab",
            "1.00",
        ],
    )
    def test_selected_from_the_eln_software_model(self, model):
        raw_data = self._parsed(eln={VENDOR_KEY: "bruker", MODEL_KEY: model})
        assert raw_data["/source_format"] == "spmlabf"

    @pytest.mark.parametrize(
        "eln",
        [
            None,
            {},
            # An unknown model must not fail: every parser registered under the
            # extension is tried in turn.
            {VENDOR_KEY: "bruker", MODEL_KEY: "SPMLab 9.99"},
            {VENDOR_KEY: "unknown vendor", MODEL_KEY: "unknown model"},
        ],
    )
    def test_falls_back_to_the_extension(self, eln):
        raw_data = self._parsed(eln=eln)
        assert raw_data["/source_format"] == "spmlabf"
        assert "/Height/data" in raw_data

    def test_uppercase_extension_is_accepted(self):
        """Bruker writes '.FLT'; the navigation table is keyed lower case."""
        assert self._parsed(file_ext="FLT")["/source_format"] == "spmlabf"
        assert self._parsed(file_ext="flt")["/source_format"] == "spmlabf"

    def test_unknown_extension_is_rejected(self):
        from pynxtools_spm.parsers import SPMParser

        with pytest.raises(KeyError):
            SPMParser().get_raw_data_dict(str(FLT_RAW_FILE), eln={}, file_ext="xyz")

    def test_module_level_helper_parses_the_file(self):
        from pynxtools_spm.parsers import get_bruker_flt_parsed_data

        assert get_bruker_flt_parsed_data(str(FLT_RAW_FILE))["/source_format"] == (
            "spmlabf"
        )


# ---------------------------------------------------------------------------
# SPMReader — dispatching a .FLT file to BrukerFltAFM
# ---------------------------------------------------------------------------

FLT_ELN_FILE = FLT_DATA_DIR / "eln_data.yaml"


class TestFltReaderDispatch:
    """The reader picks the formatter from experiment_technique plus extension."""

    @staticmethod
    def _read(*file_paths) -> dict:
        from pynxtools.dataconverter.template import Template

        from pynxtools_spm.reader import SPMReader

        return SPMReader().read(template=Template(), file_paths=tuple(file_paths))

    @pytest.fixture(scope="class")
    def filled_template(self) -> dict:
        return self._read(str(FLT_RAW_FILE), str(FLT_ELN_FILE))

    def test_nxafm_is_supported(self):
        from pynxtools_spm.reader import SPMReader

        assert "NXafm" in SPMReader.supported_nxdls

    def test_template_is_filled_from_the_flt_file(self, filled_template):
        assert filled_template[f"{ENTRY}/definition"] == "NXafm"
        groups = {
            key[: -len("/@signal")]: val
            for key, val in filled_template.items()
            if key.endswith("/@signal") and key.startswith(f"{ENTRY}/DATA[")
        }
        ((group, signal_name),) = groups.items()
        signal = filled_template[f"{group}/DATA[{signal_name}]"]
        assert isinstance(signal, np.ndarray)
        assert signal.shape == (FLT_RESOLUTION, FLT_RESOLUTION)

    def test_definition_version_is_stamped(self, filled_template):
        """Set by the reader for every format; the value tracks the installed
        NeXus definitions, so only its presence is asserted."""
        assert filled_template[f"{ENTRY}/definition/@version"]

    def test_empty_values_are_dropped(self, filled_template):
        """'end_time' is empty in the config, so it must not reach the file."""
        for key, val in filled_template.items():
            if isinstance(val, np.ndarray):
                continue
            assert val not in (None, ""), f"{key} was kept although it is empty"

    def test_eln_file_is_required(self):
        with pytest.raises(ValueError, match="ELN file is required"):
            self._read(str(FLT_RAW_FILE))

    def test_data_file_is_required(self):
        with pytest.raises(ValueError, match="Data file is required"):
            self._read(str(FLT_ELN_FILE))

    def test_wrong_technique_for_the_extension_is_rejected(self, tmp_path):
        """A .FLT declared as STM matches no formatter and must not pass silently."""
        eln = tmp_path / "eln_data.yaml"
        eln.write_text(
            FLT_ELN_FILE.read_text().replace(
                "experiment_technique: AFM", "experiment_technique: STM"
            ),
            encoding="utf-8",
        )
        with pytest.raises(ValueError, match="IncorrectExperiment"):
            self._read(str(FLT_RAW_FILE), str(eln))
