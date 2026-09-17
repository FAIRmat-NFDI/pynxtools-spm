"""Tests for the image orientation of RHK SM4 scans read by the Omicron formatter.

The convention of this plugin is the one of a scientific plot: the origin of an
image is its bottom-left corner. Row 0 of a stored signal is the bottom row,
column 0 is the left column, and both axes ascend.

An SM4 page stores row i at y = RHK_Yoffset + i * RHK_Yscale, so the sign of
'RHK_Yscale' is the slow scan direction: > 0 up, < 0 down. Gwyddion flips the
rows of an up scan and always flips the columns, so it returns every image with
row 0 at the top, and a correctly stored signal is 'np.flipud' of the Gwyddion
channel for either direction.
"""

from pathlib import Path

import numpy as np
import pytest
from gwyddionpy import load
from pynxtools.dataconverter.template import Template

from pynxtools_spm.parsers.rhk_sm4_metadata import read_sm4_pages
from pynxtools_spm.reader import SPMReader

SM4_DATA_DIR = Path(__file__).parent / "data" / "omicron" / "stm"
# Folder name -> the sign of 'RHK_Yscale' of its raw file (+1 up, -1 down).
SM4_FOLDERS = {
    "sm4_dflt_conf_up": 1,
    "sm4_dflt_conf_down": -1,
}
ENTRY = "/ENTRY[entry]"


def _raw_file(folder: str) -> Path:
    directory = SM4_DATA_DIR / folder
    return next(path for path in directory.iterdir() if path.suffix.lower() == ".sm4")


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
    return float(np.corrcoef(np.ravel(first), np.ravel(second))[0, 1])


@pytest.fixture(scope="module")
def templates():
    """One converted template per test folder, built on first use."""
    cache: dict[str, Template] = {}

    def build(folder: str) -> Template:
        if folder not in cache:
            files = (_raw_file(folder), SM4_DATA_DIR / folder / "eln_data.yaml")
            # 'SPMReader.read' annotates 'file_paths' as a one-element tuple,
            # although every call passes at least a raw file and an ELN.
            cache[folder] = SPMReader().read(
                template=Template(),
                file_paths=tuple(str(file) for file in files),  # type: ignore[arg-type]
            )
        return cache[folder]

    return build


@pytest.mark.parametrize("folder", sorted(SM4_FOLDERS))
class TestStoredImages:
    """Every image of a converted scan follows the bottom-left convention."""

    def test_raw_file_has_the_scan_direction_of_its_folder(self, folder):
        signs = {
            int(np.sign(page.attrs["RHK_Yscale"]))
            for page in read_sm4_pages(_raw_file(folder))
            if page.is_image
        }
        assert signs == {SM4_FOLDERS[folder]}

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
            scores = [
                abs(_correlation(signal, np.flipud(channel)))
                for channel in channels
                if channel.shape == signal.shape and channel.std() > 0
            ]
            assert max(scores) > 0.9999, f"{folder}/{group}"

    @pytest.mark.parametrize("dim", [0, 1])
    def test_axes_ascend_and_match_the_signal(self, templates, folder, dim):
        template = templates(folder)
        for group in _groups(template):
            axis = _axis(template, group, dim)
            assert len(axis) == np.shape(_signal(template, group))[dim], group
            assert np.all(np.diff(axis) > 0), f"{group}: axis {dim} must ascend"
