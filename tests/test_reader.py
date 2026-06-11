"""
Basic example based test for the stm reader
"""

import os

import pytest
from pynxtools.testing.nexus_conversion import ReaderTest

module_dir = os.path.dirname(os.path.abspath(__file__))

ignore_lines: list = []
ignore_sections = {
    "FIELD /entry/start_time ": ["Value"],
    "FIELD /entry/end_time ": ["Value"],
    "FIELD /entry/instrument/height_piezo_sensor/piezo_configuration/calibration/calibration_date ": [
        "Value"
    ],
}


@pytest.mark.parametrize(
    "nxdl,reader_name,files_or_dir",
    [
        (
            "NXsts",
            "spm",
            f"{module_dir}/data/nanonis/sts/v_gen_5e_descrb_nx_dt",
        ),
        (
            "NXsts",
            "spm",
            f"{module_dir}/data/nanonis/sts/v_gen_5_descrb_nx_dt",
        ),
        (
            "NXsts",
            "spm",
            f"{module_dir}/data/nanonis/sts/v_gen_5e_dflt_conf",
        ),
    ],
)
def test_sts_reader(nxdl, reader_name, files_or_dir, tmp_path, caplog):
    "Generic test from pynxtools."
    # test plugin reader
    test = ReaderTest(nxdl, reader_name, files_or_dir, tmp_path, caplog)
    test.convert_to_nexus(caplog_level="ERROR", ignore_undocumented=True)
    test.check_reproducibility_of_nexus(
        ignore_lines=ignore_lines,
        ignore_sections=ignore_sections,
    )


@pytest.mark.parametrize(
    "nxdl,reader_name,files_or_dir",
    [
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/nanonis/stm/v_gen_5_dflt_conf_down",
        ),
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/nanonis/stm/v_gen_5e_descrb_nx_dt_down",
        ),
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/nanonis/stm/v_gen_5_descrb_nx_dt_down",
        ),
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/nanonis/stm/v_gen_4_dflt_conf_up",
        ),
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/nanonis/stm/v_gen_4_dflt_conf_down",
        ),
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/nanonis/stm/v_gen_4_descrb_nx_dt_up",
        ),
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/nanonis/stm/v_gen_4_descrb_nx_dt_down",
        ),
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/omicron/stm/sm4_dflt_conf_up",
        ),
        (
            "NXstm",
            "spm",
            f"{module_dir}/data/omicron/stm/sm4_dflt_conf_down",
        ),
    ],
)
def test_stm_reader(nxdl, reader_name, files_or_dir, tmp_path, caplog):
    "Generic test from pynxtools."
    # test plugin reader
    test = ReaderTest(nxdl, reader_name, files_or_dir, tmp_path, caplog)
    test.convert_to_nexus(caplog_level="ERROR", ignore_undocumented=True)
    test.check_reproducibility_of_nexus(
        ignore_lines=ignore_lines,
        ignore_sections=ignore_sections,
    )


@pytest.mark.parametrize(
    "nxdl,reader_name,files_or_dir",
    [
        (
            "NXafm",
            "spm",
            f"{module_dir}/data/nanonis/afm/v_gen_4_descrb_nx_dt_up",
        ),
        (
            "NXafm",
            "spm",
            f"{module_dir}/data/nanonis/afm/v_gen_4_dflt_conf_up",
        ),
        (
            "NXafm",
            "spm",
            f"{module_dir}/data/bruker/afm/flt_dflt_conf",
        ),
        (
            "NXafm",
            "spm",
            f"{module_dir}/data/bruker/afm/flt_descrb_nx_dt",
        ),
        (
            "NXafm",
            "spm",
            f"{module_dir}/data/bruker/afm/spm_v_9_4_dflt_conf_down",
        ),
        (
            "NXafm",
            "spm",
            f"{module_dir}/data/bruker/afm/spm_v_9_4_dflt_conf_up",
        ),
        (
            "NXafm",
            "spm",
            f"{module_dir}/data/bruker/afm/txt_dflt_conf",
        ),
        (
            "NXafm",
            "spm",
            f"{module_dir}/data/bruker/afm/default_config",
        ),
    ],
)
def test_afm_reader(nxdl, reader_name, files_or_dir, tmp_path, caplog):
    "Generic test from pynxtools."
    # test plugin reader
    test = ReaderTest(nxdl, reader_name, files_or_dir, tmp_path, caplog)
    test.convert_to_nexus(caplog_level="ERROR", ignore_undocumented=True)
    test.check_reproducibility_of_nexus(
        ignore_lines=ignore_lines,
        ignore_sections=ignore_sections,
    )
