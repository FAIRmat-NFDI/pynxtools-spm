#!/usr/bin/env python3
"""
A formatter that formats the STM (Scanning Tunneling Microscopy) experiment's raw data
to NeXus application definition NXstm.
"""

# -*- coding: utf-8 -*-
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

import re
from pynxtools_spm.nxformatters.base_formatter import SPMformatter
from typing import TYPE_CHECKING, Optional, Union, Any
import re
from pynxtools_spm.configs import load_default_config
import pynxtools_spm.nxformatters.helpers as fhs
from pathlib import Path
from pynxtools_spm.nxformatters.helpers import (
    _get_data_unit_and_others,
    _scientific_num_pattern,
    to_intended_t,
)
from pynxtools_spm.nxformatters.helpers import replace_variadic_name_part
import datetime
import numpy as np

if TYPE_CHECKING:
    from pynxtools.dataconverter.template import Template


class OmicronSM4STMFormatter(SPMformatter):
    """
    Formatter for Omicron SM4 STM data.
    """

    _grp_to_func = {"lockin_amplifier": "_construct_lockin_amplifier_grp",
                    "SCAN_CONTROL[scan_control_*]" : "_construct_nxscan_controllers"}
    _scan_list = []



    def __init__(
            self,
            template: "Template",
            raw_file: str | Path,
            eln_file: str | Path,
            config_file: str | Path = None,  # Incase it is not provided by users
            entry: Optional[str] = None,
    ):
        super().__init__(template, raw_file, eln_file, config_file, entry)

    def get_nxformatted_template(self):
        self.walk_though_config_nested_dict(self.config_dict, parent_path="")
        self._format_template_from_eln()
        # self._handle_special_fields()

    def _get_conf_dict(self, config_file = None):
        if config_file is not None:
            return fhs.read_config_file(config_file)
        else:
            return load_default_config("omicron_sm4_stm")

    @staticmethod
    def find_active_channel(raw_dt_dct: dict=None, key: str=None):
        """
        Find active channel from a bunch of available channels.
        """
        if not (raw_dt_dct or key):
            raise ValueError("NoInputData: Unable to find the active channels due to lack of input data.")
        
        search = lambda key_: re.search(r"RHK_CH(\d+)Drive_MasterOscillator", 
                                       key_, 
                                       flags=re.A)
        # print(' #### key : ', raw_dt_dct.keys())
        if key is not None:
            srch = search(key)
            if srch:
                return srch.groups()[0]
         
        # Get the active channel
        for key_, val in raw_dt_dct.items():

            srch = search(key_)
            # expect val string of 1 of 0 
            if srch and int(val) == 1:
                return srch.groups()[0]
        
        return

    @staticmethod
    def get_key_with(active_chnl=None, key=None):
        if not active_chnl:
            return key
        
        repl = rf"RHK_CH{active_chnl}Drive"

        return re.sub(pattern=r"RHK_CH[0-9]+Drive", repl=repl, string=key)
    
    def _handle_fields_with_modified_raw_data_key(self, 
                                                partial_conf_dict: dict, 
                                                parent_path: str,
                                                group_name: str,
                                                func_to_raw_key: callable):

        # only field
        for fld_key, end_dct in partial_conf_dict.items():
            if not (isinstance(end_dct, dict) and "raw_path" in end_dct):
                continue
                      
            mod_val_dct = {}
            # correct the active channel in the raw data key
            for tag, raw_str in end_dct.items():
                if tag == "note":
                    continue
                mod_vval = func_to_raw_key(raw_str)
                mod_val_dct[tag] = mod_vval
            data, unit, other_attrs = _get_data_unit_and_others(data_dict=self.raw_data, 
                                                                end_dict=mod_val_dct)
            self.template[f"{parent_path}/{group_name}/{fld_key}/@units"] = unit
            self.template[f"{parent_path}/{group_name}/{fld_key}"] = to_intended_t(data)
            if other_attrs:
                for k, v in other_attrs.items():
                    self.template[f"{parent_path}/{fld_key}/@{k}"] = v
    
    def _handle_variadic_field_with_modified_raw_data_key(self,
                                                          varidic_dct: dict,
                                                          parent_parh: str,
                                                          group_name: str,
                                                          fld_to_modify,
                                                          func_to_raw_key):
        if len(varidic_dct) >= 1:
            part_to_embed, raw_path_dct = list(varidic_dct.items())[0]
        else:
            raise ValueError(f"Variadic dict should have only one element.")
        
        mod_fld = replace_variadic_name_part(fld_to_modify, part_to_embed)

        self._handle_fields_with_modified_raw_data_key(partial_conf_dict={mod_fld: raw_path_dct},
                                                       parent_path=parent_parh,
                                                       group_name=group_name,
                                                       func_to_raw_key=func_to_raw_key)
        
    def walk_through_config_by_modified_raw_data_key(self, 
                                                         partial_conf_dict: dict, 
                                                         parent_path: str,
                                                         group_name: str,
                                                         func_to_raw_key: callable):

        self._handle_fields_with_modified_raw_data_key(partial_conf_dict=partial_conf_dict,
                                                       parent_path=parent_path,
                                                       group_name=group_name,
                                                       func_to_raw_key=func_to_raw_key)
                # Walk through the nested group                                                      
        for key, val in partial_conf_dict.items():
            # skips fields
            if isinstance(val, dict) and "raw_path" in val:
                continue
            # Variadic fields
            elif isinstance(val, list) and all("raw_path" in enddct for vardict in val for _, enddct in vardict.items()):
                for var_fld_dct in val:
                    self._handle_variadic_field_with_modified_raw_data_key(varidic_dct=var_fld_dct,
                                                                           parent_parh=parent_path,
                                                                           group_name=group_name,
                                                                           fld_to_modify=key,
                                                                           func_to_raw_key=func_to_raw_key)
            # Nested group
            elif isinstance(val, dict):
                self.walk_through_config_by_modified_raw_data_key(partial_conf_dict=val,
                                                                      parent_path=f"{parent_path}/{group_name}",
                                                                      group_name=key,
                                                                      func_to_raw_key=func_to_raw_key
                                                                      )


    def _construct_lockin_amplifier_grp(self,
                                    partial_conf_dict: dict,
                                    parent_path: str = "",
                                    group_name: Optional[str] = None):
        
        # TODO: Make the active channel object level variable
        actv_chnl = self.find_active_channel(raw_dt_dct=self.raw_data)
        self.walk_through_config_by_modified_raw_data_key(partial_conf_dict=partial_conf_dict,
                                                              parent_path=parent_path,
                                                              group_name=group_name,
                                                              func_to_raw_key=lambda k: self.get_key_with(active_chnl=actv_chnl, key=k))


    def _construct_scan_pattern_group(self,
                                      partial_conf_dict: dict,
                                      parent_path: str,
                                      group_name: Optional[str],
                                      scan_tag: str):
        ...
        

    def _construct_scan_region_group(self,
                                     partial_conf_dict: dict,
                                     parent_path: str,
                                     group_name: Optional[str],
                                     scan_tag: str):
        x_range = None
        x_start = None
        x_end = None
        y_range = None
        y_start = None
        y_end = None
        x_arr = None
        y_arr = None
        for k, v in self.raw_data.items():
            m = re.match(pattern=rf"/{scan_tag}/[\w/]*coords/[\w]+(x|y)", string=k, flags=re.I)
            if m and m.groups()[-1] == 'x':
                x_arr = v
            elif m and k.endswith('y'):
                y_arr = v
        
        if isinstance(x_arr, np.ndarray):
            x_end = x_arr[-1]
            x_start = x_arr[0]
            x_range = x_end - x_start
        if isinstance(y_arr, np.ndarray):
            y_end = y_arr[-1]
            y_start = y_arr[0]
            y_range = y_end - y_start            
        print(" #### partial_conf_dict : ", partial_conf_dict)
        # handle fields
        for key, val in partial_conf_dict.items():
            if re.match(pattern=r"scan_range_[\w]{1}\[", string=key, flags=re.I) and "raw_path" in val:
                print(" #### scan_range key : ", f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed="x")}")
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed="x")}"] = x_range
                # TODO collect unit from raw data dict
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed="x")}/@units"] = "m"
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed="y")}"] = y_range
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed="y")}/@units"] = "m"
            elif re.match(pattern=r"scan_start_[\w]{1}\[", string=key, flags=re.I) and "raw_path" in val:
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed="x")}"] = x_start
                # TODO collect unit from raw data dict
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed="x")}/@units"] = "m"
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed='y')}"] = y_start
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed='y')}/@units"] = "m"
            elif re.match(pattern=r"scan_end_[\w]{1}\[", string=key, flags=re.I) and "raw_path" in val:
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed='x')}"] = x_end
                # TODO collect unit from raw data dict
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed='x')}/@units"] = "m"
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed='y')}"] = y_end
                self.template[f"{parent_path}/{group_name}/{replace_variadic_name_part(key, part_to_embed='y')}/@units"] = "m"


    def _construct_nxscan_controllers(self,
                                      partial_conf_dict: dict,
                                      parent_path: str = "",
                                      group_name: Optional[str] = None):
        # Check the begining part of each and every key which will give you the end name of the groups
        # note that each key raw_data dictionary starts with the name of scan like `topography_backward`,
        # topography_forward, current_forward.

        for key, _ in self.raw_data.items():
            m = re.match(
                pattern=r'/(?=topography|current|backward|forward)([\w]+)/',
                string=key,
                flags=re.I
            )
            if m and (scan := m.groups()[0]) and scan not in self._scan_list:
                self._scan_list.append(m.groups()[0])
        
        print(" #### scan list : ", self._scan_list)
        m = re.search(pattern=r'(SCAN_CONTROL\[scan_control_)\*(\])', string=group_name)
        
        if not m:
            raise ValueError("UnavailableGroup: Scan controller group has not been found in config file.")
        
        groups = m.groups()
        for scan_tag in self._scan_list:
            group_name_mod = groups[0] + scan_tag + groups[1]
            
            parent_path_mod = f"{parent_path}/{group_name_mod}"
            for key, val in partial_conf_dict.items():
                if re.match(pattern=r"^mesh_SCAN\[mesh_scan\]$", string=rf"{key}", flags=re.I):
                    self._construct_scan_pattern_group(partial_conf_dict=val,
                                                       parent_path=parent_path_mod,
                                                       group_name=key,
                                                       scan_tag=scan_tag
                                                       )
                elif re.match(pattern=r"^scan_region$", string=rf"{key}", flags=re.I):
                    self._construct_scan_region_group(partial_conf_dict=val,
                                                      parent_path=parent_path_mod,
                                                      group_name=key,
                                                      scan_tag=scan_tag
                    )
                elif isinstance(val, dict) and "raw_path" in val:
                    if "#note" in val:
                        continue
                    # TODO raw path should be replaced by the corresponding scan_tag
                    data, unit, other_attrs = _get_data_unit_and_others(
                        data_dict=self.raw_data, end_dict=val
                        )
                    self.template[f"{parent_path_mod}/{key}"] = to_intended_t(data)
                    self.template[f"{parent_path_mod}/{key}/@units"] = unit
                    if other_attrs:
                        for k, v in other_attrs.items():
                            self.template[f"{parent_path_mod}/{key}/@{k}"] = v
                
