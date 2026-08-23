# __Installation__

`pynxtools-spm` is a Python package published on [PyPI](https://pypi.org/project/pynxtools-spm/). This tutorial walks you through installing it, either as a standalone package or together with [NOMAD](https://nomad-lab.eu/nomad-lab/).

## __Who is this tutorial for?__

This tutorial is for anyone who wants to convert Scanning Probe Microscopy (SPM) data into NeXus files with `pynxtools-spm`:

- experimentalists who want to run the reader from the command line on their own STM, STS, or AFM files,
- users of a [NOMAD Oasis](https://nomad-lab.eu/prod/v1/docs/howto/oasis/configure.html) who want the SPM reader available inside their Oasis,
- developers who want to extend the reader orchestra with a new vendor file format.

## __What should you know before this tutorial?__

You should be comfortable with a terminal and with Python virtual environments. If either is new to you, these are good starting points:

- [Python virtual environments](https://realpython.com/python-virtual-environments-a-primer/)
- [Getting started with `pynxtools`, NeXus, and NOMAD](https://fairmat-nfdi.github.io/pynxtools/getting-started.html)
- [Installation guide of `pynxtools`](https://fairmat-nfdi.github.io/pynxtools/tutorial/installation.html)

## __What you will know at the end of this tutorial?__

You will know

- how to create a virtual environment for `pynxtools-spm`,
- how to install `pynxtools-spm`, either standalone or as a plugin of `pynxtools`,
- how to install `pynxtools-spm` in development (editable) mode,
- how to install `pynxtools-spm` together with NOMAD,
- how to verify that the `spm` reader is available.

## __Steps__

### __1. Create and activate a virtual environment__

`pynxtools-spm` requires Python `3.10` or newer (tested up to `3.13`); we recommend Python `3.12`. Create a dedicated virtual environment so that the installation does not interfere with other Python projects. We recommend [`uv`](https://docs.astral.sh/uv/getting-started/first-steps/), an extremely fast Python package and project manager, but the [`venv`](https://docs.python.org/3/library/venv.html) module of the standard library works as well.

=== "uv"

    `uv` creates the virtual environment and installs the requested Python version in one step.

    ```bash
    uv venv .venv --python=3.12
    ```

=== "venv"

    Note that the Python version has to be installed beforehand.

    ```bash
    python3 -m venv .venv
    ```

Both commands create the environment in a directory called `.venv`. Activate it:

```bash
source .venv/bin/activate
```

!!! note
    Ensure that the virtual environment is activated in all the following steps.

### __2. Install the `pynxtools-spm` package__

Install the latest stable release from PyPI to use `pynxtools-spm` as a standalone package:

=== "uv"

    ```bash
    uv pip install pynxtools-spm
    ```

=== "pip"

    ```bash
    pip install pynxtools-spm
    ```

Alternatively, install it as a plugin of the `pynxtools` package, which pulls in `pynxtools-spm` through the `spm` extra:

=== "uv"

    ```bash
    uv pip install pynxtools[spm]
    ```

=== "pip"

    ```bash
    pip install pynxtools[spm]
    ```

You can also install the latest _development_ version directly from GitHub:

=== "uv"

    ```bash
    uv pip install git+https://github.com/FAIRmat-NFDI/pynxtools-spm.git
    ```

=== "pip"

    ```bash
    pip install git+https://github.com/FAIRmat-NFDI/pynxtools-spm.git
    ```

!!! note
    Every installation method also installs `pynxtools` as a dependency with a suitable version (`pynxtools>=0.15.0`).

### __3. Install in development mode (optional)__

If you want to contribute to the code repository, e.g. to [extend the reader orchestra](../how-to-guides/how-to-extend-readers.md) with a new vendor file format, clone the repository and install it in editable mode together with the `dev` and `docs` extras:

```bash
git clone https://github.com/FAIRmat-NFDI/pynxtools-spm.git
cd pynxtools-spm
```

=== "uv"

    ```bash
    uv pip install -e ".[dev,docs]"
    ```

=== "pip"

    ```bash
    pip install -e ".[dev,docs]"
    ```

Then install the pre-commit hooks and create a branch to work on:

```bash
pre-commit install
git checkout -b <branch_name>
```

The `docs` extra installs [MkDocs](https://www.mkdocs.org/) and its plugins, so that you can build this documentation locally with `mkdocs serve` (the build additionally requires the `tree` command line utility).

### __4. Install `pynxtools-spm` with NOMAD__ { #install-pynxtools-spm-with-nomad }

To use `pynxtools-spm` in [NOMAD](https://nomad-lab.eu/nomad-lab/), install it into the same Python environment as the `nomad-lab` package. NOMAD discovers `pynxtools-spm` automatically through its Python entry points, so no further configuration is needed. It also picks up the three example uploads (STS, STM, and AFM) that the package ships.

First install NOMAD (see the [NOMAD installation guide](https://nomad-lab.eu/prod/v1/docs/howto/programmatic/pythonlib.html)), then install `pynxtools-spm`:

=== "uv"

    ```bash
    uv pip install nomad-lab --extra-index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple
    uv pip install pynxtools[spm]
    ```

=== "pip"

    ```bash
    pip install nomad-lab --extra-index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple
    pip install pynxtools[spm]
    ```

!!! note
    Installing `pynxtools-spm` with NOMAD does not provide any additional advantage unless you deploy NOMAD, called `NOMAD Oasis`, on your premises or in the cloud. For installation and configuration details, see [NOMAD Oasis](https://nomad-lab.eu/prod/v1/docs/howto/oasis/configure.html).

### __5. Verify the installation__

The reader is used through the `pynx convert` command line interface of `pynxtools`. Check that the command is available and that `spm` is listed among the installed readers:

```bash
pynx convert --help
```

The `--reader` option of the printed help lists the installed readers; `spm` must be one of them. A minimal conversion looks like this:

```bash
pynx convert --nxdl NXstm --reader spm --output output.nxs eln_data.yaml nanonis_stm_file.sxm config.json
```

## __Further reading__

- [Use Reader in NOMAD](use-reader-in-nomad.md)
- [Use Reader from Command Line](../reference/standalone-usages.md)
- [Work with Reader](../how-to-guides/work-with-reader.md)
- [Supported vendor files and formats](../explanation/reader-orchestra.md#supported-vendor-files-and-formats)
