"""
A reader for the metadata of RHK SM4 files (written by Omicron instruments).
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
# The binary layout, the attribute names and their dtypes follow the SM4 reader
# of spym (https://github.com/rescipy-project/spym, 'spym/io/rhksm4/_sm4.py'),
# so that configs written against spym keep addressing the same keys. That code
# is distributed under the MIT License:
#
#   Copyright (c) 2025 Mirco Panighel
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to
#   deal in the Software without restriction, including without limitation the
#   rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#   sell copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#   IN THE SOFTWARE.

import zlib
from dataclasses import dataclass, field
from os import PathLike
from typing import Any, NamedTuple

import numpy as np

# SM4 is written on Windows, so every number is little endian.
U8 = np.dtype("<u1")
U16 = np.dtype("<u2")
U32 = np.dtype("<u4")
U64 = np.dtype("<u8")
F32 = np.dtype("<f4")
F64 = np.dtype("<f8")

# Object ids of the SM4 object table that this reader needs to locate.
OBJECT_PAGE_INDEX_HEADER = 1
OBJECT_PAGE_INDEX_ARRAY = 2
OBJECT_PAGE_HEADER = 3
OBJECT_STRING_DATA = 10
OBJECT_PRM = 13

# 'Page data type' of an image page and of a sequential page, whose header is
# laid out differently from all other page types.
PAGE_DATA_IMAGE = 0
PAGE_DATA_SEQUENTIAL = 6

# Enumerations of the SM4 format; the position in the tuple is the stored value.
PAGE_DATA_TYPES = (
    "RHK_DATA_IMAGE",
    "RHK_DATA_LINE",
    "RHK_DATA_XY_DATA",
    "RHK_DATA_ANNOTATED_LINE",
    "RHK_DATA_TEXT",
    "RHK_DATA_ANNOTATED_TEXT",
    "RHK_DATA_SEQUENTIAL",
    "RHK_DATA_MOVIE",
)
PAGE_SOURCE_TYPES = (
    "RHK_SOURCE_RAW",
    "RHK_SOURCE_PROCESSED",
    "RHK_SOURCE_CALCULATED",
    "RHK_SOURCE_IMPORTED",
)
PAGE_TYPES = (
    "RHK_PAGE_UNDEFINED",
    "RHK_PAGE_TOPOGRAPHIC",
    "RHK_PAGE_CURRENT",
    "RHK_PAGE_AUX",
    "RHK_PAGE_FORCE",
    "RHK_PAGE_SIGNAL",
    "RHK_PAGE_FFT_TRANSFORM",
    "RHK_PAGE_NOISE_POWER_SPECTRUM",
    "RHK_PAGE_LINE_TEST",
    "RHK_PAGE_OSCILLOSCOPE",
    "RHK_PAGE_IV_SPECTRA",
    "RHK_PAGE_IV_4x4",
    "RHK_PAGE_IV_8x8",
    "RHK_PAGE_IV_16x16",
    "RHK_PAGE_IV_32x32",
    "RHK_PAGE_IV_CENTER",
    "RHK_PAGE_INTERACTIVE_SPECTRA",
    "RHK_PAGE_AUTOCORRELATION",
    "RHK_PAGE_IZ_SPECTRA",
    "RHK_PAGE_4_GAIN_TOPOGRAPHY",
    "RHK_PAGE_8_GAIN_TOPOGRAPHY",
    "RHK_PAGE_4_GAIN_CURRENT",
    "RHK_PAGE_8_GAIN_CURRENT",
    "RHK_PAGE_IV_64x64",
    "RHK_PAGE_AUTOCORRELATION_SPECTRUM",
    "RHK_PAGE_COUNTER",
    "RHK_PAGE_MULTICHANNEL_ANALYSER",
    "RHK_PAGE_AFM_100",
    "RHK_PAGE_CITS",
    "RHK_PAGE_GPIB",
    "RHK_PAGE_VIDEO_CHANNEL",
    "RHK_PAGE_IMAGE_OUT_SPECTRA",
    "RHK_PAGE_I_DATALOG",
    "RHK_PAGE_I_ECSET",
    "RHK_PAGE_I_ECDATA",
    "RHK_PAGE_I_DSP_AD",
    "RHK_PAGE_DISCRETE_SPECTROSCOPY_PP",
    "RHK_PAGE_IMAGE_DISCRETE_SPECTROSCOPY",
    "RHK_PAGE_RAMP_SPECTROSCOPY_RP",
    "RHK_PAGE_DISCRETE_SPECTROSCOPY_RP",
)
LINE_TYPES = (
    "RHK_LINE_NOT_A_LINE",
    "RHK_LINE_HISTOGRAM",
    "RHK_LINE_CROSS_SECTION",
    "RHK_LINE_LINE_TEST",
    "RHK_LINE_OSCILLOSCOPE",
    "RHK_LINE_RESERVED",
    "RHK_LINE_NOISE_POWER_SPECTRUM",
    "RHK_LINE_IV_SPECTRUM",
    "RHK_LINE_IZ_SPECTRUM",
    "RHK_LINE_IMAGE_X_AVERAGE",
    "RHK_LINE_IMAGE_Y_AVERAGE",
    "RHK_LINE_NOISE_AUTOCORRELATION_SPECTRUM",
    "RHK_LINE_MULTICHANNEL_ANALYSER_DATA",
    "RHK_LINE_RENORMALIZED_IV",
    "RHK_LINE_IMAGE_HISTOGRAM_SPECTRA",
    "RHK_LINE_IMAGE_CROSS_SECTION",
    "RHK_LINE_IMAGE_AVERAGE",
    "RHK_LINE_IMAGE_CROSS_SECTION_G",
    "RHK_LINE_IMAGE_OUT_SPECTRA",
    "RHK_LINE_DATALOG_SPECTRUM",
    "RHK_LINE_GXY",
    "RHK_LINE_ELECTROCHEMISTRY",
    "RHK_LINE_DISCRETE_SPECTROSCOPY",
    "RHK_LINE_DATA_LOGGER",
    "RHK_LINE_TIME_SPECTROSCOPY",
    "RHK_LINE_ZOOM_FFT",
    "RHK_LINE_FREQUENCY_SWEEP",
    "RHK_LINE_PHASE_ROTATE",
    "RHK_LINE_FIBER_SWEEP",
)
IMAGE_TYPES = ("RHK_IMAGE_NORMAL", "RHK_IMAGE_AUTOCORRELATED")
SCAN_TYPES = ("RHK_SCAN_RIGHT", "RHK_SCAN_LEFT", "RHK_SCAN_UP", "RHK_SCAN_DOWN")
DRIFT_OPTION_TYPES = (
    "RHK_DRIFT_DISABLED",
    "RHK_DRIFT_EACH_SPECTRA",
    "RHK_DRIFT_EACH_LOCATION",
)

# The x label a line page falls back to when the file leaves it empty.
LINE_TYPE_XLABELS = {
    "RHK_LINE_IV_SPECTRUM": "Bias",
    "RHK_LINE_IZ_SPECTRUM": "Z",
    "RHK_LINE_TIME_SPECTROSCOPY": "Time",
}

# Suffix of the page label per scan direction. spym names only the first two;
# the vertical directions get their own suffix so that their labels stay unique.
SCAN_DIRECTION_SUFFIXES = {0: "_Forward", 1: "_Backward", 2: "_Up", 3: "_Down"}

# The strings of a page's 'String Data' object, in file order. Later strings the
# format may add are kept as 'RHK_Unknown000', 'RHK_Unknown001', ...
STRING_DATA_KEYS = (
    "RHK_Label",
    "RHK_SystemText",
    "RHK_SessionText",
    "RHK_UserText",
    "RHK_FileName",
    "RHK_Date",
    "RHK_Time",
    "RHK_Xunits",
    "RHK_Yunits",
    "RHK_Zunits",
    "RHK_Xlabel",
    "RHK_Ylabel",
    "RHK_StatusChannelText",
    "RHK_CompletedLineCount",
    "RHK_OverSamplingCount",
    "RHK_SlicedVoltage",
    "RHK_PLLProStatus",
    "RHK_SetpointUnit",
    "CHlist",
)
FILE_NAME_STRING = 4
INTEGER_STRINGS = (13, 14)
CHANNEL_DRIVE_STRING = 18


def _enum_name(names: tuple[str, ...], value: Any, unknown: str) -> str:
    """Name of an enumeration value, or 'unknown' for a value the format lacks."""
    index = int(value)
    return names[index] if 0 <= index < len(names) else unknown


class Sm4Object(NamedTuple):
    """An entry of an SM4 object table: what is stored, where, and how large."""

    id: int
    offset: int
    size: int


@dataclass
class Sm4Page:
    """The metadata of one page (one scan or spectrum) of an SM4 file.

    Attributes
    ----------
    attrs:
        The page metadata, keyed with the 'RHK_*' names of spym.
    page_id:
        The page GUID as 32 lowercase hex digits, the form Gwyddion reports it
        in as the 'Page ID' metadata of a channel.
    label:
        The page label, e.g. 'Topography_Forward'.
    data_type:
        The 'Page data type'; 'PAGE_DATA_IMAGE' for an image page.
    """

    attrs: dict[str, Any] = field(default_factory=dict)
    page_id: str = ""
    label: str = ""
    data_type: int = 0
    objects: list[Sm4Object] = field(default_factory=list)
    string_count: int = 0

    @property
    def is_image(self) -> bool:
        return self.data_type == PAGE_DATA_IMAGE


class _ByteReader:
    """Sequential reader of little endian values out of an in-memory file."""

    def __init__(self, raw: bytes):
        self._raw = raw
        self.position = 0

    def seek(self, offset: int) -> None:
        self.position = int(offset)

    def array(self, dtype: np.dtype, count: int) -> np.ndarray:
        """Read 'count' values; raises 'ValueError' when the file ends early."""
        count = int(count)
        if self.position + dtype.itemsize * count > len(self._raw):
            raise ValueError(
                f"SM4 file ends at byte {len(self._raw)}, but {count} value(s) of "
                f"type {dtype} were expected at byte {self.position}."
            )
        values = np.frombuffer(
            self._raw, dtype=dtype, count=count, offset=self.position
        )
        self.position += dtype.itemsize * count
        return values

    def scalar(self, dtype: np.dtype) -> Any:
        return self.array(dtype, 1)[0]

    def skip(self, dtype: np.dtype, count: int = 1) -> None:
        self.array(dtype, count)

    def chars(self, count: int) -> str:
        """Read 'count' UTF-16 code units, without trailing NUL characters."""
        return "".join(chr(code) for code in self.array(U16, count)).rstrip("\x00")

    def string(self) -> str:
        """Read an SM4 string: a 'uint16' length followed by UTF-16 code units.

        A string that cannot be encoded as UTF-8 (e.g. a lone surrogate) is read
        as an empty string, as in spym.
        """
        text = self.chars(self.scalar(U16))
        try:
            text.encode("utf8")
        except UnicodeEncodeError:
            return ""
        return text


class _Sm4MetadataReader:
    """Walks the object tables of an SM4 file and collects the page metadata."""

    def __init__(self, raw: bytes, file_name: str):
        self._reader = _ByteReader(raw)
        self._file_name = file_name
        self._signature = ""
        self._file_objects: list[Sm4Object] = []

    def read_pages(self) -> list[Sm4Page]:
        reader = self._reader
        header_size = reader.scalar(U16)
        self._signature = reader.chars(18)
        reader.skip(U32)  # total page count, repeated in the page index header
        object_count = reader.scalar(U32)
        # The object field size and two reserved fields; the header size is
        # used to seek past them, in case a later version extends the header.
        reader.seek(header_size + 2)
        self._file_objects = self._read_object_list(object_count)

        reader.seek(self._offset_of(self._file_objects, OBJECT_PAGE_INDEX_HEADER))
        page_count = reader.scalar(U32)
        object_count = reader.scalar(U32)
        reader.skip(U32, 2)  # reserved
        index_objects = self._read_object_list(object_count)

        reader.seek(self._offset_of(index_objects, OBJECT_PAGE_INDEX_ARRAY))
        pages = [self._read_page_index() for _ in range(page_count)]
        for page in pages:
            self._read_page(page)
        return pages

    def _read_object_list(self, count: int) -> list[Sm4Object]:
        return [
            Sm4Object(*(int(value) for value in self._reader.array(U32, 3)))
            for _ in range(count)
        ]

    @staticmethod
    def _offset_of(objects: list[Sm4Object], object_id: int) -> int:
        for obj in objects:
            if obj.id == object_id:
                return obj.offset
        raise ValueError(f"SM4 object table has no object with id {object_id}.")

    def _read_page_index(self) -> Sm4Page:
        reader = self._reader
        page = Sm4Page()
        attrs = page.attrs
        attrs["RHK_PRMdata"] = ""
        guid = reader.array(U16, 8)
        # spym keeps only the first 'uint16' of the GUID; the full GUID is what
        # pairs the page with its channel in gwyddionpy.
        attrs["RHK_PageID"] = guid[0]
        page.page_id = guid.tobytes().hex()

        page.data_type = int(reader.scalar(U32))
        attrs["RHK_PageDataType"] = np.uint32(page.data_type)
        attrs["RHK_PageDataTypeName"] = _enum_name(
            PAGE_DATA_TYPES, page.data_type, "RHK_DATA_UNKNOWN"
        )
        source_type = reader.scalar(U32)
        attrs["RHK_PageSourceType"] = source_type
        attrs["RHK_PageSourceTypeName"] = _enum_name(
            PAGE_SOURCE_TYPES, source_type, "RHK_SOURCE_UNKNOWN"
        )
        object_count = reader.scalar(U32)
        attrs["RHK_MinorVer"] = reader.scalar(U32)
        attrs["RHK_Signature"] = self._signature
        page.objects = self._read_object_list(object_count)
        return page

    def _read_page(self, page: Sm4Page) -> None:
        self._reader.seek(self._offset_of(page.objects, OBJECT_PAGE_HEADER))
        if page.data_type == PAGE_DATA_SEQUENTIAL:
            object_count = self._read_sequential_header(page)
        else:
            object_count = self._read_default_header(page)
        header_objects = self._read_object_list(object_count)

        if page.data_type == PAGE_DATA_SEQUENTIAL:
            self._read_sequential_parameters(page)
        for obj in header_objects:
            self._read_object_content(page, obj)

        page.label = self._page_label(page.attrs)
        # The PRM data is referenced from the file header, not from the page.
        for obj in self._file_objects:
            self._read_object_content(page, obj)

    @staticmethod
    def _page_label(attrs: dict[str, Any]) -> str:
        """The label of a page, e.g. 'Topography_Forward'.

        An image page gets its scan direction appended; a page without a label
        is named after its id, e.g. 'ID4162'.
        """
        label = attrs.get("RHK_Label", "")
        if not label:
            return f"ID{attrs['RHK_PageID']}"
        # Instruments pad a label, e.g. 'Current ', and the padding would
        # otherwise become part of the name ('Current__Forward').
        label = label.strip().replace(" ", "_").replace("-", "_")
        if label.startswith("_"):
            label = label[1:]
        if attrs["RHK_PageDataType"] == PAGE_DATA_IMAGE:
            label += SCAN_DIRECTION_SUFFIXES.get(int(attrs["RHK_ScanType"]), "")
        return label

    def _read_default_header(self, page: Sm4Page) -> int:
        reader = self._reader
        attrs = page.attrs
        reader.skip(U16)  # field size
        page.string_count = int(reader.scalar(U16))

        attrs["RHK_PageType"] = reader.scalar(U32)
        attrs["RHK_PageTypeName"] = _enum_name(
            PAGE_TYPES, attrs["RHK_PageType"], "RHK_PAGE_UNKNOWN"
        )
        attrs["RHK_DataSubSource"] = reader.scalar(U32)
        attrs["RHK_LineType"] = reader.scalar(U32)
        attrs["RHK_LineTypeName"] = _enum_name(
            LINE_TYPES, attrs["RHK_LineType"], "RHK_LINE_UNKNOWN"
        )
        # Xsize is the number of pixels in x of an image, or the number of points
        # per spectrum of a line page; Ysize the pixels in y, or the spectra count.
        self._read_values(attrs, "RHK_", U32, ("Xcorner", "Ycorner", "Xsize", "Ysize"))
        attrs["RHK_ImageType"] = reader.scalar(U32)
        attrs["RHK_ImageTypeName"] = _enum_name(
            IMAGE_TYPES, attrs["RHK_ImageType"], "RHK_IMAGE_UNKNOWN"
        )
        attrs["RHK_ScanType"] = reader.scalar(U32)
        attrs["RHK_ScanTypeName"] = _enum_name(
            SCAN_TYPES, attrs["RHK_ScanType"], "RHK_SCAN_UNKNOWN"
        )
        attrs["RHK_GroupId"] = reader.scalar(U32)
        reader.skip(U32)  # page data size
        self._read_values(attrs, "RHK_", U32, ("MinZvalue", "MaxZvalue"))
        self._read_values(
            attrs,
            "RHK_",
            F32,
            (
                "Xscale",
                "Yscale",
                "Zscale",
                "XYscale",
                "Xoffset",
                "Yoffset",
                "Zoffset",
                "Period",
                "Bias",
                "Current",
                "Angle",
            ),
        )
        reader.skip(U32)  # color info count; the color info is not read
        self._read_values(attrs, "RHK_", U32, ("GridXsize", "GridYsize"))
        object_count = reader.scalar(U32)
        reader.skip(U8, 64)  # 32 bit data flag, reserved flags, reserved
        return object_count

    def _read_sequential_header(self, page: Sm4Page) -> int:
        reader = self._reader
        attrs = page.attrs
        self._read_values(attrs, "RHK_", U32, ("DataType", "DataLength", "ParamCount"))
        object_count = reader.scalar(U32)
        self._read_values(attrs, "RHK_", U32, ("DataInfoSize", "DataInfoStringCount"))
        # A sequential page has no page or line type; spym sets them to 0 so
        # that the attributes are present for every page.
        attrs["RHK_PageType"] = 0
        attrs["RHK_PageTypeName"] = PAGE_TYPES[0]
        attrs["RHK_LineType"] = 0
        attrs["RHK_LineTypeName"] = LINE_TYPES[0]
        return object_count

    def _read_sequential_parameters(self, page: Sm4Page) -> None:
        reader = self._reader
        gains, labels, units = [], [], []
        for _ in range(page.attrs["RHK_ParamCount"]):
            gains.append(reader.scalar(F32))
            labels.append(reader.string())
            units.append(reader.string())
        page.attrs["RHK_Sequential_ParamGain"] = gains
        page.attrs["RHK_Sequential_ParamLabel"] = labels
        page.attrs["RHK_Sequential_ParamUnit"] = units

    def _read_values(
        self, attrs: dict[str, Any], prefix: str, dtype: np.dtype, names: tuple
    ) -> None:
        for name in names:
            attrs[f"{prefix}{name}"] = self._reader.scalar(dtype)

    def _read_strings(self, attrs: dict[str, Any], prefix: str, names: tuple) -> None:
        for name in names:
            attrs[f"{prefix}{name}"] = self._reader.string()

    def _read_object_content(self, page: Sm4Page, obj: Sm4Object) -> None:
        # An object without an offset or size is a placeholder; ids without a
        # reader (page data, thumbnails, color info) carry no metadata we keep.
        if obj.offset == 0 or obj.size == 0:
            return
        object_readers = {
            5: self._read_image_drift_header,
            6: self._read_image_drift,
            7: self._read_spec_drift_header,
            8: self._read_spec_drift_data,
            11: self._read_tip_track_header,
            12: self._read_tip_track_data,
            15: self._read_prm,
            17: self._read_api_info,
            19: self._read_piezo_sensitivity,
            20: self._read_frequency_sweep,
            21: self._read_scan_processor,
            22: self._read_pll,
            23: lambda attrs: self._read_channel_drive(attrs, "RHK_CH1Drive"),
            24: lambda attrs: self._read_channel_drive(attrs, "RHK_CH2Drive"),
            25: lambda attrs: self._read_lockin(attrs, "RHK_Lockin0"),
            26: lambda attrs: self._read_lockin(attrs, "RHK_Lockin1"),
            27: lambda attrs: self._read_pi_controller(attrs, "RHK_ZPI"),
            28: lambda attrs: self._read_pi_controller(attrs, "RHK_KPI"),
            29: lambda attrs: self._read_pi_controller(attrs, "RHK_AuxPI"),
            30: lambda attrs: self._read_low_pass_filter(attrs, "RHK_LowPassFilter0"),
            31: lambda attrs: self._read_low_pass_filter(attrs, "RHK_LowPassFilter1"),
        }
        if obj.id == OBJECT_STRING_DATA:
            self._reader.seek(obj.offset)
            self._read_string_data(page)
            return
        read = object_readers.get(obj.id)
        if read is not None:
            self._reader.seek(obj.offset)
            read(page.attrs)

    def _read_string_data(self, page: Sm4Page) -> None:
        reader = self._reader
        attrs = page.attrs
        for index in range(page.string_count):
            key = (
                STRING_DATA_KEYS[index]
                if index < len(STRING_DATA_KEYS)
                else f"RHK_Unknown{index - len(STRING_DATA_KEYS):03d}"
            )
            text = reader.string()
            if index == FILE_NAME_STRING:
                # The path the file was saved under on the instrument PC is
                # replaced by the path it is read from, as in spym.
                attrs[key] = self._file_name
            elif index in INTEGER_STRINGS:
                attrs[key] = int(text)
            elif index == CHANNEL_DRIVE_STRING:
                # One line per channel, e.g. 'CH1 Drive Value: -1 V'.
                for channel, line in enumerate(text.split("\n"), start=1):
                    parts = line.split(" ")
                    if len(parts) < 5:
                        continue
                    attrs[f"RHK_CH{channel}DriveValue"] = float(parts[3])
                    attrs[f"RHK_CH{channel}DriveValueUnits"] = parts[4]
            else:
                attrs[key] = text

        date_parts = attrs.get("RHK_Date", "").split("/")
        if len(date_parts) == 3:
            month, day, year = date_parts
            attrs["RHK_DateTime"] = f"20{year}-{month}-{day}T{attrs['RHK_Time']}.000"
        if attrs.get("RHK_Xlabel") == "":
            attrs["RHK_Xlabel"] = LINE_TYPE_XLABELS.get(attrs["RHK_LineTypeName"], "")

    def _read_image_drift_header(self, attrs: dict[str, Any]) -> None:
        attrs["RHK_ImageDrift_Filetime"] = self._reader.scalar(U64)
        attrs["RHK_ImageDrift_DriftOptionType"] = self._reader.scalar(U32)
        attrs["RHK_ImageDrift_DriftOptionTypeName"] = _enum_name(
            DRIFT_OPTION_TYPES,
            attrs["RHK_ImageDrift_DriftOptionType"],
            "RHK_DRIFT_UNKNOWN",
        )

    def _read_image_drift(self, attrs: dict[str, Any]) -> None:
        self._read_values(
            attrs,
            "RHK_ImageDrift_",
            F32,
            ("Time", "dX", "dY", "CumulativeX", "CumulativeY", "VectorX", "VectorY"),
        )

    def _read_spec_drift_header(self, attrs: dict[str, Any]) -> None:
        attrs["RHK_SpecDrift_Filetime"] = self._reader.scalar(U64)
        attrs["RHK_SpecDrift_DriftOptionType"] = self._reader.scalar(U32)
        attrs["RHK_SpecDrift_DriftOptionTypeName"] = _enum_name(
            DRIFT_OPTION_TYPES,
            attrs["RHK_SpecDrift_DriftOptionType"],
            "RHK_DRIFT_UNKNOWN",
        )
        self._reader.skip(U32)  # string count
        attrs["RHK_SpecDrift_Channel"] = self._reader.string()

    def _read_spec_drift_data(self, attrs: dict[str, Any]) -> None:
        names = ("Time", "Xcoord", "Ycoord", "dX", "dY", "CumulativeX", "CumulativeY")
        # One record of seven values per spectrum.
        records = [
            self._reader.array(F32, len(names)) for _ in range(attrs["RHK_Ysize"])
        ]
        for column, name in enumerate(names):
            attrs[f"RHK_SpecDrift_{name}"] = [record[column] for record in records]

    def _read_tip_track_header(self, attrs: dict[str, Any]) -> None:
        attrs["RHK_TipTrack_Filetime"] = self._reader.scalar(U64)
        self._read_values(
            attrs,
            "RHK_TipTrack_",
            F32,
            ("FeatureHeight", "FeatureWidth", "TimeConstant", "CycleRate", "PhaseLag"),
        )
        self._reader.skip(U32)  # string count
        attrs["RHK_TipTrack_TipTrackInfoCount"] = self._reader.scalar(U32)
        attrs["RHK_TipTrack_Channel"] = self._reader.string()

    def _read_tip_track_data(self, attrs: dict[str, Any]) -> None:
        names = ("CumulativeTime", "Time", "dX", "dY")
        records = [
            self._reader.array(F32, len(names))
            for _ in range(attrs["RHK_TipTrack_TipTrackInfoCount"])
        ]
        for column, name in enumerate(names):
            attrs[f"RHK_TipTrack_{name}"] = [record[column] for record in records]

    def _read_prm(self, attrs: dict[str, Any]) -> None:
        """Read the PRM text, written by RHK XPMPro and optionally zlib compressed."""
        reader = self._reader
        compressed = reader.scalar(U32)
        data_size = reader.scalar(U32)
        compressed_size = reader.scalar(U32)
        reader.seek(self._offset_of(self._file_objects, OBJECT_PRM))
        if compressed:
            data = zlib.decompress(reader.array(U8, compressed_size).tobytes())
        else:
            data = reader.array(U8, data_size).tobytes()
        attrs["RHK_PRMdata"] = data.decode("cp437")

    def _read_api_info(self, attrs: dict[str, Any]) -> None:
        self._read_values(
            attrs, "RHK_API_", F32, ("VoltageHigh", "VoltageLow", "Gain", "Offset")
        )
        self._read_values(
            attrs,
            "RHK_API_",
            U32,
            ("RampMode", "RampType", "Step", "ImageCount", "DAC", "MUX", "STMBias"),
        )
        self._reader.skip(U32)  # string count
        attrs["RHK_API_Units"] = self._reader.string()

    def _read_piezo_sensitivity(self, attrs: dict[str, Any]) -> None:
        names = (
            "TubeX",
            "TubeY",
            "TubeZ",
            "TubeZOffset",
            "ScanX",
            "ScanY",
            "ScanZ",
            "Actuator",
        )
        self._read_values(attrs, "RHK_PiezoSensitivity_", F64, names)
        self._reader.skip(U32)  # string count
        self._read_strings(
            attrs,
            "RHK_PiezoSensitivity_",
            tuple(f"{name}Unit" for name in names)
            + ("TubeCalibration", "ScanCalibration", "ActuatorCalibration"),
        )

    def _read_frequency_sweep(self, attrs: dict[str, Any]) -> None:
        self._read_values(
            attrs,
            "RHK_FrequencySweep_",
            F64,
            (
                "PSDTotalSignal",
                "PeakFrequency",
                "PeakAmplitude",
                "DriveAmplitude",
                "Signal2DriveRatio",
                "QFactor",
            ),
        )
        self._reader.skip(U32)  # string count
        self._read_strings(
            attrs,
            "RHK_FrequencySweep_",
            (
                "TotalSignalUnit",
                "PeakFrequencyUnit",
                "PeakAmplitudeUnit",
                "DriveAmplitudeUnit",
                "Signal2DriveRatioUnit",
                "QFactorUnit",
            ),
        )

    def _read_scan_processor(self, attrs: dict[str, Any]) -> None:
        names = ("XSlopeCompensation", "YSlopeCompensation")
        self._read_values(attrs, "RHK_ScanProcessor_", F64, names)
        self._reader.skip(U32)  # string count
        self._read_strings(
            attrs, "RHK_ScanProcessor_", tuple(f"{name}Unit" for name in names)
        )

    def _read_pll(self, attrs: dict[str, Any]) -> None:
        self._reader.skip(U32)  # string count
        attrs["RHK_PLL_AmplitudeControl"] = self._reader.scalar(U32)
        self._read_values(
            attrs,
            "RHK_PLL_",
            F64,
            (
                "DriveAmplitude",
                "DriveRefFrequency",
                "LockinFreqOffset",
                "LockinHarmonicFactor",
                "LockinPhaseOffset",
                "PIGain",
                "PIIntCutoffFreq",
                "PILowerBound",
                "PIUpperBound",
                "DissPIGain",
                "DissPIIntCutoffFreq",
                "DissPILowerBound",
                "DissPIUpperBound",
            ),
        )
        self._read_strings(
            attrs,
            "RHK_PLL_",
            (
                "LockinFilterCutoffFreq",
                "DriveAmplitudeUnit",
                "DriveFrequencyUnit",
                "LockinFreqOffsetUnit",
                "LockinPhaseUnit",
                "PIGainUnit",
                "PIICFUnit",
                "PIOutputUnit",
                "DissPIGainUnit",
                "DissPIICFUnit",
                "DissPIOutputUnit",
            ),
        )

    def _read_channel_drive(self, attrs: dict[str, Any], prefix: str) -> None:
        self._reader.skip(U32)  # string count
        attrs[f"{prefix}_MasterOscillator"] = self._reader.scalar(U32)
        self._read_values(
            attrs,
            f"{prefix}_",
            F64,
            ("Amplitude", "Frequency", "PhaseOffset", "HarmonicFactor"),
        )
        self._read_strings(
            attrs,
            f"{prefix}_",
            ("AmplitudeUnit", "FrequencyUnit", "PhaseOffsetUnit", "ReservedUnit"),
        )

    def _read_lockin(self, attrs: dict[str, Any], prefix: str) -> None:
        self._reader.skip(U32)  # string count
        attrs[f"{prefix}_NonMasterOscillator"] = self._reader.scalar(U32)
        self._read_values(
            attrs, f"{prefix}_", F64, ("Frequency", "HarmonicFactor", "PhaseOffset")
        )
        # Older file versions end the object before these strings.
        names = ("FilterCutoffFrequency", "FreqUnit", "PhaseUnit")
        try:
            self._read_strings(attrs, f"{prefix}_", names)
        except ValueError:
            for name in names:
                attrs[f"{prefix}_{name}"] = ""

    def _read_pi_controller(self, attrs: dict[str, Any], prefix: str) -> None:
        self._read_values(
            attrs,
            f"{prefix}_",
            F64,
            (
                "SetPoint",
                "ProportionalGain",
                "IntegralGain",
                "LowerBound",
                "UpperBound",
            ),
        )
        self._reader.skip(U32)  # string count
        self._read_strings(
            attrs,
            f"{prefix}_",
            (
                "FeedbackType",
                "SetPointUnit",
                "ProportionalGainUnit",
                "IntegralGainUnit",
                "OutputUnit",
            ),
        )

    def _read_low_pass_filter(self, attrs: dict[str, Any], prefix: str) -> None:
        self._reader.skip(U32)  # string count
        # A single string holding value and unit, e.g. '100 kHz'.
        frequency, unit = self._reader.string().split(" ")
        attrs[f"{prefix}_CutoffFrequency"] = float(frequency)
        attrs[f"{prefix}_CutoffFrequencyUnits"] = unit


def read_sm4_pages(file_path: str | PathLike) -> list[Sm4Page]:
    """Read the metadata of every page of an RHK SM4 file, in file order.

    Only the metadata is read; the page data itself is read with gwyddionpy.

    Raises
    ------
    ValueError
        If the file is truncated or its object tables are inconsistent.
    """
    with open(file_path, "rb") as file_obj:
        raw = file_obj.read()
    return _Sm4MetadataReader(raw, str(file_path)).read_pages()
