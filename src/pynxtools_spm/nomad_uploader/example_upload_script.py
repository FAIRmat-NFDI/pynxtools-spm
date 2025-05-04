from pynxtools_spm.nomad_uploader.uploader import (
    run_uploader_with,
    NOMADSettings,
    DataProcessingSettings,
)
from pathlib import Path

current_dir = Path(__file__).resolve().parent

nomad_settings = NOMADSettings(
    url_protocol="https",
    url_domain="nomad-lab.eu",
    url_version="prod/v1/oasis-b/api/v1/",
    url="https://nomad-lab.eu/prod/v1/oasis-b/api/v1/",
    username="Mozumder",
    password="",
    token="",
    modify_upload_metadata=False,
    publish_to_nomad=False,
)
local_src_dir = Path(
    "/home/rubel/NOMAD-FAIRmat/nomad-distro-dev-RM/packages/pynxtools-spm/tests/data/nanonis"
)
total_upload = 3
data_processing_settings = DataProcessingSettings(
    raw_file_exts=(
        ".dat",
        ".sxm",
    ),
    single_batch_processing_time=total_upload * 90,  # seconds
    src_dir=Path("/home/rubel/NOMAD-FAIRmat/SPMfolder/DataFilesForUpload"),
    # copy_file_elsewhere=False,
    dst_dir="",
    create_pseudo_file=True,
    pseudo_exts=".done",
    spm_params_obj_l=[],
    sts_eln=local_src_dir / "sts/version_gen_5e_with_described_nxdata/eln_data.yaml",
    sts_config="",
    stm_eln=local_src_dir / "stm/version_gen_4_5_with_described_nxdata/eln_data.yaml",
    stm_config="",
    afm_eln=local_src_dir / "afm/version_gen_4_with_described_nxdata/eln_data.yaml",
    afm_config="",
    logger_dir=current_dir,
    number_of_uploads=total_upload,
)

if __name__ == "__main__":
    run_uploader_with(
        data_settings=nomad_settings,
        data_processing_settings=data_processing_settings,
    )
