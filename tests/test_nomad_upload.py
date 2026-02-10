from pynxtools_spm.nomad_uploader.files_movers import copy_directory_structure
from pynxtools_spm.nomad_uploader.helper import setup_logger
from pynxtools_spm.nomad_uploader.reader_config_setup import (
    SPMConvertInputParameters,
    convert_spm_experiments,
)
from pynxtools_spm.nomad_uploader.helper import (
    setup_logger,
)
import pytest
from pathlib import Path
import os
import shutil

data_dir = Path(__file__).parent / "data"


# data_dir = data_dir / "data_dir"


def test_directory_structure(tmp_path):
    dst_dir_tree = Path(tmp_path) / "dst_dir_tree"
    os.makedirs(dst_dir_tree, exist_ok=True)

    copy_file_ls = []

    def run_action_on_files(file):
        copy_file_ls.append(file)

    copy_directory_structure(
        data_dir,
        dst_dir_tree,
        extension=".sxm",
        run_action_on_files=run_action_on_files,
    )
    assert len(copy_file_ls) == 5, "File no properly copied over."

    copy_file_ls = []
    copy_directory_structure(
        data_dir,
        dst_dir_tree,
        extension=".dat",
        run_action_on_files=run_action_on_files,
    )
    assert len(copy_file_ls) == 3, "File no properly copied over."


@pytest.fixture
def spm_reader_input_params(tmp_path):
    upload_logger, upload_handler = setup_logger(
        name="uploader", log_file=tmp_path / "upload.log"
    )
    stm_file_name = "Au_mica_2023_Y_A_diPAMY_195.sxm"
    eln_file_name = "eln_data.yaml"
    stm_raw = (
        data_dir
        / "nanonis"
        / "stm"
        / "version_gen_5_with_default_config"
        / stm_file_name
    )
    stm_eln = (
        data_dir
        / "nanonis"
        / "stm"
        / "version_gen_5_with_default_config"
        / eln_file_name
    )

    stm_raw_tmp_path = tmp_path / stm_file_name
    stm_eln_tmp_path = tmp_path / eln_file_name

    shutil.copy2(stm_raw, stm_raw_tmp_path)
    shutil.copy2(stm_eln, stm_eln_tmp_path)

    input_params = SPMConvertInputParameters(
        input_file=(stm_raw_tmp_path,),
        eln=stm_eln_tmp_path,
        experiment_type="stm",
        reader="spm",
        nxdl="NXstm",
        raw_extension=".sxm",
        create_zip=True,
        skip_verify=True,
    )
    _ = convert_spm_experiments(input_params, upload_logger, upload_handler)
    return input_params


def test_run_spm_reader(spm_reader_input_params):
    assert spm_reader_input_params.zip_file_path.exists(), "Zip file not created."
    assert str(spm_reader_input_params.output).endswith(".nxs"), (
        "No NeXus file is created."
    )


# def test_upload_to_nomad(spm_reader_input_params):
#     token
