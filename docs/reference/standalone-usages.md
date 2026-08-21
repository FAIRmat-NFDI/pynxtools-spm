# Standalone Usages
`pynxtools-spm` is a tool for converting content from a raw data file and user provided data to the NeXus file according to the NeXus application definitions for SPM techniques.

One can use [NOMAD](https://nomad-lab.eu/) (see how to upload in NOMAD [documentation](../tutorials/use-reader-in-nomad.md)) research data management system (RMD) to upload the raw data files or command in terminal (needs `pynxtools-spm` installed in your local Python environment, see [installation guide](../tutorials/installation.md)) to convert the raw data files into NeXus file.

## __Convert Data__
After installing `pynxtools-spm` package, one can use the command line interface (CLI) to convert the raw data files into NeXus file. (see all available options by `pynx convert --help`).

To convert the raw data files from various techniques, use a command similar to the following -

```bash
$ pynx convert --nxdl NXstm --reader SPM  --output output_file.nxs  <list of the input files>
```

__1.__ Command to convert a STS raw data file into NeXus file
```bash
$ pynx convert --nxdl NXsts --reader spm --output output.nxs eln_data.yaml nanonis_sts_file.dat config.json
```
Download and try with [STS example files](../assets/command_line_examples/sts.zip){:sts} or visit the [GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/nanonis/sts/version_gen_5_with_described_nxdata).

__2.__ Command to convert a STM raw data file into NeXus file
```bash
$ pynx convert --nxdl NXstm --reader spm --output output.nxs eln_data.yaml nanonis_stm_file.sxm config.json
```

Download and try with [STM example files](../assets/command_line_examples/stm.zip){:stm} or visit the [GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/nanonis/stm/version_gen_5_with_described_nxdata).

__3.__ Command to convert a Nanonis AFM raw data file (`.sxm`, Nanonis generic version 4) into NeXus file
```bash
$ pynx convert --nxdl NXafm --reader spm --output output.nxs eln_data.yaml nanonis_afm_file.sxm config.json
```

Download and try with [AFM example files](../assets/command_line_examples/afm.zip){:afm} or visit the [GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/nanonis/afm/version_gen_4_with_described_nxdata).

__4.__ Command to convert a Bruker AFM raw data file (`.FLT`, written by `SPMLab` version `1.00`) into NeXus file
```bash
$ pynx convert --nxdl NXafm --reader spm --output output.nxs eln_data.yaml bruker_afm_file.FLT config.json
```

Visit the [GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/bruker/afm/flt_described_config) for an example `.FLT` file with its config and ELN file.

!!! note
    A Bruker `SPMLab` FLT file contains one channel of one scan direction (e.g. `B3320_13_061726074638.SIG_TOPO_FRW.FLT` is the forward height image), so each file is converted into its own NeXus file. The config file may be omitted, in which case the default config `configs/bruker/bruker_flt_afm.json` shipped with the package is used.