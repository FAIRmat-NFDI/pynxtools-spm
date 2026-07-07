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

from __future__ import annotations
from pathlib import Path

import numpy as np

from pynxtools import logger as pynx_logger

from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
import pynxtools_spm.nxformatters.helpers as fhs
from pynxtools_spm.configs import load_default_config
from pynxtools.dataconverter.template import Template
from pynxtools_spm.nxformatters.helpers import _get_data_unit_and_others
from pynxtools.units import ureg


class BrukerSpmAFM(BrukerBase):
    """
    Formatter for Bruker AFM data from .spm files..
    """

    _grp_to_func: dict[str, str] = {
        "SPM_SCAN_CONTROL[spm_scan_control]": "_construct_nxscan_controllers"
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

    def _get_conf_dict(self, config_file: str | Path = None):
        if config_file:
            return fhs.read_config_file(config_file)

        return load_default_config(config_type="bruker_spm_afm")

    def _construct_nxscan_controllers(
        self, partial_conf_dict, parent_path, group_name="scan_control", **kwarg
    ):
        scan_region_grp = "scan_region"
        scan_region_dict = partial_conf_dict.get(scan_region_grp)
        if scan_region_dict is not None:
            self.construct_region_region_grp(
                partial_conf_dict=scan_region_dict,
                parent_path=f"{parent_path}/{group_name}",
            )

        scan_pattern_grp = "meshSCAN[mesh_scan]"
        scan_pattern_dict = partial_conf_dict.get(scan_pattern_grp)
        if scan_pattern_dict is not None:
            self.construct_scan_pattern_grp(
                partial_conf_dict=scan_pattern_dict,
                parent_path=f"{parent_path}/{group_name}",
                group_name=scan_pattern_grp,
            )

    @staticmethod
    def _scalar_with_unit(value, fallback_unit):
        """Normalize a scan-geometry value to a numeric magnitude and a unit.

        Newer NanoScope (v9.x) ``.spm`` files store some geometry values as
        unit-bearing strings such as ``"-3750 nm"``, whereas older files store a
        bare number together with a unit taken from the config. ``pint`` is used
        to split an embedded unit off the value and, when a ``fallback_unit`` is
        given, to express the magnitude in that unit. Non-string or
        non-parsable values are returned unchanged alongside ``fallback_unit``.
        """
        if not isinstance(value, str):
            return value, fallback_unit
        try:
            quantity = ureg.Quantity(value)
        except Exception:  # noqa: BLE001 - pint raises several error types
            return value, fallback_unit
        if quantity.dimensionless:
            return quantity.magnitude, fallback_unit
        if fallback_unit:
            try:
                quantity = quantity.to(fallback_unit)
                return quantity.magnitude, fallback_unit
            except Exception:  # noqa: BLE001 - incompatible/unknown unit
                pass
        return quantity.magnitude, str(quantity.units)

    def construct_region_region_grp(
        self, partial_conf_dict, parent_path, group_name="scan_region"
    ):
        """To construct the scan region.

        Raw data needed to calculate the scan region:
        /Scanner_list/0/Scan_Size : 20000 nm;
        /Scanner_list/0/X_Position : 0
        /Scanner_list/0/Y_Position : 0
        /Scanner_list/0/X_Offset : 0
        /Scanner_list/0/Y_Offset : 0
        /Scanner_list/0/Stage_X : 0
        /Scanner_list/0/Stage_Y : 0
        /Scanner_list/0/Aspect_Ratio : 1:1

        Scan origin (start):
        - ``start = position`` when the absolute ``X_Position``/``Y_Position``
          is available.
        - ``start = stage + offset`` otherwise (e.g. NanoScope v9.x ``.spm``
          files, which do not store an absolute position), using the stage
          position ``Stage_X``/``Stage_Y`` and the scan offset.
        """
        offset_fld = "scan_offset_valueN[scan_offset_value_n]"
        offset_fld_list = partial_conf_dict.get(offset_fld, None)

        # list of variadic fields and dict of raw_path and units
        if isinstance(offset_fld_list, list) and isinstance(offset_fld_list[0], dict):
            for offset_field in offset_fld_list:
                key_ext, end_dict = offset_field.popitem()
                data, unit, _ = _get_data_unit_and_others(
                    data_dict=self.raw_data, end_dict=end_dict
                )
                data, unit = self._scalar_with_unit(data, unit)
                if key_ext.endswith("x"):
                    self.scan_control.x_offset = data
                    self.scan_control.x_offset_unit = unit
                elif key_ext.endswith("y"):
                    self.scan_control.y_offset = data
                    self.scan_control.y_offset_unit = unit

        start_fld = "scan_startN[scan_start_n]"
        start_fld_list = partial_conf_dict.get(start_fld)
        if isinstance(start_fld_list, list) and isinstance(start_fld_list[0], dict):
            for start_field in start_fld_list:
                key_ext, end_dict = start_field.popitem()
                data, unit, _ = _get_data_unit_and_others(
                    data_dict=self.raw_data, end_dict=end_dict
                )
                data, unit = self._scalar_with_unit(data, unit)
                axis = "x" if key_ext.endswith("x") else "y"
                offset = getattr(self.scan_control, f"{axis}_offset")
                offset_unit = getattr(self.scan_control, f"{axis}_offset_unit")
                if data is not None:
                    # Absolute position is available; it already is the origin.
                    start, start_unit = data, unit
                else:
                    # NanoScope v9.x has no absolute position field: derive the
                    # scan origin from the stage position, start = stage + offset.
                    stage_data = self.raw_data.get(
                        f"/Scanner_list/0/Stage_{axis.upper()}"
                    )
                    stage, stage_unit = self._scalar_with_unit(
                        stage_data, unit or offset_unit
                    )
                    stage = 0 if stage is None else stage
                    start = stage + (0 if offset is None else offset)
                    start_unit = stage_unit or offset_unit
                setattr(self.scan_control, f"{axis}_start", start)
                setattr(self.scan_control, f"{axis}_start_unit", start_unit)

        range_fld = "scan_rangeN[scan_range_n]"
        range_fld_dict = partial_conf_dict.get(range_fld)
        if isinstance(range_fld_dict, dict):
            data, unit, _ = _get_data_unit_and_others(
                data_dict=self.raw_data, end_dict=range_fld_dict
            )
            aspect_ratio = self.raw_data.get("/Scanner_list/0/Aspect_Ratio", 1)
            aspect_ratio_val = 1.0
            if aspect_ratio and isinstance(aspect_ratio, str) and ":" in aspect_ratio:
                aspect_ratio_vals = aspect_ratio.split(":")
                if len(aspect_ratio_vals) == 2 and all(
                    val.replace(".", "", 1).isdigit() for val in aspect_ratio_vals
                ):
                    aspect_ratio_val = float(aspect_ratio_vals[0]) / float(
                        aspect_ratio_vals[1]
                    )
                else:
                    pynx_logger.warning(
                        "Aspect ratio value is not found in expected format, defaulting to 1:1. Aspect ratio value: %s",
                        aspect_ratio,
                    )
            range_val = ureg.Quantity(data, unit).to(self.scan_control.x_start_unit)
            self.scan_control.x_range = range_val.magnitude
            self.scan_control.y_range = range_val.magnitude / aspect_ratio_val
            self.scan_control.x_range_unit = str(range_val.units)
            self.scan_control.y_range_unit = str(range_val.units)
            self.scan_control.x_end = (
                self.scan_control.x_start + self.scan_control.x_range
            )
            self.scan_control.x_end_unit = self.scan_control.x_range_unit
            self.scan_control.y_end = (
                self.scan_control.y_start + self.scan_control.y_range
            )
            self.scan_control.y_end_unit = self.scan_control.y_range_unit
        self.put_scan_2d_region_field_in_template(
            parent_path=parent_path, group_name=group_name
        )

    def construct_scan_pattern_grp(
        self,
        partial_conf_dict,
        parent_path: str,
        group_name="scan_mesh",
    ):
        """Construct data scan pattern for group "meshSCAN[mesh_scan]"."""
        scan_points_fld = "scan_pointsN[scan_points_n]"
        scan_points_fld_list = partial_conf_dict.get(scan_points_fld)
        if isinstance(scan_points_fld_list, list) and isinstance(
            scan_points_fld_list[0], dict
        ):
            for scan_points_field in scan_points_fld_list:
                key_ext, end_dict = scan_points_field.popitem()
                data, _, _ = _get_data_unit_and_others(
                    data_dict=self.raw_data, end_dict=end_dict
                )
                if key_ext.endswith("x"):
                    self.scan_control.x_points = data
                elif key_ext.endswith("y"):
                    self.scan_control.y_points = data
        else:
            pynx_logger.warning(
                "Scan points information is missing or not in expected format. "
                "Please check config file and raw data."
            )
        # Calculate step size from scan range and scan points
        self.template[f"{parent_path}/{group_name}/step_size_x"] = (
            self.scan_control.x_range / (self.scan_control.x_points - 1)
        )
        self.template[f"{parent_path}/{group_name}/step_size_x/@units"] = (
            self.scan_control.x_range_unit
        )
        self.template[f"{parent_path}/{group_name}/step_size_y"] = (
            self.scan_control.y_range / (self.scan_control.y_points - 1)
        )
        self.template[f"{parent_path}/{group_name}/step_size_y/@units"] = (
            self.scan_control.y_range_unit
        )

        self.put_scan_pattern_field_in_template(
            parent_path=parent_path, group_name=group_name
        )

    def _nxdata_grp_from_conf_description(
        self,
        partial_conf_dict,
        parent_path: str,
        group_name: str,
        group_index=0,
        is_forward: bool | None = None,
        rearrange_2d_data: bool = False,
    ):
        """Determine the nxdata group name from the config description and construct the nxdata group in the template if possible. This is to handle the case when there are multiple data groups of the same type (e.g. forward and backward scan) and the group name in the config file does not explicitly indicate which one is forward or backward scan. The function will try to determine which one is forward or backward scan based on the raw data path provided in the config file. If it can determine which one is forward or backward scan, it will construct the nxdata group accordingly. If it cannot determine, it will return None and skip constructing the nxdata group for that data group. The function also handles rearranging 2D data if needed based on the scan pattern (e.g. for line scan, the data needs to be rearranged to have x and y axes). The function also adds axis information to the nxdata group based on the scan pattern and scan region information provided in the config file."""
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

        title, _, _ = _get_data_unit_and_others(
            data_dict=self.raw_data, end_dict=partial_conf_dict.get("title", "")
        )
        if title:
            self.template[f"{parent_path}/{nxdata_group}/title"] = title

        if "0" not in partial_conf_dict and "1" not in partial_conf_dict:
            axis_x = "x"
            axis_x_key = f"{parent_path}/{nxdata_group}/AXISNAME[{axis_x}]"
            axis_y = "y"
            axis_y_key = f"{parent_path}/{nxdata_group}/AXISNAME[{axis_y}]"
            axis_x_data = np.linspace(
                self.scan_control.x_start,
                self.scan_control.x_end,
                int(self.scan_control.x_points),
            )
            axis_y_data = np.linspace(
                self.scan_control.y_end,
                self.scan_control.y_start,
                int(self.scan_control.y_points),
            )
            nxdata_path = f"{parent_path}/{nxdata_group}"
            signal_name = self.template[f"{nxdata_path}/@signal"]
            signal_path = f"{nxdata_path}/DATA[{signal_name}]"
            signal_data = self.template[signal_path]
            axes_path = f"{nxdata_path}/@axes"
            axes_data = self.template.get(axes_path, [])

            if isinstance(signal_data, np.ndarray) and signal_data.ndim == 2:
                expected_x_points = signal_data.shape[0]
                expected_y_points = signal_data.shape[1]

                x_points_match = isinstance(axis_x_data, np.ndarray) and (
                    axis_x_data.size == expected_x_points
                )
                y_points_match = isinstance(axis_y_data, np.ndarray) and (
                    axis_y_data.size == expected_y_points
                )
                if not (x_points_match and y_points_match):
                    pynx_logger.warning(
                        "The signal data is 2D with shape (%s, %s)."
                        "Scan region data has %s x points and %s y points.",
                        expected_x_points,
                        expected_y_points,
                        self.scan_control.x_points,
                        self.scan_control.y_points,
                    )
                    pynx_logger.warning(
                        f"Recreating 'X' and 'Y' axis data based on the shape of the signal data."
                        f"{expected_x_points} x points and {expected_y_points} y points"
                    )

                if not x_points_match:
                    axis_x_data = np.linspace(
                        self.scan_control.x_start,
                        self.scan_control.x_end,
                        expected_x_points,
                    )
                self.template[f"{axis_x_key}"] = axis_x_data
                self.template[f"{axis_x_key}/@units"] = self.scan_control.x_start_unit

                if not y_points_match:
                    axis_y_data = np.linspace(
                        self.scan_control.y_end,
                        self.scan_control.y_start,
                        expected_y_points,
                    )
                self.template[f"{axis_y_key}"] = axis_y_data

                self.template[f"{axis_y_key}/@units"] = self.scan_control.y_start_unit

                if not axes_data:
                    self.template[f"{axes_path}"] = [
                        axis_y,
                        axis_x,
                    ]
        return nxdata_group
