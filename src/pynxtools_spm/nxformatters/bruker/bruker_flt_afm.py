#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Formatter for Bruker (SPMLab) AFM data from .FLT files."""

from __future__ import annotations

import datetime
import re
from pathlib import Path

import numpy as np
from pynxtools import logger as pynx_logger
from pynxtools.dataconverter.template import Template
from pynxtools.units import ureg

from pynxtools_spm.configs import load_default_config
from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
import pynxtools_spm.nxformatters.helpers as fhs
from pynxtools_spm.nxformatters.helpers import _get_data_unit_and_others, unit_short

# A .FLT file stores exactly one channel, so the parser nests every value under
# the channel name (e.g. '/Height/data'). The config cannot know that name, so
# it spells the prefix as this literal placeholder and the formatter resolves it
# once, when the config is loaded.
CHANNEL_PLACEHOLDER = "/CHANNEL/"

# SPMLab writes e.g. 'Jun.17.2026 08:03:43' — neither ISO 8601 nor the
# '%I:%M:%S %p %a %b %d %Y' form of the NanoScope TXT export.
SPMLAB_TIMESTAMP = re.compile(
    r"^(?P<month>[A-Za-z]{3})\.(?P<day>\d{1,2})\.(?P<year>\d{4})\s+"
    r"(?P<hour>\d{1,2}):(?P<minute>\d{2}):(?P<second>\d{2})$"
)

# Matched explicitly rather than through '%b', whose meaning depends on the
# active locale and would make parsing environment-dependent.
_MONTH_ABBR_TO_NUM = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


class BrukerFltAFM(BrukerBase):
    """Formatter for Bruker AFM image data from SPMLab .FLT files.

    Unlike ``BrukerSpmAFM``, this formatter does not build the ``scan_region``
    group: the SPMLab header exposes ``OffsetX``/``OffsetY``,
    ``ScanRangeX``/``ScanRangeY`` and ``Rotation`` as plain scalars that the
    config maps one-to-one onto the NeXus fields, so the generic config walker
    writes them. Only the mesh-scan step sizes and the NXdata axes need code,
    because both are derived quantities.
    """

    _grp_to_func: dict[str, str] = {
        "SPM_SCAN_CONTROL[spm_scan_control]": "_construct_nxscan_controllers",
        "start_time": "_set_start_end_time",
    }
    _axes = ["x", "y", "z"]

    def __init__(
        self,
        template: Template,
        raw_file: str | Path,
        eln_file: str | Path | None = None,
        config_file: str | Path | None = None,
        auxiliary_files: list[str | Path] | None = None,
        entry: str | None = None,
    ):
        super().__init__(
            template, raw_file, eln_file, config_file, auxiliary_files, entry
        )

    def get_nxformatted_template(self):
        self.walk_though_config_nested_dict(self.config_dict, "")
        self._format_template_from_eln()
        self._handle_special_fields()
        return self.template

    # ------------------------------------------------------------------
    # Config loading and channel-placeholder resolution
    # ------------------------------------------------------------------

    def _get_conf_dict(self, config_file: str | Path = None):
        config_dict = (
            fhs.read_config_file(config_file)
            if config_file
            else load_default_config(config_type="bruker_flt_afm")
        )
        return self._resolve_channel_placeholder(config_dict)

    def _get_channel_name(self) -> str | None:
        """Return the name of the single channel stored in the .FLT file.

        The image array is the one unambiguous marker of a channel group, so
        the name is taken from the key holding it ('/Height/data' -> 'Height')
        rather than from a header field, which may be absent or renamed.
        """
        for key, val in self.raw_data.items():
            if key.endswith("/data") and isinstance(val, np.ndarray):
                return key.split("/")[1]
        return None

    def _resolve_channel_placeholder(self, config_dict: dict) -> dict:
        """Replace '/CHANNEL/' in every raw path with the actual channel prefix.

        Done once here rather than through the 'func_on_raw_key' argument of
        ``walk_though_config_nested_dict``, because the base implementation of
        ``_nxdata_grp_from_conf_description`` does not forward that callable;
        the NXdata signal would then never resolve and the group would be
        silently dropped.
        """
        channel = self._get_channel_name()
        if channel is None:
            pynx_logger.warning(
                "No channel data found in %s, so the '%s' placeholder in the "
                "config cannot be resolved.",
                self.raw_file,
                CHANNEL_PLACEHOLDER,
            )
            return config_dict

        prefix = f"/{channel}/"

        def substitute(node):
            if isinstance(node, dict):
                return {key: substitute(val) for key, val in node.items()}
            if isinstance(node, list):
                return [substitute(item) for item in node]
            if isinstance(node, str):
                return node.replace(CHANNEL_PLACEHOLDER, prefix)
            return node

        return substitute(config_dict)

    # ------------------------------------------------------------------
    # Timestamp handling (registered in _grp_to_func)
    # ------------------------------------------------------------------

    def _set_start_end_time(self, end_dict: dict, parent_path: str, group_name: str):
        """Write the SPMLab 'CreationTime' to the template as ISO 8601."""
        raw_date, _, _ = _get_data_unit_and_others(
            data_dict=self.raw_data, end_dict=end_dict
        )
        if not isinstance(raw_date, str) or not raw_date.strip():
            return

        match = SPMLAB_TIMESTAMP.match(raw_date.strip())
        if match is None:
            pynx_logger.warning(
                "Could not parse Bruker SPMLab date '%s' for field '%s'.",
                raw_date,
                group_name,
            )
            return

        month = _MONTH_ABBR_TO_NUM.get(match.group("month").lower())
        if month is None:
            pynx_logger.warning(
                "Unknown month abbreviation '%s' in Bruker SPMLab date '%s'.",
                match.group("month"),
                raw_date,
            )
            return

        date_time = datetime.datetime(
            year=int(match.group("year")),
            month=month,
            day=int(match.group("day")),
            hour=int(match.group("hour")),
            minute=int(match.group("minute")),
            second=int(match.group("second")),
        )
        self.template[f"{parent_path}/{group_name}"] = date_time.isoformat()

    # ------------------------------------------------------------------
    # Scan-controller hook (registered in _grp_to_func)
    # ------------------------------------------------------------------

    def _construct_nxscan_controllers(
        self,
        partial_conf_dict,
        parent_path: str,
        group_name: str = "scan_control",
        **kwarg,
    ):
        scan_region_grp = "scan_region"
        scan_region_dict = partial_conf_dict.get(scan_region_grp)
        if scan_region_dict is not None:
            self.construct_scan_region_grp(
                partial_conf_dict=scan_region_dict,
                parent_path=f"{parent_path}/{group_name}",
                group_name=scan_region_grp,
            )

        scan_pattern_grp = "meshSCAN[mesh_scan]"
        scan_pattern_dict = partial_conf_dict.get(scan_pattern_grp)
        if scan_pattern_dict is not None:
            self.construct_scan_pattern_grp(
                partial_conf_dict=scan_pattern_dict,
                parent_path=f"{parent_path}/{group_name}",
                group_name=scan_pattern_grp,
            )

    def _read_xy_fields(
        self, partial_conf_dict: dict, field_key: str
    ) -> dict[str, tuple]:
        """Read a variadic x/y field pair into ``{'x': (value, unit), ...}``.

        The config entries are read without mutating them (``next(iter(...))``
        rather than ``popitem()``), because the walker recurses into the same
        dicts afterwards to write the fields themselves.
        """
        values: dict[str, tuple] = {}
        field_list = partial_conf_dict.get(field_key)
        if not (isinstance(field_list, list) and field_list):
            return values

        for item in field_list:
            if not isinstance(item, dict) or not item:
                continue
            key_ext, end_dict = next(iter(item.items()))
            if not isinstance(end_dict, dict):
                continue
            data, unit, _ = _get_data_unit_and_others(
                data_dict=self.raw_data, end_dict=end_dict
            )
            if data in ("", None):
                continue
            axis = key_ext.strip("_").lower()
            if axis in ("x", "y"):
                values[axis] = (data, unit)
        return values

    def construct_scan_region_grp(
        self,
        partial_conf_dict: dict,
        parent_path: str,
        group_name: str = "scan_region",
    ):
        """Construct the scan region group from the SPMLab header.

        ``scan_offset_value`` and ``scan_range`` each map onto a single header
        key, but ``scan_start`` and ``scan_end`` are derived from both and have
        no header key of their own, so the whole group is written here through
        ``put_scan_2d_region_field_in_template``. The config marks the four
        header-backed fields with '#note' to keep the config walker from
        writing them a second time.

        ``scan_start``/``scan_end`` follow Gwyddion's reading of the SPMLab
        header, in which ``OffsetX``/``OffsetY`` is the origin (corner) of the
        frame, so that x runs from ``offset`` to ``offset + range``. Note this
        differs from NanoScope .spm, where Bruker documents the offset as the
        *centre* of the scan. See ``nxformatters/bruker/README.md``.

        The cached values are reused for the two derived quantities that need
        code — the mesh-scan step sizes and the NXdata axis arrays.
        """
        offsets = self._read_xy_fields(
            partial_conf_dict, "scan_offset_valueN[scan_offset_value_n]"
        )
        ranges = self._read_xy_fields(partial_conf_dict, "scan_rangeN[scan_range_n]")

        for axis, (offset, unit) in offsets.items():
            setattr(self.scan_control, f"{axis}_offset", offset)
            setattr(self.scan_control, f"{axis}_offset_unit", unit)
        for axis, (scan_range, unit) in ranges.items():
            setattr(self.scan_control, f"{axis}_range", scan_range)
            setattr(self.scan_control, f"{axis}_range_unit", unit)

        for axis in ("x", "y"):
            offset = getattr(self.scan_control, f"{axis}_offset")
            offset_unit = getattr(self.scan_control, f"{axis}_offset_unit")
            scan_range = getattr(self.scan_control, f"{axis}_range")
            range_unit = getattr(self.scan_control, f"{axis}_range_unit")
            if offset is None or scan_range is None:
                continue

            if offset_unit and range_unit and offset_unit != range_unit:
                try:
                    scan_range = (
                        ureg.Quantity(scan_range, range_unit).to(offset_unit).magnitude
                    )
                except Exception as error:
                    pynx_logger.warning(
                        "Could not convert %s scan range from '%s' to '%s': %s. "
                        "Scan start and end are skipped for this axis.",
                        axis,
                        range_unit,
                        offset_unit,
                        error,
                    )
                    continue

            unit = offset_unit or range_unit
            setattr(self.scan_control, f"{axis}_start", offset)
            setattr(self.scan_control, f"{axis}_start_unit", unit)
            setattr(self.scan_control, f"{axis}_end", offset + scan_range)
            setattr(self.scan_control, f"{axis}_end_unit", unit)

        self.put_scan_2d_region_field_in_template(parent_path, group_name)

    def construct_scan_pattern_grp(
        self,
        partial_conf_dict: dict,
        parent_path: str,
        group_name: str = "meshSCAN[mesh_scan]",
    ):
        """Collect the point counts and write the derived step sizes."""
        points = self._read_xy_fields(partial_conf_dict, "scan_pointsN[scan_points_n]")
        if not points:
            pynx_logger.warning(
                "Scan points information is missing or not in expected format. "
                "Please check config file and raw data."
            )
        for axis, (data, _) in points.items():
            setattr(self.scan_control, f"{axis}_points", data)

        # SPMLab records the raster orientation in 'Rotation', which is 0 in
        # every file seen so far. A rotated frame would make 'x' and 'y' the
        # wrong names for the fast and slow axis.
        self.scan_control.fast_axis = "x"
        self.scan_control.slow_axis = "y"

        for axis in ("x", "y"):
            scan_range = getattr(self.scan_control, f"{axis}_range")
            n_points = getattr(self.scan_control, f"{axis}_points")
            if scan_range is None or not n_points or int(n_points) < 2:
                continue
            step_key = f"{parent_path}/{group_name}/step_sizeN[step_size_{axis}]"
            self.template[step_key] = scan_range / (int(n_points) - 1)
            self.template[f"{step_key}/@units"] = getattr(
                self.scan_control, f"{axis}_range_unit"
            )

        self.put_scan_pattern_field_in_template(
            parent_path=parent_path, group_name=group_name
        )

    # ------------------------------------------------------------------
    # NXdata axes
    # ------------------------------------------------------------------

    def _nxdata_grp_from_conf_description(
        self,
        partial_conf_dict,
        parent_path: str,
        group_name: str,
        group_index=0,
        is_forward: bool | None = None,
        rearrange_2d_data: bool = False,
    ):
        """Attach physical x and y axes to the NXdata group.

        The SPMLab config describes no axes of its own (there are no '0'/'1'
        entries), because the .FLT header stores the scan geometry as scalars
        rather than as coordinate arrays. The axes are therefore built here
        from the cached scan region.
        """
        nxdata_group = super()._nxdata_grp_from_conf_description(
            partial_conf_dict,
            parent_path,
            group_name,
            group_index,
            is_forward,
            rearrange_2d_data,
        )

        if nxdata_group is None:
            return None

        # Axes described in the config take precedence over the derived ones.
        if "0" in partial_conf_dict or "1" in partial_conf_dict:
            return nxdata_group

        nxdata_path = f"{parent_path}/{nxdata_group}"
        signal_name = self.template.get(f"{nxdata_path}/@signal")
        if not signal_name:
            return nxdata_group
        signal_data = self.template.get(f"{nxdata_path}/DATA[{signal_name}]")
        if not (isinstance(signal_data, np.ndarray) and signal_data.ndim == 2):
            return nxdata_group

        scan_control = self.scan_control
        if scan_control.x_start is None or scan_control.y_start is None:
            pynx_logger.warning(
                "Scan region is unknown, so no physical axes are attached to '%s'.",
                nxdata_path,
            )
            return nxdata_group

        # The raster is stored row by row: the first index runs along the slow
        # (y) axis and the second along the fast (x) axis. Row 0 holds the
        # lowest y, so y ascends with the row index.
        n_y, n_x = signal_data.shape
        axis_to_data = {
            "y": np.linspace(scan_control.y_start, scan_control.y_end, n_y),
            "x": np.linspace(scan_control.x_start, scan_control.x_end, n_x),
        }

        for index, (axis, axis_data) in enumerate(axis_to_data.items()):
            axis_key = f"{nxdata_path}/AXISNAME[{axis}]"
            unit = getattr(scan_control, f"{axis}_start_unit")
            self.template[axis_key] = axis_data
            self.template[f"{axis_key}/@units"] = unit
            if unit:
                self.template[f"{axis_key}/@long_name"] = f"{axis} ({unit_short(unit)})"
            self.template[f"{nxdata_path}/@AXISNAME_indices[{axis}_indices]"] = index

        self.template[f"{nxdata_path}/@axes"] = list(axis_to_data)

        return nxdata_group
