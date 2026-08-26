# Data from Bruker instruments

The reader supports three Bruker file formats, all of which are converted into the
[NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html)
application definition. They come from two different instrument lineages:

- `.flt` — written by `SPMLab`, the software of the TopoMetrix → ThermoMicroscopes → Veeco →
  Bruker (Innova) lineage.
- `.spm` and `.spm.txt` — written by `NanoScope`, the software of the Bruker Dimension family
  (the reference files here were recorded on a __Dimension Icon__). The `.spm` file is the native
  binary image file; the `.spm.txt` file is the NanoScope ASCII export of a __force ramp__
  (force-distance) measurement.

## Supported formats and versions

| Technique | Extension | Software | Tested versions | Formatter | Default config |
| --- | --- | --- | --- | --- | --- |
| `AFM` | `.flt`, `.FLT` | Bruker `SPMLab` (read with [gwyddionpy](https://pypi.org/project/gwyddionpy/)) | `1.00` | `BrukerFltAFM` | `configs/bruker/bruker_flt_afm.json` |
| `AFM` | `.spm` | Bruker `NanoScope` (read with [pySPM](https://github.com/scholi/pySPM)) | `9.x` (Dimension Icon) | `BrukerSpmAFM` | `configs/bruker/bruker_spm_afm.json` |
| `AFM (force curve)` | `.spm.txt` | Bruker `NanoScope` ASCII export | `9.x` (Dimension Icon) | `BrukerTxtAFM` | `configs/bruker/bruker_txt_afm.json` |

If no config file is passed on the command line, the default config shipped with the package
is used.

The version of an FLT file is stated in the `[Data Version]` section at the beginning of the file
header (`Program=SPMLab` and `Version=1.00`). The NanoScope version is stated by the `\Version`
key at the top of the header of both `.spm` and `.spm.txt` (`\Version: 0x09400105` in the
reference files, i.e. NanoScope 9.x). The reader compares extensions case-insensitively, so the
`.FLT` spelling written by SPMLab is accepted as well.

The parser is selected from the file extension together with the ELN entries
`INSTRUMENT[instrument]/software/vendor` and `INSTRUMENT[instrument]/software/model`. For the
Bruker formats the recognized `model` values are `SPMLab 1.00` (`.flt`), `9.64` (`.spm`) and
`NanoScope` (`.spm.txt`), each with `vendor: Bruker`. If `model` is left empty, the reader falls
back to trying every parser registered for the extension, which is unambiguous today because each
Bruker extension has exactly one parser.

## `.flt` data (AFM, SPMLab)

An FLT file consists of an INI style text header followed by the binary raster data. It is
read with the [gwyddionpy](https://pypi.org/project/gwyddionpy/) package (the `spmlabf`
importer of [Gwyddion](http://gwyddion.net/)) in
[`src/pynxtools_spm/parsers/bruker_flt.py`](https://github.com/FAIRmat-NFDI/pynxtools-spm/blob/main/src/pynxtools_spm/parsers/bruker_flt.py)
(class `FltBruker`).

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

### Behaviors specific to the FLT format

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

## `.spm` data (AFM, NanoScope)

A `.spm` file starts with an ASCII header (the `\Key: value` lines up to `\*File list end`)
followed by the binary image block of every recorded channel. It is read with the
[pySPM](https://github.com/scholi/pySPM) package in
[`src/pynxtools_spm/parsers/bruker_spm.py`](https://github.com/FAIRmat-NFDI/pynxtools-spm/blob/main/src/pynxtools_spm/parsers/bruker_spm.py)
(class `SpmBruker`, which extends pySPM's `Bruker` class in
[`parsers/bruker/pySPMbruker.py`](https://github.com/FAIRmat-NFDI/pynxtools-spm/blob/main/src/pynxtools_spm/parsers/bruker/pySPMbruker.py)
so that the `*File list` and `*Equipment list` sections are read as well).

!!! warning "pySPM is currently installed from a fork"
    `pyproject.toml` pins `pySPM` to [a fork](https://github.com/RubelMozumder/pySPM) rather than
    the release on PyPI, because the upstream package still carries a dependency pin that
    conflicts with this plugin. The pin will be reverted to `pySPM>=0.6.3` once that relaxation
    is released upstream.

```console
pynx convert --nxdl NXafm --reader spm --output output.nxs eln_data.yaml VGEP-15m-.0_00000.spm
```

Download and try with the [Bruker NanoScope metadata example](../assets/command_line_examples/bruker_spm.zip){:bruker_spm},
or visit the
[GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/bruker/afm/default_config).

!!! warning "The download contains the readable header only"
    A `.spm` file is dominated by its binary image block (16 MB for the reference file), so the
    downloadable bundle contains only the human-readable ASCII header
    (`VGEP-15m-.0_00000.spm.header.txt`) together with `eln_data.yaml`, as a preview of the
    metadata that the reader sees. To run the command above, take the complete `.spm` file from
    the [GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/bruker/afm/default_config)
    or use your own.

### Behaviors specific to the `.spm` format

!!! note "One `.spm` file holds many channels and both scan directions"
    Unlike FLT, a single `.spm` file stores every recorded channel in both scan directions. The
    parser exposes them as `/<Channel>/forward` and `/<Channel>/backward` (e.g.
    `/Height_Sensor/forward`, `/Phase/backward`), with `Trace` mapped to `forward` and `Retrace`
    to `backward`, and lists the available combinations under `/Scan_list`. One `.spm` file is
    therefore converted into one NeXus file that contains __several__ `NXdata` groups. With the
    default config these are `z_forward`, `z_backward`, `amplitude_error_forward`,
    `amplitude_error_backward`, `phase_forward`, `phase_backward`, `amplitude_forward`,
    `amplitude_backward`, `tm_deflection_forward` and `tm_deflection_backward`.

!!! note "Scan region from `Scan Size` and `Aspect Ratio`"
    The header states one scan size and an aspect ratio rather than an explicit X and Y range.
    `BrukerSpmAFM` therefore builds the scan region from `/Scanner_list/0/Scan_Size`,
    `/Scanner_list/0/X_Offset`, `/Scanner_list/0/Y_Offset` and `/Scanner_list/0/Aspect_Ratio`:
    the Y range is the X range divided by the aspect ratio. A malformed aspect ratio falls back
    to `1:1` and is reported as a warning.

!!! note "Axis values are rebuilt when the header disagrees with the image"
    The `x` and `y` axes are computed with `numpy.linspace` from the scan region and the point
    counts in the header. If those counts do not match the shape of the image actually stored in
    the file, the axes are regenerated from the image shape instead and a warning naming both
    shapes is logged, so that signal and axes always stay consistent.

## `.spm.txt` data (AFM force curve, NanoScope)

The `.spm.txt` file is the NanoScope ASCII export of a force ramp. Every line is wrapped in
double quotes: a `"\Key: value"` header terminated by `"\*Force file list end"`, followed by a
tab-separated column header and the numeric columns. It is read without any external library in
[`src/pynxtools_spm/parsers/bruker_txt.py`](https://github.com/FAIRmat-NFDI/pynxtools-spm/blob/main/src/pynxtools_spm/parsers/bruker_txt.py)
(class `TxtBruker`).

```console
pynx convert --nxdl NXafm --reader spm --output output.nxs eln_data.yaml SB04-MG1.0_00000.spm.txt
```

Download and try with the [Bruker NanoScope force-curve example files](../assets/command_line_examples/bruker_txt.zip){:bruker_txt},
or visit the
[GitHub folder](https://github.com/FAIRmat-NFDI/pynxtools-spm/tree/main/tests/data/bruker/afm/txt_default_config).

### Behaviors specific to the `.spm.txt` format

!!! note "Extend and retract columns"
    Each measured quantity is exported twice, once for the extend (approach) half of the ramp and
    once for the retract half, marked by the suffixes `_Ex` and `_Rt` in the column name. The
    physical unit is part of the column name as well, either before the direction marker
    (`Time_s_Ex` → `s`) or after it (`Calc_Ramp_Ex_nm` → `nm`), and is stored next to the array
    under the `/unit` suffix (e.g. `/Defl_pN_Ex` and `/Defl_pN_Ex/unit`). With the default config
    the four resulting `NXdata` groups are `deflection_extension`, `height_sensor_extension`,
    `deflection_retrace` and `height_sensor_retrace`, each plotting the quantity against the
    corresponding ramp position.

!!! note "Point force scan instead of mesh scan"
    A force curve is not a raster image, so `BrukerTxtAFM` writes a
    `point_forceSCAN[point_force_scan]` group where the image formatters write
    `meshSCAN[mesh_scan]`. Start, end and range of both halves of the ramp are taken from the
    first and last element of the ramp arrays `/Calc_Ramp_Ex_nm` and `/Calc_Ramp_Rt_nm`, so that
    the physical direction of the ramp is preserved rather than only its sorted extent. The step
    sizes are then derived as `range / (points - 1)`.

!!! note "`Samps/line` may carry one or two counts"
    The point counts for the approach and the retrace half are read from `Samps/line`, which
    NanoScope writes either as a single shared count (`512`) or as two space-separated counts
    (`256 512`, approach first). A single count is used for both halves.

!!! note "The amplitude setpoint is a ratio"
    NanoScope stores the amplitude setpoint as a dimensionless fraction of the free amplitude, so
    the physical `amplitude_setpoint` is computed as `Amplitude_Ratio × reference_amplitude` and
    inherits the unit of the reference amplitude.

!!! warning "Any `.txt` input is treated as a Bruker force-curve export"
    The reader dispatches on the file extension. With `experiment_technique: AFM` in the ELN file,
    __every__ `.txt` file handed to the reader is routed to `BrukerTxtAFM`. Do not pass unrelated
    text files as input files alongside your data.

## Further reading

- [Supported vendor files and formats](../explanation/reader-orchestra.md#supported-vendor-files-and-formats)
- [Work with Reader](../how-to-guides/work-with-reader.md)
- [Use Reader from Command Line](standalone-usages.md)
- [gwyddionpy](https://pypi.org/project/gwyddionpy/) — reads the `SPMLab` `.flt` format
- [pySPM](https://github.com/scholi/pySPM) — reads the NanoScope `.spm` format
