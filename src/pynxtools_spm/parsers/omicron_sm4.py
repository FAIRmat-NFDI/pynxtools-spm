import re

import numpy as np
from pynxtools import logger as pynx_logger
from spym.io.rhksm4 import load

from pynxtools_spm.parsers.base_parser import SPMBase


class Sm4Omicron(SPMBase):
    """
    Parser for Omicron SM4 STM files.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def parse(self):
        """
        Parse the Omicron SM4 STM file and return the parsed data.

        RHKsm4 Object:
            RHKsm4 object is a container containing RHKpage (can be called scan page) object
            each of the page has object public attributes
                - attrs --> has all the metadata for each scan
                - label --> label for each scan page
                - data  --> 2D matrix image data
                - coords --> list of coordinates for each image data

        Returns:
            parsed data object (RHKsm4) object containing all the parsed data.
        """
        rhk_file_obj = load(self.file_path)

        # Process the parsed data as needed
        # For example, you can convert it to a specific format or extract certain fields

        sm4_data_dict = {}
        for page in rhk_file_obj:
            label = page.label
            for key, val in page.attrs.items():
                key = re.sub(
                    pattern=r"(units|unit)$", repl=r"/@unit", string=key, flags=re.I
                )

                sm4_data_dict[f"/{label}/{key}"] = val
            for coord, arr in page.coords:
                coord = re.sub(
                    pattern=r"(unit|units)$", repl=r"/@unit", string=coord, flags=re.I
                )
                sm4_data_dict[f"/{label}/coords/{coord}"] = arr
            sm4_data_dict[f"/{label}/data"] = self._calibrated_z(page)

        return sm4_data_dict

    @staticmethod
    def _calibrated_z(page) -> np.ndarray:
        """Convert the raw counts of a page into the physical values of 'RHK_Zunits'.

        'spym' hands back the image as the signed integers written by the ADC and
        leaves 'RHK_Zscale'/'RHK_Zoffset' in the page attributes, so the array is
        several orders of magnitude away from the unit it is labelled with, and
        carries the wrong sign whenever the scale is negative. Gwyddion applies
        the same affine conversion when it reads an SM4 file.
        """
        data = np.asarray(page.data)
        z_scale = page.attrs.get("RHK_Zscale")
        z_offset = page.attrs.get("RHK_Zoffset", 0.0)

        if z_scale in (None, 0):
            # Without a scale the counts cannot be converted, so they are passed
            # through unchanged rather than dropping the page altogether.
            pynx_logger.warning(
                "No usable 'RHK_Zscale' on page '%s'; its data stays in raw counts "
                "and will not match the unit it is labelled with.",
                page.label,
            )
            return data

        return data * z_scale + (0.0 if z_offset is None else z_offset)

    # def get_stm_raw_file_info(self):
    #     return self.parse()
