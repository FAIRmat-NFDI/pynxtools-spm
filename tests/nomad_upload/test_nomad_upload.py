from pynxtools_spm.nomad_uploader.files_movers import copy_directory_structure
from pynxtools_spm.nomad_uploader.reader_config_setup import (
    SPMConvertInputParameters,
    convert_spm_experiments,
)
import pytest
from pathlib import Path
import os
import shutil

nomad_upload_data_dir = Path(__file__).parent / "data"
src_dir_tree = nomad_upload_data_dir / "src_dir_tree"


def test_directory_structure(tmp_path):
    dst_dir_tree = Path(tmp_path) / "dst_dir_tree"
    os.makedirs(dst_dir_tree, exist_ok=True)

    copy_file_ls = []

    def run_action_on_files(file):
        copy_file_ls.append(file)

    copy_directory_structure(
        src_dir_tree,
        dst_dir_tree,
        extension=".sxm",
        run_action_on_files=run_action_on_files,
    )
    assert len(copy_file_ls) == 1, "File no properly copied over."

    copy_directory_structure(
        src_dir_tree,
        dst_dir_tree,
        extension=".dat",
        run_action_on_files=run_action_on_files,
    )
    assert len(copy_file_ls) == 2, "File no properly copied over."


@pytest.fixture
def spm_reader_input_params(tmp_path):
    stm_file_name = "STM_nanonis_generic_4_5.sxm"
    eln_file_name = "eln_data.yaml"
    stm_raw = src_dir_tree / "stm" / stm_file_name
    stm_eln = src_dir_tree / "stm" / eln_file_name

    stm_raw_tmp_path = tmp_path / stm_file_name
    stm_eln_tmp_path = tmp_path / eln_file_name

    shutil.copy2(stm_raw, stm_raw_tmp_path)
    shutil.copy2(stm_eln, stm_eln_tmp_path)

    input_params = SPMConvertInputParameters(
        input_file=(stm_raw_tmp_path,),
        eln=stm_eln_tmp_path,
        expriement_type="stm",
        reader="spm",
        nxdl="NXstm",
        raw_extension=".sxm",
        create_zip=True,
        skip_verify=True,
    )
    _ = convert_spm_experiments(input_params)
    return input_params


def test_run_spm_reader(spm_reader_input_params):
    assert spm_reader_input_params.zip_file_path.exists(), "Zip file not created."
    assert str(spm_reader_input_params.output).endswith(".nxs"), (
        "No NeXus file is created."
    )


# def test_upload_to_nomad(spm_reader_input_params):
#     tocken
