#!/usr/bin/env python3
"""
Customized parser for Bruker SPM data files.
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
#

import contextlib
import re
from pySPM import Bruker


class SPMBruker(Bruker):
    """
    Extended class to handle additional features of Bruker SPM images
    """

    def __init__(self, path, encoding="latin1"):
        Bruker.__init__(self, path)
        self.encoding = encoding
        self.file = []
        self.equipment = []
        with open(self.path, "rb") as file:
            mode = ""
            line = ""
            while True:
                line = file.readline().rstrip().replace(b"\\", b"")
                if line == b"*File list":
                    mode = "File"
                    self.file.append({})
                elif line == b"*Equipment":
                    mode = "Equipment"
                    self.equipment.append({})
                elif (
                    line == b"*Ciao image list"
                    or line == b"*Scanner list"
                    or line.startswith(b"*EC")
                ):
                    break

                elif mode == "File" or mode == "Equipment":
                    args = line.split(b": ")
                    if len(args) > 1:
                        if mode == "File":
                            self.file[-1][args[0]] = args[1]
                        elif mode == "Equipment":
                            self.equipment[-1][args[0]] = args[1]

    @property
    def channels(self):
        return self.get_list_of_channels(encoding=self.encoding)

    def get_list_of_channels(self, encoding=None):
        if encoding is None:
            encoding = self.encoding
        channels = []
        for layer in self.layers:
            with contextlib.suppress(KeyError):
                channel_info = layer[b"@2:Image Data"][0].decode(encoding)
                result = re.match(
                    r'([^ ]+) \[([^]]*)] "([^"]*)"', channel_info
                ).groups()
                channels.append(result[2])
        for layer in self.layers:
            with contextlib.suppress(KeyError):
                channel_info = layer[b"@3:Image Data"][0].decode(encoding)
                result = re.match(
                    r'([^ ]+) \[([^]]*)] "([^"]*)"', channel_info
                ).groups()
                channels.append(result[2])
        return channels

    def get_layer_with_channel(self, channel, encoding=None):
        if encoding is None:
            encoding = self.encoding
        for _, layer in enumerate(self.layers):
            with contextlib.suppress(KeyError):
                channel_info = layer[b"@2:Image Data"][0].decode(encoding)
                result = re.match(
                    r'([^ ]+) \[([^]]*)] "([^"]*)"', channel_info
                ).groups()
                if result[2] == channel:
                    return layer
            with contextlib.suppress(KeyError):
                channel_info = layer[b"@3:Image Data"][0].decode(encoding)
                result = re.match(
                    r'([^ ]+) \[([^]]*)] "([^"]*)"', channel_info
                ).groups()
                if result[2] == channel:
                    return layer
        raise ValueError(f"Channel {channel} not found")

    def get_channel_data(
        self,
        channel="Height Sensor",
        backward=False,
        corr=None,
        debug=False,
        encoding="latin1",
        lazy=True,
        mfm=False,
        mock_data=False,
    ):
        image = self.get_channel(
            channel=channel,
            backward=backward,
            corr=corr,
            debug=debug,
            encoding=encoding,
            lazy=lazy,
            mfm=mfm,
            mock_data=mock_data,
        )
        return image.pixels
