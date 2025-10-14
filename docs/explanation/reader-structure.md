# Reader Structure
The reader orchestra of `pynxtools-spm` hosting multiple readers for `STS`, `STM` and `AFM` experiments. It is envisioned that in future more and more readers for other SPM techniques will be included in this package. The reader structure is designed in a modular way to make it easy to add new readers for other file formats and extend the existing readers.

## __`parsers` subpackage__
The aim of the parser modules to read the raw data files from various SPM file formats and convert the raw data path into slash separated hierarchical path. So, that the common function can build for all the file formats to read the raw data from the files. For reading the raw data into slash separated hierarchical path, we used several third party python package e.g.,  `spym` python package [ref] for reading `sm4` from `Omicron` or code from third party package like `nanonispy`. 
 TODO: Mention all parser should build `SPMBase` class from `base_parser` module.
Module structure of `parsers` subpackage:

```bash
--8<-- "included_file_content/subpackages_structure/parsers.txt"
```


## __`nxformatters` subpackage__
The aim of the formatter modules to curate the data from various SPM file formats and convert and store them in `Template[link_goes_here]`. So, that the `writer[link_goes_here]` can write the data NeXus format according to the NeXus application definitions for SPM techniques.

The `nxformatter` hosts modules `base_formatter`, `helpers` and nested subpackages for each SPM vendors (e.g., `nanonis`, `omicron`) with corresponding formatter modules for `STS`, `STM` and `AFM`.

Module structure of `nxformatters` subpackage:

```
--8<-- "included_file_content/subpackages_structure/nxformatters.txt"

```

The class `SPMformatter` in module `base_formatter` holding the common interface and methods for all the formatters, whereas the vendor specific base formatters (e.g., `NanonisBase`, `omicronBase` in the modules `nanonis_base` and `omicron_base` respectively) in a modules of corresponding subpackages. On top of this base classes, we developed specific methods to curate the unstructured data coming from the raw files and `ELN` yaml file flowing the instruction given in `config` file. 

## __`config` subpackage__
The `config` subpackage hosts some attribute config files for running the readers using those config files (not recommended because user may need modify some of the concepts). This config files can be considered as source for writing the custom config files for specific use cases.

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
