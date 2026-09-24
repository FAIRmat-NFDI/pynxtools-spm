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
<<<<<<< HEAD
from pathlib import Path

import numpy as np
<<<<<<< HEAD

=======
from typing import Optional, Union
>>>>>>> e7ff512 (parser.)
=======
>>>>>>> 03fa66e (Formater)
from pynxtools import logger as pynx_logger

from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
import pynxtools_spm.nxformatters.helpers as fhs
from pynxtools_spm.configs import load_default_config
from pynxtools.dataconverter.template import Template
<<<<<<< HEAD
from pynxtools_spm.nxformatters.helpers import _get_data_unit_and_others
from pynxtools.units import ureg
=======
from pathlib import Path
<<<<<<< HEAD
from pynxtools_spm.parsers import SPMParser
>>>>>>> e7ff512 (parser.)
=======
from pynxtools_spm.nxformatters.helpers import _get_data_unit_and_others
from pynxtools.units import ureg
>>>>>>> 03fa66e (Formater)


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
<<<<<<< HEAD
        auxiliary_files: list[str | Path] | None = None,
        entry: str | None = None,
    ):
        super().__init__(
            template, raw_file, eln_file, config_file, auxiliary_files, entry
=======
        auxilary_files: Optional[list[str | Path]] = None,
        entry: str | None = None,
    ):
        super().__init__(
            template, raw_file, eln_file, config_file, auxilary_files, entry
>>>>>>> e7ff512 (parser.)
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
<<<<<<< HEAD
        if scan_region_dict is not None:
            self.construct_scan_region_grp(
=======
        if scan_region_dict:
            self.construct_region_region_grp(
>>>>>>> 03fa66e (Formater)
                partial_conf_dict=scan_region_dict,
                parent_path=f"{parent_path}/{group_name}",
            )

        scan_pattern_grp = "meshSCAN[mesh_scan]"
<<<<<<< HEAD
        scan_pattern_dict = partial_conf_dict.get(scan_pattern_grp)
=======
        scan_pattern_dict = partial_conf_dict.get(scan_pattern_grp, None)
>>>>>>> 03fa66e (Formater)
        if scan_pattern_dict is not None:
            self.construct_scan_pattern_grp(
                partial_conf_dict=scan_pattern_dict,
                parent_path=f"{parent_path}/{group_name}",
                group_name=scan_pattern_grp,
            )

<<<<<<< HEAD
    @staticmethod
    def _scalar_with_unit(value, fallback_unit):
        """Normalize a scan-geometry value to a numeric magnitude and a unit.

        Newer NanoScope (v9.x) ``.spm`` files store some geometry values as
        unit-bearing strings such as ``"-3750 nm"``, whereas older files store a
        bare number together with a unit taken from the config. ``pint`` is used
        to split an embedded unit off the value and, when a ``fallback_unit`` is
        given, to express the magnitude in that unit. Non-string values are
        returned unchanged alongside ``fallback_unit``.

        The returned magnitude is always numeric or ``None``: the callers do
        arithmetic on it (``start = stage + offset``) and write it into numeric
        NeXus fields, so a string that cannot be resolved to a number is
        reported as ``None`` -- the callers already treat ``None`` as "not
        available" -- rather than being passed through.
        """
        if not isinstance(value, str):
            return value, fallback_unit
        try:
            quantity = ureg.Quantity(value)
        except Exception:  # noqa: BLE001 - pint raises several error types
            # pint could not tokenize the string at all (e.g. '', '  ', 'abc').
            # Retry with the reader's own string->scalar coercion before giving up.
            numeric = fhs.to_intended_t(value)
            if isinstance(numeric, (int, float)) and not isinstance(numeric, bool):
                return numeric, fallback_unit
            pynx_logger.warning(
                "Could not read a scalar scan-geometry value from %r; "
                "treating it as unavailable.",
                value,
            )
            return None, fallback_unit
        if quantity.dimensionless:
            return quantity.magnitude, fallback_unit
        if fallback_unit:
            try:
                quantity = quantity.to(fallback_unit)
                return quantity.magnitude, fallback_unit
            except Exception:  # noqa: BLE001 - incompatible/unknown unit
                pass
        return quantity.magnitude, str(quantity.units)

    def construct_scan_region_grp(
        self, partial_conf_dict, parent_path, group_name="scan_region"
    ):
        """To construct the scan region.

        Raw data needed to calculate the scan region:
        /Scanner_list/0/Scan_Size : 20000 nm;
=======
    def construct_region_region_grp(
        self, partial_conf_dict, parent_path, group_name="scan_region"
    ):
        """To construct the scan region.
        Raw data needed to calculate the scan region:
        /Scanner_list/0/Scan_Size : 20000 nm;
        /Scanner_list/0/X_Position : 0
        /Scanner_list/0/Y_Position : 0
>>>>>>> 03fa66e (Formater)
        /Scanner_list/0/X_Offset : 0
        /Scanner_list/0/Y_Offset : 0
        /Scanner_list/0/Aspect_Ratio : 1:1

<<<<<<< HEAD
        Bruker documents ``X Offset``/``Y Offset`` as the centre position of the
        scan, in the scanner (piezo) frame, so the area runs from
        ``offset - range/2`` to ``offset + range/2``. ``X_Position`` and the
        coarse stage ``Stage_X`` are not used: the stage is a different frame
        of reference. See 'tests/README.md'.
=======
>>>>>>> 03fa66e (Formater)
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
<<<<<<< HEAD
                data, unit = self._scalar_with_unit(data, unit)
                unit = fhs.unit_short(unit)
                if key_ext.endswith("x"):
                    self.scan_control.x_offset = data
                    self.scan_control.x_offset_unit = unit
                elif key_ext.endswith("y"):
                    self.scan_control.y_offset = data
                    self.scan_control.y_offset_unit = unit
=======
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
>>>>>>> 03fa66e (Formater)

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
<<<<<<< HEAD
                        "Aspect ratio value is not found in expected format, defaulting to 1:1. Aspect ratio value: %s",
                        aspect_ratio,
                    )
            range_val = ureg.Quantity(data, unit).to(self.scan_control.x_offset_unit)
            self.scan_control.x_range = range_val.magnitude
            self.scan_control.y_range = range_val.magnitude / aspect_ratio_val
            self.scan_control.x_range_unit = fhs.unit_short(range_val.units)
            self.scan_control.y_range_unit = fhs.unit_short(range_val.units)

        self.derive_scan_2d_start_end()
        self.put_scan_2d_region_field_in_template(
            parent_path=parent_path, group_name=group_name
=======
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
>>>>>>> 03fa66e (Formater)
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
        # '\\Frame direction' is the slow scan direction: 'Up' restarts the
        # scan at the bottom of the frame, 'Down' at the top. The fast axis
        # stays unsigned because Trace and Retrace layers are both stored.
        directions = {
            str(val).strip().lower()
            for key, val in self.raw_data.items()
            if key.endswith("/Frame_direction")
        }
        slow_axis = "y"
        if directions == {"up"}:
            slow_axis = "+y"
        elif directions == {"down"}:
            slow_axis = "-y"
        elif len(directions) > 1:
            pynx_logger.warning(
                "The image layers disagree on '\\Frame direction' (%s), so the "
                "slow scan direction is left unspecified.",
                ", ".join(sorted(directions)),
            )
        self.scan_control.fast_axis = "x"
        self.scan_control.slow_axis = slow_axis
        # 'independent_scan_axes' sits on the scan control group, the parent of
        # the mesh scan.
        self.put_independent_scan_axes_in_template(parent_path, axes=("x", slow_axis))

        # The step is the pixel pitch, so the axis values are pixel centres.
        self.template[f"{parent_path}/{group_name}/step_size_x"] = (
            self.scan_control.x_range / self.scan_control.x_points
        )
        self.template[f"{parent_path}/{group_name}/step_size_x/@units"] = (
            self.scan_control.x_range_unit
        )
        self.template[f"{parent_path}/{group_name}/step_size_y"] = (
            self.scan_control.y_range / self.scan_control.y_points
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
        rearrange_2d_data: bool = True,
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
            axis_x = "X"
            axis_y = "Y"
            nxdata_path = f"{parent_path}/{nxdata_group}"
            signal_name = self.template[f"{nxdata_path}/@signal"]
            signal_data = self.template[f"{nxdata_path}/DATA[{signal_name}]"]
            axes_path = f"{nxdata_path}/@axes"
            axes_data = self.template.get(axes_path, [])

            if isinstance(signal_data, np.ndarray) and signal_data.ndim == 2:
                # NeXus @axes for a 2D image is [slow, fast] == ['Y', 'X']:
                # signal dim 0 is the slow (y) axis and dim 1 the fast (x) axis.
                # Size each axis from its own signal dimension so that
                # non-square or partial (interrupted) scans stay aligned with
                # @axes instead of having x/y lengths swapped.
                expected_y_points, expected_x_points = signal_data.shape
                if (
                    self.scan_control.x_points,
                    self.scan_control.y_points,
                ) != (expected_x_points, expected_y_points):
                    pynx_logger.warning(
                        "The signal data is 2D with shape (%s, %s), while the scan "
                        "region has %s x points and %s y points. The axes are "
                        "rebuilt from the shape of the signal data.",
                        expected_x_points,
                        expected_y_points,
                        self.scan_control.x_points,
                        self.scan_control.y_points,
                    )
                    self.scan_control.x_points = expected_x_points
                    self.scan_control.y_points = expected_y_points

                # Both axes ascend: row 0 and column 0 are the bottom-left
                # corner. The values are the pixel centres around the scan
                # offset, which is the centre of the scanned area.
                for axis in (axis_x, axis_y):
                    axis_key = f"{nxdata_path}/AXISNAME[{axis}]"
                    self.template[axis_key] = self._pixel_centres(axis.lower())
                    self.template[f"{axis_key}/@units"] = fhs.unit_short(
                        getattr(self.scan_control, f"{axis.lower()}_start_unit")
                    )

                if not axes_data:
                    self.template[f"{axes_path}"] = [
                        axis_y,
                        axis_x,
                    ]
        return nxdata_group
