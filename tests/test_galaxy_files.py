"""The files for the Galaxy ELN tools are shipped and fit together."""

import re

import pytest
import yaml

from pynxtools_spm.galaxy import ELN_INSTRUCTIONS_FILE, ELN_RULES_FILE

RULES = yaml.safe_load(ELN_RULES_FILE.read_text(encoding="utf-8"))


def read_sections():
    """{name: text} of the `# <name>` sections, as the Galaxy tool reads them."""
    sections, name, fenced = {}, None, False
    for line in ELN_INSTRUCTIONS_FILE.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("# "):
            name = line[2:].strip()
            sections[name] = []
        elif name:
            sections[name].append(line)
    return {key: "\n".join(lines) for key, lines in sections.items()}


SECTIONS = read_sections()


@pytest.mark.parametrize("definition", sorted(RULES["definitions"]))
def test_eln_job_names_every_allowed_value_and_field(definition):
    """The Galaxy tool stops on such a mismatch, so it is checked here first."""
    text = "\n".join(SECTIONS[name] for name in ("Common", definition, "Output"))
    for value in RULES["definitions"][definition]["scan_mode"]:
        assert value in text, value
    for field in RULES["fill"] + RULES["replace"]:
        assert field in text, field


def test_detection_names_every_technique_and_scan_mode():
    for entry in RULES["definitions"].values():
        for value in [entry["technique"], *entry["scan_mode"]]:
            assert value in SECTIONS["Detection"], value


def test_check_lists_are_fields_the_llm_may_write():
    writable = set(RULES["fill"]) | set(RULES["replace"])
    assert set(RULES["exact"]) <= writable
    assert set(RULES["literal"]) <= writable


def test_header_fields_are_fields_the_llm_may_write():
    assert set(RULES["header"]) <= set(RULES["fill"]) | set(RULES["replace"])


def test_each_extension_names_one_technique():
    """The ELN builder takes the technique from the raw file's extension, as a last resort."""
    extensions = [
        ext for entry in RULES["definitions"].values() for ext in entry["extensions"]
    ]
    assert extensions, "no extensions"
    assert len(extensions) == len(set(extensions))
    assert all(ext.startswith(".") and ext == ext.lower() for ext in extensions)


@pytest.mark.parametrize(
    "line, technique",
    [
        ("channel: Frequency_Shift (Forward)", "AFM"),
        ("Oscillation Control::Amplitude controller on: TRUE", "AFM"),
        (":Oscillation Control>Amplitude controller on:\nTRUE", "AFM"),
        ("MicroscopeList: Tapping", "AFM"),
        ("Mode: Peak Force Tapping", "AFM"),
        ("Oscillation Control::Amplitude controller on: FALSE", None),
        ("channel: Current (Forward)", None),
        ("", None),
    ],
)
def test_header_markers(line, technique):
    """Header lines of pynxtools-spm test files mark only AFM; an off controller marks nothing."""
    hits = [
        entry["technique"]
        for entry in RULES["definitions"].values()
        if any(
            re.search(marker, line, flags=re.MULTILINE)
            for marker in entry["header_markers"]
        )
    ]
    assert hits == ([technique] if technique else [])
