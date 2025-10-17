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