from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

tool = NORTHTool(
    short_description="Jupyter Notebook server in NOMAD NORTH for NOMAD and pynxtools plugin pynxtools-spm.",
    image="ghcr.io/fairmat-nfdi/pynxtools-spm/jupyter:latest",
    description="Jupyter Notebook server in NOMAD NORTH for NOMAD and pynxtools plugin pynxtools-spm.",
    external_mounts=[],
    file_extensions=["ipynb", "nxs"],
    icon="logo/jupyter.svg",
    image_pull_policy="Always",
    default_url="/lab",
    maintainer=[{"email": "fairmat@physik.hu-berlin.de", "name": "The NOMAD authors"}],
    mount_path="/home/jovyan",
    path_prefix="lab/tree",
    privileged=False,
    with_path=True,
    display_name="spm",
)

north_tool = NorthToolEntryPoint(id_url_safe="pynxtools_spm_spm", north_tool=tool)
