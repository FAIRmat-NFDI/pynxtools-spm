#!/usr/bin/env python3
"""
Base formatter for Nanonis SPM data.
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
from __future__ import annotations

import numpy as np

from pynxtools_spm.nxformatters.base_formatter import SPMformatter


class OmicronBase(SPMformatter):
    """Base class for Omicron SPM data formatters."""

    def rearrange_data_according_to_axes(self, data, is_forward: bool | None = None):
        """Put row 0 of the image at the top, which is the convention of this plugin.

        'spym' orders the rows of an SM4 image the other way round, so the first
        row it returns is the bottom one. Every other vendor already hands over,
        or is flipped into, top-row-first order, and a viewer draws row 0 at the
        top, so an SM4 image would otherwise be shown upside down.

        'is_forward' is accepted for the signature of the hook but not used:
        'spym' already returns each scan direction in the right x order, so the
        forward and backward images need no lateral flip.
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            return data
        return np.flipud(data)
