from pynxtools_spm.parsers.base_parser import SPMBase
import numpy as np
import re


class TxtBruker(SPMBase):
    """
    Parser for Bruker TXT files.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def parse(self):
        """Parse the Bruker TXT file and return a dictionary with the parsed data."""

        bruker_data_dict = {}

        # Got array header
        array_header = None
        array_data = []
        with open(self.file_path) as f_ob:
            lines = f_ob.readlines()
            for line in lines:
                line = line.strip()
                if line == "":
                    continue
                if (
                    ":" not in line
                    and not array_header
                    and "Force file list end" not in line
                ):
                    array_header = line
                elif ":" not in line and array_header:
                    cols = line.split()
                    # print(f"Cols: {cols}")
                    if len(array_data) == 0:
                        array_data = [[col.strip()] for col in cols]
                        print(f"Array data initialized: {array_data}")
                        continue
                    elif len(cols) != len(array_data):
                        # Use pynxtools logger
                        print(
                            f"Warning: line has different number of columns than header. "
                            f"Line: {line}, Header: {array_data}"
                        )
                        break
                    # Append data to each column
                    for ind, col in enumerate(cols):
                        array_data[ind].append(col.strip())
                    continue
                elif ":" in line and array_header:
                    array_header = None
                    key, val = line.split(":", 1)
                    key = key.strip()
                    val = val.strip()
                    temp_dict = self.extract_data_unit(key, val)
                    bruker_data_dict.update(temp_dict)
        if array_header and array_data:
            array_names = array_header.strip().split()
            print(f"Array names: {len(array_names)}")
            print(f"Array data length: {len(array_data)}")
            for ind, arr_name in enumerate(array_names):
                bruker_data_dict[f"/{arr_name.strip()}"] = np.array(
                    [float(x) for x in array_data[ind]]
                )
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

        # 172.0493 kHz
        pattern = r"^\s*([\d]+[.]?[\d]*)\s+(\w+)\s*$"
        matches = re.match(pattern=pattern, string=val)
        if matches and (match_grps := matches.groups()) and len(match_grps) == 2:
            temp_dict[f"{key}"] = match_grps[0]
            temp_dict[f"{key}/@unit"] = match_grps[1]
            return temp_dict

        temp_dict[f"{key}"] = val

        return temp_dict
