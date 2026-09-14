"""Image orientation of the two Bruker image formats, NanoScope .spm and SPMLab .FLT.

Both are read through ``gwyddionpy``, which returns the rows bottom first, so
both need the same flip. It is applied once, by
``BrukerBase.rearrange_data_according_to_axes``, rather than separately in each
parser. These tests pin that the flip reaches both formats, that the slow axis
is written in the direction that matches it, and that the force-curve path,
which shares the same base class, is left alone.
"""

from pathlib import Path

import numpy as np
import pytest
from pynxtools.dataconverter.template import Template

from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
from pynxtools_spm.parsers.bruker_flt import FltBruker
from pynxtools_spm.parsers.bruker_spm import SpmBruker
from pynxtools_spm.reader import SPMReader

TEST_DATA_DIR = Path(__file__).parent / "data"
SPM_DATA_DIR = TEST_DATA_DIR / "bruker" / "afm" / "default_config"
FLT_DATA_DIR = TEST_DATA_DIR / "bruker" / "afm" / "flt_default_config"

SPM_RAW_FILE = next(SPM_DATA_DIR.glob("*.spm"))
FLT_RAW_FILE = next(FLT_DATA_DIR.glob("*.flt"), None) or next(
    FLT_DATA_DIR.glob("*.FLT")
)

ENTRY = "/ENTRY[entry]"
# Every NXdata group of the NanoScope reference, with the parser key it is
# built from, as spelled in configs/bruker/bruker_spm_afm.json.
SPM_GROUP_TO_RAW_PATH = {
    "z_forward": "/Height_Sensor/forward",
    "z_backward": "/Height_Sensor/backward",
    "amplitude_error_forward": "/Amplitude_Error/forward",
    "amplitude_error_backward": "/Amplitude_Error/backward",
    "phase_forward": "/Phase/forward",
    "phase_backward": "/Phase/backward",
    "amplitude_forward": "/Amplitude/forward",
    "amplitude_backward": "/Amplitude/backward",
    "tm_deflection_forward": "/TM_Deflection/forward",
    "tm_deflection_backward": "/TM_Deflection/backward",
}


def _read(raw_file, data_dir):
    return SPMReader().read(
        template=Template(),
        file_paths=(str(raw_file), str(data_dir / "eln_data.yaml")),
    )


def _signal(template, group):
    name = template[f"{ENTRY}/DATA[{group}]/@signal"]
    return template[f"{ENTRY}/DATA[{group}]/DATA[{name}]"]


def _slow_axis(template, group):
    """The axis of dimension 0, which is the one describing the rows."""
    axes = template[f"{ENTRY}/DATA[{group}]/@axes"]
    return template[f"{ENTRY}/DATA[{group}]/AXISNAME[{axes[0]}]"]


@pytest.fixture(scope="module")
def spm_template():
    return _read(SPM_RAW_FILE, SPM_DATA_DIR)


@pytest.fixture(scope="module")
def spm_parsed():
    return SpmBruker(str(SPM_RAW_FILE)).parse()


@pytest.fixture(scope="module")
def flt_template():
    return _read(FLT_RAW_FILE, FLT_DATA_DIR)


@pytest.fixture(scope="module")
def flt_parsed():
    return FltBruker(str(FLT_RAW_FILE)).parse()


class TestOrientationHook:
    """The hook is called through the class with ``None`` in place of ``self``.

    It reads nothing off the instance, and building one would need a raw file
    and an ELN just to reach a transformation of its argument.
    """

    def test_a_two_dimensional_image_is_flipped(self):
        data = np.arange(6).reshape(3, 2)
        np.testing.assert_array_equal(
            BrukerBase.rearrange_data_according_to_axes(None, data), np.flipud(data)
        )

    @pytest.mark.parametrize("is_forward", [True, False, None])
    def test_scan_direction_causes_no_lateral_flip(self, is_forward):
        """``gwyddionpy`` already returns both directions in the right x order."""
        data = np.arange(6).reshape(3, 2)
        np.testing.assert_array_equal(
            BrukerBase.rearrange_data_according_to_axes(None, data, is_forward),
            np.flipud(data),
        )

    @pytest.mark.parametrize(
        "data",
        [
            np.arange(4),  # a force curve, as the NanoScope TXT export yields
            np.arange(8).reshape(2, 2, 2),
            [1, 2, 3],  # not an array at all
            None,
        ],
    )
    def test_anything_that_is_not_an_image_is_left_alone(self, data):
        result = BrukerBase.rearrange_data_according_to_axes(None, data)
        assert result is data


class TestNanoScopeSpmOrientation:
    """The parser leaves the rows as ``gwyddionpy`` returns them.

    The flip used to live there, so these also pin that moving it to the base
    class kept the output identical.
    """

    @pytest.mark.parametrize("group,raw_path", sorted(SPM_GROUP_TO_RAW_PATH.items()))
    def test_signal_is_flipped_against_the_parsed_image(
        self, spm_template, spm_parsed, group, raw_path
    ):
        np.testing.assert_array_equal(
            _signal(spm_template, group), np.flipud(spm_parsed[raw_path])
        )

    @pytest.mark.parametrize("group", sorted(SPM_GROUP_TO_RAW_PATH))
    def test_slow_axis_descends_so_its_first_value_labels_row_zero(
        self, spm_template, group
    ):
        assert np.all(np.diff(_slow_axis(spm_template, group)) < 0)

    @pytest.mark.parametrize("group", sorted(SPM_GROUP_TO_RAW_PATH))
    def test_slow_axis_length_matches_the_signal(self, spm_template, group):
        assert (
            len(_slow_axis(spm_template, group))
            == _signal(spm_template, group).shape[0]
        )


class TestSpmLabFltOrientation:
    """A .FLT file holds exactly one channel, so there is one NXdata group."""

    @staticmethod
    def _only_group(template):
        groups = {
            key[len(f"{ENTRY}/DATA[") : -len("]/@signal")]
            for key in template
            if key.startswith(f"{ENTRY}/DATA[") and key.endswith("/@signal")
        }
        (group,) = groups
        return group

    def test_signal_is_flipped_against_the_parsed_image(self, flt_template, flt_parsed):
        group = self._only_group(flt_template)
        ((raw_path, image),) = (
            (key, val)
            for key, val in flt_parsed.items()
            if isinstance(val, np.ndarray) and val.ndim == 2
        )
        assert raw_path.endswith("/data")
        np.testing.assert_array_equal(_signal(flt_template, group), np.flipud(image))

    def test_slow_axis_descends_so_its_first_value_labels_row_zero(self, flt_template):
        group = self._only_group(flt_template)
        assert np.all(np.diff(_slow_axis(flt_template, group)) < 0)

    def test_slow_axis_runs_from_the_far_edge_back_to_the_origin(self, flt_template):
        """Row 0 is the top, so the axis starts at 'scan_end_y', not 'scan_start_y'."""
        group = self._only_group(flt_template)
        axis = _slow_axis(flt_template, group)
        scan_region = (
            f"{ENTRY}/INSTRUMENT[instrument]/SCAN_ENVIRONMENT[scan_environment]"
            "/SPM_SCAN_CONTROL[spm_scan_control]/scan_region"
        )
        start = flt_template[f"{scan_region}/scan_start_y"]
        end = flt_template[f"{scan_region}/scan_end_y"]
        assert start is not None and end is not None and start < end
        assert axis[0] == pytest.approx(end)
        assert axis[-1] == pytest.approx(start)

    def test_slow_axis_length_matches_the_signal(self, flt_template):
        group = self._only_group(flt_template)
        assert (
            len(_slow_axis(flt_template, group))
            == _signal(flt_template, group).shape[0]
        )
