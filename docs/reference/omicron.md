# Data from Omicron instruments

The reader supports `.sm4` files from [Scienta Omicron](https://scientaomicron.com/)
instruments. The files are converted into the
[NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html)
application definition.

The `.sm4` file is read with the [spym](https://github.com/rescipy-project/spym) package in
[`src/pynxtools_spm/parsers/omicron_sm4.py`](https://github.com/FAIRmat-NFDI/pynxtools-spm/blob/main/src/pynxtools_spm/parsers/omicron_sm4.py)
(class `Sm4Omicron`).

## Supported formats and versions

| Technique | Extension | Software | Tested versions | Formatter | Default config |
| --- | --- | --- | --- | --- | --- |
| `STM` | `.sm4` | Omicron | not version specific | `OmicronSM4STM` | `configs/omicron/omicron_sm4_stm.json` |

The `.sm4` format carries no software version concept that the reader depends on, so no
version is listed here — the reader handles the format as such. If no config file is passed
on the command line, the default config shipped with the package is used.

## .sm4 data (STM)

Download and try with the [Omicron STM example files](../assets/command_line_examples/omicron.zip){:omicron},
or visit the
[GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/omicron/stm/default_config).

```console
pynx convert --nxdl NXstm --reader spm --output output.nxs eln_data.yaml VT220120_A2_0001.sm4
```

The example above relies on the default config. To use your own mapping, add the config file
as a further input:

```console
pynx convert --nxdl NXstm --reader spm --output output.nxs eln_data.yaml VT220120_A2_0001.sm4 config.json
```

!!! note "One scan control group per scan"
    An Omicron `.sm4` file holds several scans (e.g. `current_forward`, `current_backward`,
    `topography_forward`, `topography_backward`). The config file therefore instantiates the
    group `SPM_SCAN_CONTROL[spm_scan_control_*]` once per scan, where the asterisk `*` is
    replaced by the scan name. See
    [Work with Reader](../how-to-guides/work-with-reader.md) for how to write such a config
    entry.

## Further reading

- [Supported vendor files and formats](../explanation/reader-orchestra.md#supported-vendor-files-and-formats)
- [Work with Reader](../how-to-guides/work-with-reader.md)
- [Use Reader from Command Line](standalone-usages.md)
