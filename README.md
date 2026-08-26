[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![](https://github.com/FAIRmat-NFDI/pynxtools-spm/actions/workflows/pytest.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/pynxtools-spm/actions/workflows/pylint.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/pynxtools-spm/actions/workflows/publish.yml/badge.svg)
![](https://img.shields.io/pypi/pyversions/pynxtools-spm)
![](https://img.shields.io/pypi/l/pynxtools-spm)
![](https://img.shields.io/pypi/v/pynxtools-spm)
![](https://coveralls.io/repos/github/FAIRmat-NFDI/pynxtools-spm/badge.svg?branch=main)
[![DOI](https://zenodo.org/badge/759916501.svg)](https://doi.org/10.5281/zenodo.17390485)

# `pynxtools-spm`: A `pynxtools` reader for SPM data

.

This `pynxtools` plugin was generated with [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) using the [`pynxtools-plugin-template`](https://github.com/FAIRmat-NFDI/`pynxtools-plugin-template) template.

## Supported file formats

| Technique | Vendor | Instrument software (flavor) | Tested version | Extension |
| --- | --- | --- | --- | --- |
| STS | Nanonis | Nanonis SPM control software | Generic 5, Generic 5e | `.dat` |
| STM | Nanonis | Nanonis SPM control software | Generic 5, Generic 5e | `.sxm` |
| STM | Omicron | SM4 (read with [spym](https://github.com/rescipy-project/spym)) | not version specific | `.sm4` |
| AFM | Nanonis | Nanonis SPM control software | Generic 4 | `.sxm` |
| AFM | Bruker | Bruker `SPMLab` (read with [gwyddionpy](https://pypi.org/project/gwyddionpy/)) | `1.00` | `.flt`, written by the instrument as `.FLT` |
| AFM | Bruker | Bruker `NanoScope` (read with [gwyddionpy](https://pypi.org/project/gwyddionpy/)) | `9.x` (Dimension Icon) | `.spm` |
| AFM (force curve) | Bruker | Bruker `NanoScope` ASCII export | `9.x` (Dimension Icon) | `.spm.txt` |

See [supported vendor files and formats](https://fairmat-nfdi.github.io/pynxtools-spm/explanation/reader-orchestra.html#supported-vendor-files-and-formats) for details, e.g. that one Bruker `SPMLab` FLT file holds a single channel of a single scan direction and is therefore converted into its own NeXus file, whereas one Bruker `NanoScope` `.spm` file holds every channel in both scan directions and yields a single NeXus file with several `NXdata` groups. The `.spm.txt` export is a force ramp (force-distance curve) rather than an image.

## Installation

It is recommended to use python 3.12 with a dedicated virtual environment for this package.
Learn how to manage [python versions](https://github.com/pyenv/pyenv) and
[virtual environments](https://realpython.com/python-virtual-environments-a-primer/).

This package is a reader plugin for [`pynxtools`](https://github.com/FAIRmat-NFDI/pynxtools) and can be installed together with `pynxtools`:

```shell
uv pip install pynxtools[spm]
```

for the latest released version.

## Docs

More information about this pynxtools plugin is available in the [documentation](https://fairmat-nfdi.github.io/pynxtools-spm/). You will find information about getting started, how-to guides, the supported file formats, how to get involved, and much more there.

## Contact person in FAIRmat for this reader

Rubel Mozumder


**Note**: This repository is an upgraded and renamed version of [pynxtools-stm](https://github.com/FAIRmat-NFDI/pynxtools-stm), which is now archived. In addition to the integration of new readers (e.g., `AFM`), all functionalities of `pynxtools-stm` remain available in this repository.