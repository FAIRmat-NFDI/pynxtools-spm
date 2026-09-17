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
        taken_labels: set[str] = set()
        for page in pages:
            label = self._unique_label(page, taken_labels)
            for key, val in page.attrs.items():
                sm4_data_dict[f"/{label}/{UNIT_SUFFIX.sub('/@unit', key)}"] = val

            if not page.is_image:
                pynx_logger.warning(
                    "Page '%s' of %s is not an image; only its metadata is read.",
                    label,
                    self.file_path,
                )
                continue

            for coord, arr in self._image_coords(page, label):
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

    def _unique_label(self, page: Sm4Page, taken: set[str]) -> str:
        """The label of a page, kept apart from a page already named that way.

        A label is the channel name and the scan direction, so a file that holds
        both a raw and a processed copy of one image has the same label twice
        (e.g. 'Topography_Forward'). The later page is named after its source,
        'Topography_Forward_Processed', instead of replacing the earlier one.
        """
        label = page.label
        if label not in taken:
            taken.add(label)
            return label

        # 'RHK_SOURCE_PROCESSED' -> 'Processed'.
        source = str(page.attrs.get("RHK_PageSourceTypeName", "")).rsplit("_", 1)[-1]
        candidate = f"{label}_{source.capitalize()}" if source else label
        index = 2
        while candidate in taken:
            candidate = f"{label}_{index}" if not source else f"{label}_{source}{index}"
            index += 1
        pynx_logger.warning(
            "Page label '%s' of %s is used by more than one page; "
            "this page is named '%s'.",
            label,
            self.file_path,
            candidate,
        )
        taken.add(candidate)
        return candidate

    @staticmethod
    def _image_coords(page: Sm4Page, label: str) -> list[tuple[str, np.ndarray]]:
        """The x and y coordinates of an image page, ascending.

        Index i of a page sits at 'RHK_Xoffset' + i * 'RHK_Xscale' along x and
        at 'RHK_Yoffset' + i * 'RHK_Yscale' along y, so a negative scale runs
        from the offset backwards. The image is stored with its origin at the
        bottom-left corner, so the coordinates are returned in ascending order.
        """
        attrs = page.attrs
        coords = []
        for axis in ("x", "y"):
            key = f"RHK_{axis.upper()}"
            positions = float(attrs[f"{key}offset"]) + float(
                attrs[f"{key}scale"]
            ) * np.arange(int(attrs[f"{key}size"]), dtype=np.float64)
            if positions[-1] < positions[0]:
                positions = positions[::-1]
            coords.append((f"{label}_{axis}", positions))
        return coords
