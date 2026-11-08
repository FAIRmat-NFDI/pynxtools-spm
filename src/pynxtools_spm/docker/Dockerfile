# syntax=docker/dockerfile:1
# Image with pynxtools and pynxtools-spm, e.g. for the Galaxy tool `pynxtools_dataconverter`.
# Build from the repo root: docker build -f src/pynxtools_spm/docker/Dockerfile .
ARG PYTHON_VERSION=3.12
ARG UV_VERSION=0.9
# local: pynxtools-spm from this checkout; pypi: the released PYNXTOOLS_SPM_VERSION.
ARG PYNXTOOLS_SPM_SOURCE=local

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv_stage

# Build the pynxtools-spm wheel from this checkout.
FROM python:${PYTHON_VERSION}-slim-bookworm AS build-local
# setuptools-scm cannot read git here (.git is not copied), so the version is given.
ARG PYNXTOOLS_SPM_VERSION
RUN test -n "${PYNXTOOLS_SPM_VERSION}" || \
    (echo "Set --build-arg PYNXTOOLS_SPM_VERSION=<version>" >&2; exit 1)
WORKDIR /src
COPY pyproject.toml MANIFEST.in README.md LICENSE ./
COPY src ./src
RUN --mount=type=bind,from=uv_stage,source=/uv,target=/bin/uv \
    SETUPTOOLS_SCM_PRETEND_VERSION="${PYNXTOOLS_SPM_VERSION}" \
    uv build --no-cache --wheel --out-dir /wheels .

# No wheel: the final stage installs pynxtools-spm from PyPI.
FROM python:${PYTHON_VERSION}-slim-bookworm AS build-pypi
RUN mkdir /wheels

# BuildKit builds only the stage chosen here.
FROM build-${PYNXTOOLS_SPM_SOURCE} AS build

FROM python:${PYTHON_VERSION}-slim-bookworm
ARG PYNXTOOLS_SPM_SOURCE
ARG PYNXTOOLS_SPM_VERSION
# Empty: uv picks the newest pynxtools that pynxtools-spm allows.
ARG PYNXTOOLS_VERSION=""

# Install into the image's Python; compile .pyc like pip, so each run starts faster.
ENV UV_SYSTEM_PYTHON=1 \
    UV_NO_CACHE=1 \
    UV_COMPILE_BYTECODE=1

# uv is mounted only for this step, so it is not in the final image.
RUN --mount=type=bind,from=uv_stage,source=/uv,target=/bin/uv \
    --mount=type=bind,from=build,source=/wheels,target=/wheels \
    if [ "${PYNXTOOLS_SPM_SOURCE}" = pypi ]; then \
        spm="pynxtools-spm${PYNXTOOLS_SPM_VERSION:+==${PYNXTOOLS_SPM_VERSION}}"; \
    else \
        spm=$(ls /wheels/*.whl); \
    fi && \
    uv pip install "${spm}" \
        ${PYNXTOOLS_VERSION:+"pynxtools==${PYNXTOOLS_VERSION}"}

# Tools like Galaxy run the container with their own --user, which has no writable home.
ENV MPLCONFIGDIR=/tmp/matplotlib

COPY --chmod=0755 src/pynxtools_spm/docker/entrypoint.sh /usr/local/bin/entrypoint.sh

LABEL org.opencontainers.image.title="pynxtools-spm" \
      org.opencontainers.image.source="https://github.com/FAIRmat-NFDI/pynxtools-spm" \
      org.opencontainers.image.licenses="Apache-2.0" \
      org.opencontainers.image.version="${PYNXTOOLS_SPM_VERSION}"

ENTRYPOINT ["entrypoint.sh"]
CMD []
