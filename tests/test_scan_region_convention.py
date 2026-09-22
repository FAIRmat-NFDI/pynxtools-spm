"""The scan region convention, checked on the reference file of every flavour.

The convention itself is described in 'tests/README.md': the scan offset is the
centre of the scanned area, so 'scan_start' and 'scan_end' are
'offset -/+ range/2' and the axis values are the pixel centres around the
offset. Axis names are upper case, '@axes' is [slow, fast] and
'independent_scan_axes' lists the axes from the fastest to the slowest, with
the scan direction as the sign of the name.

The per-flavour tests cover how each raw format is read; this one only checks
that every written file agrees with the convention.
"""

import glob
import os
import re

import h5py
import numpy as np
import pytest

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
REFERENCE_FILES = sorted(glob.glob(f"{MODULE_DIR}/data/**/*.nxs", recursive=True))
AXIS_NAME = re.compile(r"^[+-]?[A-Z][A-Z_]*$")


def _text(value):
    return value.decode() if isinstance(value, bytes) else value


def _scan_regions(h5_file):
    """Every group holding a 2D scan region, keyed by the group path."""
    fields = ("scan_offset_value", "scan_range", "scan_start", "scan_end")
    groups: dict[str, dict[str, float]] = {}

    def visit(name, obj):
        parent, _, field = name.rpartition("/")
        if isinstance(obj, h5py.Dataset) and field.startswith(fields):
            groups.setdefault(parent, {})[field] = float(obj[()])

    h5_file.visititems(visit)
    return {
        path: values
        for path, values in groups.items()
        if {"scan_offset_value_x", "scan_range_x"} <= values.keys()
    }


def _region_of(image_path: str, regions: dict[str, dict[str, float]]):
    """The scan region that describes one NXdata group.

    An image nested under a scan control group takes that group's region. An
    image written at entry level is not tied to a region by the file, so the
    regions must agree on the offsets; that is asserted here rather than
    assumed, because a file whose regions disagree would otherwise be compared
    against an arbitrary one of them.
    """
    for path, values in regions.items():
        scan_control = path.rsplit("/", 1)[0]
        if image_path.startswith(f"{scan_control}/"):
            return values

    for axis in ("x", "y"):
        offsets = [values[f"scan_offset_value_{axis}"] for values in regions.values()]
        assert max(offsets) == pytest.approx(min(offsets)), (
            f"{image_path}: the file holds scan regions with different "
            f"{axis} offsets ({min(offsets)} to {max(offsets)}), so no single "
            "region describes this image"
        )
    return next(iter(regions.values()))


def _images(h5_file):
    """Every NXdata group with two axes, as (path, axis names, group)."""
    images = []

    def visit(name, obj):
        axes = obj.attrs.get("axes") if isinstance(obj, h5py.Group) else None
        if axes is None:
            return
        names = [_text(axis) for axis in np.atleast_1d(axes)]
        if len(names) == 2:
            images.append((name, names, obj))

    h5_file.visititems(visit)
    return images


def _independent_scan_axes(h5_file):
    found = []

    def visit(name, obj):
        if isinstance(obj, h5py.Dataset) and name.endswith("independent_scan_axes"):
            found.append([_text(axis) for axis in np.atleast_1d(obj[()])])

    h5_file.visititems(visit)
    return found


@pytest.fixture(
    params=REFERENCE_FILES, ids=lambda path: os.path.relpath(path, MODULE_DIR)
)
def image_file(request):
    """An open reference file that holds a 2D scan; the others are skipped."""
    with h5py.File(request.param, "r") as h5_file:
        if not _scan_regions(h5_file):
            pytest.skip("no 2D scan region: a bias sweep or a force ramp")
        yield h5_file


def test_start_and_end_bracket_the_offset(image_file):
    """scan_start/scan_end are offset -/+ range/2 on both axes."""
    for region in _scan_regions(image_file).values():
        for axis in ("x", "y"):
            offset = region[f"scan_offset_value_{axis}"]
            half = region[f"scan_range_{axis}"] / 2
            assert region[f"scan_start_{axis}"] == pytest.approx(offset - half)
            assert region[f"scan_end_{axis}"] == pytest.approx(offset + half)


def test_axes_are_upper_case_and_centred_on_the_offset(image_file):
    """'@axes' is [Y, X], both ascend, and their midpoint is the scan offset."""
    regions = _scan_regions(image_file)
    images = _images(image_file)
    assert images, "a 2D scan must write at least one NXdata group with two axes"
    for path, names, group in images:
        assert names == ["Y", "X"], path
        region = _region_of(path, regions)
        for name in names:
            values = group[name][()]
            assert np.all(np.diff(values) > 0), f"{path}: {name} must ascend"
            midpoint = (values[0] + values[-1]) / 2
            offset = region[f"scan_offset_value_{name.lower()}"]
            assert midpoint == pytest.approx(offset), f"{path}: {name}"


def test_independent_scan_axes_runs_fast_to_slow(image_file):
    """Every 2D scan names its axes fastest first, upper case, sign optional."""
    written = _independent_scan_axes(image_file)
    assert written, "a 2D scan must write independent_scan_axes"
    for axes in written:
        assert [name.lstrip("+-") for name in axes] == ["X", "Y"]
        for name in axes:
            assert AXIS_NAME.match(name), name
