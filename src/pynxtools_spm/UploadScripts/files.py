#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Modules to handle files."""

from dataclasses import dataclass
from pathlib import Path
import os
import shutil
from typing import Optional


@dataclass
class Dir:
    full_path: Path
    parent_dir: str


@dataclass
class File:
    full_path: Path
    file: str
    ext: str
    base: str
    parent_dir: Dir


# Copy create an script that copies a directory structure from source to destination directory
def copy_directory_structure(
    src: Path, dst: Path, extension: Optional[str], run_action_on_files=None
):
    """
    Copies a directory structure from source to destination directory
    only with the files having a specific extension.

    :param src: Source directory path
    :param dst: Destination directory path
    :param extension: File extension to filter by
    """
    if not src.is_dir():
        raise ValueError(f"Source {src} is not a directory")
    if not dst.is_dir():
        raise ValueError(f"Destination {dst} is not a directory")

    for root, dirs, files in os.walk(src):
        if files:
            for file in files:
                if extension:
                    if not file.endswith(extension):
                        continue

                src_file = Path(root) / file
                dest_file = dst / file
                shutil.copy2(src_file, dest_file)
                if run_action_on_files is not None:
                    run_action_on_files(dest_file)

        if dirs:
            for dir_ in dirs:
                nested_dir = dst / dir_
                os.makedirs(nested_dir, exist_ok=True)
                copy_directory_structure(src / dir_, nested_dir, extension)
