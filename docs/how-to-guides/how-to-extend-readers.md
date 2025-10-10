The `pynxtools-spm` reader package is designed in a modular way to make it easy to add new readers for file formats and extend the existing readers for newer file formats. Currently, the reader suite of `pynxtools-spm` hosts multiple readers for `STS`, `STM`, and `AFM` experiments. It is envisioned that in the future, more readers for diverse file formats of other SPM techniques will be included in this package.

## __Extend File Formats or Add New Techniques__

This is an open-source project, and any contribution to this project is welcome. Before proceeding with the steps below, please first read the [reader structure](../explanation/reader-structure.md) to understand the modular design of the reader package.

To include a new reader for a technique or extend the reader capability by including other file formats, follow the steps below:

__0.__ Clone and prepare the development environment for `pynxtools-spm` ([follow the installation guide](../tutorials/installation.md)).

__1.__ Go through the reader structure [here](../explanation/reader-structure.md) to understand the modular design of the reader package.

__2.__ Create a new parser module in the `parsers` subpackage to read the raw data files from the new SPM file format and convert the raw data path into a slash-separated hierarchical path. For reading the raw data into a slash-separated hierarchical path (see the `Raw Data File` section in [How to Interact with Reader](../how-to-guides/how-to-use-the-reader.md)), you can use a third-party Python package (if available for that file format) or build your own code to read the raw data from the files. All parsers should inherit from `SPMBase` class in the `base_parser` module (you may look at an existing module, e.g., `nanonis_sxm.py` or `nanonis_dat.py`).

__3.__ Create a new formatter module in the corresponding subpackage of the `nxformatters` subpackage. Always ensure that the new formatter class is built by inheriting a formater base class (e.g., `NanonisBase`, `OmicronBase` in the modules `nanonis_base` and `omicron_base`, respectively). By inheriting the base class, you can use existing methods or develop specific methods to curate the unstructured data coming from the raw files and the `ELN` YAML file, following the instructions given in the `config` file (please refer to one of the formatters, e.g., `nanonis_dat_sts`). Note that, in the data curation, formatter should strictly focus on [application definition](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/spm-structure.html#spm-structure) of the corresponding SPM technique.

If you are adding a new technique (e.g., scanning gate microscopy (SGM)), the prerequisite step is to develop an application definition in the [NeXus definitions repository](https://github.com/FAIRmat-NFDI/nexus_definitions). Please follow the documentation on [writing an application definition](https://fairmat-nfdi.github.io/pynxtools/how-tos/nexus/writing-an-appdef.html) or reach out to us for assistance.

__4.__ Run the converter to test your development. If the raw data is not properly curated according to the application definition, you will encounter warning messages. These warning messages indicate which data is missing or does not follow the correct conventions. Check your code, config file, ELN file, and the content of those files. Fix the issues one by one until all warning messages disappear. Please let us know if you need further assistance.

__5.__ Write test cases for your new parser and formatter modules. This is an easy but important part of the contribution process. Add your test cases to the `test_reader` module in `tests` and include only the necessary input files in the subdirectory of the `data` directory.

__6.__ Create a pull request (PR) to include your contributions in the main branch of the `pynxtools-spm` repository. You may create the PR as a draft while development is ongoing and keep us in the discussion loop.

__7.__ We will review your code and provide feedback. Once all changes are finalized, we will merge your code into the main branch of the `pynxtools-spm` repository and release a new version of the package, including your contributions.