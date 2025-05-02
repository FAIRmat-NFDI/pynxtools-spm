from pynxtools.dataconverter.convert import convert
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict
import zipfile
import logging


@dataclass
class SPMConvertInputParameters:
    input_file: tuple[Path]  # raw_files and eln (merged later)
    eln: str | Path
    expriement_type: str
    reader: str = "spm"
    output: Optional[str | Path] = None
    nxdl: Optional[str] = None
    create_zip: Optional[bool] = True
    zip_file_path: Optional[str | Path] = None
    skip_verify: Optional[bool] = False
    config: Optional[str | Path] = None
    raw_extension: Optional[str] = None


def convert_spm_experiments(
    input_params: SPMConvertInputParameters,
    converter_logger: Optional[logging.Logger],
    converter_handeler: Optional[logging.Handler] = None,

):
    """Convert SPM (STS, STM and AFM) experirment data files to NeXus format.
    Later, the input files and generated output file are zipped together to
    upload to NOMAD.

    Required input files:
    - raw_file: SPM data file e.g. `sxm` for STM and AFM, `dat` for STS
    - eln: ELN file
    Output files:
    - output: NeXus file, named from the raw file base name
    - zip_file: Zipped file, named from the raw file base name
    Required parameters in input_params:
    - expriement_type: SPM experiment type (STM, AFM, STS)
    """

    if not isinstance(input_params, SPMConvertInputParameters):
        converter_logger.error(
            "Input parameters must be an instance of SPMConvertInputParameters"
        )

    if not input_params.input_file:
        converter_logger.error("Input files are required to run an SPM experiment")
    if not input_params.eln:
        converter_logger.error(f"ELN file is requred to run an {input_params.expriement_type} experiment")

    if not input_params.expriement_type:
        converter_logger.error(
            "Experiment type is required to run an SPM experiment"
        )

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
            # TODO remoce the following line
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
    # TODO Try with input_file as tuple of Path objects
    # Use handler only for conver function. Do not close the handler 
    # after the function call as it will be used again and again
    if converter_handeler not in converter_logger.handlers:
        converter_logger.addHandler(converter_handeler)
    try:
        kwargs = asdict(input_params)
        print("#### kwargs:", kwargs)
        kwargs["input_file"] = tuple(map(str, input_params.input_file))
        kwargs["output"] = str(input_params.output)
        # with converter_logger:
        convert(**kwargs)
        print("#### kwargs after conversion:", kwargs)
        if input_params.create_zip:
            with zipfile.ZipFile(zip_file, "w") as zipf:
                zipf.write(
                    str(input_params.output),
                    arcname=str(input_params.output).split("/")[-1],
                )
                for file in map(str, input_params.input_file):
                    zipf.write(file, arcname=file.split("/")[-1])
            input_params.zip_file_path = Path(zip_file)

    except Exception as e:
        print("NeXusConverterError:", e)
    finally:
        converter_logger.removeHandler(converter_handeler)
    # finally:
    #     input_params.input_file = tuple(
    #         Path(file) if isinstance(file, str) else file
    #         for file in input_params.input_file
    #     )

    return input_params


# if __name__ == "__main__":
#     input_params = SPMConvertInputParameters(
#         input_file=(afm_reader_raw,), eln=afm_reader_eln, expriement_type="afm"
#     )
#     convert_spm_experiments(input_params)
