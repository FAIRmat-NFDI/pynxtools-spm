"""
A parser for files from AFM experiment (Bruker NanoScope) into a simple dict.
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

import re
from typing import Any

import numpy as np
from gwyddionpy import GwyData, load
from pynxtools import logger as pynx_logger
from pynxtools.units import ureg

from pynxtools_spm.parsers.base_parser import SPMBase

# The ASCII header is Windows written text with single byte characters
# ('µ' is 0xB5, '°' is 0xB0); 'latin-1' decodes all 256 byte values without
# raising, which matters because the header precedes the binary image block.
HEADER_ENCODING = "latin-1"
# Terminates the ASCII header; everything after it is the binary image block.
HEADER_END = b"\\*File list end"
# A section header, e.g. '\*Ciao image list'.
SECTION = re.compile(r"^\\\*(?P<section>.+?)\s*$")
# A key-value line, e.g. '\Scan Size: 20000 nm'. The separator is a colon
# followed by a space, because a key may itself contain a colon, as in
# '\@2:Image Data: S [ZSensor] "Height Sensor"'.
KEY_VALUE = re.compile(r"^\\(?P<key>.+?):(?:\s(?P<value>.*))?$")

# 'V (0.00001164153 kHz/LSB) 172.0493 kHz' -> value '172.0493', unit 'kHz'.
SCALED_VALUE = re.compile(r"^\s*(\w+)\s+\(([\d.]+)\s+([\w/]+)\)\s+([\d.]+)\s+(\w+)\s*$")
# '172.0493 kHz' -> value '172.0493', unit 'kHz'.
VALUE_WITH_UNIT = re.compile(r"^\s*([\d]+[.]?[\d]*)\s+(\w+)\s*$")
# 'S [ZSensor] "Height Sensor"' -> channel title 'Height Sensor'.
IMAGE_DATA = re.compile(r'^\s*(\w+)\s+\[(\w+)\]\s+["]*([\w\s]+)["]*$')
# '\@2:Z scale: V [Sens. ZsensSens] (0.00000000572205 V/LSB) 1.195962 V' ->
# sensitivity name 'Sens. ZsensSens' and the unit the scale is written in, 'V'.
Z_SCALE = re.compile(
    r"^\s*\w+\s+\[(?P<sens>[^]]+)\]\s+\([^)]*\)\s+[\d.]+\s*(?P<unit>\S*)"
)
# '\@Sens. ZsensSens: V 485.6748 nm/V' -> the unit the sensitivity converts to, 'nm'.
SENSITIVITY = re.compile(r"^\s*\w+\s+[\d.]+\s+(?P<unit>[^/\s]+)(?:/\w+)?\s*$")

# The section holding the scan parameters, exposed under '/Scanner_list/<i>/'.
SCAN_SECTION = "Ciao scan list"
# One section per recorded image layer.
IMAGE_SECTION = "Ciao image list"
# Sections copied verbatim, mapped to their prefix in the flattened dict.
PLAIN_SECTIONS = {"File list": "File", "Equipment list": "Equipment_list"}
# NanoScope names the two halves of a line scan this way.
DIRECTIONS = {"Trace": "forward", "Retrace": "backward"}

# NanoScope writes the Z scale of some channels in millivolts while the matching
# sensitivity is given per volt. The channel values keep the scale's own prefix,
# so the conversion to the sensitivity unit carries this factor.
MILLI_VOLT_FACTOR = 1000.0


class SpmBruker(SPMBase):
    """Parser for Bruker (NanoScope) SPM AFM files.

    A single '.spm' file stores every recorded channel in both scan directions.
    ``gwyddionpy.load`` returns the image layers in file order; the ASCII header
    is read here as well, because gwyddionpy merges all header sections into one
    flat per-channel dict and the section a key came from is part of the key
    path this parser exposes.
    """

    def parse(self, encoding: str = HEADER_ENCODING) -> dict[str, Any]:
        """Parse the Bruker SPM file into a slash separated key-value dict.

        Returns
        -------
        dict
            Flattened dict, e.g.::

                /Height_Sensor/forward           : ndarray of shape (512, 512)
                /Scan_list                       : ['Height_Sensor/backward', ...]
                /File/Version                    : '0x09400105'
                /Scanner_list/0/Scan_Size        : '20000'
                /Scanner_list/0/Scan_Size/@unit  : 'nm'
                /Scan/Height_Sensor/forward/Line_Direction : 'Trace'
        """
        sections = self._read_header_sections(encoding)
        gwy_data: GwyData = load(self.file_path)

        spm_dict: dict[str, Any] = {}
        scan_list: list[str] = []
        channel_data: dict[str, dict[str, np.ndarray]] = {}
        scan_index = 0
        equipment_index = 0
        image_index = 0
        # gwyddionpy yields one channel per image layer, in header order.
        channels = list(gwy_data.channels.values())

        for name, entries in sections:
            if name in PLAIN_SECTIONS:
                prefix = PLAIN_SECTIONS[name]
                if name == "Equipment list":
                    prefix = f"{prefix}/{equipment_index}"
                    equipment_index += 1
                spm_dict.update(self._prefixed(entries, prefix))
            elif name == SCAN_SECTION:
                spm_dict.update(self._prefixed(entries, f"Scanner_list/{scan_index}"))
                scan_index += 1
            elif name == IMAGE_SECTION:
                if image_index >= len(channels):
                    pynx_logger.warning(
                        "Image layer %s has no matching channel in the file.",
                        image_index,
                    )
                    continue
                channel_name, direction = self._channel_and_direction(entries)
                image_index += 1
                if channel_name is None:
                    continue
                spm_dict.update(
                    self._prefixed(entries, f"Scan/{channel_name}/{direction}")
                )
                scan_list.append(f"{channel_name}/{direction}")
                channel_data.setdefault(channel_name, {})[direction] = np.flipud(
                    channels[image_index - 1].data
                ) * self._scale_factor(entries, sections)

        for channel_name, per_direction in channel_data.items():
            for direction in DIRECTIONS.values():
                # A channel recorded in one direction only is exposed under both,
                # so that a config can address either without having to know which
                # half of the line scan the instrument stored.
                data = per_direction.get(direction)
                if data is None:
                    data = next(iter(per_direction.values()))
                spm_dict[f"/{channel_name}/{direction}"] = data

        spm_dict["/Scan_list"] = scan_list
        return spm_dict

    def _read_header_sections(self, encoding: str) -> list[tuple[str, dict[str, str]]]:
        """Read the ASCII header into (section name, key-value dict) pairs.

        Sections repeat, so the result is a list rather than a dict: a file holds
        one 'Ciao image list' section per recorded image layer.
        """
        with open(self.file_path, "rb") as file_obj:
            raw = file_obj.read()
        header_end = raw.find(HEADER_END)
        if header_end == -1:
            pynx_logger.warning(
                "No '%s' marker in %s; the ASCII header is skipped.",
                HEADER_END.decode(encoding),
                self.file_path,
            )
            return []

        sections: list[tuple[str, dict[str, str]]] = []
        entries: dict[str, str] = {}
        for line in raw[:header_end].decode(encoding).splitlines():
            line = line.rstrip()
            section_match = SECTION.match(line)
            if section_match is not None:
                entries = {}
                sections.append((section_match.group("section"), entries))
                continue
            key_value = KEY_VALUE.match(line)
            if key_value is not None:
                entries[key_value.group("key").strip()] = key_value.group("value") or ""
        return sections

    def _prefixed(self, entries: dict[str, str], prefix: str) -> dict[str, Any]:
        """Flatten one header section under the given key prefix."""
        flattened: dict[str, Any] = {}
        for key, value in entries.items():
            for sub_key, sub_value in self.extract_data_unit(key, value).items():
                flattened[f"/{prefix}/{sub_key}"] = sub_value
        return flattened

    @staticmethod
    def _channel_and_direction(entries: dict[str, str]) -> tuple[str | None, str]:
        """Read the channel name and scan direction of one image layer.

        The channel name is the quoted title of '@2:Image Data', e.g.
        'S [ZSensor] "Height Sensor"' names the channel 'Height_Sensor'.
        """
        image_data = entries.get("@2:Image Data", "")
        matches = IMAGE_DATA.match(image_data)
        if matches is None:
            pynx_logger.warning(
                "Image layer is not annotated with a channel name: %r.", image_data
            )
            return None, ""
        channel_name = matches.groups()[-1].strip().replace(" ", "_")
        # A layer without a stated direction is the forward half of the scan.
        direction = DIRECTIONS.get(entries.get("Line Direction", ""), "forward")
        return channel_name, direction

    @staticmethod
    def _scale_factor(
        entries: dict[str, str], sections: list[tuple[str, dict[str, str]]]
    ) -> float:
        """Convert a layer from the SI values of gwyddionpy to its own unit.

        The layer's '@2:Z scale' names the sensitivity that turns the recorded
        volts into a physical quantity; the unit of that sensitivity is the unit
        the channel values are expressed in, e.g. 'nm' for
        '\\@Sens. ZsensSens: V 485.6748 nm/V'. A sensitivity without a unit
        leaves the values as gwyddionpy returns them.
        """
        z_scale = Z_SCALE.match(entries.get("@2:Z scale", ""))
        if z_scale is None:
            return 1.0

        sensitivity = None
        for _, section_entries in sections:
            sensitivity = section_entries.get(f"@{z_scale.group('sens')}")
            if sensitivity is not None:
                break
        if sensitivity is None:
            return 1.0

        sens_match = SENSITIVITY.match(sensitivity)
        if sens_match is None:
            return 1.0
        try:
            factor = (
                1.0
                / ureg.Quantity(1.0, sens_match.group("unit")).to_base_units().magnitude
            )
        except Exception:
            return 1.0

        if z_scale.group("unit") == "mV":
            factor *= MILLI_VOLT_FACTOR
        return factor

    def extract_data_unit(self, key: str, val: str) -> dict[str, Any]:
        """Split a header value into its value and, when present, its unit.

        Handles the two shapes NanoScope writes a scaled quantity in::

            V (0.00001164153 kHz/LSB) 172.0493 kHz
            172.0493 kHz

        Values that match neither are stored as they are.
        """
        key = re.sub(r"\s+", "_", key)
        temp_dict: dict[str, Any] = {}

        matches = SCALED_VALUE.match(val)
        if matches:
            match_grps = matches.groups()
            temp_dict[key] = match_grps[3]
            temp_dict[f"{key}/@units"] = match_grps[4]
            return temp_dict

        matches = VALUE_WITH_UNIT.match(val)
        if matches:
            match_grps = matches.groups()
            temp_dict[key] = match_grps[0]
            temp_dict[f"{key}/@unit"] = match_grps[1]
            return temp_dict

        temp_dict[key] = val
        return temp_dict
