#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Time zones of timestamps that come without one"""

# cspell:ignore tzset
import logging
import shutil
import time
from datetime import datetime
from pathlib import Path

import pytest
from pynxtools.dataconverter.convert import get_reader
from pynxtools.dataconverter.template import Template

from pynxtools_spm.nxformatters.helpers import add_local_timezone

STM_DIR = Path(__file__).parent / "data" / "nanonis" / "stm" / "v_gen_4_dflt_conf_up"
SM4_DIR = Path(__file__).parent / "data" / "omicron" / "stm" / "sm4_dflt_conf_up"


@pytest.fixture
def machine_in_tokyo(monkeypatch):
    """Pretend the converting machine runs in Tokyo (UTC+09:00)."""
    monkeypatch.setenv("TZ", "Asia/Tokyo")
    time.tzset()
    yield
    monkeypatch.undo()
    time.tzset()


def test_timestamp_with_zone_is_kept(machine_in_tokyo):
    assert (
        add_local_timezone("2023-08-24T14:19:47+02:00") == "2023-08-24T14:19:47+02:00"
    )


def test_given_zone_is_attached(machine_in_tokyo, caplog):
    with caplog.at_level(logging.WARNING):
        assert (
            add_local_timezone("2023-08-24T14:19:47", tz="Europe/Berlin")
            == "2023-08-24T14:19:47+02:00"
        )
    assert caplog.records == []


def test_without_zone_the_machine_zone_is_assumed_with_a_warning(
    machine_in_tokyo, caplog
):
    """No zone in the file and none given: use the machine's zone, but say so."""
    with caplog.at_level(logging.WARNING):
        assert add_local_timezone("2023-08-24T14:19:47") == "2023-08-24T14:19:47+09:00"
    assert "time zone of the converting machine" in caplog.text


def test_unknown_zone_falls_back_to_the_machine_zone(machine_in_tokyo, caplog):
    with caplog.at_level(logging.WARNING):
        assert (
            add_local_timezone("2023-08-24T14:19:47", tz="Mars/Olympus")
            == "2023-08-24T14:19:47+09:00"
        )
    assert "Mars/Olympus" in caplog.text
    assert "time zone of the converting machine" in caplog.text


def test_timezone_from_the_eln_is_used(machine_in_tokyo, tmp_path):
    """`timezone` in the ELN sets the zone and is not written as data."""
    for file in STM_DIR.iterdir():
        if file.suffix != ".nxs":
            shutil.copy(file, tmp_path / file.name)
    eln = tmp_path / "eln_data.yaml"
    eln.write_text(eln.read_text() + "\ntimezone: America/New_York\n")

    template = get_reader("spm")().read(
        template=Template(), file_paths=tuple(str(f) for f in tmp_path.iterdir())
    )

    assert template["/ENTRY[entry]/start_time"] == "2021-11-22T01:48:07-05:00"
    assert not any("timezone" in key for key in template.keys())


def test_omicron_end_time_adds_the_scan_time_in_seconds(tmp_path):
    """end_time is start_time plus the scan time in seconds, not in days."""
    for file in SM4_DIR.iterdir():
        if file.suffix != ".nxs":
            shutil.copy(file, tmp_path / file.name)
    eln = tmp_path / "eln_data.yaml"
    eln.write_text(eln.read_text() + "\ntimezone: Europe/Berlin\n")

    template = get_reader("spm")().read(
        template=Template(), file_paths=tuple(str(f) for f in tmp_path.iterdir())
    )

    start = datetime.fromisoformat(template["/ENTRY[entry]/start_time"])
    end = datetime.fromisoformat(template["/ENTRY[entry]/end_time"])
    assert start == datetime.fromisoformat("2022-01-20T16:07:09+01:00")
    assert (end - start).total_seconds() == pytest.approx(86.13, abs=0.01)
