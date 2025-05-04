#! /bin/bash

# Stop on error
set -e

current_dir=$(pwd)
uploader_script="/home/rubel/NOMAD-FAIRmat/nomad-distro-dev-RM/packages/pynxtools-spm/src/pynxtools_spm/nomad_uploader/example_upload_script.py"
venv="/home/rubel/NOMAD-FAIRmat/nomad-distro-dev-RM/.venv"
python_3="$venv/bin/python3"
echo "Running uploader script..."
"$python_3" "$uploader_script" > "$current_dir/debug.txt" 2>&1
echo "Uploader script finished. Check debug.txt for details."