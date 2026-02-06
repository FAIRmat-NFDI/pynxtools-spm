from pynxtools_spm.nomad_uploader.uploader import (
    run_uploader_with,
    NOMADSettings,
    DataProcessingSettings,
)
from pathlib import Path

current_dir = Path(__file__).resolve().parent
project_dir = current_dir.parent.parent.parent

nomad_settings = NOMADSettings(
    url_protocol="https",
    url_domain="nomad-lab.eu",
    url_version="prod/v1/develop/api/v1/",
    url="https://nomad-lab.eu/prod/v1/develop/api/v1/",
    username="Mozumder",
    password="*#R516660a*#",
    token="",
    modify_upload_metadata=True,
    publish_to_nomad=False,
)
nanonis = project_dir / "tests/data/nanonis"

total_upload = 3

data_proc_settings = DataProcessingSettings(
    raw_file_exts=(
        ".dat",
        ".sxm",
    ),
    single_batch_processing_time=total_upload * 90,  # seconds
    src_dir=nanonis,
    # copy_file_elsewhere=False,
    dst_dir="",
    create_pseudo_file=True,
    pseudo_exts=".done",
    spm_params_obj_l=[],
    sts_eln=nanonis / "sts/version_gen_5e_with_described_nxdata/eln_data.yaml",
    sts_config="",
    stm_eln=nanonis / "stm/version_gen_5_with_described_nxdata/eln_data.yaml",
    stm_config="",
    afm_eln=nanonis / "afm/version_gen_4_with_described_nxdata/eln_data.yaml",
    afm_config="",
    logger_dir=current_dir,
    number_of_uploads=total_upload,
    file_to_convert_data={
        f"{nanonis / 'stm/version_gen_5_with_described_nxdata/Au_mica_2023_Y_A_diPAMY_195.sxm'}": {
            "eln": "",
            "technique": "stm",
        },
        f"{nanonis / 'sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat'}": {
            "eln": "",
            "technique": "sts",
        },
        f"{nanonis / 'stm/version_gen_5_with_described_nxdata/Au_mica_2023_Y_A_diPAMY_195.sxm'}": {
            "eln": "",
            "technique": "stm",
        },
        f"{nanonis / 'sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat'}": {
            "eln": "",
            "technique": "sts",
        },
        f"{nanonis / 'stm/version_gen_5_with_described_nxdata/Au_mica_2023_Y_A_diPAMY_195.sxm'}": {
            "eln": "",
            "technique": "stm",
        },
        f"{nanonis / 'sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat'}": {
            "eln": "",
            "technique": "sts",
        },
        f"{nanonis / 'stm/version_gen_5_with_described_nxdata/Au_mica_2023_Y_A_diPAMY_195.sxm'}": {
            "eln": "",
            "technique": "stm",
        },
        f"{nanonis / 'sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat'}": {
            "eln": "",
            "technique": "sts",
        },
        f"{nanonis / 'stm/version_gen_5_with_described_nxdata/Au_mica_2023_Y_A_diPAMY_195.sxm'}": {
            "eln": "",
            "technique": "stm",
        },
        f"{nanonis / 'sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat'}": {
            "eln": "",
            "technique": "sts",
        },
        f"{nanonis / 'stm/version_gen_5_with_described_nxdata/Au_mica_2023_Y_A_diPAMY_195.sxm'}": {
            "eln": "",
            "technique": "stm",
        },
        f"{nanonis / 'sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat'}": {
            "eln": "",
            "technique": "sts",
        },
        f"{nanonis / 'stm/version_gen_5_with_described_nxdata/Au_mica_2023_Y_A_diPAMY_195.sxm'}": {
            "eln": "",
            "technique": "stm",
        },
        f"{nanonis / 'sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat'}": {
            "eln": "",
            "technique": "sts",
        },
        f"{nanonis / 'stm/version_gen_5_with_described_nxdata/Au_mica_2023_Y_A_diPAMY_195.sxm'}": {
            "eln": "",
            "technique": "stm",
        },
        f"{nanonis / 'sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat'}": {
            "eln": "",
            "technique": "sts",
        },
    },
    #     metadata = {
    #     "metadata": {
    #     "upload_name": upload_name,
    #     "references": ["https://doi.org/xx.xxxx/xxxxxx"],
    #     "datasets": dataset_id,
    #     "embargo_length": 0,
    #     "coauthors": ["coauthor@affiliation.de"],
    #     "comment": 'This is a test upload...'
    #     },
    # }
    upload_metadata={
        "metadata": {
            "coauthors": ["cojaddl@physik.hu-berlin.de"],
            "upload_name": "test_upload",
        }
    },
)

if __name__ == "__main__":
    run_uploader_with(
        nomad_settings=nomad_settings,
        data_proc_settings=data_proc_settings,
    )
