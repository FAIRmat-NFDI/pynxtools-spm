from pynxtools_spm.parsers.bruker.bruker_spm import SPMBruker
from pynxtools_spm.parsers.base_parser import SPMBase
import re


class SpmBruker(SPMBase):
    """
    Parser for Omicron SM4 STM files.
    """

    def __init__(self, file_path):
        # delete
        super().__init__(file_path)

    def decode_bytes(self, val, encoding="latin-1"):
        if isinstance(val, list):
            return [self.decode_bytes(v, encoding=encoding) for v in val]
        elif isinstance(val, bytes):
            return val.decode(encoding)
        else:
            return val

    def parse(self, encoding="latin1"):
        """Parse the Bruker SPM file and return a dictionary with the parsed data."""
        spm_obj = SPMBruker(self.file_path, encoding=encoding)

        bruker_data_dict = {}
        channel_list = spm_obj.channels

        # file is list of dic; dict : metadata/path to value
        if len(spm_obj.file) > 0:
            for meta_dict in spm_obj.file:
                for key, val in meta_dict.items():
                    temp_dict = self.extract_data_unit(key, val, encoding=encoding)
                    bruker_data_dict.update(
                        {f"/File/{k}": v for k, v in temp_dict.items()}
                    )
        if len(spm_obj.equipment) > 0:
            for ind, meta_dict in enumerate(spm_obj.equipment):
                for key, val in meta_dict.items():
                    temp_dict = self.extract_data_unit(key, val, encoding=encoding)
                    bruker_data_dict.update(
                        {f"/Equipment_list/{ind}/{k}": v for k, v in temp_dict.items()}
                    )

        # Ciao scan list (for image)
        for layer in spm_obj.layers:
            tmp_dict = {}
            scan_name = ""
            direction = ""
            for key, val in layer.items():
                tmp_d = self.extract_data_unit(key, val, encoding=encoding)
                tmp_dict.update({f"/Scan/{k}": v for k, v in tmp_d.items()})
                if not scan_name:
                    scan_name = {
                        "image_data": v
                        for k, v in tmp_d.items()
                        if k.endswith(":Image_Data")
                    }.get("image_data", "")
                if not direction:
                    direction = {
                        "direction": v
                        for k, v in tmp_d.items()
                        if k.endswith("Line_Direction")
                    }.get("direction", "")

            # example pattern: 'S [AmplitudeActual] "Amplitude"'
            matches = re.match(
                pattern=r'^\s*(\w+)\s+\[(\w+)\]\s+["]*([\w\s]+)["]*$', string=scan_name
            )
            if not matches:
                print("warning: image layer does not have any image data")
                continue
            elif (match_grp := matches.groups()) and len(match_grp) != 3:
                print("warning: image data is not properly annotated")
                continue
            else:
                scan_name = matches.groups()[-1].strip().replace(" ", "_")

            if not direction:
                # make default forward
                direction = "forward"
            else:
                # tace or retrace
                direction = "forward" if direction == "Trace" else "backward"

            tmp_dict_update = {}
            for key, val in tmp_dict.items():
                k_parts = key.split("/")
                k_parts = [*k_parts[0:2], scan_name, direction, *k_parts[2:]]
                key = "/".join(k_parts)
                tmp_dict_update[key] = val

            bruker_data_dict.update(tmp_dict_update)

        # Scanner list
        if len(spm_obj.scanners) > 0:
            for ind, scanner in enumerate(spm_obj.scanners):
                for key, val in scanner.items():
                    temp_dict = self.extract_data_unit(key, val, encoding)
                    bruker_data_dict.update(
                        {f"/Scanner_list/{ind}/{k}": v for k, v in temp_dict.items()}
                    )

        # Image data
        for channel in channel_list:
            channel_clean = re.sub(r"\s+", "_", channel.strip())
            key = f"/{channel_clean}"
            bruker_data_dict[f"{key}/backward"] = spm_obj.get_channel_data(
                channel=channel, backward=True
            )
            bruker_data_dict[f"{key}/forward"] = spm_obj.get_channel_data(
                channel=channel, backward=False
            )

        return bruker_data_dict

    def extract_data_unit(self, key, val, encoding="latin1"):
        """
        Some data comes in complex string extract them and store in data_dict.

        A example key value pair is
        `/Scanner_list/0/@2:ReferenceFrequencyTappingMode : V (0.00001164153 kHz/LSB) 172.0493 kHz`
        Where  is hosting the data `172.049` and unit.

        return: tuple[value, unit]
        """
        key = self.decode_bytes(key, encoding=encoding)
        key = re.sub(r"\s+", "_", key)
        val = self.decode_bytes(val, encoding=encoding)[0]
        temp_dict = {}
        # V (0.00001164153 kHz/LSB) 172.0493 kHz
        pattern = r"^\s*(\w+)\s+\(([\d.]+)\s+([\w/]+)\)\s+([\d.]+)\s+(\w+)\s*$"
        matches = re.match(pattern=pattern, string=val)
        if matches and (match_grps := matches.groups()) and len(match_grps) == 5:
            temp_dict[f"{key}"] = match_grps[3]
            temp_dict[f"{key}/@units"] = match_grps[4]
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
