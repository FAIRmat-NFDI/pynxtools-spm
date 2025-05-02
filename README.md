[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![](https://github.com/FAIRmat-NFDI/pynxtools-spm/actions/workflows/pytest.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/pynxtools-spm/actions/workflows/pylint.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/pynxtools-spm/actions/workflows/publish.yml/badge.svg)
![](https://img.shields.io/pypi/pyversions/pynxtools-spm)
![](https://img.shields.io/pypi/l/pynxtools-spm)
![](https://img.shields.io/pypi/v/pynxtools-spm)
![](https://coveralls.io/repos/github/FAIRmat-NFDI/pynxtools_spm/badge.svg?branch=master)

# SPM Reader
 !!WARNING!! The is under development.

## Automated Uploader to Nomad
The experimental data e.g., data from spm experiment can be upload, store and publish to the central NOMAD or to NOMAD oasis. For that we have a uploader script to make the task simple and reuseable from several labs.

### Run uploader
The uploader python script can be run from windows and linux.
If someone wants to run the script from linux in a windows pc he may need to install `Windows Subsystem for Linux (WSL)`.

#### Install WSL2 with ubuntu distro and launch WSL
Follow full documentation on [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install) from Microsoft. Complete the instalation steps and launch linux terminal vis wsl, before following the next steps. After launching the linux terminal via `WSL` follow the next setps from you linux terminal
#### Create python virtual environment in Linux
There are several package managers are available arround such as pip (probably most popular one), poetry, uv (highly faster compare to others). You can use one of them, but we recommand to use `uv` and we used `uv` tools througout the documentation.

1. Install `uv` package manager: Before creating python virtial environment, [`uv`](https://docs.astral.sh/uv/) package manager needs to be [installed](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) in first place. 
The simplest way is to use `curl` or `wget` command tools -
```console
# Install latest version
$ curl -LsSf https://astral.sh/uv/install.sh | sh
``` 
or,
```console
# Install latest version
$ wget -qO- https://astral.sh/uv/install.sh | sh
```
Check if `uv` is properly intalled hiting command `uv --version` or just `uv` from your linux terminal.

2. Install Python: At the time of writting this documentation `pynxtools` and `pynxtools-spm` both are compatible with python `3.12` version (check for future updates for [`pynxtools`](https://github.com/FAIRmat-NFDI/pynxtools/blob/master/pyproject.toml#L16) and [`pynxtools-spm`](https://github.com/FAIRmat-NFDI/pynxtools-spm/blob/main/pyproject.toml#L15)).
From your linux terminal run

```console
# Install python3.12, replace the python version if you want
$ uv python install python3.12  
```
to install python 3.12. In any case, uninstall python by

```console
# Unintall python3.12, replace the python version if you want
$ uv python uninstall python3.12
```
4. Create and activate virtual enveronment : Create virtual environment with `uv` tool.

```console
# Create virtual environment in your current work directory (CWD)
$ uv venv --python python3.13 .venv

# Activate the environment 
$ source .venv/bin/activate
```

5. Install `pynxtool` and `pynxtools-spm` in virtual environment: Both of the `pynxtools` and `pynxtools-spm` are available in PyPI repository, and install the same versions installed in NOMAD where you planed to store you data ([▶️ Watch the video]()).

```console
# Install pynxtools in your python virtual environment
$ uv pip install pynxtools

# Install pynxtools-spm
$ uv pip install pynxtools-som
```




##### TODO:
2. Add uploader as a script in pynxtools-spm
