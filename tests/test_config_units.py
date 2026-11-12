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
"""Units in the spm config files"""

import json
from pathlib import Path

import pytest
from pynxtools.units import ureg

CONFIG_DIR = Path(__file__).parents[1] / "src" / "pynxtools_spm" / "configs"
CONFIG_FILES = sorted(CONFIG_DIR.rglob("*.json"))


def _invalid_unit_values(node, path=""):
    """Yield every '@units' value that is neither empty, a lookup nor a valid unit.

    Allowed are None and "", a lookup path into the raw data ("/..."), and
    "@default:<unit>" with a unit pint can parse.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            if key != "@units":
                yield from _invalid_unit_values(value, f"{path}/{key}")
                continue
            for unit in value if isinstance(value, list) else [value]:
                if unit in (None, "") or unit.startswith("/"):
                    continue
                if unit.startswith("@default:"):
                    try:
                        ureg(unit.removeprefix("@default:"))
                        continue
                    except Exception:
                        pass
                yield f"{path}: {unit!r}"
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from _invalid_unit_values(item, f"{path}[{index}]")


@pytest.mark.parametrize(
    "config_file", CONFIG_FILES, ids=[f.name for f in CONFIG_FILES]
)
def test_config_units_are_lookups_or_valid_units(config_file):
    config = json.loads(config_file.read_text())
    assert list(_invalid_unit_values(config)) == []
