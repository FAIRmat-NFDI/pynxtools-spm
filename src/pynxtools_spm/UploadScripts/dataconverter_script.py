import importlib.metadata
from pynxtools.dataconverter.convert import convert
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict
import zipfile

import importlib

package_path = Path(importlib.metadata.PackagePath("pynxtools_spm"))


afm_path = package_path / "nomad" / "afm"
stm_path = package_path / "nomad" / "stm"
sts_path = package_path / "nomad" / "sts"

afm_reader_inputs = (afm_path / "AFMExampleWithCustomization" / "eln_data.yaml",)
stm_reader_inputs = (stm_path / "STMExampleWithCustomization" / "eln_data.yaml",)
sts_reader_inputs = sts_path / "STSExampleWithCustomization" / "eln_data.yaml"


@dataclass
class SPMConvertInputParameters:
    input_files: tuple
    eln: str | Path
    expriement_type: str
    reader: str = "spm"
    output: str = None
    nxdl: Optional[str] = None
    create_zip: Optional[bool] = True
    skip_verify: Optional[bool] = False
    config: Optional[str | Path] = None
    raw_extension: Optional[str] = None


def convert_spm_experiments(
    input_params: SPMConvertInputParameters,
):
    """Convert SPM experirments."""

    def get_base_raw__path(input_files: tuple, ext):
        for file in input_files:
            f_str = str(file)
            if f_str.endswith(ext):
                return f_str.split(".", maxsplit=1)[0]

    base_path = None
    if not isinstance(input_params, SPMConvertInputParameters):
        raise ValueError(
            "Input parameters must be an instance of SPMConvertInputParameters"
        )

    if not input_params.input_files:
        raise ValueError("Input files are required to run an SPM experiment")
    if not input_params.eln:
        raise ValueError(
            f"ELN is required to run an {input_params.expriement_type} experiment."
        )
    if not input_params.expriement_type:
        raise ValueError("Experiment type is required to run an SPM experiment")

    input_params.input_files = (input_params.input_files, input_params.eln)
    if input_params.config is not None:
        input_params.input_files = (
            input_params.input_files,
            input_params.config,
        )

    if input_params.expriement_type.lower() == "sts":
        input_params.nxdl = input_params.nxdl | "NXsts"
        if input_params.raw_extension is None:
            input_params.raw_extension = ".dat"

    elif input_params.expriement_type.lower() == "stm":
        input_params.nxdl = input_params.nxdl | "NXstm"
        if input_params.raw_extension is None:
            input_params.raw_extension = ".sxm"

    elif input_params.expriement_type.lower() == "afm":
        input_params.nxdl = input_params.nxdl | "NXafm"
        if input_params.raw_extension is None:
            input_params.raw_extension = ".sxm"

    base_path = get_base_raw__path(input_params.input_files, input_params.raw_extension)
    if input_params.output is None:
        input_params.output = base_path + ".nxs"
    zip_file = base_path + ".zip"

    convert(**asdict(input_params))

    if input_params.create_zip:
        with zipfile.ZipFile(zip_file, "w") as zipf:
            zipf.write(input_params.output)
            for file in input_params.input_files:
                zipf.write(file)
        return zip_file
