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
import re

from pynxtools_spm.nxformatters.base_formatter import SPMformatter
from pynxtools_spm.nxformatters.helpers import _get_data_unit_and_others


class BrukerBase(SPMformatter):
    """
    Base class for Bruker SPM formatters.
    """

    _grp_to_func = {}
