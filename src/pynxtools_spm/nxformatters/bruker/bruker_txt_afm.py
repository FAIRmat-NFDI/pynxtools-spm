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

"""Formatter for Bruker AFM data from TXT (force-curve) export files."""

from __future__ import annotations

import datetime
from pathlib import Path

from pynxtools import logger as pynx_logger
from pynxtools.dataconverter.template import Template
from pynxtools.units import ureg

from pynxtools_spm.configs import load_default_config
from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
import pynxtools_spm.nxformatters.helpers as fhs
from pynxtools_spm.nxformatters.helpers import _get_data_unit_and_others, to_intended_t


class BrukerTxtAFM(BrukerBase):
    """Formatter for Bruker AFM force-curve data from .txt export files."""

    _grp_to_func: dict[str, str] = {
        "SPM_SCAN_CONTROL[spm_scan_control]": "_construct_nxscan_controllers",
        "start_time": "_set_start_end_time",
    }

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

    def _get_conf_dict(self, config_file: str | Path = None):
        if config_file:
            return fhs.read_config_file(config_file)
        return load_default_config(config_type="bruker_txt_afm")

    # ------------------------------------------------------------------
    # Timestamp handling
    # ------------------------------------------------------------------

    def _set_start_end_time(self, end_dict: dict, parent_path: str, group_name: str):
        """Parse Bruker TXT date string and write ISO 8601 to the template.

        Bruker TXT encodes date as '03:44:35 PM Mon May 15 2023' — different
        from the SPM binary format used by BrukerSpmAFM.
        """
        raw_date, _, _ = _get_data_unit_and_others(
            data_dict=self.raw_data, end_dict=end_dict
        )
        if not isinstance(raw_date, str) or not raw_date.strip():
            return
        # Single-space and double-space variants cover day < 10 (e.g. " 5").
        for fmt in ("%I:%M:%S %p %a %b %d %Y", "%I:%M:%S %p %a %b  %d %Y"):
            try:
                dt = datetime.datetime.strptime(raw_date.strip(), fmt)
                self.template[f"{parent_path}/{group_name}"] = dt.isoformat()
                return
            except ValueError:
                continue
        pynx_logger.warning(
            "Could not parse Bruker TXT date '%s' for field '%s'.",
            raw_date,
            group_name,
        )

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
        scan_region_dict = partial_conf_dict.get("scan_region")
        if scan_region_dict is not None:
            self.construct_scan_region_grp(
                partial_conf_dict=scan_region_dict,
                parent_path=f"{parent_path}/{group_name}",
            )

        scan_pattern_dict = partial_conf_dict.get("meshSCAN[mesh_scan]")
        if scan_pattern_dict is not None:
            self.construct_scan_pattern_grp(
                partial_conf_dict=scan_pattern_dict,
                parent_path=f"{parent_path}/{group_name}",
                group_name="meshSCAN[mesh_scan]",
            )

    # ------------------------------------------------------------------
    # Scan-region geometry
    # ------------------------------------------------------------------

    def construct_scan_region_grp(
        self,
        partial_conf_dict: dict,
        parent_path: str,
        group_name: str = "scan_region",
    ):
        """Populate scan_control from Ciao_scan_list offset and Scan_Size fields.

        Raw keys used (all under /Ciao_scan_list/0/):
          X_Offset, Y_Offset  → scan origin offsets
          X_Position, Y_Position → stage position (defaults to 0)
          Scan_Size, Aspect_Ratio → image size for x_range/y_range
        """
        # --- X/Y offsets ---
        offset_fld = "scan_offset_valueN[scan_offset_value_n]"
        offset_list = partial_conf_dict.get(offset_fld)
        if isinstance(offset_list, list):
            for item in offset_list:
                key_ext, end_dict = next(iter(item.items()))
                data, unit, _ = _get_data_unit_and_others(
                    data_dict=self.raw_data, end_dict=end_dict
                )
                if key_ext.endswith("x"):
                    self.scan_control.x_offset = data
                    self.scan_control.x_offset_unit = unit
                elif key_ext.endswith("y"):
                    self.scan_control.y_offset = data
                    self.scan_control.y_offset_unit = unit

        # --- Stage position (absent in most force-curve TXT files → 0) ---
        x_pos = to_intended_t(self.raw_data.get("/Ciao_scan_list/0/X_Position", 0))
        y_pos = to_intended_t(self.raw_data.get("/Ciao_scan_list/0/Y_Position", 0))

        # --- start = position + offset ---
        if self.scan_control.x_offset is not None:
            try:
                self.scan_control.x_start = float(x_pos or 0) + float(
                    self.scan_control.x_offset
                )
                self.scan_control.x_start_unit = self.scan_control.x_offset_unit
            except (TypeError, ValueError):
                pass
        if self.scan_control.y_offset is not None:
            try:
                self.scan_control.y_start = float(y_pos or 0) + float(
                    self.scan_control.y_offset
                )
                self.scan_control.y_start_unit = self.scan_control.y_offset_unit
            except (TypeError, ValueError):
                pass

        # --- Scan range (Scan_Size + Aspect_Ratio) ---
        range_fld = "scan_rangeN[scan_range_n]"
        range_dict = partial_conf_dict.get(range_fld)
        if isinstance(range_dict, dict) and "raw_path" in range_dict:
            data, unit, _ = _get_data_unit_and_others(
                data_dict=self.raw_data, end_dict=range_dict
            )
            if data is not None:
                target_unit = self.scan_control.x_start_unit or unit
                try:
                    range_q = ureg.Quantity(float(data), unit).to(target_unit)
                except Exception:
                    range_q = ureg.Quantity(float(data), unit)
                aspect_str = self.raw_data.get("/Ciao_scan_list/0/Aspect_Ratio", "1:1")
                aspect_val = self._parse_aspect_ratio(aspect_str)
                self.scan_control.x_range = range_q.magnitude
                self.scan_control.y_range = range_q.magnitude / aspect_val
                self.scan_control.x_range_unit = str(range_q.units)
                self.scan_control.y_range_unit = str(range_q.units)
                if self.scan_control.x_start is not None:
                    self.scan_control.x_end = (
                        self.scan_control.x_start + self.scan_control.x_range
                    )
                    self.scan_control.x_end_unit = self.scan_control.x_range_unit
                if self.scan_control.y_start is not None:
                    self.scan_control.y_end = (
                        self.scan_control.y_start + self.scan_control.y_range
                    )
                    self.scan_control.y_end_unit = self.scan_control.y_range_unit

        self.put_scan_2d_region_field_in_template(
            parent_path=parent_path, group_name=group_name
        )

    @staticmethod
    def _parse_aspect_ratio(aspect_str) -> float:
        """Convert a 'W:H' string to W/H as float. Returns 1.0 on any parse error."""
        if isinstance(aspect_str, str) and ":" in aspect_str:
            parts = aspect_str.split(":")
            if len(parts) == 2:
                try:
                    return float(parts[0]) / float(parts[1])
                except (ValueError, ZeroDivisionError):
                    pass
        pynx_logger.warning(
            "Aspect ratio '%s' is not in expected 'W:H' format; defaulting to 1:1.",
            aspect_str,
        )
        return 1.0

    # ------------------------------------------------------------------
    # Scan-pattern geometry
    # ------------------------------------------------------------------

    def construct_scan_pattern_grp(
        self,
        partial_conf_dict: dict,
        parent_path: str,
        group_name: str = "meshSCAN[mesh_scan]",
    ):
        """Extract pixel counts and write step sizes for the mesh-scan group."""
        scan_points_fld = "scan_pointsN[scan_points_n]"
        scan_points_list = partial_conf_dict.get(scan_points_fld)
        if isinstance(scan_points_list, list):
            for item in scan_points_list:
                key_ext, end_dict = next(iter(item.items()))
                data, _, _ = _get_data_unit_and_others(
                    data_dict=self.raw_data, end_dict=end_dict
                )
                if key_ext.endswith("x"):
                    self.scan_control.x_points = data
                elif key_ext.endswith("y"):
                    self.scan_control.y_points = data
        else:
            pynx_logger.warning(
                "Scan points missing or not in expected list format; "
                "check config and raw data."
            )

        try:
            if self.scan_control.x_range and self.scan_control.x_points:
                self.template[f"{parent_path}/{group_name}/step_size_x"] = (
                    self.scan_control.x_range / (int(self.scan_control.x_points) - 1)
                )
                self.template[f"{parent_path}/{group_name}/step_size_x/@units"] = (
                    self.scan_control.x_range_unit
                )
            if self.scan_control.y_range and self.scan_control.y_points:
                self.template[f"{parent_path}/{group_name}/step_size_y"] = (
                    self.scan_control.y_range / (int(self.scan_control.y_points) - 1)
                )
                self.template[f"{parent_path}/{group_name}/step_size_y/@units"] = (
                    self.scan_control.y_range_unit
                )
        except (TypeError, ZeroDivisionError):
            pynx_logger.warning(
                "Could not compute step sizes: missing range or point-count data."
            )

        self.put_scan_pattern_field_in_template(
            parent_path=parent_path, group_name=group_name
        )
