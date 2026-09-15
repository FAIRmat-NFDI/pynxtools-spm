"""Tests for the image orientation of Bruker NanoScope '.spm' and SPMLab '.FLT' scans.

The convention of this plugin is the one of a scientific plot: the origin of an
image is its bottom-left corner. Row 0 of a stored signal is the bottom row,
column 0 is the left column, and both axes ascend.

Both formats store the rows in a fixed order, bottom row first: a NanoScope
file for a 'Frame direction' of Up and of Down alike, and an SPMLab file, which
records no slow scan direction at all. Gwyddion turns every image of either
format upside down once, so a correctly stored signal is 'np.flipud' of the
Gwyddion channel.
"""

import re
from pathlib import Path

import numpy as np
import pytest
from gwyddionpy import load
from pynxtools.dataconverter.template import Template

from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
from pynxtools_spm.reader import SPMReader

SPM_DATA_DIR = Path(__file__).parent / "data" / "bruker" / "afm"
# Folder name -> the 'Frame direction' its raw file was recorded with.
SPM_FOLDERS = {
    "spm_v_9_4_dflt_conf_down": "Down",
    "spm_v_9_4_dflt_conf_up": "Up",
}
ENTRY = "/ENTRY[entry]"


def _raw_file(folder: str) -> Path:
    return next((SPM_DATA_DIR / folder).glob("*.spm"))


def _header_values(raw_file: Path, key: str) -> list[str]:
    """All values of a backslash-prefixed key in the ASCII header."""
    with open(raw_file, "rb") as file_obj:
        header = file_obj.read(200_000).decode("latin-1")
    return re.findall(rf"\\{re.escape(key)}:\s*([^\r\n]*)", header)


def _groups(template) -> list[str]:
    """Names of the NXdata groups with a two dimensional signal."""
    prefix = f"{ENTRY}/DATA["
    names = {
        key[len(prefix) :].split("]", 1)[0]
        for key in template
        if key.startswith(prefix)
    }
    return sorted(name for name in names if np.ndim(_signal(template, name)) == 2)


def _signal(template, group: str) -> np.ndarray:
    name = template[f"{ENTRY}/DATA[{group}]/@signal"]
    return template[f"{ENTRY}/DATA[{group}]/DATA[{name}]"]


def _axis(template, group: str, dim: int) -> np.ndarray:
    """The axis of dimension 'dim': 0 describes the rows, 1 the columns."""
    axes = template[f"{ENTRY}/DATA[{group}]/@axes"]
    return template[f"{ENTRY}/DATA[{group}]/AXISNAME[{axes[dim]}]"]


def _correlation(first: np.ndarray, second: np.ndarray) -> float:
    """Pearson correlation; the parser rescales values, so equality is too strict."""
    return float(np.corrcoef(np.ravel(first), np.ravel(second))[0, 1])


@pytest.fixture(scope="module")
def templates():
    """One converted template per test folder, built on first use."""
    cache: dict[str, Template] = {}

    def build(folder: str) -> Template:
        if folder not in cache:
            files = (_raw_file(folder), SPM_DATA_DIR / folder / "eln_data.yaml")
            # 'SPMReader.read' annotates 'file_paths' as a one-element tuple,
            # although every call passes at least a raw file and an ELN.
            cache[folder] = SPMReader().read(
                template=Template(),
                file_paths=tuple(str(file) for file in files),  # type: ignore[arg-type]
            )
        return cache[folder]

    return build


class TestOrientationHook:
    """'rearrange_data_according_to_axes' puts the origin at the bottom left.

    The hook is called through the class with 'None' in place of 'self': it
    reads nothing off the instance, and building one would need a raw file and
    an ELN just to reach a transformation of its argument.
    """

    @pytest.mark.parametrize("is_forward", [True, False, None])
    def test_every_image_is_turned_upside_down(self, is_forward):
        data = np.arange(12).reshape(3, 4)
        np.testing.assert_array_equal(
            BrukerBase.rearrange_data_according_to_axes(None, data, is_forward),  # type: ignore[arg-type]
            np.flipud(data),
        )

    @pytest.mark.parametrize("data", [np.arange(4), np.arange(8).reshape(2, 2, 2)])
    def test_non_image_data_is_left_alone(self, data):
        np.testing.assert_array_equal(
            BrukerBase.rearrange_data_according_to_axes(None, data),  # type: ignore[arg-type]
            data,
        )


@pytest.mark.parametrize("folder", sorted(SPM_FOLDERS))
class TestStoredImages:
    """Every image of a converted scan follows the bottom-left convention."""

    def test_raw_file_has_the_frame_direction_of_its_folder(self, folder):
        assert set(_header_values(_raw_file(folder), "Frame direction")) == {
            SPM_FOLDERS[folder]
        }

    def test_signal_is_a_gwyddion_channel_turned_upside_down(self, templates, folder):
        template = templates(folder)
        channels = [
            np.asarray(channel.data, float)
            for channel in load(str(_raw_file(folder))).channels.values()
        ]
        groups = _groups(template)
        assert groups, "no two dimensional NXdata group was written"
        for group in groups:
            signal = np.asarray(_signal(template, group), float)
            same_shape = [
                channel for channel in channels if channel.shape == signal.shape
            ]
            scores = [
                _correlation(signal, np.flipud(channel)) for channel in same_shape
            ]
            assert max(scores) > 0.9999, f"{folder}/{group}"

    @pytest.mark.parametrize("dim", [0, 1])
    def test_axes_ascend_and_match_the_signal(self, templates, folder, dim):
        template = templates(folder)
        for group in _groups(template):
            axis = _axis(template, group, dim)
            assert len(axis) == np.shape(_signal(template, group))[dim], group
            assert np.all(np.diff(axis) > 0), f"{group}: axis {dim} must ascend"

    def test_axes_span_the_scan_size(self, templates, folder):
        scan_size = float(_header_values(_raw_file(folder), "Scan Size")[0].split()[0])
        template = templates(folder)
        for group in _groups(template):
            for dim in (0, 1):
                axis = _axis(template, group, dim)
                assert axis[-1] - axis[0] == pytest.approx(scan_size), (
                    f"{group} axis {dim}"
                )


# SPMLab '.FLT' stores no slow scan direction; Gwyddion turns every image upside
# down once as well, so the same flip applies.
FLT_FOLDERS = ["flt_dflt_conf", "flt_descrb_nx_dt"]


def _flt_header(raw_file: Path) -> dict[str, str]:
    """The 'key=value' lines of the ASCII header of an SPMLab '.FLT' file."""
    with open(raw_file, "rb") as file_obj:
        header = file_obj.read(4000).decode("latin-1")
    return {
        key: value.strip()
        for key, value in re.findall(r"^(\w+)=([^\r\n]*)", header, re.MULTILINE)
    }


def _flt_template(folder: str) -> Template:
    directory = SPM_DATA_DIR / folder
    files = [next(directory.glob("*.FLT")), directory / "eln_data.yaml"]
    if (directory / "config.json").is_file():
        files.append(directory / "config.json")
    return SPMReader().read(
        template=Template(),
        file_paths=tuple(str(file) for file in files),  # type: ignore[arg-type]
    )


def _all_2d_groups(template) -> list[str]:
    """Paths of every NXdata group with a two dimensional signal."""
    return sorted(
        {
            key.rsplit("/@signal", 1)[0]
            for key in template
            if key.endswith("/@signal")
            and np.ndim(
                template[f"{key.rsplit('/@signal', 1)[0]}/DATA[{template[key]}]"]
            )
            == 2
        }
    )


@pytest.mark.parametrize("folder", FLT_FOLDERS)
class TestStoredFltImages:
    """Every SPMLab image follows the bottom-left convention."""

    def test_signal_is_the_gwyddion_channel_turned_upside_down(self, folder):
        template = _flt_template(folder)
        raw_file = next((SPM_DATA_DIR / folder).glob("*.FLT"))
        (channel,) = load(str(raw_file)).channels.values()
        groups = _all_2d_groups(template)
        assert groups, "no two dimensional NXdata group was written"
        for group in groups:
            signal = template[f"{group}/DATA[{template[f'{group}/@signal']}]"]
            assert _correlation(signal, np.flipud(channel.data)) > 0.9999, group

    def test_axes_ascend_and_span_the_scan_range(self, folder):
        template = _flt_template(folder)
        header = _flt_header(next((SPM_DATA_DIR / folder).glob("*.FLT")))
        for group in _all_2d_groups(template):
            signal = template[f"{group}/DATA[{template[f'{group}/@signal']}]"]
            axes = template[f"{group}/@axes"]
            for dim, key in ((0, "ScanRangeY"), (1, "ScanRangeX")):
                axis = template[f"{group}/AXISNAME[{axes[dim]}]"]
                scan_range = float(header[key].split()[0])
                assert len(axis) == np.shape(signal)[dim], group
                assert np.all(np.diff(axis) > 0), f"{group}: axis {dim} must ascend"
                assert axis[-1] - axis[0] == pytest.approx(scan_range), group
