import json
import shutil
import subprocess
from pathlib import Path


# Root path is the path where mkdocs.yaml is located
def copy_config_and_plain_eln():
    # STS
    dst_config = "docs/included_file_content/sts/config.json"
    src_config = "tests/data/nanonis/sts/version_gen_5_with_described_nxdata/config.json"
    dst_eln = "docs/included_file_content/sts/eln_data.yaml"
    src_eln = "tests/data/nanonis/sts/version_gen_5_with_described_nxdata/eln_data.yaml"

    dst_path = Path(dst_config)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_config, dst_config)
    shutil.copy(src_eln, dst_eln)

    # STM
    dst_config = "docs/included_file_content/stm/config.json"
    src_config = "tests/data/nanonis/stm/version_gen_5_with_described_nxdata/config.json"
    dst_eln = "docs/included_file_content/stm/eln_data.yaml"
    src_eln = "tests/data/nanonis/stm/version_gen_5_with_described_nxdata/eln_data.yaml"
    dst_path = Path(dst_config)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_config, dst_config)
    shutil.copy(src_eln, dst_eln)

    # AFM
    dst_config = "docs/included_file_content/afm/config.json"
    src_config = "tests/data/nanonis/afm/version_gen_4_with_described_nxdata/config.json"
    dst_eln = "docs/included_file_content/afm/eln_data.yaml"
    src_eln = "tests/data/nanonis/afm/version_gen_4_with_described_nxdata/eln_data.yaml"
    dst_path = Path(dst_config)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_config, dst_config)
    shutil.copy(src_eln, dst_eln)


def copy_eln_schema():
    # STS
    dst = "docs/included_file_content/sts/sts.scheme.archive.yaml"
    src = "src/pynxtools_spm/nomad/examples/sts/STSExampleWithCustomization/sts.scheme.archive.yaml"
    dst_path = Path(dst)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)

    # STM
    dst = "docs/included_file_content/stm/stm.scheme.archive.yaml"
    src = "src/pynxtools_spm/nomad/examples/stm/STMExampleWithCustomization/stm.scheme.archive.yaml"
    dst_path = Path(dst)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)

    # AFM
    dst = "docs/included_file_content/afm/afm.scheme.archive.yaml"
    src = "src/pynxtools_spm/nomad/examples/afm/AFMExampleWithCustomization/afm.scheme.archive.yaml"
    dst_path = Path(dst)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)


def copy_miscelleneous_files():
    # STS nanonis dat file
    dst = "docs/included_file_content/sts/Bias-Spectroscopy00015_20230420.dat"
    src = "tests/data/nanonis/sts/version_gen_5_with_described_nxdata/Bias-Spectroscopy00015_20230420.dat"
    dst_path = Path(dst)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)

    # STS nomad archive file
    dst = "docs/included_file_content/sts/STSExample.archive.json"
    src = "src/pynxtools_spm/nomad/examples/sts/STSExampleWithCustomization/STSExample.archive.json"
    dst_path = Path(dst)
    dst_path.parent.mkdir(parents=True, exist_ok=True)

    # write in proper json with indentation
    with open(src, "r") as src_file:
        content = json.load(src_file)
        dst_path.write_text(json.dumps(content, indent=4))


def generate_folder_structure():
    # Parsers
    dst = "docs/included_file_content/subpackages_structure"
    parser_output_path = Path(dst) / "parsers.txt"
    nxformatter_output_path = Path(dst) / "nxformatters.txt"
    config_output_path = Path(dst) / "configs.txt"
    nomad_output_path = Path(dst) / "nomad.txt"

    # Subpackages
    parser_path = Path("src/pynxtools_spm/parsers")
    nxformatters_path = Path("src/pynxtools_spm/nxformatters")
    config_path = Path("src/pynxtools_spm/configs")
    nomad_path = Path("src/pynxtools_spm/nomad")
    parser_path.parent.mkdir(parents=True, exist_ok=True)
    nxformatters_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.parent.mkdir(parents=True, exist_ok=True)
    nomad_path.parent.mkdir(parents=True, exist_ok=True)

    command_input_tuple = (
        (parser_path, parser_output_path),
        (nxformatters_path, nxformatter_output_path),
        (config_path, config_output_path),
        (nomad_path, nomad_output_path),
    )

    cmd = [
        "tree",
        "-L",
        "2",
    ]

    for input_path, output_file in command_input_tuple:
        try:
            cmd_with_arg = [*cmd, str(input_path.absolute())]
            result = subprocess.run(cmd_with_arg, capture_output=True, text=True, check=True)
            # create file if does not exist and  Write the output to file
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(result.stdout.split("pynxtools-spm/src/")[-1])
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"Error executing command {' '.join(cmd_with_arg)}: {e.stderr}"
            ) from e


def copy_hook(*args, **kwargs):
    copy_config_and_plain_eln()
    copy_eln_schema()
    copy_miscelleneous_files()
    generate_folder_structure()
