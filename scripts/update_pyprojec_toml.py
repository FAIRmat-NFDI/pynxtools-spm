import tomllib
from pathlib import Path

root_dir = Path(__file__).parent.parent
spym_toml = root_dir / "src" / "pynxtools_spm" / "parsers" / "spym" / "pyproject.toml"
spm_toml = root_dir / "pyproject.toml"

with open(spym_toml, "rb") as f:
    spym_dep = tomllib.load(f)["build-system"]["requires"]

with open(spm_toml, "r+b") as f:
    spm_file_content = tomllib.load(f)
    spm_dep = spm_file_content["project"]["dependencies"]

    spm_dep = set(spym_dep + spm_dep)
    print(f"Updating {spm_toml} with {spym_toml} dependencies")
    spm_file_content["project"]["dependencies"] = list(spm_dep)
