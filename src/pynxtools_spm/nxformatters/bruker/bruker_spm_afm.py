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
from pynxtools import logger as pynx_logger

from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
import pynxtools_spm.nxformatters.helpers as fhs
from pynxtools_spm.configs import load_default_config
from pynxtools.dataconverter.template import Template
from pathlib import Path
from pynxtools_spm.nxformatters.helpers import _get_data_unit_and_others
from pynxtools.units import ureg


class BrukerSpmAFM(BrukerBase):
    """
    Formatter for Bruker AFM data from .spm files..
    """

    __grp_to_func: dict[str, str] = {
        "SPM_SCAN_CONTROL[spm_scan_control]": "_construct_nxscan_controllers"
    }
    _axes = ["x", "y", "z"]

    def __init__(
        self,
        template: Template,
        raw_file: str | Path,
        eln_file: str | Path | None = None,
        config_file: str | Path | None = None,
        auxilary_files: Optional[list[str | Path]] = None,
        entry: str | None = None,
    ):
        super().__init__(
            template, raw_file, eln_file, config_file, auxilary_files, entry
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

    # def get_raw_data_dict(self):
    #     data_dict = {}
    #     data_dict_raw_data = SPMParser().get_raw_data_dict(self.raw_file, eln=self.eln)
    #     data_dict_raw_data.update(data_dict_raw_data)
    #     # if self.auxilary_files is not None:
    #     #     for aux_file in self.auxilary_files:
    #     #         aux_data_dict = SPMParser().get_raw_data_dict(aux_file, eln=self.eln)
    #     #         data_dict.update(aux_data_dict)
    #     # else:
    #     #     pynx_logger.error(
    #     #         "No auxilary file of .txt is provided for Bruker AFM data. "
    #     #         "To parse a Bruker AFM .spm file, an auxilary .txt file containing experiment metadata is required. "
    #     #     )
    #     #     raise ValueError(
    #     #         "An ausilary .txt file is required for Bruker AFM data for experiment matadata."
    #     #         "Please provide the path to the .txt file as an auxiliary file when initializing the formatter."
    #     #     )

    #     return data_dict

    def _construct_nxscan_controllers(
        self, partial_conf_dict, parent_path, group_name="scan_control", **kwarg
    ):
        scan_region_grp = "scan_region"
        scan_region_dict = partial_conf_dict.get(scan_region_grp)
        if scan_region_dict:
            self.construct_region_region_grp(
                partial_conf_dict=scan_region_dict,
                parent_path=f"{parent_path}/{group_name}",
            )

        scan_pattern_grp = "meshSCAN[mesh_scan]"
        scan_pattern_dict = partial_conf_dict.get(scan_pattern_grp, None)
        if scan_pattern_dict is not None:
            self.construct_scan_pattern_grp(
                partial_conf_dict=scan_pattern_dict,
                parent_path=f"{parent_path}/{group_name}",
                group_name=scan_pattern_grp,
            )

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
        /Scanner_list/0/Aspect_Ratio : 1:1

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
                if key_ext.endswith("x"):
                    self.NXScanControl.x_offset = data
                    self.NXScanControl.x_offset_unit = unit
                elif key_ext.endswith("y"):
                    self.NXScanControl.y_offset = data
                    self.NXScanControl.y_offset_unit = unit

        start_fld = "scan_startN[scan_start_n]"
        start_fld_list = partial_conf_dict.get(start_fld)
        if isinstance(start_fld_list, list) and isinstance(start_fld_list[0], dict):
            for start_field in start_fld_list:
                key_ext, end_dict = start_field.popitem()
                data, unit, _ = _get_data_unit_and_others(
                    data_dict=self.raw_data, end_dict=end_dict
                )
                if key_ext.endswith("x"):
                    self.NXScanControl.x_start = data + self.NXScanControl.x_offset
                    self.NXScanControl.x_start_unit = unit
                elif key_ext.endswith("y"):
                    self.NXScanControl.y_start = data + self.NXScanControl.y_offset
                    self.NXScanControl.y_start_unit = unit

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
                        "Aspect ratio value is not in expected format, defaulting to 1:1. Aspect ratio value: %s",
                        aspect_ratio,
                    )
            range_val = ureg.Quantity(data, unit).to(self.NXScanControl.x_start_unit)
            self.NXScanControl.x_range = range_val.magnitude
            self.NXScanControl.y_range = range_val.magnitude / aspect_ratio_val
            self.NXScanControl.x_range_unit = str(range_val.units)
            self.NXScanControl.y_range_unit = str(range_val.units)
            self.NXScanControl.x_end = (
                self.NXScanControl.x_start + self.NXScanControl.x_range
            )
            self.NXScanControl.y_end = (
                self.NXScanControl.y_start + self.NXScanControl.y_range
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
                    self.NXScanControl.x_points = data
                elif key_ext.endswith("y"):
                    self.NXScanControl.y_points = data
        else:
            pynx_logger.warning(
                "Scan points information is missing or not in expected format. "
                "Please check config file and raw data."
            )

        # Calculate step size from scan range and scan points
        self.template[f"{parent_path}/{group_name}/step_size_x"] = (
            self.NXScanControl.x_range / (self.NXScanControl.x_points - 1)
        )
        self.template[f"{parent_path}/{group_name}/step_size_x/@units"] = (
            self.NXScanControl.x_range_unit
        )
        self.template[f"{parent_path}/{group_name}/step_size_y"] = (
            self.NXScanControl.y_range / (self.NXScanControl.y_points - 1)
        )
        self.template[f"{parent_path}/{group_name}/step_size_y/@units"] = (
            self.NXScanControl.y_range_unit
        )
