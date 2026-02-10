#! /bin/bash

# Stop on error
set -e

current_dir=$(dirname $(realpath $0))
echo "Current directory: $current_dir"
uploader_script="$current_dir/example_upload_script.py"
venv="/home/rubel/NOMAD-FAIRmat/GH/pynxtools-spm/.venv"
python_3="$venv/bin/python3"
echo "Running uploader script..."
"$python_3" "$uploader_script" > "$current_dir/debug.txt" 2>&1
echo "Uploader script finished. Check debug.txt for details."