- parser test:
```python
file = "./del_dev_folder/VGEP-15m-.0_00000.spm"
from pynxtools_spm.parsers.bruker_spm import SpmBruker
data_dict = SpmBruker(file).parse()
writing_file = "data_keys.txt"

with open(writing_file, mode="r+") as f:
    for key, val in data_dict.items():
        if isinstance(val, str):
            f.write(f'{key}: {val}\n')


from pynxtools_spm.parsers.bruker.bruker_spm import SPMBruker
spm_obj = SPMBruker(file, encoding=encoding)
```

