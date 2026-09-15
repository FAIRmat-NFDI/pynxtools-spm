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

`\Frame direction: Up|Down` in the image list header. To be completed when the
Bruker flavour is handled.

### Bruker SPMLab (`.FLT`)

`ScanDirection=FORWARD|BACKWARD` only; no slow scan direction is stored. To be
completed when the FLT flavour is handled.

### Omicron / RHK (`.sm4`)

`RHK_ScanType` enumerates `RIGHT=0, LEFT=1, UP=2, DOWN=3`; Gwyddion decides the
vertical orientation from the sign of the page's `y_scale`. To be completed when
the SM4 flavour is handled.

Sources:

- Gwyddion forum, "rhk-sm4: additional metadata and upward flipping" (2021).
  <https://sourceforge.net/p/gwyddion/discussion/fileformats/thread/3377ed98fa/>
- RHK SM4 reader derived from Gwyddion (`RHKScanType` enum).
  <https://github.com/caldarolamartin/read_sm4_files/blob/master/devel_files/rhk-sm4.c>

## Test data

### Folder naming

`<vendor>/<technique>/<name>`, where `<name>` is

- Nanonis: `v_gen_<version>_<config>[_<direction>]`, with `<version>` taken from
  the header tag `NanonisMain>SW Version` (e.g. `Generic 5e` → `5e`).
- Other vendors: `<format>_<config>[_<direction>]`, e.g. `spm_v_9_4_dflt_conf_down`.

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
