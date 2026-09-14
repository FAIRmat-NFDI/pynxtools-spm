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
from typing import List, Optional
import numpy as np

from pynxtools_spm.nxformatters.base_formatter import SPMformatter


class NanonisBase(SPMformatter):
    """Base class for Nanonis SPM data formatters."""

    def _arange_axes(self, direction="down"):
        """Arrange fast and slow axes according to the scan direction."""

        fast_slow: list[str]
        if direction.lower() == "down":
            fast_slow = ["-Y", "X"]
        elif direction.lower() == "up":
            fast_slow = ["Y", "X"]
        elif direction.lower() == "right":
            fast_slow = ["X", "Y"]
        elif direction.lower() == "left":
            fast_slow = ["-X", "Y"]
        else:
            fast_slow = ["X", "Y"]
        self.scan_control.fast_axis = fast_slow[0].lower()
        self.scan_control.slow_axis = fast_slow[1].lower()

        return fast_slow

    def rearrange_data_according_to_axes(self, data, is_forward: bool | None = None):
        """Put the origin of an image at its bottom-left corner.

        An SXM file stores the lines in the order they were recorded, and each
        backward line in the order the tip traveled, from right to left. A
        'down' scan starts at the top, so its rows are flipped to put the bottom
        row first; an 'up' scan already starts at the bottom. Gwyddion's Nanonis
        module applies the same two flips, from 'SCAN_DIR' and the channel
        direction (see 'tests/README.md').

        '_arange_axes' records a 'down' scan as fast axis '-y'.

        Parameters
        ----------
        data : np.ndarray
            Two dimensional array data from scan.
        is_forward : bool, optional
            False for the backward image of a channel.
        """
        fast_axis = getattr(self.scan_control, "fast_axis", None)
        # No scan axes (e.g. bias spectroscopy) or no image: nothing to orient.
        if fast_axis is None or not isinstance(data, np.ndarray) or data.ndim != 2:
            return data
        if fast_axis == "-y":
            data = np.flipud(data)
        if is_forward is False:
            data = np.fliplr(data)
        return data

    def _pixel_centres(self, axis: str) -> np.ndarray:
        """Ascending positions of the pixel centres along 'x' or 'y'.

        'SCAN_OFFSET' is the centre of the scan frame, so the frame spans
        'offset - range/2' to 'offset + range/2' and pixel 'i' of 'n' sits at
        'offset - range/2 + (i + 0.5) * range/n'.
        """
        offset = getattr(self.scan_control, f"{axis}_offset")
        scan_range = getattr(self.scan_control, f"{axis}_range")
        points = int(getattr(self.scan_control, f"{axis}_points"))
        step = scan_range / points
        return offset - scan_range / 2 + (np.arange(points) + 0.5) * step
