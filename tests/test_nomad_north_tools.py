"""Tests for the NOMAD NORTH tool."""

import pytest

try:
    import nomad  # noqa: F401
except ImportError:
    pytest.skip(
        "Skipping NOMAD NORTH tool tests because nomad-lab is not installed",
        allow_module_level=True,
    )


def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from pynxtools_spm.nomad.north_tools.spm import (
        north_tool,
    )

    assert (
        north_tool.id_url_safe == "pynxtools_spm_spm"
        or north_tool.id == "nomad-north-spm"
    ), "NORTHtool entry point has incorrect id or id_url_safe"
