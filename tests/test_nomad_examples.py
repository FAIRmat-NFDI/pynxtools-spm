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
"""Test for NOMAD examples in MPES reader plugin."""

import pytest

try:
    # Check if nomad is installed properly
    import nomad
except ImportError:
    pytest.skip(
        "Skipping NOMAD example tests because nomad is not installed",
        allow_module_level=True,
    )

from pynxtools.testing.nomad_example import (
    get_file_parameter,
    parse_nomad_examples,
    example_upload_entry_point_valid,
)

from pynxtools_spm.nomad.entrypoints import (
    sts_default_example,
    sts_example_with_customization,
    stm_default_example,
    stm_example_with_customization,
    afm_default_example,
    afm_example_with_customization,
)

from pynxtools_spm.nomad.nomad_example_paths import (
    STS_DEFAULT_CONF_EXAMPLE_PATH,
    STS_CUSTOMIZED_EXAMPLE_PATH,
    STM_DEFAULT_CONF_EXAMPLE_PATH,
    STM_CUSTOMIZED_EXAMPLE_PATH,
    AFM_DEFAULT_CONF_EXAMPLE_PATH,
    AFM_CUSTOMIZED_EXAMPLE_PATH,
)

@pytest.mark.parametrize(
    "mainfile",
    list(get_file_parameter(STS_DEFAULT_CONF_EXAMPLE_PATH))
    + list(get_file_parameter(STS_CUSTOMIZED_EXAMPLE_PATH))
    + list(get_file_parameter(STM_DEFAULT_CONF_EXAMPLE_PATH))
    + list(get_file_parameter(STM_CUSTOMIZED_EXAMPLE_PATH))
    + list(get_file_parameter(AFM_DEFAULT_CONF_EXAMPLE_PATH))
    + list(get_file_parameter(AFM_CUSTOMIZED_EXAMPLE_PATH)),
)
def test_parse_nomad_examples(mainfile):
    """Test if NOMAD examples work."""
    print(mainfile)
    archive_dict = parse_nomad_examples(mainfile)


@pytest.mark.parametrize(
    ("entrypoint", "example_path"),
    [
        pytest.param(
            sts_default_example,
            STS_DEFAULT_CONF_EXAMPLE_PATH,
            id="sts_default_example",
        ),
        pytest.param(
            sts_example_with_customization,
            STS_CUSTOMIZED_EXAMPLE_PATH,
            id="sts_example_with_customization",
        ),
        pytest.param(
            stm_default_example,
            STM_DEFAULT_CONF_EXAMPLE_PATH,
            id="stm_default_example",
        ),
        pytest.param(
            stm_example_with_customization,
            STM_CUSTOMIZED_EXAMPLE_PATH,
            id="stm_example_with_customization",
        ),
        pytest.param(
            afm_default_example,
            AFM_DEFAULT_CONF_EXAMPLE_PATH,
            id="afm_default_example",
        ),
        pytest.param(
            afm_example_with_customization,
            AFM_CUSTOMIZED_EXAMPLE_PATH,
            id="afm_example_with_customization",
        ),
    ],
)
def test_example_upload_entry_point_valid(entrypoint, example_path):
    """Test if NOMAD ExampleUploadEntryPoint works."""
    example_upload_entry_point_valid(
        entrypoint=entrypoint,
        example_path=example_path,
    )
