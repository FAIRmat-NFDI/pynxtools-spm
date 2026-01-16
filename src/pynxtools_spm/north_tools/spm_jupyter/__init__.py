from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

tool = NORTHTool(
    short_description="Jupyter Notebook server for SPM techniques in NOMAD NORTH.",
    image="ghcr.io/fairmat-nfdi/pynxtools-spm/jupyter:pr-70",
    description="Jupyter Notebook server for SPM (Scanning Probe Microscopy)",
    external_mounts=[],
    file_extensions=["ipynb", "nxs", "h5", "hdf5"],
    icon="logo/jupyter.svg",
    image_pull_policy="Always",
    default_url="/lab",
    maintainer=[
        {"email": "rubel.mozumder@physik.hu-berlin.de", "name": "Rubel Mozumder"}
    ],
    mount_path="/home/jovyan",
    path_prefix="lab/tree",
    privileged=False,
    with_path=True,
    display_name="SPM-Jupyter",
)

spm_jupyter = NorthToolEntryPoint(id_url_safe="spm_jupyter", north_tool=tool)
