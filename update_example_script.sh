#!/bin/sh

set -e
scpt_dir=$(dirname $0)
root_dir=$(dirname $scpt_dir)



# # STS Nanonis 5e
echo " !!! Converting Nanonis STS data !!! "
find ${root_dir}/tests/data/nanonis/sts/version_gen_5e_default_config -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXsts --reader spm --output sts_5e_default_config.nxs #--skip-verify
find ${root_dir}/tests/data/nanonis/sts/version_gen_5e_default_config -type f -name '*.nxs' | xargs mv sts_5e_default_config.nxs

find ${root_dir}/tests/data/nanonis/sts/version_gen_5e_with_described_nxdata -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXsts --reader spm --output sts_5e_with_described_nxdata.nxs #--skip-verify
find ${root_dir}/tests/data/nanonis/sts/version_gen_5e_with_described_nxdata -type f -name '*.nxs' | xargs mv sts_5e_with_described_nxdata.nxs

find ${root_dir}/tests/data/nanonis/sts/version_gen_5_with_described_nxdata -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXsts --reader spm --output sts_5_with_described_nxdata.nxs #--skip-verify
find ${root_dir}/tests/data/nanonis/sts/version_gen_5_with_described_nxdata -type f -name '*.nxs' | xargs mv sts_5_with_described_nxdata.nxs

STM Nanonis 4.5
find ${root_dir}/tests/data/nanonis/stm/version_gen_4_5_with_described_nxdata -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXstm --reader spm --output stm_4_5_with_described_nxdata.nxs
find ${root_dir}/tests/data/nanonis/stm/version_gen_4_5_with_described_nxdata -type f -name '*.nxs' | xargs mv stm_4_5_with_described_nxdata.nxs

# STM Nanonis 5e and 5
echo " !!! Converting Nanonis STM data !!! "

find ${root_dir}/tests/data/nanonis/stm/version_gen_5e_with_described_nxdata -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXstm --reader spm --output stm_5e_with_described_nxdata.nxs
find ${root_dir}/tests/data/nanonis/stm/version_gen_5e_with_described_nxdata -type f -name '*.nxs' | xargs mv stm_5e_with_described_nxdata.nxs

find ${root_dir}/tests/data/nanonis/stm/version_gen_5_with_described_nxdata -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXstm --reader spm --output stm_5_with_described_nxdata.nxs
find ${root_dir}/tests/data/nanonis/stm/version_gen_5_with_described_nxdata -type f -name '*.nxs' | xargs mv stm_5_with_described_nxdata.nxs

find ${root_dir}/tests/data/nanonis/stm/version_gen_5_with_default_config -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXstm --reader spm --output stm_5_with_default_config.nxs
find ${root_dir}/tests/data/nanonis/stm/version_gen_5_with_default_config -type f -name '*.nxs' | xargs mv stm_5_with_default_config.nxs

# STM Omicron
echo " !!! Converting Omicron STM data !!! "
find ${root_dir}/tests/data/omicron/stm/default_config -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXstm --reader spm --output omicron_stm_default_config.nxs
find ${root_dir}/tests/data/omicron/stm/default_config -type f -name '*.nxs' | xargs mv omicron_stm_default_config.nxs

# # # AFM Nanonis 4
echo " !!! Converting Nanonis AFM data !!! "
find ${root_dir}/tests/data/nanonis/afm/version_gen_4_default_config -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXafm --reader spm --output afm_4_with_default_config.nxs
find ${root_dir}/tests/data/nanonis/afm/version_gen_4_default_config -type f -name '*.nxs' | xargs mv afm_4_with_default_config.nxs

find ${root_dir}/tests/data/nanonis/afm/version_gen_4_with_described_nxdata -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXafm --reader spm --output afm_4_with_described_nxdata.nxs
find ${root_dir}/tests/data/nanonis/afm/version_gen_4_with_described_nxdata -type f -name '*.nxs' | xargs mv afm_4_with_described_nxdata.nxs

