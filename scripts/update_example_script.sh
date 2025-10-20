#!/bin/sh

# Update nexus file in tests/data directory

set -e
scpt_dir=$(dirname $0)
root_dir=$(dirname $scpt_dir)

# # STS Nanonis 5e
echo " !!! Converting Nanonis STS data !!! "

sts_5e_default_config=${root_dir}/tests/data/nanonis/sts/version_gen_5e_default_config
find $sts_5e_default_config -type f ! \( -name '*.log -o -name *.nxs' \) | xargs dataconverter --nxdl NXsts --reader spm --output ${sts_5e_default_config}/output.nxs #--skip-verify
read_nexus -f $sts_5e_default_config/output.nxs > ${sts_5e_default_config}/ref_nexus.log 2>&1
rm ${sts_5e_default_config}/output.nxs

sts_5e_with_described_nxdata=${root_dir}/tests/data/nanonis/sts/version_gen_5e_with_described_nxdata
find ${sts_5e_with_described_nxdata} -type f ! \( -name '*.nxs' -o -name '*.log' \) | xargs dataconverter --nxdl NXsts --reader spm --output ${sts_5e_with_described_nxdata}/output.nxs #--skip-verify
read_nexus -f ${sts_5e_with_described_nxdata}/output.nxs > ${sts_5e_with_described_nxdata}/ref_nexus.log 2>&1
rm ${sts_5e_with_described_nxdata}/output.nxs

sts_5_with_described_nxdata=${root_dir}/tests/data/nanonis/sts/version_gen_5_with_described_nxdata
find ${sts_5_with_described_nxdata} -type f ! \( -name '*.nxs' -o -name '*.log' \) | xargs dataconverter --nxdl NXsts --reader spm --output ${sts_5_with_described_nxdata}/output.nxs #--skip-verify
read_nexus -f ${sts_5_with_described_nxdata}/output.nxs > ${sts_5_with_described_nxdata}/ref_nexus.log 2>&1
rm ${sts_5_with_described_nxdata}/output.nxs

# STM Nanonis 5e and 5
echo " !!! Converting Nanonis STM data !!! "

stm_5e_with_described_nxdata=${root_dir}/tests/data/nanonis/stm/version_gen_5e_with_described_nxdata
find ${stm_5e_with_described_nxdata} -type f ! \( -name '*.nxs' -o -name '*.log' \) | xargs dataconverter --nxdl NXstm --reader spm --output ${stm_5e_with_described_nxdata}/output.nxs
read_nexus -f ${stm_5e_with_described_nxdata}/output.nxs > ${stm_5e_with_described_nxdata}/ref_nexus.log 2>&1
rm ${stm_5e_with_described_nxdata}/output.nxs

stm_5_with_described_nxdata=${root_dir}/tests/data/nanonis/stm/version_gen_5_with_described_nxdata
find ${stm_5_with_described_nxdata} -type f ! \( -name '*.nxs' -o -name '*.log' \) | xargs dataconverter --nxdl NXstm --reader spm --output ${stm_5_with_described_nxdata}/output.nxs
read_nexus -f ${stm_5_with_described_nxdata}/output.nxs > ${stm_5_with_described_nxdata}/ref_nexus.log 2>&1
rm ${stm_5_with_described_nxdata}/output.nxs

stm_5_with_default_config=${root_dir}/tests/data/nanonis/stm/version_gen_5_with_default_config
find ${stm_5_with_default_config} -type f ! \( -name '*.nxs' -o -name '*.log' \) | xargs dataconverter --nxdl NXstm --reader spm --output ${stm_5_with_default_config}/output.nxs
read_nexus -f ${stm_5_with_default_config}/output.nxs > ${stm_5_with_default_config}/ref_nexus.log 2>&1
rm ${stm_5_with_default_config}/output.nxs


# STM Omicron
echo " !!! Converting Omicron STM data !!! "

afm_default_config=${root_dir}/tests/data/omicron/stm/default_config

find ${afm_default_config} -type f ! \( -name '*.nxs' -o -name '*.log' \) | xargs dataconverter --nxdl NXstm --reader spm --output ${afm_default_config}/output.nxs
read_nexus -f ${afm_default_config}/output.nxs > ${afm_default_config}/ref_nexus.log 2>&1
rm ${afm_default_config}/output.nxs


# # # # AFM Nanonis 4
echo " !!! Converting Nanonis AFM data !!! "

afm_4_with_default_config=${root_dir}/tests/data/nanonis/afm/version_gen_4_default_config
find ${afm_4_with_default_config} -type f ! \( -name '*.nxs' -o -name '*.log' \) | xargs dataconverter --nxdl NXafm --reader spm --output ${afm_4_with_default_config}/output.nxs
read_nexus -f ${afm_4_with_default_config}/output.nxs > ${afm_4_with_default_config}/ref_nexus.log 2>&1
rm ${afm_4_with_default_config}/output.nxs

afm_4_with_described_nxdata=${root_dir}/tests/data/nanonis/afm/version_gen_4_with_described_nxdata
find ${afm_4_with_described_nxdata} -type f ! \( -name '*.nxs' -o -name '*.log' \) | xargs dataconverter --nxdl NXafm --reader spm --output ${afm_4_with_described_nxdata}/output.nxs
read_nexus -f ${afm_4_with_described_nxdata}/output.nxs > ${afm_4_with_described_nxdata}/ref_nexus.log 2>&1
rm ${afm_4_with_described_nxdata}/output.nxs
