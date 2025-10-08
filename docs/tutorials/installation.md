# Installation

`pynxtools-spm` is a Python package published on PyPI. It can be installed via Python package managers such as `uv` or `pip`. For beginners, we show basic and common ways to install the package.

Create a virtual environment with the `venv` module or `uv` package manager and activate it. In the following steps, ensure the virtual environment is always activated.

**Create an environment with [`venv`](https://docs.python.org/3/library/venv.html) in `.venv`:**

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

**Create an environment with [`uv`](https://docs.astral.sh/uv/getting-started/first-steps/) in `.venv`:**

```bash
$ uv venv .venv --python=3.12
$ source .venv/bin/activate
```

**Note:** _We recommend using the `uv` package manager to create and manage virtual environments, as well as for all package management tasks (e.g., development, installation, etc.)._

## **Install the `pynxtools-spm` package**

Install the `pynxtools-spm` package from PyPI to use it as a standalone package in your activated Python environment:

```bash
$ uv pip install pynxtools-spm  # Install from PyPI
```

Or, install the `pynxtools-spm` package from the source code (with a specific branch) to use it as a standalone package in your activated Python environment.
```bash
$ uv pip install git+https://github.com/FAIRmat-NFDI/pynxtools-spm.git@<branch-name>#egg=pynxtools-spm  # Replace <branch-name> with the branch you want to install
```

Alternatively, install `pynxtools-spm` as a plugin for the `pynxtools` package from PyPI in your activated Python environment:

```bash
$ uv pip install pynxtools[spm]  # Install from PyPI
```

Or, install the `pynxtools-spm` package in development mode in activated Python environment to contribute in the code repository:

```bash
$ git clone https://github.com/FAIRmat-NFDI/pynxtools-spm.git
$ cd pynxtools-spm
$ uv pip install -e .  # Install in editable mode
```

**Note:** _All `pynxtools-spm` installation methods will also install `pynxtools` as a dependency with the appropriate version._

## **Install `pynxtools-spm` with NOMAD**

To install `pynxtools-spm` with [NOMAD](https://nomad-lab.eu/nomad-lab/), first install NOMAD ([NOMAD installation guide](https://nomad-lab.eu/prod/v1/docs/howto/programmatic/pythonlib.html)), then install `pynxtools-spm` using one of the above installation commands:

```bash
$ uv pip install nomad-lab --extra-index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple
$ uv pip install pynxtools[spm]
```

Note that installing `pynxtools-spm` with NOMAD does not provide any additional advantages unless you deploy NOMAD, called `NOMAD-Oasis`, on your premises or in the cloud. For installation and configuration details, see [NOMAD Oasis](https://nomad-lab.eu/prod/v1/docs/howto/oasis/configure.html).
