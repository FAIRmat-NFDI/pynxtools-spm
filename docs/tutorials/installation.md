# Installation

The `pynxtools-spm` is published on PyPI and can be installed via python's package managers like `uv` or `pip`.
For beginers, we will show very basic and common ways to install the package.

Create a virtual environments with `venv` module and activate it:

**Environment with [`venv`](https://docs.python.org/3/library/venv.html) module in `.venv`**

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

**Environment with [`uv`](https://docs.astral.sh/uv/getting-started/first-steps/) python package manager in `.venv`**

```bash
$ uv venv .venv --python=3.11
$ source .venv/bin/activate
```

<!-- Italic -->

**Note:** _We recommend to use `uv` package manager to create and manage virtual environments and for all the package managing tasks (development, installation, etc.)._

## **Install `pynxtools-spm` package**

Install `pynxtools-spm` package from (PyPI) to use as a standalone package in activated pyton environment.

```bash
$ uv pip install pynxtools-spm # from PyPI
```

Or, install `pynxtools-spm` package from the source code (with a specific branch) to use as a standalone package in activated pyton environment. Use this installation method to develop or play with the `pynxtools-spm` code.

```bash
$ uv pip install git+https://github.com/FAIRmat-NFDI/pynxtools-spm.git@<branch-name>#egg=pynxtools-spm # Replace <branch-name> with the branch you want to install
```

Or, install `pynxtools-spm` as a plugin of `pynxtools` package from (PyPI). The earlier `pynxtools-spm` installation steps will also install `pynxtools` package with an appropriate version.

```bash
$ uv pip install pynxtools[spm] # from PyPI
```

## **Install `pynxtools-spm` package with NOMAD**

Install `pynxtools-spm` package with [NOMAD](https://nomad-lab.eu/nomad-lab/) latest release, first install NOMAD ([NOMAD installation guide](https://nomad-lab.eu/prod/v1/docs/howto/programmatic/pythonlib.html)) and then `pynxtools-spm` using one of the above installation commands.

```bash
$ uv pip install nomad-lab --extra-index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple
$ uv pip install pynxtools[spm]
```

Though installing `pynxtools-spm` with nomad would not bring any extra advantage, if user does not deploy NOMAD, called `NOMAD-Oasis`, in their premises or on cloud (Installation and configuration details of [NOMAD oasis](https://nomad-lab.eu/prod/v1/docs/howto/oasis/configure.html)) or test the `pynxtools-spm` package.
