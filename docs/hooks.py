import shutil
from pathlib import Path


def copy_config_and_eln():
    # STS
    dst_config = "docs/included_file_content/sts/config.json"
    src_config = (
        "tests/data/nanonis/sts/version_gen_5_with_described_nxdata/config.json"
    )
    dst_eln = "docs/included_file_content/sts/eln_data.yaml"
    src_eln = "tests/data/nanonis/sts/version_gen_5_with_described_nxdata/eln_data.yaml"

    dst_path = Path(dst_config)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_config, dst_config)
    shutil.copy(src_eln, dst_eln)

    # STM
    dst_config = "docs/included_file_content/stm/config.json"
    src_config = (
        "tests/data/nanonis/stm/version_gen_5_with_described_nxdata/config.json"
    )
    dst_eln = "docs/included_file_content/stm/eln_data.yaml"
    src_eln = "tests/data/nanonis/stm/version_gen_5_with_described_nxdata/eln_data.yaml"
    dst_path = Path(dst_config)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src_config, dst_config)
    shutil.copy(src_eln, dst_eln)

    # AFM
    dst_config = "docs/included_file_content/afm/config.json"
    src_config = (
        "tests/data/nanonis/afm/version_gen_4_with_described_nxdata/config.json"
    )
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


def copy_hook(*args, **kwargs):
    copy_config_and_eln()
    copy_eln_schema()
