"""
Functionality tests for functions and classes developed in spm reader
"""

from pynxtools_spm.nxformatters.helpers import replace_variadic_name_part
import pytest

@pytest.mark.parametrize(
    "name, part_to_embed, expected",
    [
        ('yy_NM[yy_nm]', 'x', 'yy_NM[yy_x]'),
        ('yy_M_N[yy_m_n]', 'x', 'yy_M_N[yy_x]'),
        ('Myy[myy]', 'x', 'Myy[x_yy]'),
        ('y_M_yy[y_m_yy]', 'x', 'y_M_yy[y_x_yy]'),
        ('y_M_N_yy[y_x_yy]', 'x', 'y_M_N_yy[y_x_yy]'),
        ('yy_ff[yy_mn]', 'x', 'yy_ff[yy_mn]'),
        # Additional test cases
        ('test[abc]', 'z', 'test[abc]'),
        ('prefixM[prefix_m]', '_y', 'prefixM[prefix_y]'),
        ('no_brackets', 'x', 'no_brackets'),
        ('[only]', 'x', '[only]'),
        ('multi_M_N_M[multi_m_n_m]', '_z', 'multi_M_N_M[multi_z]'),
        ('', 'x', ''),
        ('complex_M_N[complex_m_n]', 'a', 'complex_M_N[complex_a]'),
        ('already_x[already_x]', 'x', 'already_x[already_x]'),
    ]
)
def test_replace_variadic_name_part(name, part_to_embed, expected):
    result = replace_variadic_name_part(name, part_to_embed)
    assert result == expected, f"Failed for {name}, {part_to_embed}: got {result}, expected {expected}"
