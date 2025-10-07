The reader orchestra of `pynxtools-spm` hosting multiple readers for `STS`, `STM` and `AFM` experiments. It is envisioned that in future more and more readers for other SPM techniques will be included in this package. The reader structure is designed in a modular way to make it easy to add new readers for other file formats and extend the existing readers.

## __`parsers` subpackage__
The aim of the parser modules to read the raw data files from various SPM file formats and convert the raw data path into slash separated hierarchical path. So, that the common function can build for all the file formats to read the raw data from the files. For reading the raw data into slash separated hierarchical path, we used several third party python package e.g.,  `spym` python package [ref] for reading `sm4` from `Omicron` or code from third party package like `nannispy`. 
 TODO: Mention all parser should build `SPMBase` class from `base_parser` module.
Module structure of `parsers` subpackage:

```
./parsers/
├── base_parser.py
├── helpers.py
├── __init__.py
├── nanonis_dat.py
├── nanonispy
│   ├── constants.py
│   ├── __init__.py
│   ├── README.md
│   ├── read.py
│   └── utils.py
├── nanonis_sxm.py
└── omicron_sm4.py
```

## __`nxformatters` subpackage__
The aim of the formatter modules to curate the data from various SPM file formats and convert and store them in `Template[link_goes_here]`. So, that the `writer[link_goes_here]` can write the data NeXus format according to the NeXus application definitions for SPM techniques.

The `nxformatter` hosts modules `base_formatter`, `helpers` and nested subpackages for each SPM vendors (e.g., `nanonis`, `omicron`) with correspding formatter modules for `STS`, `STM` and `AFM`.

Module structure of `nxformatters` subpackage:

```
./nxformatters/
├── base_formatter.py
├── helpers.py
├── __init__.py
├── nanonis
│   ├── __init__.py
│   ├── nanonis_base.py
│   ├── nanonis_dat_sts.py
│   ├── nanonis_sxm_afm.py
│   └── nanonis_sxm_stm.py
└── omicron
    ├── __init__.py
    ├── omicron_base.py
    └── omicron_sm4_stm.py
```

The class `SPMformatter` in module `base_formatter` holding the common interface and methods for all the formatters, whereas the vendor specific base formatters (e.g., `NanonisBase`, `omicronBase` in the modules `nanonis_base` and `omicron_base` repectively) in a modules of corresponding subpackages. On top of this base classes, we developed specific methods to curate the unstructure data coming from the raw files and `ELN` yaml file flowing the instruction given in `config` file. 

## __`config` subpackage__
The `config` subpackage hosts some default config files for running the readers using those config files (not recommended becuase user may need modify some of the concepts). This config files can be considered as source for writing the custom config files for specific use cases.

Module structure of `config` subpackage:

```
./configs/
├── __init__.py
├── nanonis
│   ├── nanonis_dat_generic_sts.json
│   ├── nanonis_sxm_generic_afm.json
│   └── nanonis_sxm_generic_stm.json
└── omicron
    └── omicron_sm4_stm.json
```

## __`nomad` subpackage__
The `nomad` subpackage hosts module for nomad entry points in the `entrypoints` module and examples in the `examples` directory. The modules `nomad_example_paths` keep the example paths to be used in `entrypoints` module.

Module structure of `nomad` subpackage:

```
./nomad/
├── entrypoints.py
├── examples
│   ├── afm
│   ├── stm
│   └── sts
└── nomad_example_paths.py
```
