"""Tests for the Omicron RHK SM4 STM format.

Covers the two properties that decide whether an SM4 image is usable: the Z
calibration applied by ``Sm4Omicron``, which turns the raw ADC counts of
``spym`` into the physical values the field is labelled with, and the row
orientation applied by ``OmicronBase``, which puts row 0 of the image at the
top so that it is not shown upside down.
"""

from pathlib import Path

import numpy as np
import pytest
from pynxtools.dataconverter.template import Template
from spym.io.rhksm4 import load

from pynxtools_spm.nxformatters.omicron.omicron_base import OmicronBase
from pynxtools_spm.parsers.omicron_sm4 import Sm4Omicron
from pynxtools_spm.reader import SPMReader

TEST_DATA_DIR = Path(__file__).parent / "data"
SM4_DATA_DIR = TEST_DATA_DIR / "omicron" / "stm" / "default_config"
SM4_RAW_FILE = next(SM4_DATA_DIR.glob("*.sm4"), None) or next(
    SM4_DATA_DIR.glob("*.SM4"), None
)
assert SM4_RAW_FILE is not None, f"no .sm4 file found in {SM4_DATA_DIR}"
SM4_ELN_FILE = SM4_DATA_DIR / "eln_data.yaml"

ENTRY = "/ENTRY[entry]"
# The four pages of the reference file, as ``spym`` labels them, paired with the
# NXdata group each one ends up in.
PAGE_TO_GROUP = {
    "Topography_Forward": "z_forward",
    "Topography_Backward": "z_backward",
    "Current_Forward": "current_forward",
    "Current_Backward": "current_backward",
}


def _signal(template, group):
    """The image of an NXdata group, found through its '@signal' attribute."""
    name = template[f"{ENTRY}/DATA[{group}]/@signal"]
    return template[f"{ENTRY}/DATA[{group}]/DATA[{name}]"]


def _slow_axis(template, group):
    """The axis of dimension 0, which is the one describing the rows."""
    axes = template[f"{ENTRY}/DATA[{group}]/@axes"]
    return template[f"{ENTRY}/DATA[{group}]/AXISNAME[{axes[0]}]"]


@pytest.fixture(scope="module")
def spym_pages():
    """The raw pages as ``spym`` returns them, before any of our handling."""
    return {page.label: page for page in load(str(SM4_RAW_FILE))}


@pytest.fixture(scope="module")
def parsed():
    return Sm4Omicron(str(SM4_RAW_FILE)).parse()


@pytest.fixture(scope="module")
def template():
    return SPMReader().read(
        template=Template(),
        file_paths=(str(SM4_RAW_FILE), str(SM4_ELN_FILE)),
    )


class TestZCalibration:
    """``spym`` returns ADC counts and leaves the scale in the page attributes.

    Without applying it the field holds numbers many orders of magnitude away
    from the unit it is labelled with, and with the wrong sign whenever the
    scale is negative, which is the case for topography in the reference file.
    """

    @pytest.mark.parametrize("label", sorted(PAGE_TO_GROUP))
    def test_counts_are_converted_to_physical_values(self, parsed, spym_pages, label):
        page = spym_pages[label]
        expected = np.asarray(page.data) * page.attrs["RHK_Zscale"] + page.attrs.get(
            "RHK_Zoffset", 0.0
        )
        np.testing.assert_allclose(parsed[f"/{label}/data"], expected, rtol=0, atol=0)

    def test_topography_sign_follows_a_negative_scale(self, parsed, spym_pages):
        """The scale of this file is negative, so the counts must change sign."""
        page = spym_pages["Topography_Forward"]
        assert page.attrs["RHK_Zscale"] < 0
        assert np.all(np.asarray(page.data) > 0)
        assert np.all(parsed["/Topography_Forward/data"] < 0)

    def test_page_attributes_are_left_untouched(self, parsed, spym_pages):
        """Only the image is converted; the scale stays readable by a config."""
        page = spym_pages["Topography_Forward"]
        assert parsed["/Topography_Forward/RHK_Zscale"] == page.attrs["RHK_Zscale"]
        assert parsed["/Topography_Forward/RHK_Zoffset"] == page.attrs["RHK_Zoffset"]


class TestZCalibrationEdgeCases:
    """A page whose scale is unusable falls back to raw counts with a warning."""

    class _Page:
        """A stand-in for an ``spym`` page, holding only what the parser reads."""

        def __init__(self, z_scale, z_offset=0.0):
            self.label = "Stub_Page"
            self.data = np.array([[1.0, 2.0], [3.0, 4.0]])
            self.attrs = {"RHK_Zscale": z_scale, "RHK_Zoffset": z_offset}

    @pytest.mark.parametrize("z_scale", [None, 0])
    def test_unusable_scale_passes_counts_through(self, z_scale, caplog):
        page = self._Page(z_scale)
        with caplog.at_level("WARNING"):
            result = Sm4Omicron._calibrated_z(page)
        np.testing.assert_array_equal(result, page.data)
        assert "RHK_Zscale" in caplog.text

    def test_missing_offset_defaults_to_zero(self):
        page = self._Page(z_scale=2.0)
        del page.attrs["RHK_Zoffset"]
        np.testing.assert_array_equal(Sm4Omicron._calibrated_z(page), page.data * 2.0)

    def test_offset_is_added(self):
        page = self._Page(z_scale=2.0, z_offset=10.0)
        np.testing.assert_array_equal(
            Sm4Omicron._calibrated_z(page), page.data * 2.0 + 10.0
        )


class TestImageOrientation:
    """Row 0 of the stored signal must be the top row of the image.

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
        """``spym`` already returns both directions in the right x order."""
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
    def test_slow_axis_descends_so_its_first_value_labels_row_zero(
        self, template, group
    ):
        assert np.all(np.diff(_slow_axis(template, group)) < 0), (
            "the slow axis must descend with the row index"
        )

    @pytest.mark.parametrize("group", sorted(PAGE_TO_GROUP.values()))
    def test_slow_axis_length_matches_the_signal(self, template, group):
        assert len(_slow_axis(template, group)) == _signal(template, group).shape[0]
