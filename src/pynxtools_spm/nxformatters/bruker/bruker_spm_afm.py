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
import numpy as np
from typing import Optional, Union

from pynxtools_spm.nxformatters.bruker.bruker_base import BrukerBase
import pynxtools_spm.nxformatters.helpers as fhs
from pynxtools_spm.configs import load_default_config
from pynxtools.dataconverter.template import Template
from pathlib import Path


class BrukerSpmAFM(BrukerBase):
    """
    Formatter for Bruker AFM data from .spm files..
    """

    __grp_to_func: dict[str, str] = {
        "SPM_SCAN_CONTROL[spm_scan_control]": "_construct_nxscan_controllers"
    }

    def __init__(
        self,
        template: Template,
        raw_file: str | Path,
        eln_file: str | Path | None = None,
        config_file: str | Path | None = None,
    ):
        super().__init__(template, raw_file, eln_file, config_file)

    def get_nxformatted_template(self):
        self.walk_though_config_nested_dict(self.config_dict, "")
        self._format_template_from_eln()
        self._handle_special_fields()

    def _get_conf_dict(self, config_file: str | Path = None):
        if config_file:
            return fhs.read_config_file(config_file)

        return load_default_config(config_type="bruker_spm_afm")

    def _construct_nxscan_controllers(
        self, partial_conf_dict, parent_path, group_name="scan_control", **kwarg
    ):
        return super()._construct_nxscan_controllers(
            partial_conf_dict, parent_path, group_name, **kwarg
        )
