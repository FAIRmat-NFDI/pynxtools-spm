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
"""Scale factor of Bruker image layers (Bug B27 in
https://github.com/FAIRmat-NFDI/pynxtools-plugin-audit/blob/main/pynxtools-unification/FINDINGS.md)."""

import logging

import pytest

from pynxtools_spm.parsers.bruker_spm import SpmBruker

Z_SCALE = r"V [Sens. ZsensSens] (0.00000000572205 V/LSB) 1.195962 V"


def _scale_factor(sensitivity: str) -> float:
    entries = {"@2:Z scale": Z_SCALE}
    sections = [("Ciao scan list", {"@Sens. ZsensSens": sensitivity})]
    return SpmBruker._scale_factor(entries, sections)


def test_known_sensitivity_unit_scales_the_data():
    """'nm/V' scales the SI values from m to nm."""
    assert _scale_factor("V 485.6748 nm/V") == pytest.approx(1e9)


def test_sensitivity_without_unit_leaves_the_data(caplog):
    """A sensitivity without a unit keeps the values, as documented."""
    with caplog.at_level(logging.WARNING):
        assert _scale_factor("V 1.000000 ") == 1.0
    assert caplog.records == []


def test_unknown_sensitivity_unit_logs_a_warning(caplog):
    """An unknown unit leaves the data unscaled, but says so."""
    with caplog.at_level(logging.WARNING):
        assert _scale_factor("V 485.6748 xyz/V") == 1.0
    assert "xyz" in caplog.text
    assert "not scaled" in caplog.text
