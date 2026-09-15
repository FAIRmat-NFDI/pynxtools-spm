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


class BrukerBase(SPMformatter):
    """
    Base class for Bruker SPM formatters.
    """

    _grp_to_func = {}

    def rearrange_data_according_to_axes(self, data, is_forward: bool | None = None):
        """Put the origin of an image at its bottom-left corner.

        A NanoScope '.spm' file stores the image rows in a fixed order, bottom
        row first, whatever its 'Frame direction' (Up or Down). Gwyddion, which
        ``gwyddionpy`` runs, turns every NanoScope image upside down once to
        put row 0 at the top, and never reads 'Frame direction':
        https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/nanoscope.c

        | Frame direction | gwyddionpy row 0 is | to get row 0 = bottom |
        |-----------------|---------------------|-----------------------|
        | Up              | top                 | flipud                |
        | Down            | top                 | flipud                |

        SPMLab '.FLT' images, also read through ``gwyddionpy``, get the same flip.

        ``is_forward`` is accepted for the signature of the hook but not used:
        ``gwyddionpy`` already returns each scan direction in the right x order,
        so the forward and backward images need no lateral flip. Force curves
        from the NanoScope TXT export are one dimensional and pass through.
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            return data
        return np.flipud(data)
