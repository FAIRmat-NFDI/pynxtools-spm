#!/bin/bash

# Copy test examples from test folder to assets/command_line_examples

set -e

this_file_path=$(dirname $(dirname $(realpath "$0")))

# Copy STS file
src_path="${this_file_path}/tests/data/nanonis/sts/version_gen_5_with_described_nxdata"
sts_dst="./docs/assets/command_line_examples/sts"
mkdir -p $sts_dst


# remove all the files from dst folder if it has anything in it
rm -rf $sts_dst/*
# ignore the .nxs files while copying
cp -r $src_path/* $sts_dst/
rm -f $sts_dst/*.nxs

# create a zip file in the sts_dst
zip -jrm "$(dirname ${sts_dst})/sts.zip" "${sts_dst}/"
rm -r ${sts_dst}

# Copy STM file
src_path="${this_file_path}/tests/data/nanonis/stm/version_gen_5_with_described_nxdata"
stm_dst="./docs/assets/command_line_examples/stm"
mkdir -p $stm_dst

# remove all the files from dst folder if it has anything in it
rm -rf $stm_dst/*
cp -r $src_path/* $stm_dst/
rm -f $stm_dst/*.nxs

# create zip file and remove the stm folder
zip -jrm "$(dirname ${stm_dst})/stm.zip" "${stm_dst}/"
rm -rf ${stm_dst}

# Copy AFM file
src_path="${this_file_path}/tests/data/nanonis/afm/version_gen_4_with_described_nxdata"
afm_dst="./docs/assets/command_line_examples/afm"
mkdir -p $afm_dst

# remove all the files from dst folder if it has anything in it
rm -rf ${afm_dst}/*
cp -r $src_path/* $afm_dst/
rm -f $afm_dst/*.nxs

# create zip file and remove the afm folder
zip -jrm "$(dirname ${afm_dst})/afm.zip" ${afm_dst}
rm -r ${afm_dst}
# Copy Omicron STM file
src_path="${this_file_path}/tests/data/omicron/stm/default_config"
omicron_dst="./docs/assets/command_line_examples/omicron"
mkdir -p $omicron_dst

# remove all the files from dst folder if it has anything in it
rm -rf ${omicron_dst}/*
cp -r $src_path/* $omicron_dst/
rm -f $omicron_dst/*.nxs

# create zip file and remove the omicron folder
zip -jrm "$(dirname ${omicron_dst})/omicron.zip" ${omicron_dst}
rm -rf ${omicron_dst}

# Copy Bruker AFM file
src_path="${this_file_path}/tests/data/bruker/afm/flt_described_config"
bruker_dst="./docs/assets/command_line_examples/bruker_afm"
mkdir -p $bruker_dst

# remove all the files from dst folder if it has anything in it
rm -rf ${bruker_dst}/*
cp -r $src_path/* $bruker_dst/
rm -f $bruker_dst/*.nxs

# create zip file and remove the bruker_afm folder
zip -jrm "$(dirname ${bruker_dst})/bruker_afm.zip" ${bruker_dst}
rm -rf ${bruker_dst}

# Copy Bruker NanoScope force-curve (.spm.txt) file. The export is pure ASCII,
# so the bundle is complete and the documented command runs straight from it.
src_path="${this_file_path}/tests/data/bruker/afm/txt_default_config"
bruker_txt_dst="./docs/assets/command_line_examples/bruker_txt"
mkdir -p $bruker_txt_dst

# remove all the files from dst folder if it has anything in it
rm -rf ${bruker_txt_dst}/*
cp -r $src_path/* $bruker_txt_dst/
rm -f $bruker_txt_dst/*.nxs

# create zip file and remove the bruker_txt folder
zip -jrm "$(dirname ${bruker_txt_dst})/bruker_txt.zip" ${bruker_txt_dst}
rm -rf ${bruker_txt_dst}

# Copy Bruker NanoScope (.spm) metadata. A .spm file is dominated by its binary
# image block (16 MB for this one), so the binary part is deliberately excluded:
# only the human-readable ASCII header (up to and including '\*File list end')
# is shipped, as a preview of the metadata the reader sees.
src_path="${this_file_path}/tests/data/bruker/afm/default_config"
bruker_spm_dst="./docs/assets/command_line_examples/bruker_spm"
mkdir -p $bruker_spm_dst

# remove all the files from dst folder if it has anything in it
rm -rf ${bruker_spm_dst}/*
cp $src_path/eln_data.yaml $bruker_spm_dst/

for spm_file in "$src_path"/*.spm; do
    header_file="${bruker_spm_dst}/$(basename "$spm_file").header.txt"
    # Everything before the binary block; '\*File list end' terminates the header.
    sed -n '1,/^\\\*File list end/p' "$spm_file" > "$header_file"
done

# create zip file and remove the bruker_spm folder
zip -jrm "$(dirname ${bruker_spm_dst})/bruker_spm.zip" ${bruker_spm_dst}
rm -rf ${bruker_spm_dst}
