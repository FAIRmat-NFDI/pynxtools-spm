#!/bin/bash

set -e

script_folder="$(dirname "${BASH_SOURCE[0]}")"
root_folder="$(dirname ${script_folder})"


docker run --rm --env HOME=/home/jovyan --mount type=bind,source=${root_folder},target=/home/jovyan \
            --entrypoint bash jupyter/scipy-notebook:2023-03-20 -c \
            "pip install pip-tools && \
             pip-compile --resolver=backtracking --upgrade --output-file requirements.txt requirements.in"
