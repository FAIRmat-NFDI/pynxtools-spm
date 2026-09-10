"""
Functionality tests for functions and classes developed in spm reader
"""

import copy

import pytest

from pynxtools_spm.nxformatters.base_formatter import (
    CONVERT_DICT,
    REPEATEABLE_CONCEPTS,
    write_multiple_concepts_instance,
)
from pynxtools_spm.nxformatters.bruker.bruker_spm_afm import BrukerSpmAFM
from pynxtools_spm.nxformatters.helpers import replace_variadic_name_part


@pytest.mark.parametrize(
    "name, part_to_embed, expected",
    [
        ("yy_NM[yy_nm]", "x", "yy_NM[yy_x]"),
        ("yy_M_N[yy_m_n]", "x", "yy_M_N[yy_x]"),
        ("Myy[myy]", "x", "Myy[x_yy]"),
        ("yyM[yym]", "x", "yyM[yy_x]"),
        ("yyM[yy_m]", "x", "yyM[yy_x]"),
        ("y_M_yy[y_m_yy]", "x", "y_M_yy[y_x_yy]"),
        ("y_M_N_yy[y_x_yy]", "x", "y_M_N_yy[y_x_yy]"),
        ("yy_ff[yy_mn]", "x", "yy_ff[yy_mn]"),
        ("ALL_UPPER", "all_lower", "ALL_UPPER[all_lower]"),
        # Additional test cases
        ("test[abc]", "z", "test[abc]"),
        ("prefixM[prefix_m]", "_y", "prefixM[prefix_y]"),
        ("no_brackets", "x", "no_brackets"),
        ("[only]", "x", "[only]"),
        ("multi_M_N_M[multi_m_n_m]", "_z", "multi_M_N_M[multi_z]"),
        ("", "x", ""),
        ("complex_M_N[complex_m_n]", "a", "complex_M_N[complex_a]"),
        ("already_x[already_x]", "x", "already_x[already_x]"),
    ],
)
def test_replace_variadic_name_part(name, part_to_embed, expected):
    result = replace_variadic_name_part(name, part_to_embed)
    assert result == expected, (
        f"Failed for {name}, {part_to_embed}: got {result}, expected {expected}"
    )


@pytest.mark.parametrize(
    "value, fallback_unit, expected",
    [
        # Non-string values pass straight through with the config unit.
        (0, "nm", (0, "nm")),
        (-3750.5, "nm", (-3750.5, "nm")),
        (None, "nm", (None, "nm")),
        # NanoScope v9.x writes the unit into the value; it wins over the
        # config unit and the magnitude is converted into it.
        ("-3750 nm", "nm", (-3750, "nm")),
        ("20 um", "nm", (pytest.approx(20000), "nm")),
        # No usable fallback: keep the unit carried by the value itself.
        ("-3750 nm", "", (-3750, "nanometer")),
        ("-3750 nm", None, (-3750, "nanometer")),
        # Fallback unit is dimensionally incompatible -> keep the value's unit.
        ("20 um", "second", (20, "micrometer")),
        # Bare numeric strings keep the config unit.
        ("3750", "nm", (3750, "nm")),
        ("1e-3", "nm", (0.001, "nm")),
        # Unresolvable strings must not leak out as strings: the caller does
        # arithmetic on the magnitude and writes it to a numeric NeXus field.
        ("abc", "nm", (None, "nm")),
        ("", "nm", (None, "nm")),
        ("   ", "nm", (None, "nm")),
    ],
)
def test_bruker_spm_scalar_with_unit(value, fallback_unit, expected):
    """BrukerSpmAFM._scalar_with_unit always yields a numeric magnitude or None."""
    result = BrukerSpmAFM._scalar_with_unit(value, fallback_unit)
    assert result == expected, (
        f"Failed for {value!r}, {fallback_unit!r}: got {result}, expected {expected}"
    )
    magnitude = result[0]
    assert magnitude is None or isinstance(magnitude, (int, float)), (
        f"Magnitude {magnitude!r} for {value!r} is neither numeric nor None"
    )


def test_write_multiple_concepts_instance_rejects_the_shared_convert_dict():
    """The mapping is mutated in place, so the module-level dict must be refused.

    A 'del convert_mapping[key]' on CONVERT_DICT would remove the entry for the
    whole process and silently break every later conversion in the same run.
    """
    with pytest.raises(ValueError, match="mutates 'convert_mapping' in place"):
        write_multiple_concepts_instance(
            eln_dict={"User": [{"name": "a"}]},
            list_of_concept=REPEATEABLE_CONCEPTS,
            convert_mapping=CONVERT_DICT,
        )
    assert "User" in CONVERT_DICT, "CONVERT_DICT was mutated despite the guard"


def test_write_multiple_concepts_instance_expands_variadic_instances():
    """A copy of the mapping is expanded per instance and the singular key removed."""
    convert_mapping = copy.deepcopy(CONVERT_DICT)
    eln_dict = {
        "User": [{"name": "first"}, {"name": "second"}],
        "citeID": {"doi": ["10.1/a"], "author": ["someone"]},
    }
    result = write_multiple_concepts_instance(
        eln_dict=eln_dict,
        list_of_concept=REPEATEABLE_CONCEPTS,
        convert_mapping=convert_mapping,
    )

    # All-uppercase class: USER[user] -> user_1, user_2
    assert result["user_1"] == {"name": "first"}
    assert result["user_2"] == {"name": "second"}
    assert convert_mapping["user_1"] == "USER[user_1]"
    assert convert_mapping["user_2"] == "USER[user_2]"
    # The singular mapping of an expanded concept is consumed ...
    assert "User" not in convert_mapping
    # ... in the copy only; the module-level dict is untouched.
    assert CONVERT_DICT["User"] == "USER[user]"

    # 'citeID' is not in REPEATEABLE_CONCEPTS, so it is passed through verbatim
    # and is renamed later by flatten_and_replace via the CONVERT_DICT entry.
    assert result["citeID"] == eln_dict["citeID"]
    assert convert_mapping["citeID"] == "citeID[cite_id]"
