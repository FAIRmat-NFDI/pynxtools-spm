#!/bin/bash
READER=spm

# Function to update log
function update_log {
  local FOLDER=$1
  local NXDL=$2
  local lowercase_NXDL=$(echo "$NXDL" | tr '[:upper:]' '[:lower:]')
  local ref_file="ref_nexus.log"
  log_filename="${FOLDER}/${ref_file}"
  echo "Generating log file at $log_filename..."
  python -c "
import os
from pynxtools.testing.nexus_conversion import get_log_file
folder = os.path.join(os.getcwd(), 'tests', 'data', '$FOLDER')
nxs_filepath = os.path.join(folder,'output.nxs')
log_filepath = os.path.join(folder,'$log_filename')
get_log_file(nxs_filepath, log_filepath, './')
"
  echo "Done!"
  echo
}

function update_log_file {
  local FOLDER=$1
  local NXDL=$2
  cd $FOLDER || exit
  echo "Update $FOLDER reference log for $NXDL"
  files=$(find . -type f \( ! -name "*.log" -a ! -name "*.nxs" \))
  dataconverter ${files[@]} --reader $READER --nxdl $NXDL --ignore-undocumented
  cd ../../.. || exit
  update_log "$FOLDER" "$NXDL"
  find $FOLDER -type f -name "output.nxs" | xargs rm 
}

project_dir=$(dirname $(dirname $(realpath $0)))

folders=(
  "${project_dir}/tests/data/nanonis/afm/version_gen_4_default_config"
  "${project_dir}/tests/data/nanonis/afm/version_gen_4_with_described_nxdata"
)

nxdls=(
  "NXafm"
)

for folder in "${folders[@]}"; do
  for nxdl in "${nxdls[@]}"; do
    cd $folder
    update_log_file "$folder" "$nxdl"
  done
done

folders=(
  "${project_dir}/tests/data/omicron/stm/default_config"
  "${project_dir}/tests/data/nanonis/stm/version_gen_5_with_default_config"
  "${project_dir}/tests/data/nanonis/stm/version_gen_5_with_described_nxdata"
  "${project_dir}/tests/data/nanonis/stm/version_gen_5e_with_described_nxdata"
)

nxdls=(
  "NXstm"
)

for folder in "${folders[@]}"; do
  for nxdl in "${nxdls[@]}"; do
    cd $project_dir/tests/data
    update_log_file "$folder" "$nxdl"
  done
done

folders=(
  "${project_dir}/tests/data/nanonis/sts/version_gen_5e_default_config"
  "${project_dir}/tests/data/nanonis/sts/version_gen_5e_with_described_nxdata"
  "${project_dir}/tests/data/nanonis/sts/version_gen_5_with_described_nxdata"
)

nxdls=(
  "NXsts"
)

for folder in "${folders[@]}"; do
  for nxdl in "${nxdls[@]}"; do
    cd $project_dir/tests/data
    update_log_file "$folder" "$nxdl"
  done
done