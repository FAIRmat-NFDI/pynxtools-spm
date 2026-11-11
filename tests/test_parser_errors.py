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
"""
Errors of the raw-file parsers must not be swallowed
"""

import pytest

from pynxtools_spm.parsers import SPMParser


class _FailingParser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        raise ValueError("bad header in test file")


class _WorkingParser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        return {"parsed": True}


def _use_parsers(monkeypatch, parsers):
    """Make SPMParser try exactly these parsers, in this order."""
    monkeypatch.setattr(
        SPMParser,
        "_SPMParser__get_appropriate_parser",
        lambda self, **kwargs: iter(parsers),
    )


def test_parser_error_is_reported(monkeypatch):
    """If no parser works, the error says why each one failed."""
    _use_parsers(monkeypatch, [_FailingParser])
    with pytest.raises(ValueError, match="_FailingParser: ValueError: bad header"):
        SPMParser().get_raw_data_dict("scan.sxm", eln={})


def test_next_parser_is_tried_after_a_failure(monkeypatch):
    """A failing parser does not stop the search for one that works."""
    _use_parsers(monkeypatch, [_FailingParser, _WorkingParser])
    assert SPMParser().get_raw_data_dict("scan.sxm", eln={}) == {"parsed": True}


def test_each_parser_class_is_tried_once(monkeypatch):
    """The same class listed for several software versions is tried once."""
    _use_parsers(monkeypatch, [_FailingParser, _FailingParser])
    with pytest.raises(ValueError) as error:
        SPMParser().get_raw_data_dict("scan.sxm", eln={})
    assert str(error.value).count("_FailingParser") == 1
