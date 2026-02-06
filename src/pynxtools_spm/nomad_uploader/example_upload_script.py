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
    url_version="prod/v1/develop/api/v1/",
    url="https://nomad-lab.eu/prod/v1/develop/api/v1/",
    username="Mozumder",
    password="*#R516660a*#",
    token="eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJmb1hmZnM5QlFQWHduLU54Yk5PYlExOFhnZnlKU1FNRkl6ZFVnWjhrZzdVIn0.eyJleHAiOjE3NzAzODExMzMsImlhdCI6MTc3MDI5NDczMywianRpIjoiYjk2YjI1NTUtYmU4My00Mjk0LWFlMDMtOTFjMTNmN2RlNmMwIiwiaXNzIjoiaHR0cHM6Ly9ub21hZC1sYWIuZXUvZmFpcmRpL2tleWNsb2FrL2F1dGgvcmVhbG1zL2ZhaXJkaV9ub21hZF9wcm9kIiwic3ViIjoiOGVjOGMwOWUtOWZiMC00YTQ3LTllNTEtNDRkNWFjNjg5YWQwIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoibm9tYWRfcHVibGljIiwic2lkIjoiYjZlODVlZmUtMzViOS00M2UzLTgxMWItOWU3ZWZlMTc4MTVkIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiUnViZWwgTW96dW1kZXIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJtb3p1bWRlciIsInNlc3Npb25fc3RhdGUiOiJiNmU4NWVmZS0zNWI5LTQzZTMtODExYi05ZTdlZmUxNzgxNWQiLCJnaXZlbl9uYW1lIjoiUnViZWwiLCJmYW1pbHlfbmFtZSI6Ik1venVtZGVyIiwiZW1haWwiOiJtb3p1bWRlckBwaHlzaWsuaHUtYmVybGluLmRlIn0.ekOAgc5AIqm_uriTRj8yxt-Kmtuz5IHf6Bs3lQIaW0WK_ds7UD21itBtKFKTZlUHq2Ti6gcfsU1WqkdRJ3_5d1xSblJoKWL974o8YuAhDMNLkcv4HqthjQ_pnp3XSb_y0JXsPB0tOImjf-86sLqYqsgn9FHcln-OZb73guLlrKiwyXt4cK5pB-vO8JFKdZvChnVHhb7wyBYkJuLYtvhjQgASLDqDSAPHm6mk9ZGtqcr1KtzlopMzK2YovfgNiJSWrKyH6yI2O4wcSJzc6374N3SAQeIClYGExs0f39jKS0dfhdROI753SUvDAO-niDiyxT8LChwHtuM1IlnFSw-5ng",
    modify_upload_metadata=True,
    publish_to_nomad=False,
)
local_src_dir = Path(
    "/home/rubel/NOMAD-FAIRmat/nomad-distro-dev-RM/packages/pynxtools-spm/tests/data/nanonis"
)
total_upload = 1
data_proc_settings = DataProcessingSettings(
    raw_file_exts=(
        ".dat",
        ".sxm",
    ),
    single_batch_processing_time=total_upload * 90,  # seconds
    src_dir=local_src_dir,  # Path("/home/rubel/NOMAD-FAIRmat/SPMfolder/DataFilesForUpload"),
    # copy_file_elsewhere=False,
    dst_dir="",
    create_pseudo_file=True,
    pseudo_exts=".done",
    spm_params_obj_l=[],
    sts_eln=local_src_dir / "sts/version_gen_5e_with_described_nxdata/eln_data.yaml",
    sts_config="",
    stm_eln=local_src_dir / "stm/version_gen_5_with_described_nxdata/eln_data.yaml",
    stm_config="",
    afm_eln=local_src_dir / "afm/version_gen_4_with_described_nxdata/eln_data.yaml",
    afm_config="",
    logger_dir=current_dir,
    number_of_uploads=total_upload,
    file_specific_eln={"raw_file_name": "eln_file_path"},
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
