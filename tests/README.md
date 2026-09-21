# Tests

## Running

```bash
pytest tests/ --ignore=tests/nomad
```

## Image orientation convention

Every image written to an `NXdata` group follows the convention of a scientific
plot: the origin is the **bottom-left** corner.

- Row 0 of the signal is the bottom row, column 0 is the left column.
- Both axes ascend, so the first value of an axis labels row 0 or column 0.
- Axis values are the positions of the pixel centres in the scan frame:
  `offset - range/2 + (i + 0.5) * range/N` for pixel `i` of `N`.
- An *up* scan and a *down* scan of the same area give the same image. The scan
  direction only changes the order in which the lines were recorded.
- The scan angle is not applied: axes describe the (rotated) scan frame, and the
  angle is stored separately in `scan_region/scan_angle_*`.

Gwyddion is used as an independent reference because it reads every raw format
in this test set. It stores row 0 at the **top** , so a
correctly oriented signal equals `np.flipud` of the matching Gwyddion channel.

## Scan region: offset, start and end

`scan_start_*` and `scan_end_*` are not independent of `scan_offset_value_*`
and `scan_range_*`. `NXspm_scan_region` defines `scan_offset_valueN` as "the
offset of center of the scan region from the origin along the specific scan
axis", and notes under `scan_endN` that "the scan_offset and scan_range are
equivalent to the scan_start and scan_end".

Convention used throughout this repo, for every flavour:

- `scan_offset_value_*` is the **centre** of the scan area.
- `scan_start_n = offset_n - range_n / 2` and `scan_end_n = offset_n + range_n / 2`.
- Axis values are the pixel centres `offset - range/2 + (i + 0.5) * range/N`
  (see the section above), so the offset is the midpoint of every axis.

`scan_start = offset` with `scan_end = offset + range` is never used. If a raw
file stores a corner instead of the centre, the offset is first shifted to the
centre, `offset = corner + range/2`, and the relations above are applied to it.
Start and end are always derived from offset and range, even where a file has
a start-like key (Bruker `\X Position`).

All offsets are in the scanner (piezo) frame, measured from the centre of the
scanner's range. A stage position such as Bruker `\Stage X` is the coarse
position of the head, a different frame, and is not combined with the offset.

## Where each vendor stores the scan direction

The notes below record which raw metadata decides the orientation of an image,
and where that knowledge comes from. Add to them when a vendor is handled.

### Nanonis (`.sxm`)

The same rules apply to STM and AFM scans; both are read by `NanonisBase`.

| Header tag | Meaning |
|---|---|
| `SCAN_DIR` | `up` or `down`: the slow scan direction. |
| `SCAN_OFFSET` | x and y of the **centre** of the scan frame (m); [evidence](#nanonis-sxm-centre-vendor-file-content-and-third-party-readers). |
| `SCAN_RANGE` | width and height of the scan frame (m). |
| `SCAN_PIXELS` | number of pixels per line (x) and number of lines (y). |
| `SCAN_ANGLE` | rotation of the scan frame (deg). |
| `DATA_INFO` `Direction` | `both` means a forward and a backward image per channel. |

Data block: for each channel, the forward image and then the backward image,
each `lines × pixels`, lines in the order they were recorded. A backward line is
stored in the order the tip traveled, from right to left.

Consequence for the bottom-left convention:

| `SCAN_DIR` | Forward image | Backward image |
|---|---|---|
| `up` (first line at the bottom) | unchanged | `np.fliplr` |
| `down` (first line at the top) | `np.flipud` | `np.flipud` + `np.fliplr` |

Sources:

- Nanonis SXM file format description, posted by M. Schmotz (2006) on the GXSM
  plugin tracker: "The data is stored chronologically as it is recorded. On an
  up-scan, the first point corresponds to the lower left corner of the scanfield
  (forward scan). On a down-scan, it is the upper left corner of the scanfield.
  Hence, backward scan data start on the right side of the scanfield."
  <https://sourceforge.net/p/gxsm/plugin-requests/3/>
- Gwyddion Nanonis import module `modules/file/nanonis.c`: flips vertically
  depending on `SCAN_DIR` and flips backward channels horizontally.
  <https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/nanonis.c>
- Gwyddion forum, "Nanonis .sxm file orientation" (2018): Nanonis uses
  right-handed coordinates (y grows upwards), Gwyddion left-handed ones, and
  Gwyddion flips images to preserve coordinates.
  <https://sourceforge.net/p/gwyddion/discussion/fileformats/thread/dfea4a4f61/>
- nanonispy `read.py`: data block layout (channel, direction, lines, pixels).
  <https://github.com/underchemist/nanonispy/blob/master/nanonispy/read.py>

Verified on the test data: for up and down scans, forward and backward, the
oriented raw image equals `np.flipud` of the Gwyddion channel exactly.

### Bruker NanoScope (`.spm`, `.spm.txt`)

| Header key | Meaning |
|---|---|
| `\Frame direction` | `Up` or `Down`: where the slow scan starts. Frame Up restarts the scan at the bottom of the frame, Frame Down at the top. |
| `\Line Direction` | `Trace` (forward) or `Retrace` (backward) for one image layer. |
| `\Scan Size` | edge length of the scan frame. |
| `\X Offset`, `\Y Offset` | **centre** of the scan frame; [evidence](#bruker-nanoscope-spm-centre-vendor-manual). A more negative Y Offset moves a feature down on the image display. |

The rows are stored in a fixed order, bottom row first, whatever the frame
direction:

| `Frame direction` | gwyddionpy row 0 is | to get row 0 = bottom |
|---|---|---|
| `Up` | top | `np.flipud` |
| `Down` | top | `np.flipud` |

Evidence:

- Gwyddion NanoScope import module `modules/file/nanoscope.c`: turns every image
  upside down once (`gwy_data_field_invert(dfield, TRUE, FALSE, FALSE)`, where
  the first flag flips the rows) and never reads `Frame direction`.
  <https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/nanoscope.c>
- Gwyddion `libprocess/datafield.c`, `gwy_data_field_invert`: "yflipped: TRUE
  to reflect Y, i.e. rows within the XY plane. The image will be flipped upside
  down."
  <https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/libprocess/datafield.c>
- Bruker help, Frame Commands: Frame Up restarts the scan at the bottom of the
  frame, Frame Down at the top.
  <https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SoftwareGuide/Realtime/Tips/FrameCommands.htm>
- Bruker help, Scan View Parameters Tips: X/Y Offset use the sample as position
  reference; a more negative Y Offset moves a feature down on the display.
  <https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SoftwareGuide/Realtime/Tips/ScanViewParametersTips.htm>

Verified on the test data: reading each raw image block at `Data offset`
(bytes per pixel = `Data length` / (`Samps/line` × `Number of lines`)) gives
exactly `np.flipud` of the Gwyddion channel for every layer, Trace and Retrace:
8 of 8 layers of the Down file and 6 of 6 layers of the Up file.

Not yet verified: no Bruker document states the stored row order, and no
openly licensed Up and Down scan of the same area was found (all Bruker `.spm`
files up to 25 MB on Zenodo were checked), so direction independence rests on
the Gwyddion module above.

### Bruker SPMLab (`.FLT`)

| Header key (`[Data Parameters]`) | Meaning |
|---|---|
| `ScanDirection` | `FORWARD` or `BACKWARD`: the fast (line) direction of this file. No slow scan direction is stored. |
| `OffsetX`, `OffsetY` | **centre** of the scan frame; [evidence](#bruker-spmlab-flt-centre-empirical-test-on-vendor-data). |
| `ScanRangeX`, `ScanRangeY` | width and height of the scan frame. |
| `ResolutionX`, `ResolutionY` | pixels per line and number of lines. |
| `Rotation` | rotation of the scan frame (deg); not applied. |

The `[Data]` section holds only the height values, `ResolutionX ×
ResolutionY` 32-bit floats; axis coordinates are not stored and follow from
offset and range.

The rows are stored bottom row first, so the image gets one `np.flipud` against
gwyddionpy, like a NanoScope `.spm` file. The test folders carry no up/down
suffix because the format records no slow scan direction.

Evidence:

- Gwyddion SPMLab import module `modules/file/spmlabf.c`: turns every image
  upside down once (`gwy_data_field_invert(dfield, TRUE, FALSE, FALSE)`) and
  keeps `ScanDirection` and `Rotation` as metadata only.
  <https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/spmlabf.c>

### Omicron / RHK (`.sm4`)

| Page header field | Meaning |
|---|---|
| `RHK_ScanType` | `RIGHT`/`LEFT` for the forward/backward image: the fast (line) direction. |
| `RHK_Yscale` | step between rows. Its sign is the slow scan direction: > 0 up, < 0 down. |
| `RHK_Xscale` | step between columns; negative in every file seen so far. |
| `RHK_Xsize`, `RHK_Ysize` | pixels per line and number of lines. |
| `RHK_Xoffset`, `RHK_Yoffset` | **centre** of the scan area; [evidence](#omicron--rhk-sm4-centre-vendor-manual-and-empirical-test-on-vendor-data). |

#### How the geometry is read

An SM4 page header stores no step size, no range and no scan direction as such.
All three are read out of `RHK_Xscale`, `RHK_Yscale` and the two sizes:

- **Step (pixel pitch)** `= |RHK_Xscale|` along x and `|RHK_Yscale|` along y.
  The scale is the distance between two neighbouring pixels and is signed; its
  magnitude is the pitch. Gwyddion reads it the same way, sizing a page as
  `xres * fabs(x_scale)`
  ([`rhk-sm4.c`](https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/rhk-sm4.c)),
  as does the MATLAB `sm4reader`, `width = abs(XScale * points)`
  ([File Exchange](https://www.mathworks.com/matlabcentral/fileexchange/62561-sm4reader-fileid)).
- **Scan range** `= N × |RHK_Xscale|` for `N = RHK_Xsize` pixels, and the same
  for y with `RHK_Ysize`. It is the full width of the scanned area, edge to
  edge, so it counts `N` pitches and not `N - 1`, matching the same two readers.
- **Scan direction** comes from the **sign** of the scale. A positive
  `RHK_Yscale` means the rows advance towards increasing y, an upward scan, and
  a negative one a downward scan
  ([Gwyddion forum](https://sourceforge.net/p/gwyddion/discussion/fileformats/thread/3377ed98fa/),
  where the module author states that the sign indicates the direction, and
  [`rhk-sm4.c`](https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/rhk-sm4.c),
  which flips a page's rows exactly when `y_scale > 0`). The sign of
  `RHK_Xscale` does **not** give the fast direction: it is the same on the
  Forward and the Backward page of every file checked, so it describes the
  coordinate mapping of the stored array, not the way the tip ran along a line.

The pixel positions themselves are centred on `RHK_Xoffset`, which is the
centre of the scanned area
([evidence](#omicron--rhk-sm4-centre-vendor-manual-and-empirical-test-on-vendor-data)),
so pixel `i` of `N` sits at `offset - range/2 + (i + 0.5) * |scale|`. Placing a
coordinate at the centre of its pixel rather than at its edge is this reader's
convention, stated in the image orientation section above; RHK does not
prescribe it.

Test folders take `up`/`down` from the sign of `RHK_Yscale`.

| `RHK_Yscale` | raw row 0 is | gwyddionpy returns | to get row 0 = bottom |
|---|---|---|---|
| > 0 (up) | bottom | raw flipped in rows and columns | `np.flipud` |
| < 0 (down) | top | raw flipped in columns | `np.flipud` |

Evidence:

- Gwyddion RHK SM4 import module `modules/file/rhk-sm4.c`:
  `/* Correct flipping of up images */ gwy_data_field_invert(dfield, page->y_scale > 0.0, TRUE, FALSE);`
  i.e. rows are flipped for `y_scale > 0` and columns always.
  <https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/rhk-sm4.c>
- Gwyddion forum, "rhk-sm4: additional metadata and upward flipping" (2021):
  the sign of `y_scale` indicates the scan direction.
  <https://sourceforge.net/p/gwyddion/discussion/fileformats/thread/3377ed98fa/>
- RHK SM4 reader derived from Gwyddion (`RHKScanType` enum).
  <https://github.com/caldarolamartin/read_sm4_files/blob/master/devel_files/rhk-sm4.c>

Verified by reading each raw page (object id 4, int32) and comparing it with
gwyddionpy: every image page of an up file (`sm4_dflt_conf_up`) is flipped in
rows and columns, every image page of a down file (`sm4_dflt_conf_down`) in
columns only, as the table states.

## Scan region across the flavours

| Flavour | Offset keyword | Range keyword | Vendor meaning of the offset | [Evidence](#how-the-vendor-meaning-of-the-offset-was-resolved) |
|---|---|---|---|---|
| Nanonis `.sxm` STM, AFM | `:SCAN_OFFSET:` | `:SCAN_RANGE:` | centre | vendor file content, third-party readers |
| Omicron `.sm4` | `RHK_Xoffset`, `RHK_Yoffset` | none; `RHK_Xsize × \|RHK_Xscale\|` | centre | vendor manual, empirical test on vendor data |
| Bruker NanoScope `.spm` | `\X Offset`, `\Y Offset` | `\Scan Size` (x), `\Scan Size` / `\Aspect Ratio` (y) | centre | vendor manual |
| Bruker SPMLab `.FLT` | `OffsetX`, `OffsetY` | `ScanRangeX`, `ScanRangeY` | centre | empirical test on vendor data |
| Nanonis `.dat` STS | `Bias>Offset (V)` | none | bias sweep, no lateral frame | start and end read from `Bias Spectroscopy>Sweep Start (V)`, `>Sweep End (V)` |
| Bruker `.spm.txt` | `\X Offset`, `\Y Offset` | none | force ramp, no lateral frame | not applicable |

### How the vendor meaning of the offset was resolved

Each meaning carries one of five evidence grades, strongest first:

1. **vendor manual**: a document published by the instrument maker that
   defines the parameter.
2. **empirical test on vendor data**: raw files from the vendor's software
   where the scan geometry can be measured, and only one reading fits.
3. **vendor file content**: something the vendor's software writes into the
   raw file that only fits one reading.
4. **third-party reader**: an independent open-source reader that handles the
   format, e.g. Gwyddion; it shows how the community reads the value, not how
   the vendor defines it.
5. **none**: no source found.

The empirical tests locate a small scan inside a larger scan of the same area:
the small image is resampled to the pixel size of the large one, both are
line- and plane-levelled, and the small image is found by normalised
cross-correlation (`skimage.feature.match_template`). A centre offset and a
corner offset predict different positions; the pairs quoted below have
identical offsets, so the centre reading predicts the small scan in the middle
of the large one, whatever the axis directions.

#### Bruker NanoScope `.spm`: centre, vendor manual

- NanoScope Software 6.13 User Guide (Rev. D), Scan Controls panel, p. 60:
  "X offset, Y offset: Controls the center position of the scan in the X and Y
  directions, respectively. Range or Settings: ±220V; ± XXµm (dependent on Scan
  size and scanner)."
  <https://afmhelp.com/docs/manuals/Nanoscope6.13UserGuide.pdf>
- Same guide, "Optimizing the X Offset, Y Offset Parameter", p. 85: "Non-zero X
  and Y offsets reduce the maximum Scan size. Each volt of X or Y offset
  reduces the maximum scan size by 2V." Only a centred frame loses 2 V of size
  per volt of offset: both edges have to stay inside the piezo range. A corner
  offset would lose 1 V.
- Bruker help, Zoom and Offset Buttons: the Offset button "allows you to center
  the scan at the region of interest" and "updates the X and Y Offset
  parameters".
  <https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SoftwareGuide/Realtime/Tips/ZoomAndOffsetButtons.htm>

The ±220 V range places the offset in the scanner (piezo) frame. The guide is
for v6.13 while the test files are v9.4; the header key (`\X Offset` in
`\*Ciao scan list`) is unchanged, and no later Bruker page defines it
differently. Gwyddion's `nanoscope.c` ignores the offsets.

#### Nanonis `.sxm`: centre, vendor file content and third-party readers

- Vendor file content: every test `.sxm` (v4, v5 and v5e) carries the key
  `:Scan>Scanfield:`, written by the Nanonis Scan module, as
  `x;y;width;height;angle`, the order in which Nanonis defines a scan frame
  (centre, size, angle). Its `x;y` equals `:SCAN_OFFSET:`, e.g.
  `-235.464E-9;126.748E-9;5E-9;5E-9;0E+0` in `STM_nanonis_generic_5e.sxm`.
- `nanonis_control`, a Python client of the Nanonis TCP interface, documents
  `ScanFrameGet` as returning "centre: [float, float] - x and y value of the
  centre of the scan frame (m); size: [float, float] - width and height of the
  scan frame (m); angle: float - angle of the scan frame (°)".
  <https://github.com/dilwong/nanonis_control>
- Gwyddion `modules/file/nanonis.c`: frame origin set to
  `SCAN_OFFSET - 0.5 * SCAN_RANGE`.
  <https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/nanonis.c>

Not first-party: the SPECS SXM format description only says "Offset in x and y
for the scan. Unit is meters [m]"
(<https://sourceforge.net/p/gxsm/plugin-requests/3/>). The defining SPECS
document, the Nanonis *TCP Protocol Document* (`Scan.FrameSet`,
`Scan.FrameGet`), is available only through a MySPECS account and was not
checked.

#### Bruker SPMLab `.FLT`: centre, empirical test on vendor data

No vendor document defining `OffsetX` was found, so the meaning was measured on
A. James et al., *PiF-IR data of PMIS-C8 monolayer films on nanostructured and
planar Au substrates…*, [10.5281/zenodo.18060234](https://doi.org/10.5281/zenodo.18060234)
(CC BY 4.0, `AFM.zip`): SPMLab `.FLT` files (`Program=SPMLab`, `Version=1.00`,
closed-loop scanner linearisation on, `XLinOn=TRUE`, `YLinOn=TRUE`).

| 5 µm scan in 20 µm scan, `SIG_HEIGHT_SENSOR_FRW` | Offsets (µm) | NCC peak / next | Found at (µm) | Centre predicts | Corner predicts |
|---|---|---|---|---|---|
| `PMIS2-C8_ML2_p1_5__040925135420` in `PMIS2-C8_ML2_p1_20__040925132340` | (−33.59, 24.45), both | 0.54 / 0.10 | (10.00, 10.04) | (10.00, 10.00) | (2.50, 2.50) |

Positions are measured from the lower-left edge of the 20 µm scan. The 5 µm
scan sits in the middle of the 20 µm one, one pixel (39 nm) from the centre
prediction and 10.6 µm from the corner prediction. Three pairs of the same
record with different offsets agree (0.02, 0.05 and 0.7 µm from the centre
prediction). The match is found only with rows read bottom row first,
which also confirms the orientation above.

Other sources:

- Gwyddion `modules/file/spmlabf.c` passes `OffsetX`/`OffsetY` straight to
  `gwy_data_field_set_xoffset`/`set_yoffset`, i.e. reads a corner, without a
  cited source; the test contradicts it.
  <https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/spmlabf.c>
- SPMLab descends from Park Scientific's ProScan. The *User's Guide to
  AutoProbe CP, Part I* (Park Scientific Instruments, 48-101-1121 Rev. A,
  ProScan 1.5, 1998), p. 4-17: "The scanner coordinates are referenced to the
  scanner's undeflected, or home, position"; p. 4-18: the green cursor box
  updates "the scanner coordinates displayed in X Offset and Y Offset". It
  fixes the frame, not the reference point.
  <https://utw10193.utweb.utexas.edu/InstrumentManuals/micro-nano-afm-cp%20auto-prob-user-manual.pdf>
  (scanned; PDF pages 150 to 152)
- Not found: an SPMLab, ThermoMicroscopes or Veeco/Bruker Innova document
  defining `OffsetX`.

#### Omicron / RHK `.sm4`: centre, vendor manual and empirical test on vendor data

The `.sm4` files come from Omicron microscopes (e.g. the VT-STM) run by an RHK
R9 controller, so the file format and the offset are RHK's. No Scienta Omicron
document on the SM4 offset was found.

- RHK Technology, *R9 User Manual*, Appendix K, Scan Area Window, p. 195:
  "Move to Center: moves the Scan Area to the center of the Scan Range by
  setting the XY Offsets to 0." p. 197: "The Square button centers the Scan
  Area in the middle of the Scan Range."
  <https://www.manualslib.com/manual/2808818/Rhk-Technology-R9.html?page=195>

  The XY offset is the position of the scan-area centre, measured from the
  centre of the scanner range, and can take any value inside that range. An
  offset of 0 is the one case where the scan area is centred in the range,
  which is what "Move to Center" sets.

That defines the R9 software parameter; the page header stores the same thing:

- **Vendor file content.** `tests/data/omicron/stm/sm4_dflt_conf_down/Figure_6c.SM4`
  also carries the R9 parameter block (`RHK_PRMdata`): `X offset ::1.5773e-007 m`,
  `Y offset ::-2.7522e-008 m`, `Scan size ::1.0000e-007 m`. Its page header has
  `RHK_Xoffset = 1.6301e-07 m`, `RHK_Yoffset = -1.8566e-08 m`, within 5 to 9 nm
  of the software offsets, where a first-pixel reading would put them about
  50 nm (half the scan) apart.
- **Empirical test on vendor data.** P. M. Leidinger, *Influence of zinc oxide
  nanoparticles on the carbon accumulation on silver…*,
  [10.5281/zenodo.14268803](https://doi.org/10.5281/zenodo.14268803) (CC BY 4.0):
  STM topographs (`Topography_Forward`) from an Omicron VT-STM with an RHK
  controller.

| Scan pair, identical offsets | NCC peak / best elsewhere | Measured shift (nm) | Centre predicts | First pixel predicts |
|---|---|---|---|---|
| `VT231211_A1_0064` (10 nm) in `VT231211_A1_0065` (30 nm) | 0.71 / 0.54 | (0.53, 0.41) | (0.00, 0.00) | (9.96, 9.96) |
| `VT231205_A1_0064` (up) and `VT231205_A1_0063` (down), 20 nm | 0.44 / 0.38 | (0.94, 4.26) | (0.00, 0.00) | (0.00, 19.96) |

The 10 nm scan sits in the middle of the 30 nm one. The up and down scans
overlap, where a first-pixel reading, with `RHK_Yscale` of opposite sign, would
put them on `[Yoff - 20, Yoff]` and `[Yoff, Yoff + 20]` nm with no overlap. Three
pairs of the same record with different offsets agree as well. The residual few
nm are expected from piezo creep and drift of an open-loop STM scanner.

Other sources: Gwyddion `rhk-sm4.c` reads the offsets and never applies them;
spym (`rhksm4`, <https://github.com/rescipy-project/spym>) drops them for image
pages. RHK's "SM4 Data File Format for R9" and "Parsing an SM4 file", which
would define the header fields directly, are not publicly available.

### Axes

Two groups answer two different questions, and they are written independently
of each other.

- **`NXdata` shows the image.** It is the picture as it should be displayed:
  normalised to the bottom-left convention above, both axes ascending, the scan
  angle not applied. Every 2D image uses the axis names `X` and `Y`, upper
  case, with `@axes = [Y, X]`, because `@axes` names the axis of each data
  dimension in order and dimension 0 is the slow axis. One-dimensional data
  (STS bias sweep, force ramp) keeps its own single axis name.
- **`NXspm_scan_control` records how the scan was performed.** It describes the
  movement of the tip over the sample, not the picture, so the flips applied to
  the image never change it.

#### `independent_scan_axes` and the scan direction

`independent_scan_axes` lists the scan axes "in the order of axes of the scan
from the fastest to the slowest", so a mesh scan gives the fast axis first. The
direction the tip travelled along each axis is kept as the sign of the axis
name:

| Value | Meaning |
|---|---|
| `+Y` | the axis was travelled towards increasing Y |
| `-Y` | the axis was travelled towards decreasing Y |
| `Y` | no single direction is asserted |

An axis is signed when the entry holds exactly one pass along it and the format
records which way that pass ran. It is left bare otherwise, which covers two
cases: a bidirectional axis, which has both a forward and a backward `NXdata`
group, and an axis whose direction the format never records.

`X` and `Y` are the axes of the **scan frame**, the fast and the slow axis. When
`scan_region/scan_angle_*` is not zero the scan frame is rotated against the
sample, so they are not the x and y of the sample.

Where each sign comes from:

| Flavour | Fast axis | Slow axis |
|---|---|---|
| Nanonis `.sxm` | `X`: `DATA_INFO` `Direction` is `both`, so forward and backward are stored | `+Y` / `-Y` from `SCAN_DIR` (`up` / `down`); bare when the tag is missing or empty |
| Bruker NanoScope `.spm` | `X`: Trace and Retrace layers are both stored | `+Y` / `-Y` from `\Frame direction` (`Up` / `Down`) |
| Omicron `.sm4` | `X`: `RHK_ScanType` names the two passes, Forward and Backward, but neither it nor `RHK_Xscale`, whose sign is the same on both pages, says which way the tip ran along a line | `+Y` / `-Y` from the sign of `RHK_Yscale` |
| Bruker SPMLab `.FLT` | `+X` / `-X` from `ScanDirection` (`FORWARD` / `BACKWARD`): one channel per file | `Y`: SPMLab stores no slow scan direction |

Bruker `.FLT` is the mirror image of the others: it is the one format whose
fast direction is known per file and whose slow direction is not recorded at
all. A bare `Y` there means unknown, not upward.

## Test data

### Folder naming

`<vendor>/<technique>/<name>`, where `<name>` is

- Nanonis: `v_gen_<version>_<config>[_<direction>]`, with `<version>` taken from
  the header tag `NanonisMain>SW Version` (e.g. `Generic 5e` → `5e`).
- Bruker NanoScope: `spm_v_<version>_<config>[_<direction>]`, with `<version>`
  the major and minor version of the header key `\Version` (e.g. `0x09400202`
  → `9_4`).
- Other vendors: `<format>_<config>[_<direction>]`, e.g. `flt_dflt_conf`.

| Part | Values |
|---|---|
| `<config>` | `dflt_conf`: the default config shipped with the package; `descrb_nx_dt`: a `config.json` in the folder that describes the NXdata groups. |
| `<direction>` | `up` or `down`, the slow scan direction from the raw header. Left out when the data is not an image (STS) or the format stores no slow direction. |

### Missing scan directions

- `nanonis/afm`: only an `up` scan. No openly licensed Nanonis AFM `down` scan
  was found (Zenodo, Figshare, GitHub); the `down` flip is
  covered by the `nanonis/stm` down scans, which use the same code path.

### Provenance of data taken from public datasets

| Folder | Raw file | Dataset | Licence |
|---|---|---|---|
| `nanonis/stm/v_gen_4_dflt_conf_up` | `STM_WTip_WSe2-SL445_055.sxm` | D. Smalley, *Scanning Tunneling Microscope Images of Atomic Scale Defects in Tungsten Diselenide*, [10.5281/zenodo.10443995](https://doi.org/10.5281/zenodo.10443995) | CC BY 4.0 |
| `nanonis/stm/v_gen_4_dflt_conf_down` | `STM_WTip_WSe2-SL445_056.sxm` | as above; recorded directly after `_055` over the same area | CC BY 4.0 |
| `nanonis/stm/v_gen_4_descrb_nx_dt_up` | `const_dos_No14_003.sxm` | L. M. Rütten et al., *Data underlying the paper "Direct signatures of d-level hybridization and dimerization in magnetic adatom chains on a superconductor"*, [10.5281/zenodo.17533355](https://doi.org/10.5281/zenodo.17533355) | CC BY 4.0 |
| `nanonis/stm/v_gen_4_descrb_nx_dt_down` | `const_dos_No14_002.sxm` | as above; recorded directly before `_003` over the same area (non-square 48 × 72 px, scan angle 108.5°) | CC BY 4.0 |
| `omicron/stm/sm4_dflt_conf_down` | `Figure_6c.SM4` (original name `Figure 6(c).SM4`) | A. Shrestha, *Accommodating a Hexagonal Zeta-phase Mn2N Film on a Cubic MgO (001) Substrate*, [10.5281/zenodo.11043571](https://doi.org/10.5281/zenodo.11043571) | CC BY 4.0 |
| `bruker/afm/spm_v_9_4_dflt_conf_up` | `tecky.0_00002.spm` | J. Vymazal et al., *Dataset for 'Layer-dependent oxidation spreading in multilayer graphene during AFM local anodic oxidation'*, [10.5281/zenodo.19707666](https://doi.org/10.5281/zenodo.19707666) (folder `Data/Figure 7`) | CC BY 4.0 |
