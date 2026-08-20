"""
A parser for files from AFM experiment (Bruker FLT) into a simple dict.
"""

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

import logging
import re
from typing import Any

from gwyddionpy import Channel, GwyData, load

import pynxtools_spm.parsers.helpers as phs
from pynxtools_spm.parsers.base_parser import SPMBase
from pynxtools_spm.parsers.helpers import UNIT_TO_SKIP

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


# Bruker SPMLab writes the unit as a trailing token of the value, e.g.
# 'SetPoint=0.030000 V' or 'ScanningRate=1.0000 µm/s'.
VALUE_WITH_UNIT = re.compile(
    r"^(?P<value>[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s+(?P<unit>\S+)$"
)

# The FLT header is Windows written INI text: CRLF line endings and single byte
# characters ('µ' is 0xB5, '°' is 0xB0), so it is cp1252. 'latin-1' agrees with
# cp1252 on every byte >= 0xA0 and decodes all 256 byte values without raising,
# which matters because the header is read out of an otherwise binary file.
HEADER_ENCODING = "latin-1"
# 'DataOffset' is the first byte of the binary raster, i.e. the header length.
DATA_OFFSET = re.compile(r"^DataOffset\s*=\s*(?P<offset>\d+)\s*$", re.MULTILINE)
SECTION = re.compile(r"^\[(?P<section>.+)\]$")
# Enough to cover the header (958 bytes in the reference file) in one read.
HEADER_CHUNK_SIZE = 8192


class FltBruker(SPMBase):
    """Parser for Bruker (SPMLab) FLT AFM files.

    A single FLT file stores one channel (e.g. 'Height') of one scan direction.
    ``gwyddionpy.load`` returns a ``GwyData`` container holding that channel as a
    ``Channel`` object with the image data, the physical scan size and the
    key-value metadata of the file header.
    """

    @staticmethod
    def _split_value_and_unit(value: Any) -> tuple[Any, str | None]:
        """Split a metadata value into its numeric part and its unit.

        Returns ``(value, None)`` when the value carries no unit, so that the
        caller only writes a '/@unit' entry when a unit is really present.
        Values such as 'GainP=0.800000 (1000.000000)' (a second number rather
        than a unit) or 'Leveling=1D Line Fit' are left untouched.
        """
        if not isinstance(value, str):
            return value, None

        match = VALUE_WITH_UNIT.match(value.strip())
        if match is None:
            return value, None

        unit = match.group("unit")
        # A parenthesised or numeric trailing token is not a unit.
        if unit.startswith("(") or _is_number(unit):
            return value, None
        if unit.lower() in UNIT_TO_SKIP:
            unit = ""
        return match.group("value"), unit

    def _get_raw_header_dict(self) -> dict[str, Any]:
        """Read the ASCII header of the FLT file into a section wise nested dict.

        ``gwyddionpy`` drops a few header keys (e.g. 'OffsetX'/'OffsetY' and the
        linearization flags) and flattens the two 'Leveling' keys of the
        '[Data Parameters]' and '[PreProcessing]' sections into one. Reading the
        header directly keeps them, grouped by their section.
        """
        with open(self.file_path, "rb") as file_obj:
            chunk = file_obj.read(HEADER_CHUNK_SIZE)
            match = DATA_OFFSET.search(chunk.decode(HEADER_ENCODING))
            if match is None:
                logging.warning(
                    "No 'DataOffset' in %s, the ASCII header is skipped.",
                    self.file_path,
                )
                return {}
            header_end = int(match.group("offset"))
            if header_end > len(chunk):
                file_obj.seek(0)
                chunk = file_obj.read(header_end)

        header_dict: dict[str, Any] = {}
        section_dict: dict[str, Any] = {}
        for line in chunk[:header_end].decode(HEADER_ENCODING).splitlines():
            line = line.strip()
            if not line:
                continue
            section_match = SECTION.match(line)
            if section_match is not None:
                section_dict = header_dict.setdefault(
                    section_match.group("section"), {}
                )
                continue
            if "=" not in line:
                continue
            key, val = line.split("=", 1)
            key = key.strip()
            value, unit = self._split_value_and_unit(val.strip())
            section_dict[key] = value
            if unit is not None:
                section_dict[f"{key}/@unit"] = unit
        return header_dict

    def _get_channel_dict(self, channel: Channel) -> dict[str, Any]:
        """Build the nested dict of a single channel."""
        channel_dict: dict[str, Any] = {
            "name": channel.name,
            "data": channel.data,
            "data/@unit": channel.si_unit_z,
            "x_real": channel.xreal,
            "x_real/@unit": channel.si_unit_xy,
            "y_real": channel.yreal,
            "y_real/@unit": channel.si_unit_xy,
        }

        meta_dict: dict[str, Any] = {}
        for key, val in channel.meta.items():
            value, unit = self._split_value_and_unit(val)
            meta_dict[key] = value
            if unit is not None:
                meta_dict[f"{key}/@unit"] = unit
        channel_dict["meta"] = meta_dict

        return channel_dict

    def parse(self) -> dict[str, Any]:
        """Parse the Bruker FLT file into a slash separated key-value dict.

        Returns
        -------
        dict
            Flattened dict, e.g.::

                /source_format            : 'spmlabf'
                /Height/data              : ndarray of shape (512, 512)
                /Height/data/@unit        : 'm'
                /Height/x_real            : 1e-06
                /Height/x_real/@unit      : 'm'
                /Height/meta/Mode         : 'Peak Force Tapping'
                /Height/meta/SetPoint     : '0.030000'
                /Height/meta/SetPoint/@unit : 'V'
                /Height/header/Data Parameters/OffsetX : '1.0000'
                /Height/header/Data Parameters/OffsetX/@unit : 'µm'
        """
        gwy_data: GwyData = load(self.file_path)
        header_dict = self._get_raw_header_dict()

        nested_dict: dict[str, Any] = {"source_format": gwy_data.source_format}
        for channel_name, channel in gwy_data.channels.items():
            channel_dict = self._get_channel_dict(channel)
            # The header describes the single channel stored in the file.
            channel_dict["header"] = header_dict
            nested_dict[channel_name] = channel_dict
        flattened_dict: dict[str, Any] = {}
        phs.nested_path_to_slash_separated_path(nested_dict, flattened_dict)
        return flattened_dict


def _is_number(text: str) -> bool:
    """Check whether the text is a plain number."""
    try:
        float(text)
    except ValueError:
        return False
    return True
