"""Tests for the Omicron RHK SM4 STM format.

Covers the properties that decide whether an SM4 image is usable: the page
metadata read by ``read_sm4_pages``, which keeps the typed 'RHK_*' attributes
the config addresses; the image read by ``Sm4Omicron`` with ``gwyddionpy``,
which holds physical values rather than raw ADC counts; and the row orientation
applied by ``OmicronBase``, which puts row 0 of the image at the bottom, the
origin of a scientific plot.
"""

import struct
import zlib
from pathlib import Path

import numpy as np
import pytest
from gwyddionpy import load
from pynxtools.dataconverter.template import Template

from pynxtools_spm.nxformatters.omicron.omicron_base import OmicronBase
from pynxtools_spm.parsers import omicron_sm4
from pynxtools_spm.parsers.omicron_sm4 import Sm4Omicron
from pynxtools_spm.parsers.rhk_sm4_metadata import (
    OBJECT_PRM,
    Sm4Object,
    _ByteReader,
    _enum_name,
    _Sm4MetadataReader,
    read_sm4_pages,
)
from pynxtools_spm.reader import SPMReader

TEST_DATA_DIR = Path(__file__).parent / "data"
SM4_DATA_DIR = TEST_DATA_DIR / "omicron" / "stm" / "sm4_dflt_conf_up"
SM4_RAW_FILE = next(SM4_DATA_DIR.glob("*.sm4"), None) or next(
    SM4_DATA_DIR.glob("*.SM4"), None
)
assert SM4_RAW_FILE is not None, f"no .sm4 file found in {SM4_DATA_DIR}"
SM4_ELN_FILE = SM4_DATA_DIR / "eln_data.yaml"

ENTRY = "/ENTRY[entry]"
# The four pages of the reference file, by label, paired with the NXdata group
# each one ends up in.
PAGE_TO_GROUP = {
    "Topography_Forward": "z_forward",
    "Topography_Backward": "z_backward",
    "Current_Forward": "current_forward",
    "Current_Backward": "current_backward",
}
# The same pages as gwyddionpy names them: a forward scan runs to the right.
PAGE_TO_CHANNEL = {
    "Topography_Forward": "Topography [Right]",
    "Topography_Backward": "Topography [Left]",
    "Current_Forward": "Current [Right]",
    "Current_Backward": "Current [Left]",
}


def _signal(template, group):
    """The image of an NXdata group, found through its '@signal' attribute."""
    name = template[f"{ENTRY}/DATA[{group}]/@signal"]
    return template[f"{ENTRY}/DATA[{group}]/DATA[{name}]"]


def _slow_axis(template, group):
    """The axis of dimension 0, which is the one describing the rows."""
    axes = template[f"{ENTRY}/DATA[{group}]/@axes"]
    return template[f"{ENTRY}/DATA[{group}]/AXISNAME[{axes[0]}]"]


def _sm4_string(text: str) -> bytes:
    """Encode a string the way SM4 stores it: a uint16 length, then UTF-16."""
    return struct.pack("<H", len(text)) + text.encode("utf-16-le")


@pytest.fixture(scope="module")
def pages():
    return {page.label: page for page in read_sm4_pages(SM4_RAW_FILE)}


@pytest.fixture(scope="module")
def gwy_channels():
    """The channels as gwyddionpy returns them, before any of our handling."""
    return load(str(SM4_RAW_FILE)).channels


@pytest.fixture(scope="module")
def parsed():
    return Sm4Omicron(str(SM4_RAW_FILE)).parse()


@pytest.fixture(scope="module")
def template():
    return SPMReader().read(
        template=Template(),
        file_paths=(str(SM4_RAW_FILE), str(SM4_ELN_FILE)),
    )


class TestMetadata:
    """The page metadata keeps the names and dtypes the config is written for."""

    def test_every_page_is_read_in_file_order(self):
        labels = [page.label for page in read_sm4_pages(SM4_RAW_FILE)]
        assert sorted(labels) == sorted(PAGE_TO_GROUP)

    @pytest.mark.parametrize("label", sorted(PAGE_TO_GROUP))
    def test_page_id_pairs_the_page_with_its_gwyddion_channel(
        self, pages, gwy_channels, label
    ):
        channel = gwy_channels[PAGE_TO_CHANNEL[label]]
        assert pages[label].page_id == channel.meta["Page ID"]

    @pytest.mark.parametrize(
        "key,dtype",
        [
            ("RHK_Xsize", np.uint32),
            ("RHK_ScanType", np.uint32),
            ("RHK_Zscale", np.float32),
            ("RHK_Xoffset", np.float32),
            ("RHK_PiezoSensitivity_TubeX", np.float64),
            ("RHK_ZPI_SetPoint", np.float64),
            ("RHK_ImageDrift_Time", np.float32),
            ("RHK_ImageDrift_Filetime", np.uint64),
        ],
    )
    def test_binary_values_keep_their_stored_dtype(self, pages, key, dtype):
        assert type(pages["Topography_Forward"].attrs[key]) is dtype

    def test_strings_and_derived_values(self, pages):
        attrs = pages["Topography_Forward"].attrs
        assert attrs["RHK_Label"] == "Topography"
        assert attrs["RHK_ScanTypeName"] == "RHK_SCAN_RIGHT"
        assert attrs["RHK_DateTime"] == "2022-01-20T16:07:09.000"
        assert attrs["RHK_CompletedLineCount"] == 512
        assert attrs["RHK_CH1DriveValue"] == -1.0
        assert attrs["RHK_CH1DriveValueUnits"] == "V"
        assert attrs["RHK_LowPassFilter1_CutoffFrequency"] == 100.0
        assert attrs["RHK_LowPassFilter1_CutoffFrequencyUnits"] == "kHz"

    def test_file_name_is_the_path_the_file_is_read_from(self, pages):
        assert pages["Current_Backward"].attrs["RHK_FileName"] == str(SM4_RAW_FILE)

    def test_units_become_unit_attributes(self, parsed):
        assert parsed["/Topography_Forward/RHK_Z/@unit"] == "m"
        assert parsed["/Current_Forward/RHK_Z/@unit"] == "A"
        assert parsed["/Topography_Forward/RHK_PiezoSensitivity_TubeX/@unit"] == "m/V"
        assert "/Topography_Forward/RHK_Zunits" not in parsed


class TestMetadataEdgeCases:
    """The reader fails loudly on broken files and names odd pages sensibly."""

    def test_empty_file_raises(self, tmp_path):
        empty = tmp_path / "empty.sm4"
        empty.write_bytes(b"")
        with pytest.raises(ValueError, match="ends at byte 0"):
            read_sm4_pages(empty)

    @pytest.mark.parametrize("size", [1, 60, 4096])
    def test_truncated_file_raises(self, tmp_path, size):
        truncated = tmp_path / "truncated.sm4"
        truncated.write_bytes(SM4_RAW_FILE.read_bytes()[:size])
        with pytest.raises(ValueError):
            read_sm4_pages(truncated)

    def test_missing_object_raises(self):
        with pytest.raises(ValueError, match="no object with id 2"):
            _Sm4MetadataReader._offset_of([Sm4Object(1, 10, 20)], 2)

    @pytest.mark.parametrize(
        "scan_type,suffix",
        [(0, "_Forward"), (1, "_Backward"), (2, "_Up"), (3, "_Down"), (7, "")],
    )
    def test_image_label_carries_the_scan_direction(self, scan_type, suffix):
        attrs = {
            "RHK_Label": "Topography",
            "RHK_PageID": np.uint16(1),
            "RHK_PageDataType": np.uint32(0),
            "RHK_ScanType": np.uint32(scan_type),
        }
        assert _Sm4MetadataReader._page_label(attrs) == f"Topography{suffix}"

    @pytest.mark.parametrize(
        "label,expected", [("-dI dV", "dI_dV"), (" LIA Current", "LIA_Current")]
    )
    def test_non_image_label_is_sanitized_without_direction(self, label, expected):
        attrs = {"RHK_Label": label, "RHK_PageDataType": np.uint32(1)}
        assert _Sm4MetadataReader._page_label(attrs) == expected

    @pytest.mark.parametrize("attrs", [{}, {"RHK_Label": ""}])
    def test_page_without_label_is_named_after_its_id(self, attrs):
        attrs = {**attrs, "RHK_PageID": np.uint16(4162)}
        assert _Sm4MetadataReader._page_label(attrs) == "ID4162"

    @pytest.mark.parametrize(
        "value,expected", [(1, "B"), (2, "UNKNOWN"), (-1, "UNKNOWN")]
    )
    def test_enum_value_outside_the_format_is_unknown(self, value, expected):
        assert _enum_name(("A", "B"), value, "UNKNOWN") == expected

    def test_string_strips_trailing_nul_characters(self):
        reader = _ByteReader(_sm4_string("kHz\x00\x00"))
        assert reader.string() == "kHz"

    def test_empty_string(self):
        assert _ByteReader(_sm4_string("")).string() == ""

    def test_string_with_a_lone_surrogate_is_empty(self):
        reader = _ByteReader(struct.pack("<HH", 1, 0xD800))
        assert reader.string() == ""
        assert reader.position == 4

    @pytest.mark.parametrize("compressed", [False, True])
    def test_prm_data_is_read_plain_or_zlib_compressed(self, compressed):
        text = "[Scan]\nSpeed=1.0\n"
        payload = zlib.compress(text.encode("cp437")) if compressed else text.encode()
        prm_header = struct.pack("<III", int(compressed), len(text), len(payload))
        reader = _Sm4MetadataReader(prm_header + payload, "file.sm4")
        reader._file_objects = [Sm4Object(OBJECT_PRM, len(prm_header), len(payload))]
        attrs = {}
        reader._read_prm(attrs)
        assert attrs["RHK_PRMdata"] == text


class TestImageData:
    """gwyddionpy applies the Z scale, so the image holds physical values.

    The raw ADC counts are several orders of magnitude away from the unit the
    field is labelled with, and carry the wrong sign whenever the scale is
    negative, which is the case for topography in the reference file.
    """

    @pytest.mark.parametrize("label", sorted(PAGE_TO_GROUP))
    def test_image_is_the_gwyddion_channel(self, parsed, gwy_channels, label):
        np.testing.assert_array_equal(
            parsed[f"/{label}/data"], gwy_channels[PAGE_TO_CHANNEL[label]].data
        )

    def test_topography_sign_follows_a_negative_scale(self, parsed, pages):
        assert pages["Topography_Forward"].attrs["RHK_Zscale"] < 0
        assert np.all(parsed["/Topography_Forward/data"] < 0)

    @pytest.mark.parametrize(
        "label,limit", [("Topography_Forward", 1e-5), ("Current_Forward", 1e-7)]
    )
    def test_values_are_physical_not_counts(self, parsed, label, limit):
        """Counts reach ~1e9; topography in m and current in A stay far below."""
        assert np.max(np.abs(parsed[f"/{label}/data"])) < limit

    def test_page_attributes_are_left_untouched(self, parsed, pages):
        """Only the image is converted; the scale stays readable by a config."""
        attrs = pages["Topography_Forward"].attrs
        assert parsed["/Topography_Forward/RHK_Zscale"] == attrs["RHK_Zscale"]
        assert parsed["/Topography_Forward/RHK_Zoffset"] == attrs["RHK_Zoffset"]

    @pytest.mark.parametrize("axis", ["x", "y"])
    def test_coords_are_pixel_centres_around_the_offset(self, parsed, pages, axis):
        """'RHK_Xoffset' is the centre of the scan area and '|RHK_Xscale|' the
        pixel pitch, so index i of 'n' sits at
        'offset - n * |scale| / 2 + (i + 0.5) * |scale|', ascending."""
        attrs = pages["Topography_Forward"].attrs
        key = f"RHK_{axis.upper()}"
        coords = parsed[f"/Topography_Forward/coords/Topography_Forward_{axis}"]
        size, scale, offset = (
            attrs[f"{key}size"],
            abs(attrs[f"{key}scale"]),
            attrs[f"{key}offset"],
        )
        assert coords.dtype == np.float64
        assert len(coords) == size
        np.testing.assert_allclose(
            coords,
            offset - size * scale / 2 + (np.arange(size) + 0.5) * scale,
            rtol=1e-12,
        )
        np.testing.assert_allclose(np.diff(coords), scale, rtol=1e-12)
        assert (coords[0] + coords[-1]) / 2 == pytest.approx(offset)

    def test_page_without_gwyddion_channel_keeps_metadata_only(
        self, monkeypatch, caplog
    ):
        # 'gwyddionpy.load' is replaced by a fake returning no channels: no SM4
        # file exists whose pages Gwyddion cannot read, so this is the only way
        # to reach the branch that guards against such a file.
        class _NoChannels:
            channels: dict = {}

        monkeypatch.setattr(omicron_sm4, "load", lambda _: _NoChannels())
        with caplog.at_level("WARNING"):
            result = Sm4Omicron(str(SM4_RAW_FILE)).parse()

        assert not [key for key in result if key.endswith("/data")]
        assert "/Topography_Forward/RHK_Zscale" in result
        assert "/Topography_Forward/coords/Topography_Forward_x" in result
        assert "no matching channel" in caplog.text


class TestImageOrientation:
    """Row 0 of the stored signal must be the bottom row of the image.

    The hook is called through the class with ``None`` in place of ``self``:
    it reads nothing off the instance, and building one would need a raw file
    and an ELN just to reach a transformation of its argument.
    """

    def test_hook_flips_a_two_dimensional_image(self):
        data = np.arange(6).reshape(3, 2)
        np.testing.assert_array_equal(
            OmicronBase.rearrange_data_according_to_axes(None, data), np.flipud(data)
        )

    @pytest.mark.parametrize("is_forward", [True, False, None])
    def test_scan_direction_causes_no_lateral_flip(self, is_forward):
        """``gwyddionpy`` already returns both directions in the right x order."""
        data = np.arange(6).reshape(3, 2)
        np.testing.assert_array_equal(
            OmicronBase.rearrange_data_according_to_axes(None, data, is_forward),
            np.flipud(data),
        )

    @pytest.mark.parametrize("data", [np.arange(4), np.arange(8).reshape(2, 2, 2)])
    def test_non_image_data_is_left_alone(self, data):
        np.testing.assert_array_equal(
            OmicronBase.rearrange_data_according_to_axes(None, data), data
        )

    @pytest.mark.parametrize("label,group", sorted(PAGE_TO_GROUP.items()))
    def test_signal_is_flipped_against_the_parsed_image(
        self, template, parsed, label, group
    ):
        np.testing.assert_array_equal(
            _signal(template, group), np.flipud(parsed[f"/{label}/data"])
        )

    @pytest.mark.parametrize("group", sorted(PAGE_TO_GROUP.values()))
    def test_slow_axis_ascends_so_its_first_value_labels_row_zero(
        self, template, group
    ):
        assert np.all(np.diff(_slow_axis(template, group)) > 0), (
            "the slow axis must ascend with the row index"
        )

    @pytest.mark.parametrize("group", sorted(PAGE_TO_GROUP.values()))
    def test_slow_axis_length_matches_the_signal(self, template, group):
        assert len(_slow_axis(template, group)) == _signal(template, group).shape[0]
