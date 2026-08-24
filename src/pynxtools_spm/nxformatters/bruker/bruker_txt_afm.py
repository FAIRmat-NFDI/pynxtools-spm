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

from dataclasses import dataclass
import datetime
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np
from pynxtools import logger as pynx_logger
from pynxtools.dataconverter.template import Template

from pynxtools_spm.configs import load_default_config
from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
import pynxtools_spm.nxformatters.helpers as fhs
from pynxtools_spm.nxformatters.helpers import (
    _get_data_unit_and_others,
    to_intended_t,
    unit_short,
)

if TYPE_CHECKING:
    from pint import Quantity


@dataclass
class NXScanControlPointForce:
    """Stores scan geometry for a point force (approach/retrace) curve."""

    z_points: int | None = None
    x_offset: int | float | None = None
    x_offset_unit: str | Quantity | None = None
    y_offset: int | float | None = None
    y_offset_unit: str | Quantity | None = None
    z_offset: int | float | None = None
    z_offset_unit: str | Quantity | None = None
    approach_start: int | float | None = None
    approach_start_unit: str | Quantity | None = None
    retrace_start: int | float | None = None
    retrace_start_unit: str | Quantity | None = None
    approach_range: int | float | None = None
    approach_range_unit: str | Quantity | None = None
    retrace_range: int | float | None = None
    retrace_range_unit: str | Quantity | None = None
    approach_end: int | float | None = None
    approach_end_unit: str | Quantity | None = None
    retrace_end: int | float | None = None
    retrace_end_unit: str | Quantity | None = None
    approach_points: int | None = None
    retrace_points: int | None = None


class BrukerTxtAFM(BrukerBase):
    """Formatter for Bruker AFM force-curve data from .txt export files."""

    # Force-curve data uses approach/retrace geometry, so this formatter
    # replaces the base's 2D ``NXScanControl`` with ``NXScanControlPointForce``.
    # The two are intentionally unrelated types (point-force is not an image
    # scan), so the override is deliberate rather than a substitutable subtype.
    scan_control: NXScanControlPointForce  # type: ignore[assignment]

    _grp_to_func: dict[str, str] = {
        "SPM_SCAN_CONTROL[spm_scan_control]": "_construct_nxscan_controllers",
        "cantilever_oscillator": "_construct_cantilever_oscillator",
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
        self.scan_control = NXScanControlPointForce()

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
    # Cantilever-oscillator hook (registered in _grp_to_func)
    # ------------------------------------------------------------------

    def _construct_cantilever_oscillator(
        self, partial_conf_dict: dict, parent_path: str, group_name: str
    ):
        """Compute amplitude_setpoint = Amplitude_Ratio × reference_amplitude.

        Bruker stores the setpoint as a dimensionless ratio of the free amplitude
        (e.g. 0.9 means 90 % of Free_Amplitude).  The physical value and its unit
        are therefore derived from reference_amplitude rather than read directly.
        """
        ref_amp_dict = partial_conf_dict.get("reference_amplitude", {})
        ref_amp, ref_amp_unit, _ = _get_data_unit_and_others(
            data_dict=self.raw_data, end_dict=ref_amp_dict
        )

        setpoint_dict = partial_conf_dict.get("amplitude_setpoint", {})
        amp_ratio = to_intended_t(self.raw_data.get(setpoint_dict.get("raw_path", "")))

        if ref_amp is not None and amp_ratio is not None:
            try:
                amplitude_setpoint = float(amp_ratio) * float(ref_amp)
                path = f"{parent_path}/{group_name}/amplitude_setpoint"
                self.template[path] = amplitude_setpoint
                self.template[f"{path}/@units"] = (
                    unit_short(ref_amp_unit) if ref_amp_unit else ref_amp_unit
                )
            except (TypeError, ValueError):
                pynx_logger.warning(
                    "Could not compute amplitude_setpoint from "
                    "Amplitude_Ratio=%s and reference_amplitude=%s.",
                    amp_ratio,
                    ref_amp,
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

        point_force_dict = partial_conf_dict.get("point_forceSCAN[point_force_scan]")
        if point_force_dict is not None:
            self.construct_point_force_scan_grp(
                partial_conf_dict=point_force_dict,
                parent_path=f"{parent_path}/{group_name}",
                group_name="point_forceSCAN[point_force_scan]",
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
        """Populate scan_region from x/y offsets and ramp array start/end positions.

        Approach start/end/range are derived from the extension ramp array
        (/Calc_Ramp_Ex_nm), and retrace from the retrace ramp (/Calc_Ramp_Rt_nm).
        The first and last array elements are used so that the physical scan
        direction (not just the sorted range) is preserved.
        """
        # --- X/Y offsets from config ---
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

        # --- Approach start/end/range from extension ramp array ---
        approach_ramp = self.raw_data.get("/Calc_Ramp_Ex_nm")
        if isinstance(approach_ramp, np.ndarray) and len(approach_ramp) > 0:
            unit = self.raw_data.get("/Calc_Ramp_Ex_nm/unit", "nm")
            unit = unit_short(unit) if unit else unit
            self.scan_control.approach_start = float(approach_ramp[0])
            self.scan_control.approach_end = float(approach_ramp[-1])
            self.scan_control.approach_range = abs(
                self.scan_control.approach_end - self.scan_control.approach_start
            )
            self.scan_control.approach_start_unit = unit
            self.scan_control.approach_end_unit = unit
            self.scan_control.approach_range_unit = unit

        # --- retrace start/end/range from retrace ramp array ---
        retrace_ramp = self.raw_data.get("/Calc_Ramp_Rt_nm")
        if isinstance(retrace_ramp, np.ndarray) and len(retrace_ramp) > 0:
            unit = self.raw_data.get("/Calc_Ramp_Rt_nm/unit", "nm")
            unit = unit_short(unit) if unit else unit
            self.scan_control.retrace_start = float(retrace_ramp[0])
            self.scan_control.retrace_end = float(retrace_ramp[-1])
            self.scan_control.retrace_range = abs(
                self.scan_control.retrace_end - self.scan_control.retrace_start
            )
            self.scan_control.retrace_start_unit = unit
            self.scan_control.retrace_end_unit = unit
            self.scan_control.retrace_range_unit = unit

        self.put_point_scan_data_field_in_template(
            parent_path=parent_path, group_name=group_name
        )

    # ------------------------------------------------------------------
    # Point-force-scan pattern (approach/retrace points and step sizes)
    # ------------------------------------------------------------------

    def construct_point_force_scan_grp(
        self,
        partial_conf_dict: dict,
        parent_path: str,
        group_name: str = "point_forceSCAN[point_force_scan]",
    ):
        """Extract approach/retrace point counts and compute step sizes.

        Samps/line may encode one shared count ("512") or two space-separated
        counts ("256 512") for approach and retrace respectively.
        """
        scan_points_fld = "scan_pointsN[scan_points_n]"
        scan_points_list = partial_conf_dict.get(scan_points_fld)
        if isinstance(scan_points_list, list):
            for item in scan_points_list:
                key_ext, end_dict = next(iter(item.items()))
                raw_path = end_dict.get("raw_path", "")
                raw_val = self.raw_data.get(raw_path)
                if raw_val is None:
                    continue
                # Split by whitespace: first token → approach, second → retrace.
                # If only one token is present it is shared between both directions.
                parts = str(raw_val).split()
                if key_ext.startswith("approach"):
                    self.scan_control.approach_points = int(parts[0])
                elif key_ext.startswith("retrace"):
                    self.scan_control.retrace_points = int(
                        parts[1] if len(parts) > 1 else parts[0]
                    )
        else:
            pynx_logger.warning(
                "Scan points missing or not in expected list format; "
                "check config and raw data."
            )

        try:
            n_approach = self.scan_control.approach_points
            if self.scan_control.approach_range and n_approach and int(n_approach) > 1:
                step = self.scan_control.approach_range / (int(n_approach) - 1)
                self.template[
                    f"{parent_path}/{group_name}/step_sizeN[step_size_approach]"
                ] = step
                self.template[
                    f"{parent_path}/{group_name}/step_sizeN[step_size_approach]/@units"
                ] = self.scan_control.approach_range_unit

            n_retrace = self.scan_control.retrace_points
            if self.scan_control.retrace_range and n_retrace and int(n_retrace) > 1:
                step = self.scan_control.retrace_range / (int(n_retrace) - 1)
                self.template[
                    f"{parent_path}/{group_name}/step_sizeN[step_size_retrace]"
                ] = step
                self.template[
                    f"{parent_path}/{group_name}/step_sizeN[step_size_retrace]/@units"
                ] = self.scan_control.retrace_range_unit
        except (TypeError, ZeroDivisionError):
            pynx_logger.warning(
                "Could not compute step sizes: missing range or point-count data."
            )

        self.put_point_force_scan_field_in_template(
            parent_path=parent_path, group_name=group_name
        )

    # ------------------------------------------------------------------
    # Template writers
    # ------------------------------------------------------------------

    def put_point_scan_data_field_in_template(
        self, parent_path: str, group_name: str = "scan_region"
    ):
        """Write approach/retrace scan-region fields to the template using variadic keys.

        Variadic notation (e.g. scan_startN[scan_start_approach]) lets the NeXus
        validator match each written field back to the schema concept scan_startN.
        scan_range and scan_offset_value are omitted: ranges are used internally only
        for step-size computation, and offsets are already written by the config walker.
        """
        sc = self.scan_control
        base = f"{parent_path}/{group_name}"
        self.template[f"{base}/scan_startN[scan_start_approach]"] = sc.approach_start
        self.template[f"{base}/scan_startN[scan_start_approach]/@units"] = (
            sc.approach_start_unit
        )
        self.template[f"{base}/scan_startN[scan_start_retrace]"] = sc.retrace_start
        self.template[f"{base}/scan_startN[scan_start_retrace]/@units"] = (
            sc.retrace_start_unit
        )
        self.template[f"{base}/scan_endN[scan_end_approach]"] = sc.approach_end
        self.template[f"{base}/scan_endN[scan_end_approach]/@units"] = (
            sc.approach_end_unit
        )
        self.template[f"{base}/scan_endN[scan_end_retrace]"] = sc.retrace_end
        self.template[f"{base}/scan_endN[scan_end_retrace]/@units"] = (
            sc.retrace_end_unit
        )

    def put_point_force_scan_field_in_template(self, parent_path: str, group_name: str):
        """Write approach/retrace point counts to the template using variadic keys."""
        base = f"{parent_path}/{group_name}"
        self.template[f"{base}/scan_pointsN[scan_points_approach]"] = (
            self.scan_control.approach_points
        )
        self.template[f"{base}/scan_pointsN[scan_points_retrace]"] = (
            self.scan_control.retrace_points
        )
