"""Parser for Bruker force-curve TXT export files."""

import re

import numpy as np
from pynxtools import logger as pynx_logger

from pynxtools_spm.parsers.base_parser import SPMBase


class TxtBruker(SPMBase):
    """Parser for Bruker TXT files."""

    @staticmethod
    def _normalize_section_name(raw_name: str) -> str:
        """Convert a section header text to a snake_case path segment."""
        return re.sub(r"\s+", "_", raw_name.strip())

    @staticmethod
    def _extract_unit_from_column_name(col_name: str) -> str | None:
        """Extract the physical unit token from a Bruker array column name.

        Bruker encodes units inside column names using the direction markers
        'Ex' (extension) and 'Rt' (retrace) as anchors:
          - unit before direction:  Time_s_Ex        → 's'
          - unit after  direction:  Calc_Ramp_Ex_nm  → 'nm'
        Returns None when no direction marker is found.
        """
        direction_tokens = {"Ex", "Rt"}
        tokens = col_name.split("_")
        for i, token in enumerate(tokens):
            if token in direction_tokens:
                if i + 1 < len(tokens):
                    # unit token follows direction (e.g. Calc_Ramp_Ex_nm)
                    return tokens[i + 1]
                if i > 0:
                    # unit token precedes direction (e.g. Time_s_Ex)
                    return tokens[i - 1]
        return None

    def parse(self, *args, **kwargs):
        """Parse the Bruker TXT file and return a dictionary with the parsed data."""
        bruker_data_dict = {}

        # Track the active section so keys are stored under /SectionName/index/key.
        # section_counters counts how many times each section name has appeared,
        # giving a 0-based index that disambiguates repeated sections such as
        # "Ciao force image list".
        section_counters: dict[str, int] = {}
        current_section: str | None = None

        array_header: str | None = None
        array_data: list[list[str]] = []
        last_line = ""

        with open(self.file_path, encoding="utf-8") as f_ob:
            for line in f_ob:
                line = line.strip()
                if not line:
                    continue

                # Strip the wrapping double-quotes that Bruker TXT uses on every line.
                clean = line.strip('"')

                # Section markers start with \* (subsection) or \? (root header).
                if clean.startswith("\\*") or clean.startswith("\\?"):
                    section_raw = re.sub(r"^\\[*?]", "", clean).strip()
                    if "Force file list end" in section_raw:
                        # End of metadata — subsequent lines are array data.
                        current_section = None
                    else:
                        name = self._normalize_section_name(section_raw)
                        idx = section_counters.get(name, -1) + 1
                        section_counters[name] = idx
                        current_section = f"{name}/{idx}"
                    last_line = line
                    continue

                # Detect the tab-separated column-header line that immediately
                # follows the "Force file list end" marker.
                if (
                    ":" not in clean
                    and array_header is None
                    and current_section is None
                    and "Force file list end" in last_line
                ):
                    array_header = clean
                    last_line = line
                    continue

                # Array data rows (tab-separated numeric values).
                if ":" not in clean and array_header is not None:
                    cols = clean.split()
                    if not array_data:
                        array_data = [[col] for col in cols]
                    elif len(cols) != len(array_data):
                        pynx_logger.error(
                            "Column count mismatch in array data: got %s, expected %s.",
                            len(cols),
                            len(array_data),
                        )
                        break
                    else:
                        for ind, col in enumerate(cols):
                            array_data[ind].append(col)
                    last_line = line
                    continue

                # Key-value pair: \Key: value
                if ": " in clean:
                    raw_key, raw_val = clean.split(": ", 1)
                    temp_dict = self.extract_data_unit(raw_key.strip(), raw_val.strip())
                    if current_section is not None:
                        temp_dict = {
                            f"/{current_section}{k}": v for k, v in temp_dict.items()
                        }
                    bruker_data_dict.update(temp_dict)

                last_line = line

        if array_data and array_header is not None:
            array_names = array_header.strip().split()
            for ind, arr_name in enumerate(array_names):
                bruker_data_dict[f"/{arr_name}"] = np.array(
                    [float(x) for x in array_data[ind]]
                )
                unit = self._extract_unit_from_column_name(arr_name)
                if unit is not None:
                    bruker_data_dict[f"/{arr_name}/unit"] = unit

        return bruker_data_dict

    def extract_data_unit(self, key, val):
        """
        Some data comes in complex string, this function extract them and store in data_dict.

        A example key value pair is
        `\\@MicroscopeList: S [AFMMode] "Contact"`
        Where  is hosting the data `172.049` and unit.

        return: tuple[value, unit]
        """
        # replace space in key with underscore
        key = re.sub(r"\s+", "_", key)
        key = re.sub(r"\\", "/", key)
        key = re.sub(r"\"", "", key)

        val = re.sub(r"\"", "", val)

        temp_dict = {}
        # V (0.00001164153 kHz/LSB) 172.0493 kHz
        pattern = r"^\s*(\w+)\s+\(([\d.]+)\s+([\w/]+)\)\s+([\d.]+)\s+(\w+)\s*$"
        matches = re.match(pattern=pattern, string=val)
        if matches and (match_grps := matches.groups()) and len(match_grps) == 5:
            temp_dict[f"{key}"] = match_grps[3]
            temp_dict[f"{key}/@units"] = match_grps[4]
            return temp_dict

        # S [AFMMode] Contact
        pattern = r"^\s*(\w+)\s+\[(\w+)\]\s+(\w+)$"
        matches = re.match(pattern=pattern, string=val)
        if matches and (match_grps := matches.groups()) and len(match_grps) == 3:
            temp_dict[f"{key}/{match_grps[1]}"] = match_grps[2]
            return temp_dict

        # 172.0493 kHz  (leading minus supported for negative offsets)
        pattern = r"^\s*(-?[\d]+[.]?[\d]*)\s+(\w+)\s*$"
        matches = re.match(pattern=pattern, string=val)
        if matches and (match_grps := matches.groups()) and len(match_grps) == 2:
            temp_dict[f"{key}"] = match_grps[0]
            temp_dict[f"{key}/@unit"] = match_grps[1]
            return temp_dict

        temp_dict[f"{key}"] = val

        return temp_dict
