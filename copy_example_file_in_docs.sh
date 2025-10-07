#!/bin/bash

this_file_path=$(dirname $(realpath "$0"))

# # Copy sts file
src_path="${this_file_path}/tests/data/nanonis/sts/version_gen_5_with_described_nxdata"
sts_dst="./docs/assets/copy_files_to_examples_in_docs/sts"
mkdir -p $sts_dst


# remove all the files from dst folder if it has anything in it
rm -rf $sts_dst/*
# ignore the .nxs files while copying
cp -r $src_path/* $sts_dst/
rm -f $sts_dst/*.nxs

# create a zip file in the sts_dst
zip -r "sts.zip" "${sts_dst}/"

# Copy stm file
src_path="${this_file_path}/tests/data/nanonis/stm/version_gen_5_with_described_nxdata"
stm_dst="./docs/assets/copy_files_to_examples_in_docs/stm"
mkdir -p $stm_dst

# remove all the files from dst folder if it has anything in it
rm -rf $stm_dst/*
cp -r $src_path/* $stm_dst/
rm -f $stm_dst/*.nxs

# create a zip file in the stm_dst
zip -r "stm.zip" "${stm_dst}/*"

# Copy afm file
src_path="${this_file_path}/tests/data/nanonis/afm/version_gen_4_with_described_nxdata"
afm_dst="./docs/assets/copy_files_to_examples_in_docs/afm"
mkdir -p $afm_dst

# remove all the files from dst folder if it has anything in it
rm -rf $afm_dst/*
cp -r $src_path/* $afm_dst/
rm -f $afm_dst/*.nxs

# create a zip file in the afm_dst
zip -r "afm.zip" "${afm_dst}/"
