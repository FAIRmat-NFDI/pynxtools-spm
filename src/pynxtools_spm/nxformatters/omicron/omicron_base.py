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
        """Put the origin of an image at its bottom-left corner.

        An SM4 page stores row i at y = 'RHK_Yoffset' + i * 'RHK_Yscale', so the
        sign of 'RHK_Yscale' tells the slow scan direction: > 0 is an up scan
        (row 0 at the bottom), < 0 a down scan (row 0 at the top). Gwyddion,
        which 'gwyddionpy' runs, flips the rows of an up scan and always flips
        the columns, so every image it returns has row 0 at the top:
        https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/rhk-sm4.c

        | RHK_Yscale | raw row 0 is | gwyddionpy row 0 is | to get row 0 = bottom |
        |------------|--------------|---------------------|-----------------------|
        | > 0 (up)   | bottom       | top                 | flipud                |
        | < 0 (down) | top          | top                 | flipud                |

        'is_forward' is accepted for the signature of the hook but not used:
        'gwyddionpy' already returns each scan direction in the right x order, so the
        forward and backward images need no lateral flip.
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            return data
        return np.flipud(data)
