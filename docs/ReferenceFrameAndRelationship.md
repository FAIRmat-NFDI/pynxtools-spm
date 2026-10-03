# Reference frames in SPM and their relationships

Status: working note, not yet part of the published docs.
Convention: the **scanner frame** is the central frame of reference. This is
already the practice in pynxtools-spm: `scan_offset_value_*`, `scan_start_*` and
`scan_end_*` are measured from the scanner's undeflected centre, and stage keys
are kept separate ([scan-region conventions][repo-scan], "Frames of reference").
This note makes that choice explicit and extends it to the scan, probe, stage
and sample frames. Every other frame is defined relative to the scanner frame,
directly or through one intermediate frame.

## Why the scanner frame is central

| Candidate | Stable across scans? | Known from the raw file? | Verdict |
|---|---|---|---|
| Scan frame | No, it moves with every offset and angle | Yes | Unsuitable as root |
| **Scanner frame** | Yes, fixed by the instrument | Yes, offsets and angles are given in it | **Chosen** (already in use) |
| Stage frame | Yes, while the coarse motors stay put | Sometimes (e.g. Bruker `\Stage X`) | Too often missing |
| Sample frame | Yes, per loading | Rarely, needs fiducials | Too often missing |

The vendor parameters that place a scan (offset, scan angle) are already
expressed in the scanner frame. Bruker says so explicitly: "The Scan Angle
parameter defines the degree of rotation between the axis upon which the scanner
travels and the scanner's x-axis" ([Bruker, Raster Scan Parameters][bruker-raster]).

## The five frames

Every frame is right-handed and Cartesian.

### 1. Scanner frame (central)

| Property | Definition |
|---|---|
| Origin | Undeflected piezo position: offset = 0, scan angle = 0, Z piezo at its zero |
| Axes | `X`, `Y`: the scanner's lateral drive axes. `Z`: normal to the sample plane, pointing from the sample towards the probe |
| Physical meaning | The **relative tip–sample displacement**, which covers both tip-scanning (e.g. Bruker Dimension) and sample-scanning (e.g. Bruker MultiMode) |
| Set by | Instrument design and scanner calibration (V → m) |
| Lifetime | Fixed for an instrument and scanner. Changes only on recalibration or a scanner swap |
| Units | Length. Some vendors store offsets in volts (Bruker: ±220 V), which must be converted with the scanner calibration |

### 2. Scan frame (one per image)

| Property | Definition |
|---|---|
| Origin | Centre of the scan area (repo convention: offset = centre, see [scan-region conventions][repo-scan]) |
| Axes | `x_s`: fast scan axis. `y_s`: slow scan axis. `z_s` = scanner `Z` |
| Set by | Scan offset `o = (o_x, o_y)` and scan angle `θ`, both in the scanner frame |
| Lifetime | One image or one scan entry |
| Pixel grid | Contained in this frame, so no separate frame is needed: pixel `(i, j)` of `(N_x, N_y)` sits at `u = ((i + ½)·step_x − range_x/2, (j + ½)·step_y − range_y/2)`, with `step = range / N`, origin at the bottom-left |

### 3. Probe frame

| Property | Definition |
|---|---|
| Origin | Tip apex |
| Axes | `x_p`: projection of the cantilever's long axis, pointing from the chip towards the free end. `z_p`: tip axis, pointing from the apex up to the cantilever. `y_p` = `z_p × x_p`, the torsion-sensing direction for LFM, TFM and lateral PFM |
| Set by | Chip mount and alignment: cantilever tilt `α` (typically ~10–22°), in-plane angle `φ` between `x_p` and scanner `X` |
| Lifetime | Fixed while one probe is mounted |
| Why it matters | The angle between the fast axis and the cantilever controls lateral and torsional signals. With `θ` and `φ` both measured from scanner `X`, that angle is `θ − φ` (compensate pre scan cantilever orientation so that for `θ`= 0, scan will perform along `X` axis.). If a vendor measures its scan angle from the cantilever instead, the vendor value is already this relative angle, and `θ + φ` gives the fast axis relative to scanner `X`. In the cantilever-referenced sense, 0° means fast axis ∥ cantilever and 90° means fast axis ⊥ cantilever ([lateral PFM][lpfm]) |

#### Rule for using `θ − φ`

The scan angle relative to the cantilever, `θ − φ`, may be computed from the
scan angle `θ` (raw file) and the probe angle `φ` (settings) only if all three
conditions hold:

1. **`θ` is measured from scanner `X`.** Documented for Bruker
   ([Raster Scan Parameters][bruker-raster]). Not yet checked for other vendors,
   see [open questions](#open-questions).
2. **`φ` is known.** It is rarely in raw files. It usually comes from either:
    - the head or holder design, e.g. `φ ≈ 0` when the cantilever is aligned
      with scanner `X`, or
    - the user or the ELN.
3. **`θ` and `φ` use the same sign convention**, both counter-clockwise when
   viewed from `+Z`.

**Storage:** keep `θ` (raw, from the file) and `φ` (from the settings or ELN) as
separate fields. Write `θ − φ` only as a derived value, never in place of `θ`, so
that a later correction of `φ` cannot corrupt the raw scan angle.

### 4. Stage frame (coarse positioner, includes the sample holder)

| Property | Definition |
|---|---|
| Origin | Home or zero position of the coarse positioner |
| Axes | Directions of coarse-motor travel, nominally ∥ to scanner `X`, `Y`, `Z` |
| Set by | Coarse positioner (stick-slip piezo, stepper motor, ball-bearing stage) |
| Lifetime | Fixed between coarse moves |
| Sample holder | The holder is the plate or puck the sample is glued or clamped to. It sits on the stage and moves with it, so it is treated as part of the stage frame and adds no transform of its own |
| Exception: removable holder | If the holder is taken out and put back between scans (e.g. a UHV transfer plate), it never lands in exactly the same place. Then define a separate **holder frame** between stage and sample, and measure its position again after every insertion |

### 5. Sample frame

| Property | Definition |
|---|---|
| Origin | A point on the sample that can be found again, called a fiducial: a marker, a scratch, a sample corner or a distinctive feature |
| Axes | `x`: along a straight reference on the sample, such as an edge, a line of markers or a crystal direction. `z`: normal to the sample surface. `y` = `z × x` |
| Set by | How the sample was mounted on the holder (position and rotation). The SPM cannot change it during a measurement |
| Lifetime | Until the sample is removed or remounted |
| Relation to stage | Translation `m`: where the sample origin sits in stage coordinates. Rotation `γ`: angle between sample `x` and stage `X` |
| How it is found | Image at least two fiducials and note their stage and scanner coordinates, then solve for `m` and `γ`. Two points give translation and rotation. Three or more also give scale and shear (an affine transform) ([correlative microscopy][fiducial]) |

## Relationship graph

The arrows point in the `depends_on` direction, towards the central frame.

```text
  Scan frame (per image) ──[ offset o, scan angle θ ]────────────────┐
                                                                     │
  Probe frame ─────────────[ tilt α, in-plane angle φ ]──────────────┤
                                                                     ▼
                                                        Scanner frame (central)
                                                                     ▲
  Stage frame ─────────────[ coarse position s, misalignment β≈0 ]───┘
       ▲
       │  [ mount translation m, rotation γ (from fiducials) ]
       │
  Sample frame
```

| Frame | `depends_on` | Transform parameters |
|---|---|---|
| Scanner | — (end of every chain) | — |
| Scan | Scanner | Offset `o`, scan angle `θ` |
| Probe | Scanner | Tilt `α`, in-plane angle `φ` |
| Stage | Scanner | Coarse position `s`, misalignment `β` (≈ 0) |
| Sample | Stage | Mount translation `m`, rotation `γ` |

## Transforms

`R(·)` is a rotation about `Z`, counter-clockwise positive when viewed from `+Z`
(the probe looking down). Vendor sign conventions for `θ` are **not yet
verified** (see open questions).

Every transform maps a point from a frame into the frame it depends on, in the
same direction as `depends_on` and NeXus transformation chains. Symbols: `u`
(scan), `p` (scanner), `q` (stage), `r` (sample).

| From → to | Transform | Parameters | Source of parameters |
|---|---|---|---|
| Scan → scanner | `p = o + R(θ) · u` | `o`, `θ` | Raw file (offset, scan angle) |
| Probe → scanner | Rotation `R_z(φ) · R_y(α)`, origin = current tip position `p` | `α`, `φ` | Probe or holder spec, alignment |
| Stage → scanner | `p = R(β)ᵀ · (q − s)` | `s`, `β` | Stage keys if present, `β` assumed 0 |
| Sample → stage | `q = m + R(γ) · r` | `m`, `γ` | Fiducial registration, per loading |

Meaning of the parameters:

- `o`: scan centre in scanner coordinates. `θ`: angle of the fast axis from scanner `X`.
  The rotation pivots about the scan centre, because `u` is rotated about the scan
  frame's own origin before it is shifted by `o`.
- `s`: coarse position in stage coordinates. When the coarse positioner moves by
  `s`, a point fixed on the stage shifts by `−s` in scanner coordinates, hence
  `q − s`. Whether vendors report `s` as tip or stage displacement is not yet
  verified. `β`: misalignment between stage and scanner axes.
- `m`: sample origin in stage coordinates. `γ`: angle between sample `x` and
  stage `X`.

To go the other way, e.g. from a scan pixel to sample coordinates, chain up to
the scanner frame and then apply the inverses down to the target frame:

```text
pixel (i, j) → u → p = o + R(θ)·u          (scan → scanner)
             → q = s + R(β)·p              (inverse of stage → scanner)
             → r = R(γ)ᵀ·(q − m)           (inverse of sample → stage)
```

### Data are not transformed

The measured data stay on the scan-frame grid. Only the transforms are recorded,
as metadata. Users who need scanner, stage or sample coordinates apply the chain
themselves. This avoids resampling and keeps the data as measured.

## NeXus encoding (sketch)

```text
scanner_frame: NXcoordinate_system              # central frame, end of all chains
  depends_on = "."

scan_frame: NXcoordinate_system
  depends_on = "transformations/scan_angle"
  transformations: NXtransformations
    scan_angle = θ    @transformation_type=rotation    @vector=[0,0,1]       @depends_on="offset"
    offset     = |o|  @transformation_type=translation @vector=[o_x,o_y,0]/|o| @depends_on="/…/scanner_frame"

probe_frame: NXcoordinate_system
  depends_on = "transformations/tilt"
  transformations: NXtransformations
    tilt     = α  @transformation_type=rotation @vector=[0,1,0] @depends_on="in_plane"
    in_plane = φ  @transformation_type=rotation @vector=[0,0,1] @depends_on="/…/scanner_frame"

stage_frame: NXcoordinate_system
  depends_on = "transformations/coarse_position"
  transformations: NXtransformations
    coarse_position = |s| @transformation_type=translation @vector=-s/|s| @depends_on="/…/scanner_frame"   # β = 0; stage origin sits at −s in scanner coordinates

sample_frame: NXcoordinate_system
  depends_on = "transformations/mount_rotation"
  transformations: NXtransformations
    mount_rotation    = γ   @transformation_type=rotation    @vector=[0,0,1]  @depends_on="mount_translation"
    mount_translation = |m| @transformation_type=translation @vector=m/|m|    @depends_on="/…/stage_frame"
```

See [NXcoordinate_system][nx-cs] and [NXtransformations][nx-tr] for the
`depends_on` semantics. The group names above are placeholders. The final names
belong in NXspm.

## Fit with the current pynxtools-spm convention

From [`docs/explanation/scan-region-conventions.md`][repo-scan]:

| Existing rule | Consistent with this note? |
|---|---|
| `scan_offset_value_*` = centre of the scan area | Yes: this is `o`, the scan-frame origin in the scanner frame |
| `scan_start/end = offset ∓ range/2` | Yes, when `θ = 0` |
| `scan_angle_*` "recorded but never applied to the data" | Yes, see [Data are not transformed](#data-are-not-transformed) |
| Stage keys "never combined with the offset" | Yes: the stage frame is a separate link in the chain |
| `NXdata` axis value `X_i = offset − range/2 + (i + ½)·step` | **Only exact for `θ = 0`.** For `θ ≠ 0` the axis values combine the scanner-frame origin `o` with scan-frame directions. They are not true scanner coordinates. This should be stated in the docs, or the axes should be given in pure scan-frame coordinates `u` |

## Open questions

1. **Sign of `θ` for each vendor.** Is a positive scan angle counter-clockwise
   when viewed from above, for Nanonis `:SCAN_ANGLE:`, Bruker `\Rotate Ang.`,
   SPMLab `Rotation` and RHK `RHK_Angle`? Not verified yet.
1. **Reference of `θ` for each vendor.** Is the scan angle measured from scanner
   `X` (Bruker: "the scanner's x-axis", [Raster Scan Parameters][bruker-raster])
   or from the cantilever axis? This decides between `θ − φ` and `θ + φ` in the
   probe frame. Bruker notes that Lateral Force Mode needs "scan angles other
   than 0 degrees", which suggests `φ ≈ 0` (cantilever ∥ scanner `X`) there.
   Not verified for other vendors.
2. **Rotation pivot.** Do all vendors rotate about the scan centre, or about the
   scanner origin?
3. **Bruker offset sign.** "a more negative X Offset value will move a feature in
   the current image to the left on the Image display"
   ([Bruker, Scan View Parameters Tips][bruker-tips]). Does this match `o`
   pointing in `+X`, or is the sign flipped for sample-scanning heads?
4. **Probe angles `α`, `φ`.** Rarely in raw files. Should they come from the
   ELN/user input?
5. **Non-rigid effects.** Drift ([ISO 11039][iso11039]), creep and piezo
   nonlinearity make scan → scanner only approximately rigid. Store drift and
   calibration separately, not inside the transform.
6. **Lab frame.** Add it as a sixth frame only when correlating with other
   instruments or recording the direction of gravity or of external fields.

## Sources

### Verified (text read and quoted)

- Bruker NanoScope help, *Raster Scan Parameters*. Scan angle relative to the scanner's x-axis. [Link][bruker-raster]
- Bruker NanoScope help, *Scan Panel*. "Controls the angle of the X (fast) scan relative to the sample". Offsets ±220 V. [Link][bruker-panel]
- Bruker NanoScope help, *Scan View Parameters Tips*. "These parameters use the sample as the position reference". [Link][bruker-tips]
- pynxtools-spm, *Scan region, axes and scan direction*. [Link][repo-scan]

### Not yet read in full (seen only in search summaries)

- Lateral PFM, scan angle relative to the cantilever. [arXiv 2305.03864][lpfm]
- Torsional force microscopy, PNAS 2024. [PNAS](https://www.pnas.org/doi/10.1073/pnas.2314083121)
- Patent defining lab, cantilever and tilt angles. [US 11644478](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11644478)
- PTB metrological large-range SPM (stage + piezo + interferometers). [RSI 2004](https://pubs.aip.org/aip/rsi/article-abstract/75/4/962/466407/Metrological-large-range-scanning-probe-microscope) · [RSI 2009](https://pubs.aip.org/aip/rsi/article-abstract/80/4/043702/282343/A-metrological-large-range-atomic-force-microscope)
- NIST six-axis interferometer positioning for SPM. [PMC3926591](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3926591/)
- Topography-based navigation in an mK STM with position markers (stage ↔ sample). [arXiv 2606.04848](https://arxiv.org/html/2606.04848)
- Fiducial-based correlative microscopy (stage ↔ sample per loading). [US 9368321][fiducial] · [nanoGPS, MST](https://iopscience.iop.org/article/10.1088/1361-6501/abce39)
- Britton et al., *Tutorial: Crystal orientations and EBSD — Or which way is up?* The template for linking several frames. [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:13ae1391-937e-4a1b-9d44-66b39ed392b7)
- kikuchipy, *Reference frames* tutorial. [Docs](https://kikuchipy.readthedocs.io/en/stable/tutorials/reference_frames.html)
- ISO 11039:2012, SPM drift rate. [ISO][iso11039]
- ISO 18115-2:2021, SPM vocabulary. [ISO](https://committee.iso.org/standard/83146.html)

No published SPM document defining all five frames together was found.

[bruker-raster]: https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SPM%20Training%20Guide/Raster%20Scan%20Parameters.htm
[bruker-panel]: https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SoftwareGuide/Realtime/Views/ScanPanelInterface.htm
[bruker-tips]: https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SoftwareGuide/Realtime/Tips/ScanViewParametersTips.htm
[repo-scan]: explanation/scan-region-conventions.md
[lpfm]: https://arxiv.org/pdf/2305.03864
[fiducial]: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9368321
[nx-cs]: https://manual.nexusformat.org/classes/base_classes/NXcoordinate_system.html
[nx-tr]: https://manual.nexusformat.org/classes/base_classes/NXtransformations.html
[iso11039]: https://www.iso.org/standard/46603.html
