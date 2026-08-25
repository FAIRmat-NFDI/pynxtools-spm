#!/bin/sh

# Update nexus file in tests/data directory

set -e
scpt_dir=$(dirname $0)
root_dir=$(dirname $scpt_dir)

# STS Nanonis 5e
echo " !!! Converting Nanonis STS data !!! "
find ${root_dir}/tests/data/nanonis/sts/version_gen_5e_default_config -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXsts --reader spm --output sts_5e_default_config.nxs #--skip-verify
find ${root_dir}/tests/data/nanonis/sts/version_gen_5e_default_config -type f -name '*.nxs' | xargs mv sts_5e_default_config.nxs

find ${root_dir}/tests/data/nanonis/sts/version_gen_5e_with_described_nxdata -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXsts --reader spm --output sts_5e_with_described_nxdata.nxs #--skip-verify
find ${root_dir}/tests/data/nanonis/sts/version_gen_5e_with_described_nxdata -type f -name '*.nxs' | xargs mv sts_5e_with_described_nxdata.nxs

find ${root_dir}/tests/data/nanonis/sts/version_gen_5_with_described_nxdata -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXsts --reader spm --output sts_5_with_described_nxdata.nxs #--skip-verify
find ${root_dir}/tests/data/nanonis/sts/version_gen_5_with_described_nxdata -type f -name '*.nxs' | xargs mv sts_5_with_described_nxdata.nxs

# STM Nanonis 5e and 5
echo " !!! Converting Nanonis STM data !!! "

find ${root_dir}/tests/data/nanonis/stm/version_gen_5e_with_described_nxdata -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXstm --reader spm --output stm_5e_with_described_nxdata.nxs
find ${root_dir}/tests/data/nanonis/stm/version_gen_5e_with_described_nxdata -type f -name '*.nxs' | xargs mv stm_5e_with_described_nxdata.nxs

find ${root_dir}/tests/data/nanonis/stm/version_gen_5_with_described_nxdata -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXstm --reader spm --output stm_5_with_described_nxdata.nxs
find ${root_dir}/tests/data/nanonis/stm/version_gen_5_with_described_nxdata -type f -name '*.nxs' | xargs mv stm_5_with_described_nxdata.nxs

find ${root_dir}/tests/data/nanonis/stm/version_gen_5_with_default_config -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXstm --reader spm --output stm_5_with_default_config.nxs
find ${root_dir}/tests/data/nanonis/stm/version_gen_5_with_default_config -type f -name '*.nxs' | xargs mv stm_5_with_default_config.nxs

# STM Omicron
echo " !!! Converting Omicron STM data !!! "
find ${root_dir}/tests/data/omicron/stm/default_config -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXstm --reader spm --output omicron_stm_default_config.nxs
find ${root_dir}/tests/data/omicron/stm/default_config -type f -name '*.nxs' | xargs mv omicron_stm_default_config.nxs

# AFM Nanonis 4
echo " !!! Converting Nanonis AFM data !!! "
find ${root_dir}/tests/data/nanonis/afm/version_gen_4_default_config -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXafm --reader spm --output afm_4_with_default_config.nxs
find ${root_dir}/tests/data/nanonis/afm/version_gen_4_default_config -type f -name '*.nxs' | xargs mv afm_4_with_default_config.nxs

find ${root_dir}/tests/data/nanonis/afm/version_gen_4_with_described_nxdata -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXafm --reader spm --output afm_4_with_described_nxdata.nxs
find ${root_dir}/tests/data/nanonis/afm/version_gen_4_with_described_nxdata -type f -name '*.nxs' | xargs mv afm_4_with_described_nxdata.nxs

# AFM Bruker SPMLab (.FLT)
echo " !!! Converting Bruker SPMLab AFM (.FLT) data !!! "
flt_dir=${root_dir}/tests/data/bruker/afm/flt_default_config
find ${flt_dir} -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXafm --reader spm --output ${flt_dir}/afm_flt_default_config.nxs

echo " !!! Converting Bruker SPMLab AFM (.FLT) data with a described config !!! "
flt_desc_dir=${root_dir}/tests/data/bruker/afm/flt_described_config
find ${flt_desc_dir} -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXafm --reader spm --output ${flt_desc_dir}/afm_flt_described_config.nxs

# AFM Bruker
echo " !!! Converting Bruker AFM data !!! "
find ${root_dir}/tests/data/bruker/afm/default_config -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXafm --reader spm --output afm_default_config.nxs
find ${root_dir}/tests/data/bruker/afm/default_config -type f -name '*.nxs' | xargs mv afm_default_config.nxs

# AFM single point spectroscopy
echo " !!! Converting Bruker AFM single point spectroscopy data !!! "
find ${root_dir}/tests/data/bruker/afm/txt_default_config -type f ! -name '*.nxs' | xargs pynx convert --nxdl NXafm --reader spm --output afm_txt_default_config.nxs
find ${root_dir}/tests/data/bruker/afm/txt_default_config -type f -name '*.nxs' | xargs mv afm_txt_default_config.nxs
