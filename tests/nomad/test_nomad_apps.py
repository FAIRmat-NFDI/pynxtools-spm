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
"""Tests for the NOMAD app."""

import pytest

try:
    import nomad  # noqa: F401
except ImportError:
    pytest.skip(
        "Skipping NOMAD app tests because nomad-lab is not installed",
        allow_module_level=True,
    )


def test_importing_app():
    # this will raise an exception if pydantic model validation fails for the app
    from pynxtools_spm.nomad.apps import spm_app  # noqa: E402

    assert spm_app.app.label == "SPM"  # pylint: disable=E1101


@pytest.mark.parametrize(
    "quantity, expected",
    [
        # Repeating sub-section: needs a projection.
        ("data.sample.name", "data.sample[*].name"),
        ("data.user.affiliation", "data.user[*].affiliation"),
        # Non-repeating sub-section below a repeating one: only the repeating
        # segment gets a projection.
        (
            "data.instrument.hardware.name",
            "data.instrument[*].hardware.name",
        ),
        (
            "data.instrument.lockin_amplifier.reference_phase",
            "data.instrument[*].lockin_amplifier.reference_phase",
        ),
        # Two repeating segments in the same path.
        (
            "data.instrument.scan_environment.head_temperature",
            "data.instrument[*].scan_environment[*].head_temperature",
        ),
        (
            "data.instrument.current_sensorTAG.current",
            "data.instrument[*].current_sensorTAG[*].current",
        ),
        # Quantity directly on the root section: nothing to project.
        ("data.definition", "data.definition"),
        ("data.scan_mode", "data.scan_mode"),
        # Unknown path: left untouched rather than guessed at.
        ("data.not_a_section.whatever", "data.not_a_section.whatever"),
    ],
)
def test_as_column_projects_only_repeating_sub_sections(quantity, expected):
    """Projections must match ``repeats`` exactly; both extra and missing
    projections make JMESPath resolve the cell to null."""
    from pynxtools_spm.nomad.apps import as_column, schema

    assert as_column(f"{quantity}#{schema}") == f"{expected}#{schema}"


@pytest.mark.parametrize(
    "quantity", ["entry_id", "entry_type", "results.material.elements"]
)
def test_as_column_ignores_names_without_schema(quantity):
    """Plain NOMAD metadata carries no schema suffix and needs no projection."""
    from pynxtools_spm.nomad.apps import as_column

    assert as_column(quantity) == quantity


def test_as_column_matches_metainfo_repeats():
    """REPEATING_SUB_SECTIONS must stay in sync with the generated metainfo.

    ``as_column`` cannot read the section definitions itself (importing the
    schema package from an app module is circular), so the constant is checked
    here instead: every sub-section named in any quantity the app uses must be
    listed if and only if it repeats.
    """
    from pynxtools.nomad.metainfo.applications.spm import Spm

    from pynxtools_spm.nomad.apps import (
        REPEATING_SUB_SECTIONS,
        map_concept_to_full_quantities,
        schema,
    )

    checked = set()
    for quantity in map_concept_to_full_quantities.values():
        if schema not in quantity:
            continue
        section = Spm.m_def
        for part in quantity.split("#")[0].split(".")[1:]:
            sub_section = section.all_sub_sections.get(part)
            if sub_section is None:  # reached the quantity itself
                assert part not in REPEATING_SUB_SECTIONS, (
                    f"quantity '{part}' collides with a sub-section name"
                )
                break
            assert (part in REPEATING_SUB_SECTIONS) == sub_section.repeats, (
                f"'{part}' has repeats={sub_section.repeats} but is "
                f"{'listed' if part in REPEATING_SUB_SECTIONS else 'missing'} "
                "in REPEATING_SUB_SECTIONS"
            )
            checked.add(part)
            section = sub_section.sub_section

    # Guard against the constant listing names the app never traverses, which
    # would silently stop being checked by the loop above.
    assert REPEATING_SUB_SECTIONS <= checked
