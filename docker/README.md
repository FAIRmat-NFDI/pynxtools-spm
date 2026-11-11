# pynxtools-spm image

A Docker image with `pynxtools` and `pynxtools-spm`, to convert SPM raw files to NeXus without a
local Python setup. One use is the Galaxy tool `pynxtools_dataconverter`, because neither package is
on [conda-forge](https://conda-forge.org).

## Build

Run from the repo root. `PYNXTOOLS_SPM_VERSION` is required.

```bash
# From this checkout (the version is given, because the build cannot read git tags)
docker build -f docker/Dockerfile \
  --build-arg PYNXTOOLS_SPM_VERSION=0.4.2 -t pynxtools-spm:0.4.2 .

# From PyPI (a released version)
docker build -f docker/Dockerfile --build-arg PYNXTOOLS_SPM_SOURCE=pypi \
  --build-arg PYNXTOOLS_SPM_VERSION=0.4.2 -t pynxtools-spm:0.4.2 .
```

| Build argument | Default | Meaning |
|---|---|---|
| `PYNXTOOLS_SPM_SOURCE` | `local` | `local`: this checkout; `pypi`: the release on PyPI |
| `PYNXTOOLS_SPM_VERSION` | none | `pynxtools-spm` version |
| `PYNXTOOLS_VERSION` | empty | Empty: the newest `pynxtools` that `pyproject.toml` allows |
| `UV_VERSION` | `0.9` | [uv](https://docs.astral.sh/uv/) image used to build and install; not kept in the image |

## Run

The [entrypoint](https://docs.docker.com/reference/dockerfile/#entrypoint) chooses what to run from
the first argument:

| First argument | Runs | Example |
|---|---|---|
| None | `pynx convert --help` | `docker run --rm IMAGE` |
| An option (`-…`) | `pynx convert …` | `docker run --rm -v "$PWD:/data" -w /data IMAGE --nxdl NXstm --reader spm --output out.nxs eln_data.yaml scan.sxm` |
| A program or path | The program, unchanged | `docker run --rm IMAGE python nxs_convert.py …` (as Galaxy does) |
| Anything else | `pynx …` | `docker run --rm IMAGE convert --help` |

Without a config `.json`, the reader uses its default config.

## Automatic build

`.github/workflows/spm-docker-build.yml` builds and tests the image with the latest `pynxtools`
from PyPI. It stops if the image does not have it, if `CITATION.cff` is older than the newest
`pynxtools-spm` on PyPI, or if the reader test output differs from the reference NeXus file.
Two workflows call it:

| Workflow | Event | Builds from | Pushes |
|---|---|---|---|
| `spm-docker-test.yml` | `CITATION.cff` changes on `release/*`; PR into `release/*`; manual run | This checkout | No |
| `spm-docker-publish.yml` | `publish.yml` has published to PyPI; manual run | PyPI | `ghcr.io/fairmat-nfdi/pynxtools-spm:<version>` and `:latest` |

The test builds find a break before the release. The publish run waits up to 30 minutes for PyPI to
list the version. If `:<version>` already exists, it only builds from the checkout and tests, so a
published image never changes.
