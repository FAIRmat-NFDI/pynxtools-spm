"""Tests for the image orientation of Nanonis SXM scans (STM and AFM).

The convention of this plugin is the one of a scientific plot: the origin of an
image is its bottom-left corner. Row 0 of a stored signal is the bottom row,
column 0 is the left column, and both axes ascend so that their first value
labels that row and column.

A Nanonis SXM file stores the lines in the order they were recorded, and each
backward line in the order the tip traveled, from right to left. So the
stored image depends on the scan direction: an 'up' scan starts at the bottom
and is already in plot order, while a 'down' scan starts at the top and has to
be flipped. Gwyddion normalizes every scan to row 0 at the top, which makes it
a reference that does not depend on the direction: the stored signal must
equal 'np.flipud' of the Gwyddion channel for either direction.

The test data holds consecutive 'up' and 'down' scans of the same area. They
show the same surface, so once oriented the two images must agree without any
further flip, which checks the direction handling without Gwyddion.
"""

from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from gwyddionpy import load
from pynxtools.dataconverter.template import Template

from pynxtools_spm.nxformatters.nanonis.nanonis_base import NanonisBase
from pynxtools_spm.parsers.nanonispy.read import Scan
from pynxtools_spm.reader import SPMReader

NANONIS_DATA_DIR = Path(__file__).parent / "data" / "nanonis"
# Folders relative to NANONIS_DATA_DIR, as '<technique>/<folder>'.
IMAGE_FOLDERS = [
    "stm/v_gen_4_dflt_conf_up",
    "stm/v_gen_4_dflt_conf_down",
    "stm/v_gen_4_descrb_nx_dt_up",
    "stm/v_gen_4_descrb_nx_dt_down",
    "stm/v_gen_5_dflt_conf_down",
    "stm/v_gen_5_descrb_nx_dt_down",
    "stm/v_gen_5e_descrb_nx_dt_down",
    "afm/v_gen_4_dflt_conf_up",
    "afm/v_gen_4_descrb_nx_dt_up",
]
# Consecutive scans of the same area, recorded in opposite slow directions.
SAME_AREA_PAIRS = [
    ("stm/v_gen_4_dflt_conf_up", "stm/v_gen_4_dflt_conf_down"),
    ("stm/v_gen_4_descrb_nx_dt_up", "stm/v_gen_4_descrb_nx_dt_down"),
]
ENTRY = "/ENTRY[entry]"
FLIPS = {
    "none": lambda image: image,
    "flipud": np.flipud,
    "fliplr": np.fliplr,
    "flip": np.flip,
}


def _raw_file(folder: str) -> Path:
    return next((NANONIS_DATA_DIR / folder).glob("*.sxm"))


def _groups(template) -> list[str]:
    """Names of the NXdata groups written directly under the entry."""
    prefix = f"{ENTRY}/DATA["
    return sorted(
        {
            key[len(prefix) :].split("]", 1)[0]
            for key in template
            if key.startswith(prefix)
        }
    )


def _signal(template, group: str) -> np.ndarray:
    name = template[f"{ENTRY}/DATA[{group}]/@signal"]
    return template[f"{ENTRY}/DATA[{group}]/DATA[{name}]"]


def _axis(template, group: str, dim: int) -> np.ndarray:
    """The axis of dimension 'dim': 0 describes the rows, 1 the columns."""
    axes = template[f"{ENTRY}/DATA[{group}]/@axes"]
    return template[f"{ENTRY}/DATA[{group}]/AXISNAME[{axes[dim]}]"]


def _channels_by_group(raw_file: Path) -> dict:
    """The Gwyddion channels keyed by the NXdata group name they belong to.

    Gwyddion keeps the raw capitalization, so 'Z (Forward)' becomes 'z_forward'.
    """
    return {
        name.replace(" (", "_").rstrip(")").replace(" ", "_").lower(): channel
        for name, channel in load(str(raw_file)).channels.items()
    }


def _correlation(first: np.ndarray, second: np.ndarray) -> float:
    """Pearson correlation after removing each line's mean.

    Removing the line mean takes out the offset a feedback loop drifts through
    between lines, which would otherwise dominate two separate scans.
    """
    first = first - first.mean(axis=1, keepdims=True)
    second = second - second.mean(axis=1, keepdims=True)
    return float(np.corrcoef(first.ravel(), second.ravel())[0, 1])


@pytest.fixture(scope="module")
def templates():
    """One converted template per test folder, built on first use."""
    cache: dict[str, Template] = {}

    def build(folder: str) -> Template:
        if folder not in cache:
            directory = NANONIS_DATA_DIR / folder
            files = [_raw_file(folder), directory / "eln_data.yaml"]
            if (directory / "config.json").is_file():
                files.append(directory / "config.json")
            # 'SPMReader.read' annotates 'file_paths' as a one-element tuple,
            # although every call passes at least a raw file and an ELN.
            cache[folder] = SPMReader().read(
                template=Template(),
                file_paths=tuple(str(file) for file in files),  # type: ignore[arg-type]
            )
        return cache[folder]

    return build


def _scanner(direction: str) -> SimpleNamespace:
    """A stand-in for a formatter, holding only what the hook reads.

    The hook reads nothing but 'scan_control'; building a real formatter would
    need a raw file and an ELN just to reach a transformation of its argument.
    The axes are set by the real '_arange_axes', so the stand-in cannot drift
    from how a formatter records the scan direction.
    """
    scanner = SimpleNamespace(scan_control=SimpleNamespace())
    NanonisBase._arange_axes(scanner, direction)  # type: ignore[arg-type]
    return scanner


class TestScanAxes:
    """'_arange_axes' records the SXM scan direction for the orientation hook."""

    @pytest.mark.parametrize(
        "direction,slow_axis",
        [
            ("up", "+y"),
            ("down", "-y"),
            ("UP", "+y"),
            (" Down ", "-y"),
            # An empty tag, as in the v4 files, leaves the direction unknown.
            ("", "y"),
            ("sideways", "y"),
        ],
    )
    def test_lines_run_along_x_and_advance_along_the_scan_direction(
        self, direction, slow_axis
    ):
        scan_control = _scanner(direction).scan_control
        assert scan_control.fast_axis == "x"
        assert scan_control.slow_axis == slow_axis

    @pytest.mark.parametrize("direction", ["", "sideways"])
    def test_unknown_direction_keeps_the_recorded_order(self, direction):
        data = np.arange(12).reshape(3, 4)
        np.testing.assert_array_equal(
            NanonisBase.rearrange_data_according_to_axes(
                _scanner(direction), data, True
            ),
            data,
        )


class TestOrientationHook:
    """'rearrange_data_according_to_axes' puts the origin at the bottom left."""

    @pytest.mark.parametrize(
        "direction,is_forward,expected",
        [
            ("up", True, "none"),
            ("up", None, "none"),
            ("up", False, "fliplr"),
            ("down", True, "flipud"),
            ("down", None, "flipud"),
            ("down", False, "flip"),
        ],
    )
    def test_flip_follows_scan_and_line_direction(
        self, direction, is_forward, expected
    ):
        data = np.arange(12).reshape(3, 4)
        np.testing.assert_array_equal(
            NanonisBase.rearrange_data_according_to_axes(
                _scanner(direction), data, is_forward
            ),
            FLIPS[expected](data),
        )

    def test_non_square_image_is_flipped_along_both_dimensions(self):
        data = np.arange(6).reshape(3, 2)
        np.testing.assert_array_equal(
            NanonisBase.rearrange_data_according_to_axes(_scanner("down"), data, False),
            np.flip(data),
        )

    @pytest.mark.parametrize("data", [np.arange(4), np.arange(8).reshape(2, 2, 2)])
    def test_non_image_data_is_left_alone(self, data):
        np.testing.assert_array_equal(
            NanonisBase.rearrange_data_according_to_axes(_scanner("down"), data, False),
            data,
        )

    def test_data_without_scan_axes_is_left_alone(self):
        """Bias spectroscopy has no scan control and so no axes to orient by."""
        data = np.arange(6).reshape(3, 2)
        spectroscopy = SimpleNamespace(scan_control=SimpleNamespace())
        np.testing.assert_array_equal(
            NanonisBase.rearrange_data_according_to_axes(spectroscopy, data, False),
            data,
        )


@pytest.mark.parametrize("folder", IMAGE_FOLDERS)
class TestStoredImages:
    """Every image of a converted scan follows the bottom-left convention."""

    def test_folder_holds_an_image_for_each_direction_of_z(self, templates, folder):
        groups = _groups(templates(folder))
        assert {"z_forward", "z_backward"} <= set(groups)

    def test_signal_is_the_gwyddion_channel_flipped_upside_down(
        self, templates, folder
    ):
        template = templates(folder)
        channels = _channels_by_group(_raw_file(folder))
        compared = 0
        for group in _groups(template):
            channel = channels.get(group)
            if channel is None:
                continue
            np.testing.assert_allclose(
                _signal(template, group),
                np.flipud(channel.data),
                rtol=1e-6,
                err_msg=f"{folder}/{group}",
            )
            compared += 1
        assert compared >= 2, "no NXdata group matched a Gwyddion channel"

    @pytest.mark.parametrize("dim", [0, 1])
    def test_axes_ascend_and_match_the_signal(self, templates, folder, dim):
        template = templates(folder)
        for group in _groups(template):
            axis = _axis(template, group, dim)
            assert len(axis) == _signal(template, group).shape[dim], group
            assert np.all(np.diff(axis) > 0), f"{group}: axis {dim} must ascend"

    def test_axes_are_pixel_centres_around_the_scan_offset(self, templates, folder):
        header = Scan(str(_raw_file(folder))).header
        (x_offset, y_offset), (x_range, y_range) = (
            header["scan_offset"],
            header["scan_range"],
        )
        template = templates(folder)
        for group in _groups(template):
            for dim, offset, scan_range in (
                (1, x_offset, x_range),
                (0, y_offset, y_range),
            ):
                axis = _axis(template, group, dim)
                step = scan_range / len(axis)
                np.testing.assert_allclose(
                    [axis[0], axis[-1]],
                    [
                        offset - scan_range / 2 + step / 2,
                        offset + scan_range / 2 - step / 2,
                    ],
                    rtol=1e-9,
                    err_msg=f"{folder}/{group} axis {dim}",
                )


@pytest.mark.parametrize("up,down", SAME_AREA_PAIRS)
@pytest.mark.parametrize("group", ["z_forward", "z_backward"])
def test_up_and_down_scans_of_one_area_agree_without_a_flip(templates, up, down, group):
    """The scan direction changes when the lines were recorded, not the image."""
    up_image = _signal(templates(up), group)
    down_image = _signal(templates(down), group)
    scores = {
        name: _correlation(up_image, flip(down_image)) for name, flip in FLIPS.items()
    }
    assert max(scores, key=scores.get) == "none", scores
