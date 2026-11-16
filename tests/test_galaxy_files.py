"""The files for the Galaxy ELN tools are shipped and fit together."""

import pytest
import yaml

from pynxtools_spm.galaxy import ELN_RULES_FILE, GALAXY_DIR

RULES = yaml.safe_load(ELN_RULES_FILE.read_text(encoding="utf-8"))


@pytest.mark.parametrize("definition", sorted(RULES["definitions"]))
def test_instructions_name_every_allowed_value_and_field(definition):
    """The Galaxy tool stops on such a mismatch, so it is checked here first."""
    entry = RULES["definitions"][definition]
    instructions = (GALAXY_DIR / entry["instructions"]).read_text(encoding="utf-8")
    for value in entry["scan_mode"]:
        assert value in instructions, value
    for field in RULES["fill"] + RULES["replace"]:
        assert field in instructions, field


def test_check_lists_are_fields_the_llm_may_write():
    writable = set(RULES["fill"]) | set(RULES["replace"])
    assert set(RULES["exact"]) <= writable
    assert set(RULES["literal"]) <= writable
