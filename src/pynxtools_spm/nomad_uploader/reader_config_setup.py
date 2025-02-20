from pynxtools.dataconverter.convert import convert
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict
import zipfile


@dataclass
class SPMConvertInputParameters:
    input_file: tuple[str | Path]  # raw_file
    eln: str | Path
    expriement_type: str
    reader: str = "spm"
    output: str = None
    nxdl: Optional[str] = None
    create_zip: Optional[bool] = True
    zip_file_path: Optional[str] = None
    skip_verify: Optional[bool] = False
    config: Optional[str | Path] = None
    raw_extension: Optional[str] = None


def convert_spm_experiments(
    input_params: SPMConvertInputParameters,
):
    """Convert SPM experirments."""

    if not isinstance(input_params, SPMConvertInputParameters):
        raise ValueError(
            "Input parameters must be an instance of SPMConvertInputParameters"
        )

    if not input_params.input_file:
        raise ValueError("Input files are required to run an SPM experiment")
    if not input_params.eln:
        raise ValueError(
            f"ELN is required to run an {input_params.expriement_type} experiment."
        )

    if not input_params.expriement_type:
        raise ValueError("Experiment type is required to run an SPM experiment")

    input_params.input_file = (*input_params.input_file, input_params.eln)
    input_params.input_file = tuple(
        Path(file) if isinstance(file, str) else file
        for file in input_params.input_file
    )
    if input_params.config:
        input_params.input_file = (
            *input_params.input_file,
            input_params.config,
        )

    zip_file = None
    for file in input_params.input_file:
        if file.suffix in (
            input_params.raw_extension,
            f".{input_params.raw_extension}",
        ):
            if input_params.output is None:
                input_params.output = file.with_suffix(".nxs")
            zip_file = file.with_suffix(".zip")
            break
    if input_params.output is None or zip_file is None:
        raise ValueError(
            "Valid raw files and extension is required to run an SPM experiment"
        )
    # Fit to the reader convention
    # input_params.input_file = (str(file) for file in input_params.input_file)
    # TODO extract the convertrer arguments from input_params
    input_params.input_file = [str(file) for file in input_params.input_file]
    input_params.output = str(input_params.output)
    convert(**asdict(input_params))

    if input_params.create_zip:
        with zipfile.ZipFile(zip_file, "w") as zipf:
            zipf.write(input_params.output, arcname=input_params.output.split("/")[-1])
            for file in input_params.input_file:
                zipf.write(file, arcname=file.split("/")[-1])
        input_params.zip_file_path = zip_file
        return zip_file


# if __name__ == "__main__":
#     input_params = SPMConvertInputParameters(
#         input_file=(afm_reader_raw,), eln=afm_reader_eln, expriement_type="afm"
#     )
#     convert_spm_experiments(input_params)
