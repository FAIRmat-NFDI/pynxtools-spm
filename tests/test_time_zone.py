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
"""Timestamps never get the time zone of the converting machine"""

# cspell:ignore tzset
import logging
import time

import pytest

from pynxtools_spm.nxformatters.helpers import add_local_timezone


@pytest.fixture
def machine_in_tokyo(monkeypatch):
    """Pretend the converting machine runs in Tokyo (UTC+09:00)."""
    monkeypatch.setenv("TZ", "Asia/Tokyo")
    time.tzset()
    yield
    monkeypatch.undo()
    time.tzset()


def test_timestamp_without_zone_stays_without_zone(machine_in_tokyo, caplog):
    """No zone in the file and none given: keep the time as it is and say so."""
    with caplog.at_level(logging.WARNING):
        assert add_local_timezone("2023-08-24T14:19:47") == "2023-08-24T14:19:47"
    assert "no time zone" in caplog.text


def test_given_zone_is_attached(machine_in_tokyo):
    assert (
        add_local_timezone("2023-08-24T14:19:47", tz="Europe/Berlin")
        == "2023-08-24T14:19:47+02:00"
    )


def test_unknown_zone_is_not_replaced_by_the_local_one(machine_in_tokyo, caplog):
    with caplog.at_level(logging.WARNING):
        assert add_local_timezone("2023-08-24T14:19:47", tz="Mars/Olympus") == (
            "2023-08-24T14:19:47"
        )
    assert "Mars/Olympus" in caplog.text


def test_timestamp_with_zone_is_kept(machine_in_tokyo):
    assert (
        add_local_timezone("2023-08-24T14:19:47+02:00") == "2023-08-24T14:19:47+02:00"
    )
