# Data from Bruker instruments

The reader supports `.flt` files written by the Bruker `SPMLab` instrument software (the
instrument writes the extension in upper case, `.FLT`; the reader compares extensions
case-insensitively, so both spellings are accepted). The files are converted into the
[NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html)
application definition.

An FLT file consists of an INI style text header followed by the binary raster data. It is
read with the [gwyddionpy](https://pypi.org/project/gwyddionpy/) package (the `spmlabf`
importer of [Gwyddion](http://gwyddion.net/)) in
[`src/pynxtools_spm/parsers/bruker_flt.py`](https://github.com/FAIRmat-NFDI/pynxtools-spm/blob/main/src/pynxtools_spm/parsers/bruker_flt.py)
(class `FltBruker`).

## Supported formats and versions

The version is stated in the `[Data Version]` section at the beginning of the file header
(`Program=SPMLab` and `Version=1.00`).

| Technique | Extension | Software | Tested versions | Formatter | Default config |
| --- | --- | --- | --- | --- | --- |
| `AFM` | `.flt`, `.FLT` | Bruker `SPMLab` | `1.00` | `BrukerFltAFM` | `configs/bruker/bruker_flt_afm.json` |

If no config file is passed on the command line, the default config shipped with the package
is used.

## .flt data (AFM)

Download and try with the [Bruker AFM example files](../assets/command_line_examples/bruker_afm.zip){:bruker},
or visit the
[GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/bruker/afm/flt_described_config).

```console
pynx convert --nxdl NXafm --reader spm --output output.nxs eln_data.yaml B3320_13_061726074638.SIG_TOPO_FRW.FLT config.json
```

Without a config file, the default config is used:

```console
pynx convert --nxdl NXafm --reader spm --output output.nxs eln_data.yaml B3320_13_061726074638.SIG_TOPO_FRW.FLT
```

## Behaviors specific to the FLT format

!!! note "One FLT file holds one channel"
    An FLT file stores a __single__ channel of a __single__ scan direction, e.g.
    `B3320_13_061726074638.SIG_TOPO_FRW.FLT` holds the forward (`FRW`) height (`SIG_TOPO`)
    image, while the backward scan (`BKW`) and the further channels (e.g. `SIG_USER2`) are
    written as separate files. Therefore one FLT file is converted into one NeXus file, and
    the channel name of the file (`DataName` in the header, e.g. `Height`) determines the name
    of the resulting `NXdata` group.

!!! note "The `/CHANNEL/` placeholder"
    Because the parsed raw data keys are prefixed by the channel name of the file (e.g.
    `/Height/meta/SetPoint`), a config file cannot know that prefix in advance. The config
    therefore uses the placeholder `/CHANNEL/` in its `raw_path` entries, which is replaced by
    the channel prefix of the file when the config is loaded. The same config file thus works
    for every channel. See [Work with Reader](../how-to-guides/work-with-reader.md) for an
    example.

## Further reading

- [Supported vendor files and formats](../explanation/reader-orchestra.md#supported-vendor-files-and-formats)
- [Work with Reader](../how-to-guides/work-with-reader.md)
- [Use Reader from Command Line](standalone-usages.md)
