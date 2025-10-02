# Installation

The `pynxtools-spm` is published on PyPI and can be installed via python's package managers like `uv` or `pip`.

For beginners, we will show very basic and common ways to install the package.

Create a virtual environments with `venv` module and activate it. On the following steps, we need the virtual environment always activated.

**Environment with [`venv`](https://docs.python.org/3/library/venv.html) module in `.venv`**

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

**Environment with [`uv`](https://docs.astral.sh/uv/getting-started/first-steps/) python package manager in `.venv`**

```bash
$ uv venv .venv --python=3.12
$ source .venv/bin/activate
```

**Note:** _We recommend to use `uv` package manager to create and manage virtual environments and for all the package managing tasks (development, installation, etc.)._

## **Install `pynxtools-spm` package**

Install `pynxtools-spm` package from (PyPI) to use as a standalone package in activated Python environment.

```bash
$ uv pip install pynxtools-spm  # Install from PyPI
```

Or, install `pynxtools-spm` package from the source code (with a specific branch) to use as a standalone package in activated pyton environment. Use this installation method to develop or play with the `pynxtools-spm` code.

```bash
$ uv pip install git+https://github.com/FAIRmat-NFDI/pynxtools-spm.git@<branch-name>#egg=pynxtools-spm  # Replace <branch-name> with the exact branch you want to install
```

Or, install `pynxtools-spm` as a plugin of `pynxtools` package from (PyPI).


```bash
$ uv pip install pynxtools[spm] # from PyPI
```

**Note**: _The earlier `pynxtools-spm` installation steps will also install `pynxtools` as a dependency with an appropriate version._

## **Install `pynxtools-spm` package with NOMAD**

Install `pynxtools-spm` package with [NOMAD](https://nomad-lab.eu/nomad-lab/) latest release, first install NOMAD ([NOMAD installation guide](https://nomad-lab.eu/prod/v1/docs/howto/programmatic/pythonlib.html)) and then `pynxtools-spm` using one of the above installation commands.

```bash
$ uv pip install nomad-lab --extra-index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple
$ uv pip install pynxtools[spm]
```

Though installing `pynxtools-spm` with `NOMAD` would not bring any extra advantage, if users do not deploy NOMAD, called `NOMAD-Oasis`, in their premises or on cloud (Installation and configuration details of [NOMAD oasis](https://nomad-lab.eu/prod/v1/docs/howto/oasis/configure.html)).
