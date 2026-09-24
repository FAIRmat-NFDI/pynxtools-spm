

```python
# With spm file
file = "./del_dev_folder/VGEP-15m-.0_00000.spm"
from pynxtools_spm.parsers.bruker_spm import SpmBruker
data_dict = SpmBruker(file).parse()
writing_file = "./del_dev_folder/data_keys.txt"

with open(writing_file, mode="r+") as f:
    for key, val in data_dict.items():
        if isinstance(val, str):
            f.write(f'{key}: {val}\n')
        else:
            f.write(f'{key}: <array data>\n')


from pynxtools_spm.parsers.bruker.bruker_spm import pySPMBruker
spm_obj = pySPMBruker(file, encoding=encoding)
```


```python
# TXT file
file = "./del_dev_folder/SB04-MG1.0_00000.spm.txt"

from pynxtools_spm.parsers.bruker_txt import TxtBruker


data_dict = TxtBruker(file_path=file).parse()

file_write = "./del_dev_folder/txt_file_data_keys.txt"
with open(file_write, mode="r+") as f:
    for key, val in data_dict.items():
        if isinstance(val, str):
            f.write(f'{key}: {val}\n')
    else:
        f.write(f'{key}: <array data>\n')

```

