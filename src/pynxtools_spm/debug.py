from pynxtools.dataconverter.convert import convert 
from pathlib import Path
import os
module_dir = Path(__file__).resolve().parent
stm_raw = f"{module_dir}/../../tests/data/nanonis/sts/version_gen_5e_with_described_nxdata/STS_nanonis_generic_5e_1.dat"  # tests/data/nanonis/stm/version_gen_4_5_with_described_nxdata/STM_nanonis_generic_4_5.sxm"

config = f"{module_dir}/../../tests/data/nanonis/sts/version_gen_5e_with_described_nxdata/config.json"
eln = f"{module_dir}/../../tests/data/nanonis/sts/version_gen_5e_with_described_nxdata/eln_data.yaml"
nxdl = "NXsts"
reader_name = "spm"
stm_raw = Path(stm_raw).resolve()
if not stm_raw.exists():
    raise FileNotFoundError(stm_raw)
if not os.path.exists(eln):
    raise FileNotFoundError(eln)



if __name__ == "__main__":
    convert(nxdl=nxdl, reader=reader_name, input_file=tuple(map(str, (stm_raw, config, eln))), output='stm.nxs')