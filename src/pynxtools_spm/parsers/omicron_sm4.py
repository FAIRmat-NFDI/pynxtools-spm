import re
from typing import Any

import numpy as np
from gwyddionpy import GwyData, load
from pynxtools import logger as pynx_logger

from pynxtools_spm.parsers.base_parser import SPMBase
from pynxtools_spm.parsers.rhk_sm4_metadata import Sm4Page, read_sm4_pages

# 'RHK_Xunits' -> 'RHK_X/@unit', 'RHK_PiezoSensitivity_TubeXUnit' -> '.../TubeX/@unit'.
UNIT_SUFFIX = re.compile(r"(units|unit)$", flags=re.I)


class Sm4Omicron(SPMBase):
    """
    Parser for Omicron SM4 STM files.

    The image of every page is read with ``gwyddionpy``, which already converts
    the raw ADC counts into the physical values of 'RHK_Zunits' by applying
    'RHK_Zscale' and 'RHK_Zoffset'. The page metadata is read from the binary
    page headers by ``read_sm4_pages``, because gwyddionpy exposes only a
    subset of it, as rounded strings.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def parse(self) -> dict[str, Any]:
        """
        Parse the Omicron SM4 STM file into a slash separated key-value dict.

        Returns
        -------
        dict
            Flattened dict, e.g.::

                /Topography_Forward/RHK_Zscale                  : np.float32
                /Topography_Forward/RHK_Z/@unit                 : 'm'
                /Topography_Forward/coords/Topography_Forward_x : ndarray (512,)
                /Topography_Forward/data                        : ndarray (512, 512)
        """
        pages = read_sm4_pages(self.file_path)
        gwy_data: GwyData = load(str(self.file_path))
        # Gwyddion reports the page GUID of each channel as its 'Page ID'.
        channels = {
            channel.meta.get("Page ID", "").lower(): channel
            for channel in gwy_data.channels.values()
        }

        sm4_data_dict: dict[str, Any] = {}
        for page in pages:
            label = page.label
            for key, val in page.attrs.items():
                sm4_data_dict[f"/{label}/{UNIT_SUFFIX.sub('/@unit', key)}"] = val

            if not page.is_image:
                pynx_logger.warning(
                    "Page '%s' of %s is not an image; only its metadata is read.",
                    label,
                    self.file_path,
                )
                continue

            for coord, arr in self._image_coords(page):
                sm4_data_dict[f"/{label}/coords/{coord}"] = arr

            channel = channels.get(page.page_id)
            if channel is None:
                pynx_logger.warning(
                    "Image page '%s' of %s has no matching channel in gwyddionpy; "
                    "only its metadata is read.",
                    label,
                    self.file_path,
                )
                continue
            sm4_data_dict[f"/{label}/data"] = np.asarray(channel.data)

        return sm4_data_dict

    @staticmethod
    def _image_coords(page: Sm4Page) -> list[tuple[str, np.ndarray]]:
        """The x and y coordinates of an image page, starting at 0.

        The step is the magnitude of the scale stored in the page header, so the
        coordinates ascend regardless of the scan direction.
        """
        attrs = page.attrs
        return [
            (
                f"{page.label}_{axis}",
                abs(attrs[f"RHK_{axis.upper()}scale"])
                * np.arange(attrs[f"RHK_{axis.upper()}size"], dtype=np.float64),
            )
            for axis in ("x", "y")
        ]
