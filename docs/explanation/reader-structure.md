# Reader Structure
`pynxtools-spm` hosts multiple readers for `STS`, `STM` and `AFM` experiments. It is envisioned that in the future more and more readers for other SPM techniques will be included in this package. The reader structure is designed in a modular way to make it easy to add new readers for other new techniques (e.g., Spin-Polarized STM) and extend the existing readers.

## __`parsers` Subpackage__
The aim of the parser module is to read the raw data files from various SPM file formats and convert the raw data path into a slash-separated hierarchical path. This allows to build common function for all the file formats to read the raw data from the files. For reading the raw data into slash separated hierarchical path, we used third party python package e.g.,  [spym](https://github.com/rescipy-project/spym) python package for reading `.sm4` file from `Omicron` or code from third party open source package like [nanonispy](https://github.com/underchemist/nanonispy). 
Module structure of `parsers` subpackage:

```bash
--8<-- "included_file_content/subpackages_structure/parsers.txt"
```


## __`nxformatters` Subpackage__
The aim of the formatter modules to curate the data from various SPM file formats, and convert and store them in `pynxtools` [Template](https://github.com/FAIRmat-NFDI/pynxtools/blob/master/src/pynxtools/dataconverter/template.py). `pynxtools` [writer](https://github.com/FAIRmat-NFDI/pynxtools/blob/master/src/pynxtools/dataconverter/template.py) can write the data from Template to NeXus format according to the NeXus application definitions for SPM techniques.

The `nxformatter` hosts modules `base_formatter`, `helpers` and nested subpackages for each SPM vendors (e.g., `nanonis`, `omicron`) with corresponding formatter modules for `STS`, `STM` and `AFM`.

Module structure of `nxformatters` subpackage:

```
--8<-- "included_file_content/subpackages_structure/nxformatters.txt"

```

The class `SPMformatter` in module `base_formatter` holds the common interface and methods for all the formatters, whereas the vendor-specific base formatters (e.g., `NanonisBase`, `omicronBase` in the modules `nanonis_base` and `omicron_base` respectively) holds common methods and variables for its species. On top of this base classes, we developed specific methods to curate the unstructured data coming from the raw files and `ELN` yaml file following the instruction given in the `config` file. 

## __`config` subpackage__
The `config` subpackage hosts some config files for running the readers without providing user-specific configurations (not recommended because user may need to modify some of the concepts according to the requirements of experiment labs). These config files can be considered as a source of writing the custom config files for specific use cases.

Module structure of `config` subpackage:

```
--8<-- "included_file_content/subpackages_structure/configs.txt"

```

## __`nomad` subpackage__
The `nomad` subpackage hosts module for nomad entry points in the `entrypoints` module and examples in the `examples` directory. The modules `nomad_example_paths` keep the example paths to be used in `entrypoints` module.

Module structure of `nomad` subpackage:

```
--8<-- "included_file_content/subpackages_structure/nomad.txt"
```
