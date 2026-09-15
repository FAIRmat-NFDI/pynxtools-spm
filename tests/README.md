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
in this test set. It stores row 0 at the **top** (left-handed coordinates), so a
correctly oriented signal equals `np.flipud` of the matching Gwyddion channel.

## Where each vendor stores the scan direction

The notes below record which raw metadata decides the orientation of an image,
and where that knowledge comes from. Add to them when a vendor is handled.

### Nanonis (`.sxm`)

The same rules apply to STM and AFM scans; both are read by `NanonisBase`.

| Header tag | Meaning |
|---|---|
| `SCAN_DIR` | `up` or `down`: the slow scan direction. |
| `SCAN_OFFSET` | x and y of the **centre** of the scan frame (m). |
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
  depending on `SCAN_DIR`, flips backward channels horizontally, and sets the
  frame origin to `SCAN_OFFSET - 0.5 * SCAN_RANGE`, i.e. `SCAN_OFFSET` is the
  frame centre.
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
| `\X Offset`, `\Y Offset` | offsets that use the sample as position reference; a more negative Y Offset moves a feature down on the image display. |

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
files up to 25 MB in the S3 Zenodo mirror were checked), so direction
independence rests on the Gwyddion module above.

### Bruker SPMLab (`.FLT`)

| Header key (`[Data Parameters]`) | Meaning |
|---|---|
| `ScanDirection` | `FORWARD` or `BACKWARD`: the fast (line) direction of this file. No slow scan direction is stored. |
| `OffsetX`, `OffsetY` | origin (corner) of the scan frame. |
| `ScanRangeX`, `ScanRangeY` | width and height of the scan frame. |
| `ResolutionX`, `ResolutionY` | pixels per line and number of lines. |
| `Rotation` | rotation of the scan frame (deg); not applied. |

The rows are stored bottom row first, so the image gets one `np.flipud` against
gwyddionpy, like a NanoScope `.spm` file. The test folders carry no up/down
suffix because the format records no slow scan direction.

Evidence:

- Gwyddion SPMLab import module `modules/file/spmlabf.c`: turns every image
  upside down once (`gwy_data_field_invert(dfield, TRUE, FALSE, FALSE)`), sets
  the origin from `OffsetX`/`OffsetY`, and keeps `ScanDirection` and `Rotation`
  as metadata only.
  <https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/spmlabf.c>

### Omicron / RHK (`.sm4`)

| Page header field | Meaning |
|---|---|
| `RHK_ScanType` | `RIGHT`/`LEFT` for the forward/backward image: the fast (line) direction. |
| `RHK_Yscale` | step between rows; row i sits at y = `RHK_Yoffset` + i × `RHK_Yscale`. Its sign is the slow scan direction: > 0 up, < 0 down. |
| `RHK_Xscale` | step between columns; negative in every file seen so far. |
| `RHK_Xsize`, `RHK_Ysize` | pixels per line and number of lines. |

Test folders take `up`/`down` from the sign of `RHK_Yscale`.

| `RHK_Yscale` | raw row 0 is | gwyddionpy returns | to get row 0 = bottom |
|---|---|---|---|
| > 0 (up) | bottom | raw flipped in rows and columns | `np.flipud` |
| < 0 (down) | top | raw flipped in columns | `np.flipud` |

Evidence:

- Gwyddion RHK SM4 import module `modules/file/rhk-sm4.c`:
  `/* Correct flipping of up images */ gwy_data_field_invert(dfield, page->y_scale > 0.0, TRUE, FALSE);`
  i.e. rows are flipped for `y_scale > 0` and columns always; the offsets are
  kept as metadata only.
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
  was found (S3 Zenodo mirror, Zenodo, Figshare, GitHub); the `down` flip is
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
