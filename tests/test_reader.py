"""
Basic example based test for the stm reader
"""

import os
import shutil

import pytest
from pynxtools.dataconverter.template import Template
from pynxtools.testing.nexus_conversion import ReaderTest

from pynxtools_spm.nxformatters.nanonis.nanonis_dat_sts import NanonisDatSTS
from pynxtools_spm.reader import SPMReader

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


def _config_given_to_formatter(monkeypatch, file_paths, **kwargs):
    """Run read() and return the config_file that the STS formatter receives."""
    seen = {}
    original_init = NanonisDatSTS.__init__

    def spy_init(self, *args, **init_kwargs):
        seen["config_file"] = init_kwargs.get("config_file")
        original_init(self, *args, **init_kwargs)

    monkeypatch.setattr(NanonisDatSTS, "__init__", spy_init)
    SPMReader().read(template=Template(), file_paths=file_paths, **kwargs)
    return seen["config_file"]


def test_config_file_can_be_given_as_keyword(monkeypatch, tmp_path):
    """
    read() must accept the config file as a keyword argument, as
    `pynx convert -c <file>` passes it, and use it
    (Bug B3 in https://github.com/FAIRmat-NFDI/pynxtools-plugin-audit/blob/main/pynxtools-unification/FINDINGS.md).
    """
    folder = f"{module_dir}/data/nanonis/sts/v_gen_5e_descrb_nx_dt"
    data = f"{folder}/STS_nanonis_generic_5e_1.dat"
    eln = f"{folder}/eln_data.yaml"
    config = f"{folder}/config.json"

    # -c only
    found = _config_given_to_formatter(monkeypatch, (data, eln), config_file=config)
    assert found == config

    # -c and a .json in the file list: -c wins
    other_config = str(tmp_path / "other_config.json")
    shutil.copy(config, other_config)
    found = _config_given_to_formatter(
        monkeypatch, (data, eln, config), config_file=other_config
    )
    assert found == other_config
        # other converter kwargs are accepted and ignored
    found = _config_given_to_formatter(
        monkeypatch, (data, eln, config), some_other_option=True
    )
    assert found == config
