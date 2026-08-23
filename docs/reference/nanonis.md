# Data from Nanonis instruments

The reader supports `.dat` (spectroscopy) and `.sxm` (scan image) files written by the
[Nanonis](https://www.specs-group.com/nanonis/products/) SPM control software of
SPECS Surface Nano Analysis GmbH. The `.dat` files are converted into
[NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html),
while `.sxm` files are converted into
[NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html)
or [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html),
depending on the `experiment_technique` given in the ELN file.

Both file formats are read with the vendored
[nanonispy](https://github.com/underchemist/nanonispy) package in
[`src/pynxtools_spm/parsers/`](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/src/pynxtools_spm/parsers)
(`nanonis_dat.py` with the class `DatGenericNanonis`, and `nanonis_sxm.py` with the class
`SxmGenericNanonis`).

## Supported formats and versions

The version refers to the generation of the Nanonis SPM control software (the *generic*
version), not to the `:NANONIS_VERSION:` entry in the file header.

| Technique | Extension | Software | Tested versions | Formatter | Default config |
| --- | --- | --- | --- | --- | --- |
| `STS` | `.dat` | Nanonis SPM control software | Generic 5, Generic 5e | `NanonisDatSTS` | `configs/nanonis/nanonis_dat_generic_sts.json` |
| `STM` | `.sxm` | Nanonis SPM control software | Generic 5, Generic 5e | `NanonisSxmSTM` | `configs/nanonis/nanonis_sxm_generic_stm.json` |
| `AFM` | `.sxm` | Nanonis SPM control software | Generic 4 | `NanonisSxmAFM` | `configs/nanonis/nanonis_sxm_generic_afm.json` |

Files written by neighboring versions usually work as well, but may need an adapted config
file. If no config file is passed on the command line, the default config shipped with the
package is used.

## .dat data (STS)

Download and try with the [STS example files](../assets/command_line_examples/sts.zip){:sts},
or visit the
[GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/nanonis/sts/version_gen_5_with_described_nxdata).

```console
pynx convert --nxdl NXsts --reader spm --output output.nxs eln_data.yaml Bias-Spectroscopy00015_20230420.dat config.json
```

## .sxm data (STM)

Download and try with the [STM example files](../assets/command_line_examples/stm.zip){:stm},
or visit the
[GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/nanonis/stm/version_gen_5_with_described_nxdata).

```console
pynx convert --nxdl NXstm --reader spm --output output.nxs eln_data.yaml Au_mica_2023_Y_A_diPAMY_195.sxm config.json
```

## .sxm data (AFM)

Download and try with the [AFM example files](../assets/command_line_examples/afm.zip){:afm},
or visit the
[GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/nanonis/afm/version_gen_4_with_described_nxdata).

```console
pynx convert --nxdl NXafm --reader spm --output output.nxs eln_data.yaml A151216.123306-02602.sxm config.json
```

## Further reading

- [Supported vendor files and formats](../explanation/reader-orchestra.md#supported-vendor-files-and-formats)
- [Work with Reader](../how-to-guides/work-with-reader.md)
- [Use Reader from Command Line](standalone-usages.md)
