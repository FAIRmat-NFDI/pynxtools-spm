The unltimate goal of the `pynxtools-spm` reader package is to convert the content from a raw data file and user provided data to the NeXus file according to the NeXus application definitions for SPM techniques.

One can use [NOMAD](https://nomad-lab.eu/) (see how to upload in NOMAD [documentation](../tutorials/reader-use-in-nomad.md)) RMD to upload the raw data files or command in termainal (needs `pynxtools-spm` installed in your local python environment, see [installation guide](../tutorials/installation.md)) to convert the raw data files into NeXus file.

## __Convert Data__
After installating `pynxtools-spm` package, one can use the command line interface (CLI) to convert the raw data files into NeXus file. (see all available options by `dataconverter --help`).

In common to convert the raw data files from various techniques, one need to call something like the following command -

```bash
$ dataconverter --nxdl NXstm --reader SPM  --output output_file.nxs  <list of the input files>
```

__1.__ Command to convert the STS raw data files into NeXus file
```bash
$ dataconverter --nxdl NXsts --reader spm --output output.nxs eln_data.yaml nanonis_sts_file.dat config.json
```
Try with [STS example files](../assets/copy_files_to_examples_in_docs/sts.zip){:sts}.

__2.__ Command to convert the STM raw data files into NeXus file
```bash
$ dataconverter --nxdl NXstm --reader spm --output output.nxs eln_data.yaml nanonis_stm_file.sxm config.json
```

Try with [STM example files](../assets/copy_files_to_examples_in_docs/stm.zip){:stm}.

__3.__ Command to convert the AFM raw data files into NeXus file
```bash
$ dataconverter --nxdl NXafm --reader spm --output output.nxs eln_data.yaml nanonis_afm_file.sxm config.json
```

Try with [AFM example files](../assets/copy_files_to_examples_in_docs/afm.zip){:afm}.