# Scan region, axes and scan direction

Every SPM vendor writes the geometry of a scan differently: some store a centre,
some a corner, some no range at all and some no scan direction. This page states
the single convention `pynxtools-spm` writes into NeXus, which raw element of
each format it comes from, and how strong the evidence for each reading is.

Where a vendor documents the meaning, the vendor is cited. Where no document was
found, the meaning was measured on published data and the measurement is shown,
so that anyone can repeat it or overturn it — see
[Challenge these findings](#challenge-these-findings).

## What this page answers

| Question | Short answer | Section |
|---|---|---|
| What does the scan offset point at? | The centre of the scanned area, for every flavour | [The convention](#the-convention) |
| How are `scan_start` and `scan_end` obtained? | `offset ∓ range/2`; never `offset` and `offset + range` | [The convention](#the-convention) |
| What do the axis values mean? | Pixel centres, `step = range / N` | [The convention](#the-convention) |
| Why are there two lists of axes? | `@axes` describes the image, `independent_scan_axes` the movement of the tip | [Two kinds of axes](#two-kinds-of-axes) |
| Where is the scan direction? | In the sign of `independent_scan_axes`, e.g. `-Y` | [Scan direction as a sign](#scan-direction-as-a-sign) |
| Which raw key does a value come from? | Per-flavour tables | [Raw-file elements per flavour](#raw-file-elements-per-flavour) |
| How certain is all this? | Graded per claim, vendor manual down to none | [Evidence and confidence](#evidence-and-confidence) |

## Fields the reader writes

| NeXus field | Group | Meaning | Derived from |
|---|---|---|---|
| `scan_offset_value_x`, `_y` | `NXspm_scan_region` | Centre of the scanned area | Vendor key, converted to a centre if the vendor stores a corner |
| `scan_range_x`, `_y` | `NXspm_scan_region` | Width and height of the area | Vendor key, or `points × pitch` when not stored |
| `scan_start_x`, `_y` | `NXspm_scan_region` | Low edge of the area | `offset - range/2` |
| `scan_end_x`, `_y` | `NXspm_scan_region` | High edge of the area | `offset + range/2` |
| `scan_angle_x`, `_y` | `NXspm_scan_region` | Rotation of the scan frame | Vendor key; not applied to the data |
| `scan_points_x`, `_y` | `NXspm_scan_pattern` | Pixels per line, number of lines | Vendor key |
| `step_size_x`, `_y` | `NXspm_scan_pattern` | Pixel pitch | `range / points` |
| `AXISNAME` (`X`, `Y`) | `NXdata` | Position of each pixel centre | `offset - range/2 + (i + 0.5) × step` |
| `@axes` | `NXdata` | Axis of each data dimension | `[Y, X]`, dimension 0 first |
| `independent_scan_axes` | `NXspm_scan_control` | Scan axes, fastest to slowest, signed with the direction | Vendor direction key |

## The convention

### Offset is the centre of the scan area

```text
scan_start_n = offset_n - range_n / 2
scan_end_n   = offset_n + range_n / 2
```

`scan_start = offset` with `scan_end = offset + range` is never used. When a
format stores a corner instead of a centre, the corner is shifted first,
`offset = corner + range/2`, and the relations above are applied to it. Start and
end are always derived, even where a format has a start-like key of its own.

```mermaid
flowchart LR
    A["offset<br/>(centre)"] --- B["range"]
    B --> C["scan_start = offset - range/2"]
    B --> D["scan_end = offset + range/2"]
    C --> E["axis[0] = scan_start + step/2"]
    D --> F["axis[-1] = scan_end - step/2"]
```

### Axis values are pixel centres

An axis value is the centre of its pixel, not its edge, so pixel `i` of `N` sits
at `offset - range/2 + (i + 0.5) × step` with `step = range / N`. The first and
last axis values are therefore half a pixel inside the scan region, and the
midpoint of any axis is exactly the scan offset. Placing the coordinate at the
pixel centre is this reader's choice; no vendor prescribes it.

### Frames of reference

| Frame | What it is | Fields in it |
|---|---|---|
| Scanner (piezo) | Position within the scanner range, measured from its undeflected centre | `scan_offset_value_*`, `scan_start_*`, `scan_end_*`, `AXISNAME` |
| Stage | Coarse position of the head or sample holder | Vendor stage keys, e.g. Bruker `\Stage X`; never combined with the offset |
| Sample | Where a feature physically sits | Can be reconstructed only by combining the stage position with the scanner frame |

A non-zero `scan_angle_*` rotates the scan frame against the sample, so `X` and
`Y` are the fast and the slow axis of the **scan frame**, not the x and y of the
sample. The angle is recorded but never applied to the data.

### Image orientation

Images follow the bottom-left convention: row 0 is the bottom row, column 0 the
left column, and both axes ascend. An up scan and a down scan of the same area
give the same image; only the order in which the lines were recorded differs.
See [Reader Orchestra](reader-orchestra.md) for the reader pipeline that applies
this.

## Two kinds of axes

`@axes` and `independent_scan_axes` answer different questions and are written
independently of each other.

| | `@axes` (`NXdata`) | `independent_scan_axes` (`NXspm_scan_control`) |
|---|---|---|
| Question answered | How should the image be displayed? | How did the tip move over the sample? |
| Order | Dimension order, `[slow, fast]` = `[Y, X]` | Fastest to slowest, `[X, Y]` |
| Case | Upper case | Upper case |
| Sign | Never signed | Signed with the scan direction where known |
| Affected by the image flips | Yes, it describes the stored image | No, it describes the measurement |

### Scan direction as a sign

| Value | Meaning |
|---|---|
| `+Y` | The axis was traveled towards increasing Y |
| `-Y` | The axis was traveled towards decreasing Y |
| `Y` | No single direction is asserted |

An axis is signed when the entry holds exactly one pass along it **and** the
format records which way that pass ran.

A bare axis covers two different situations, which the file itself tells apart:

- **Both passes are stored.** The entry has a forward and a backward `NXdata`
  group, so no single direction applies to the fast axis.
- **The format never records it.** Bruker `.FLT` stores one channel and no slow
  scan direction, so its `Y` means unknown, not upward.

## Raw-file elements per flavour

| Flavour | Extension | Offset | Range | Points | Direction | Unit | Angle |
|---|---|---|---|---|---|---|---|
| [Nanonis](#nanonis-sxm-stm-afm) | `.sxm` | `:SCAN_OFFSET:` | `:SCAN_RANGE:` | `:SCAN_PIXELS:` | `:SCAN_DIR:` | `/Z-Controller/Z` unit | `:SCAN_ANGLE:` |
| [Bruker NanoScope](#bruker-nanoscope-spm) | `.spm` | `\X Offset`, `\Y Offset` | `\Scan Size`, `\Aspect Ratio` | `\Samps/line`, `\Lines` | `\Frame direction` | In the value, e.g. `20000 nm` | `\Rotate Ang.` |
| [Bruker SPMLab](#bruker-spmlab-flt) | `.FLT` | `OffsetX`, `OffsetY` | `ScanRangeX`, `ScanRangeY` | `ResolutionX`, `ResolutionY` | `ScanDirection` | Suffix of the value, e.g. `1.0000 µm` | `Rotation` |
| [Omicron / RHK](#omicron-rhk-sm4) | `.sm4` | `RHK_Xoffset`, `RHK_Yoffset` | not stored | `RHK_Xsize`, `RHK_Ysize` | sign of `RHK_Yscale` | `RHK_X/@unit`, `RHK_Y/@unit` | `RHK_Angle` |
| [No raster](#no-raster-nanonis-dat-sts-and-bruker-spmtxt) | `.dat`, `.spm.txt` | — | — | — | — | — | — |

### Nanonis `.sxm` (STM, AFM)

| Raw key | Meaning | How the reader uses it |
|---|---|---|
| `:SCAN_OFFSET:` | Centre of the scan frame, x and y | `scan_offset_value_x`, `_y` |
| `:SCAN_RANGE:` | Width and height | `scan_range_x`, `_y` |
| `:SCAN_PIXELS:` | Pixels per line, number of lines | `scan_points_x`, `_y` |
| `:SCAN_DIR:` | `up` or `down`, the slow direction | Sign of the slow axis; orients the image |
| `:SCAN_ANGLE:` | Rotation of the frame | `scan_angle_x`, `_y`, not applied |

Both passes of the fast axis are stored (`DATA_INFO` `Direction` is `both`), so
the fast axis stays unsigned. The header repeats the same geometry in
`:Scan>Scanfield:` as `centre_x;centre_y;width;height;angle`; the reader does not
read that key.

### Bruker NanoScope `.spm`

| Raw key | Meaning | How the reader uses it |
|---|---|---|
| `\X Offset`, `\Y Offset` | Centre position of the scan | `scan_offset_value_x`, `_y` |
| `\Scan Size` | Edge length of the frame | `scan_range_x`; y is divided by `\Aspect Ratio` |
| `\Aspect Ratio` | Ratio of x to y range | Malformed values fall back to `1:1` with a warning |
| `\Samps/line`, `\Lines` | Pixels per line, number of lines | `scan_points_x`, `_y` |
| `\Frame direction` | `Up` or `Down`, the slow direction | Sign of the slow axis |
| `\Rotate Ang.` | Rotation of the frame | `scan_angle_x`, not applied |

Trace and Retrace layers are both stored, so the fast axis stays unsigned.
`\X Position` and the coarse stage `\Stage X` are **not** used for the scan
region: the stage is a different frame of reference.

### Bruker SPMLab `.FLT`

| Raw key | Meaning | How the reader uses it |
|---|---|---|
| `OffsetX`, `OffsetY` | Centre of the scan frame | `scan_offset_value_x`, `_y` |
| `ScanRangeX`, `ScanRangeY` | Width and height | `scan_range_x`, `_y` |
| `ResolutionX`, `ResolutionY` | Pixels per line, number of lines | `scan_points_x`, `_y` |
| `ScanDirection` | `FORWARD` or `BACKWARD`, the fast direction | Sign of the fast axis |
| `Rotation` | Rotation of the frame | `scan_angle_x`, not applied |

A `.FLT` holds a single channel recorded in one direction, so the fast axis is
signed. The format records **no slow scan direction**, so the slow axis stays
bare. The `[Data]` block holds only the height values, `ResolutionX ×
ResolutionY` 32-bit floats; no axis coordinates are stored.

### Omicron / RHK `.sm4`

| Raw key | Meaning | How the reader uses it |
|---|---|---|
| `RHK_Xoffset`, `RHK_Yoffset` | Centre of the scan area | `scan_offset_value_x`, `_y` |
| `RHK_Xscale`, `RHK_Yscale` | Signed distance between adjacent pixels | `\|scale\|` is the pixel pitch; the sign of `RHK_Yscale` is the slow direction |
| `RHK_Xsize`, `RHK_Ysize` | Pixels per line, number of lines | `scan_points_x`, `_y` |
| `RHK_X/@unit`, `RHK_Y/@unit` | Unit of the lateral axes | Unit of offset, range, start, end and step |
| `RHK_ScanType` | Names the Forward and Backward pass | Channel naming; one scan control group per page |
| `RHK_Angle` | Rotation of the frame | `scan_angle_x`, `_y`, not applied |

No range is stored: it is `range = N × |scale|`, the edge-to-edge width, counting
`N` pitches and not `N - 1`. The fast axis stays unsigned, because neither
`RHK_ScanType` nor `RHK_Xscale`, whose sign is the same on the Forward and the
Backward page, says which way the tip ran along a line.

### No raster: Nanonis `.dat` STS and Bruker `.spm.txt`

Neither flavour rasters an area, so neither writes a 2D scan region or
`independent_scan_axes`.

| Flavour | What is written instead |
|---|---|
| Nanonis `.dat` STS | `scan_start_bias`, `scan_end_bias` and `scan_offset_bias`, read directly from `Bias Spectroscopy>Sweep Start (V)`, `>Sweep End (V)` and `Bias>Offset (V)` |
| Bruker `.spm.txt` | A `point_forceSCAN` group; start, end and range of both halves of the ramp come from the first and last element of `/Calc_Ramp_Ex_nm` and `/Calc_Ramp_Rt_nm` |

## Evidence and confidence

### Grades

| Grade | Definition |
|---|---|
| Vendor manual | A document published by the instrument maker defines the parameter |
| Empirical test | Raw files from the vendor's software where the geometry can be measured, and only one reading fits |
| Vendor file content | Something the vendor's software writes into the file that fits only one reading |
| Third-party reader | An independent open-source reader, e.g. Gwyddion; how the community reads the value, not how the vendor defines it |
| None | No source found |

### What each claim rests on

| Claim | Flavour | Grade | Source |
|---|---|---|---|
| Offset is the centre | Bruker `.spm` | Vendor manual | [NanoScope 6.13 User Guide](https://afmhelp.com/docs/manuals/Nanoscope6.13UserGuide.pdf), p. 60 |
| Offset is the centre | Omicron `.sm4` | Vendor manual + empirical test | [RHK R9 User Manual](https://www.manualslib.com/manual/2808818/Rhk-Technology-R9.html?page=195), p. 195 |
| Offset is the centre | Nanonis `.sxm` | Vendor file content + third-party readers | `:Scan>Scanfield:` in the files; [Gwyddion `nanonis.c`](https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/nanonis.c) |
| Offset is the centre | Bruker `.FLT` | Empirical test | [Measurement below](#how-the-empirical-test-works) |
| Pitch is `\|scale\|`, range is `N × \|scale\|` | Omicron `.sm4` | Third-party readers | [Gwyddion `rhk-sm4.c`](https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/rhk-sm4.c); [MATLAB `sm4reader`](https://www.mathworks.com/matlabcentral/fileexchange/62561-sm4reader-fileid) |
| Sign of `RHK_Yscale` is the slow direction | Omicron `.sm4` | Third-party reader | [Gwyddion forum](https://sourceforge.net/p/gwyddion/discussion/fileformats/thread/3377ed98fa/) |
| Row order and image flips | All image flavours | Third-party reader | Gwyddion import modules, verified against every test file |

### How the empirical test works

A small scan taken inside a larger scan of the same area shows up as a patch of
the large image. Where the patch is **found** is a measurement; where each
reading of the offset **predicts** it differs by `(range_big - range_small) / 2`
per axis. The small image is resampled to the pixel size of the large one, both
are line- and plane-levelled, and the patch is located by normalized
cross-correlation.

Pairs whose two scans share the same offset are the clearest: a centre reading
puts the small scan in the middle of the large one, a corner reading in a corner,
and that holds whatever the axis directions are.

| Pair | Flavour | Correlation peak / next | Measured | Centre predicts | Corner predicts |
|---|---|---|---|---|---|
| `PMIS2-C8_ML2_p1_5` in `…_p1_20`, identical offsets | `.FLT` | 0.54 / 0.10 | (10.00, 10.04) µm | (10.00, 10.00) µm | (2.50, 2.50) µm |
| `VT231211_A1_0064` (10 nm) in `_0065` (30 nm), identical offsets | `.sm4` | 0.71 / 0.54 | (0.53, 0.41) nm | (0.00, 0.00) nm | (9.96, 9.96) nm |
| `VT231205_A1_0064` (up) and `_0063` (down), identical offsets | `.sm4` | 0.44 / 0.38 | (0.94, 4.26) nm | (0.00, 0.00) nm | (0.00, 19.96) nm |

The last pair also rules the corner reading out on its own: under it the up and
the down scan would cover adjacent, non-overlapping strips, yet they overlap.
The few-nm residuals of the `.sm4` pairs are expected from creep and drift of an
open-loop STM scanner; the `.FLT` files were recorded with closed-loop
linearization, which is why they agree to one pixel.

### Data used

| Flavour | Files | Where | License |
|---|---|---|---|
| Bruker `.FLT` | `PMIS2-C8_ML2_p1_5__040925135420.SIG_HEIGHT_SENSOR_FRW.FLT`, `PMIS2-C8_ML2_p1_20__040925132340.SIG_HEIGHT_SENSOR_FRW.FLT` | [In this repository](../assets/empirical_offset_test/README.md), and in `AFM.zip` of [10.5281/zenodo.18060234](https://doi.org/10.5281/zenodo.18060234) | CC BY 4.0 |
| Omicron `.sm4` | `VT231211_A1_0064.sm4`, `VT231211_A1_0065.sm4`, `VT231205_A1_0063.sm4`, `VT231205_A1_0064.sm4` | [10.5281/zenodo.14268803](https://doi.org/10.5281/zenodo.14268803); the record holds many more files, so take these four by name | CC BY 4.0 |

### Still unverified

| Open question | What would settle it |
|---|---|
| Which way the tip runs along a line in `.sm4` | An RHK document defining `RHK_ScanType`, or two scans of one area with opposite `RHK_ScanType` and a feature that fixes the direction |
| The slow scan direction of a `.FLT` | An SPMLab or Innova manual, or a pair of up and down scans of the same area |
| Whether Nanonis `SCAN_OFFSET` is the centre per SPECS itself | The Nanonis TCP Protocol Document, which needs a MySPECS account |
| The stored row order of a `.spm` | A Bruker document stating it, or an openly licensed Up and Down scan of one area |

## Challenge these findings

Four of the claims above rest on measurement or on third-party readers rather
than on a vendor document. If you can show one of them is wrong, the reader
should change.

| Claim | Evidence that would overturn it |
|---|---|
| The `.FLT` offset is the centre | A Veeco, ThermoMicroscopes or Bruker Innova document defining `OffsetX`, or scans of one area that the centre reading misplaces |
| The `.sm4` range is `N × \|scale\|` | The RHK "SM4 Data File Format" document, or a calibration grating measured against the written range |
| The `.sm4` fast axis has no recorded direction | A field in the page header, or the RHK format document, that gives it |
| Nanonis `SCAN_OFFSET` is the centre | The SPECS TCP Protocol Document, if it says otherwise |

Please open an issue with the
[Challenge a scan-region convention](https://github.com/FAIRmat-NFDI/pynxtools-spm/issues/new?template=challenge-a-convention.yml)
template. A vendor document is the strongest evidence; an openly licensed raw
file that the current reading gets wrong is just as welcome, because it can be
added to the test set.

## References

| Source | What it establishes | Link |
|---|---|---|
| NanoScope 6.13 User Guide, pp. 60, 85 | Bruker `.spm` offset is the centre position of the scan | [PDF](https://afmhelp.com/docs/manuals/Nanoscope6.13UserGuide.pdf) |
| Bruker help, Zoom and Offset Buttons | The Offset command centres the scan and updates X/Y Offset | [Page](https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SoftwareGuide/Realtime/Tips/ZoomAndOffsetButtons.htm) |
| Bruker help, Scan View Parameters Tips | X/Y Offset use the sample as position reference | [Page](https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SoftwareGuide/Realtime/Tips/ScanViewParametersTips.htm) |
| Bruker help, Frame Commands | Frame Up and Frame Down restart the scan at the bottom and the top | [Page](https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SoftwareGuide/Realtime/Tips/FrameCommands.htm) |
| RHK R9 User Manual, pp. 59, 195, 197 | XY Offsets of 0 centre the scan area in the scan range | [Manual](https://www.manualslib.com/manual/2808818/Rhk-Technology-R9.html?page=195) |
| Park Scientific, User's Guide to AutoProbe CP, pp. 4-17 f. | SPMLab's ancestor keeps the offset in scanner coordinates, referenced to the undeflected scanner | [Scan](https://utw10193.utweb.utexas.edu/InstrumentManuals/micro-nano-afm-cp%20auto-prob-user-manual.pdf) |
| Nanonis SXM format description | The SXM header tags and the data block layout | [GXSM tracker](https://sourceforge.net/p/gxsm/plugin-requests/3/) |
| `nanonis_control` | Documents the Nanonis scan frame as centre, size and angle | [Repository](https://github.com/dilwong/nanonis_control) |
| Gwyddion `nanonis.c`, `nanoscope.c`, `spmlabf.c`, `rhk-sm4.c` | Community reading of each format, including the image flips | [Source tree](https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/) |
| spym | Reference Python reader for RHK SM4 | [Repository](https://github.com/rescipy-project/spym) |
| MATLAB `sm4reader` | Computes the SM4 scan size as `\|scale\| × points` | [File Exchange](https://www.mathworks.com/matlabcentral/fileexchange/62561-sm4reader-fileid) |
