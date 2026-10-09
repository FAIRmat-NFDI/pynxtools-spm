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
| Origin | Either the undeflected piezo position (offset = 0, scan angle = 0, Z piezo at its zero) or the centre found by the scanner calibration, which also fixes the axis directions. NXspm records which one in `scanner_frame/origin` |
| Axes | `X`, `Y`: the scanner's lateral drive axes. `Z`: normal to the sample plane, pointing from the sample towards the probe |
| Physical meaning | The **relative tip–sample displacement**, which covers both tip-scanning (e.g. Bruker Dimension) and sample-scanning (e.g. Bruker MultiMode) |
| Set by | Instrument design and scanner calibration (V → m) |
| Lifetime | Fixed for an instrument and scanner. Changes only on recalibration or a scanner swap |
| Units | Length. Some vendors store offsets in volts (Bruker: ±220 V), which must be converted with the scanner calibration |

Decisions: [D1](#d1), [D3](#d3), [D4](#d4), [D5](#d5), [D22](#d22), [D23](#d23), [D24](#d24), [D25](#d25), [D26](#d26), [D27](#d27).

### 2. Scan frame (one per image)

| Property | Definition |
|---|---|
| Origin | Centre of the scan area (repo convention: offset = centre, see [scan-region conventions][repo-scan]) |
| Axes | `x_s`: fast scan axis. `y_s`: slow scan axis. `z_s` = scanner `Z` |
| Set by | Scan offset `o = (o_x, o_y)` and scan angle `θ`, both in the scanner frame |
| Lifetime | One image or one scan entry |
| Pixel grid | Contained in this frame, so no separate frame is needed: pixel `(i, j)` of `(N_x, N_y)` sits at `u = ((i + ½)·step_x − range_x/2, (j + ½)·step_y − range_y/2)`, with `step = range / N`, origin at the bottom-left |

Decisions: [D6](#d6), [D7](#d7).

### 3. Probe frame (AFM cantilever)

| Property | Definition |
|---|---|
| Origin | Clamped end of the cantilever on the chip. This is the convention of cantilever beam mechanics: "The cantilever is firmly clamped at one end and the tip is located at the other end", with the tip load "at position x = L" ([Platz et al.][platz]) |
| Axes | `x_p`: along the cantilever's long axis, pointing from the chip towards the tip. The tip sits at `x_p = L`, the cantilever length. `z_p`: normal to the cantilever, pointing away from the tip side. `y_p` = `z_p × x_p`, the torsion-sensing direction for LFM, TFM and lateral PFM |
| Set by | Chip mount and alignment: cantilever tilt `α` (usually about 10°–15° [P4], positive when the tip end is lower than the chip end; Bruker `\Cantilever Angle`), in-plane angle `φ` between `x_p` and scanner `X` |
| Tip position | Not part of the probe frame. During a scan the tip position is the scanner-frame point `p` (the piezo position) |
| Lifetime | Fixed while one probe is mounted |
| Why it matters | The angle between the fast axis and the cantilever controls lateral and torsional signals. With `θ` and `φ` both measured from scanner `X`, that angle is `θ − φ` (compensate pre scan cantilever orientation so that for `θ`= 0, scan will perform along `X` axis.). If a vendor measures its scan angle from the cantilever instead, the vendor value is already this relative angle, and `θ + φ` gives the fast axis relative to scanner `X`. In the cantilever-referenced sense, 0° means fast axis ∥ cantilever and 90° means fast axis ⊥ cantilever ([lateral PFM][lpfm]) |

Decisions: [D10](#d10), [D11](#d11), [D12](#d12), [D13](#d13).

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

### 4. Stage frame (sample stage or coarse positioner, includes the sample holder)

| Property | Definition |
|---|---|
| Origin | Home or zero position of the coarse positioner |
| Axes | Directions of stage travel, nominally ∥ to scanner `X`, `Y`, `Z` |
| Direction of each axis | Each axis may move the sample or the head. On a Bruker Dimension Icon, "The XY stage permits micrometer-scale positioning of samples beneath the tip", while the motorized Z stage provides "tip engagement and approach" ([Bruker, System Overview][bruker-overview]). The direction in which a positive value moves the sample relative to the tip therefore depends on the instrument and the axis, and is recorded per file |
| In raw files | Bruker `.spm`: `\Stage X`, `\Stage Y`, `\Stage Z`, without a unit in the header (`\Engage X Pos` is in µm). The Bruker stage is "open loop (unencoded)" ([Bruker, Stage System][bruker-stage]). Nanonis `.sxm` and `.dat`: no stage position. Then the stage frame coincides with the scanner frame. The Nanonis coarse-motor approach direction is set per instrument (`plus` or `minus`, [rusty-tip #29][rusty-tip]) |
| Set by | Coarse positioner (stick-slip piezo, stepper motor, ball-bearing stage) |
| Lifetime | Fixed between coarse moves |
| Sample holder | The holder is the plate or puck the sample is glued or clamped to. It sits on the stage and moves with it, so it is treated as part of the stage frame and adds no transform of its own |
| Exception: removable holder | If the holder is taken out and put back between scans (e.g. a UHV transfer plate), it never lands in exactly the same place. Then define a separate **holder frame** between stage and sample, and measure its position again after every insertion |

Decisions: [D14](#d14), [D15](#d15), [D16](#d16), [D17](#d17), [D18](#d18).

### 5. Sample frame

| Property | Definition |
|---|---|
| Origin | A point on the sample that can be found again, called a fiducial: a marker, a scratch, a sample corner or a distinctive feature |
| Axes | `x`: along a straight reference on the sample, such as an edge, a line of markers or a crystal direction. `z`: normal to the sample surface. `y` = `z × x` |
| Set by | How the sample was mounted on the holder (position and rotation). The SPM cannot change it during a measurement |
| Lifetime | Until the sample is removed or remounted |
| Relation to stage | Rotation `γ`: angle between sample `x` and stage `X`. Translation `m = (m_x, m_y, m_z)`: where the sample origin sits in stage coordinates |
| How it is found | Image at least two fiducials and note their stage and scanner coordinates, then solve for `m` and `γ`. Two points give translation and rotation. Three or more also give scale and shear (an affine transform) ([correlative microscopy][fiducial]) |

Decisions: [D21](#d21).

## Relationship graph

The arrows point in the `depends_on` direction, towards the central frame.

```text
  Scan frame (per image) ──[ offset o, scan angle θ ]────────────────┐
                                                                     │
  Probe frame ─────────────[ tilt α, in-plane angle φ ]──────────────┤
                                                                     ▼
                                                        Scanner frame (central)
                                                                     ▲
  Stage frame ─────────────[ stage position s, misalignment β≈0 ]────┘
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
| Stage | Scanner | Stage position `s`, misalignment `β` (≈ 0) |
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
| Probe → scanner | Rotation `R_z(φ) · R_y(α)`, orientation only | `α`, `φ` | Probe or holder spec, alignment |
| Stage → scanner | `p = q + Σᵢ sᵢ·vᵢ` (with `β = 0`) | `sᵢ`, `vᵢ` | Stage keys if present, `vᵢ` from the instrument, `β` assumed 0 |
| Sample → stage | `q = m + R(γ) · r` | `m`, `γ` | Fiducial registration, per loading |

Meaning of the parameters:

- `o`: scan centre in scanner coordinates. `θ`: angle of the fast axis from scanner `X`.
  The rotation pivots about the scan centre, because `u` is rotated about the scan
  frame's own origin before it is shifted by `o`.
- `sᵢ`: stage position along axis `i` (x, y, z). `vᵢ`: unit vector, in the scanner
  frame, along which a positive `sᵢ` moves the sample relative to the tip. It
  depends on the instrument and the axis (sample-moving or head-moving), so it is
  recorded per file, not fixed. `β`: misalignment between stage and scanner axes.
- `α`: positive when the tip end of the cantilever is lower than the chip end.
  With `x_p` pointing from the chip towards the tip, this is a rotation about `+y_p`.
- `m`: sample origin in stage coordinates. `γ`: angle between sample `x` and
  stage `X`. The rotation is applied first, about the sample origin, then the
  translations along stage `x`, `y` and `z`.

To go the other way, e.g. from a scan pixel to sample coordinates, chain up to
the scanner frame and then apply the inverses down to the target frame:

```text
pixel (i, j) → u → p = o + R(θ)·u          (scan → scanner)
             → q = p − Σᵢ sᵢ·vᵢ             (inverse of stage → scanner, β = 0)
             → r = R(γ)ᵀ·(q − m)           (inverse of sample → stage)
```

### Data are not transformed

The measured data stay on the scan-frame grid. Only the transforms are recorded,
as metadata. Users who need scanner, stage or sample coordinates apply the chain
themselves. This avoids resampling and keeps the data as measured.

## NeXus encoding (as defined in NXspm and NXafm)

```text
ENTRY
  scanner_frame: NXcoordinate_system               # the only NXcoordinate_system; end of every chain
    origin = "undeflected piezo position" | "calibrated piezo position"
    type = "cartesian"   x = [1,0,0]   y = [0,1,0]   z = [0,0,1]
    z_direction = "from sample towards probe"
    depends_on = "."
  INSTRUMENT
    SCAN_ENVIRONMENT/SPM_SCAN_CONTROL/scan_region  # scan frame
      scan_offset_value_x, scan_offset_value_y, scan_angle_x (scan_angle_y, if given, is equal)
      depends_on = "transformations/scan_angle"
      transformations: NXtransformations
        scan_angle = θ    rotation     [0,0,1]  @depends_on=offset_y
        offset_y   = o_y  translation  [0,1,0]  @depends_on=offset_x
        offset_x   = o_x  translation  [1,0,0]  @depends_on=/ENTRY/scanner_frame
    SPM_CANTILEVER: NXspm_cantilever (NXafm)       # probe frame, orientation only
      depends_on = "transformations/tilt"
      transformations: NXtransformations
        tilt       = α    rotation     [0,1,0]  @depends_on=in_plane
        in_plane   = φ    rotation     [0,0,1]  @depends_on=/ENTRY/scanner_frame
    stage: NXmanipulator                           # stage frame
      depends_on = "transformations/stage_z"
      transformations: NXtransformations
        stage_z    = s_z  translation  v_z      @depends_on=stage_y
        stage_y    = s_y  translation  v_y      @depends_on=stage_x
        stage_x    = s_x  translation  v_x      @depends_on=/ENTRY/scanner_frame
      stage_motorAXIS: NXpositioner                # optional motor details; value links to stage_AXIS
  SAMPLE                                           # sample frame
    depends_on = "transformations/mount_rotation"
    transformations: NXtransformations
      mount_rotation      = γ    rotation     [0,0,1]  @depends_on=mount_translation_x
      mount_translation_x = m_x  translation  [1,0,0]  @depends_on=mount_translation_y
      mount_translation_y = m_y  translation  [0,1,0]  @depends_on=mount_translation_z
      mount_translation_z = m_z  translation  [0,0,1]  @depends_on=/ENTRY/INSTRUMENT/stage/transformations/stage_z
                                                       (or /ENTRY/scanner_frame without a stage position)
```

Notes on the encoding:

- Only the scanner frame is an [NXcoordinate_system][nx-cs]. Every other frame is
  the `depends_on` chain of the group it describes. With a single
  `NXcoordinate_system` in the entry, a `depends_on` that is left out falls back to
  `scanner_frame`.
- `depends_on` names the next transformation in the chain. The direction of each
  step is its `vector`. See [NXtransformations][nx-tr].
- Offsets and stage positions are split into one translation per axis. This avoids
  the undefined unit vector `o/|o|` when `o = 0`.
- The stage vectors `v_x`, `v_y`, `v_z` are not fixed in NXspm, because they depend
  on the instrument.

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
2. **Reference of `θ` for each vendor.** Is the scan angle measured from scanner
   `X` (Bruker: "the scanner's x-axis", [Raster Scan Parameters][bruker-raster])
   or from the cantilever axis? This decides between `θ − φ` and `θ + φ` in the
   probe frame. Bruker notes that Lateral Force Mode needs "scan angles other
   than 0 degrees", which suggests `φ ≈ 0` (cantilever ∥ scanner `X`) there.
   Not verified for other vendors.
3. **Rotation pivot.** Do all vendors rotate about the scan centre, or about the
   scanner origin?
4. **Bruker offset sign.** "a more negative X Offset value will move a feature in
   the current image to the left on the Image display"
   ([Bruker, Scan View Parameters Tips][bruker-tips]). Does this match `o`
   pointing in `+X`, or is the sign flipped for sample-scanning heads?
5. **Sign of the vendor Z.** The scanner frame's `z` points from the sample
   towards the probe.
    - **Bruker force ramps: answered.** In `SB04-MG1.0_00000.spm.txt` (Dimension
      4000), `Height_Sensor_nm` rises from −1576 to +925 nm during the extend half,
      while the deflection stays near −51 nm and jumps to +22 nm at contact at the
      end of extend. So the Bruker height sensor increases as the tip moves
      towards the sample, the opposite sign to scanner `z`. Only one file was
      checked.
    - **Bruker images: open.** No evidence found on whether image height uses the
      same sign.
    - **Nanonis `Z (m)`: open.** The headers and the accessible SPECS documents do
      not state the sign. A height-skewness test on the test images was
      inconclusive. One test file has a negative Z calibration
      (`Calib. Z (m/V)` = `-871E-12`, [R1]), which suggests that the sign of
      Nanonis `Z` is set per instrument through the calibration. A Nanonis
      Z-spectroscopy file (approach curve) would settle it, in the same way as
      the Bruker ramp.
6. **Stage direction and unit.** The direction `vᵢ` of each stage axis depends on
   the instrument. The unit of Bruker `\Stage X/Y/Z` is not given in the header
   (µm assumed).
7. **Probe angles `α`, `φ`.** Rarely in raw files. Should they come from the
   ELN/user input?
8. **Non-rigid effects.** Drift ([ISO 11039][iso11039]), creep and piezo
   nonlinearity make scan → scanner only approximately rigid. Store drift and
   calibration separately, not inside the transform.
9. **Lab frame.** Add it as a sixth frame only when correlating with other
   instruments or recording the direction of gravity or of external fields.

## Decision log

Each decision links to the evidence behind it. **Evidence types:** *Standard* (NeXus
definition text), *Vendor* (manufacturer documentation), *Paper*, *Raw data* (test
files in this repository), *Derived* (follows from the above by geometry), *Team*
(a convention chosen in the review, without external evidence). The sources are
listed under [Sources](#sources), each with the decisions it supports.

| ID | Decision | What the evidence says | Type | Source | In NeXus |
|---|---|---|---|---|---|
| <a id="d1"></a>D1 | One `NXcoordinate_system`, `scanner_frame`, directly under `NXentry`. All other frames are `depends_on` chains of their own groups | With exactly one `NXcoordinate_system`, a missing `depends_on` falls back to it ("traversing up the hierarchy until the first ancestor that contains one and only one ``NXcoordinate_system``"). With two or more, the interpretation becomes ambiguous | Standard | [S1] | `NXspm/ENTRY/scanner_frame` |
| <a id="d2"></a>D2 | Follow the pattern of an existing application definition | `NXxps` defines one `xps_coordinate_system` under `NXentry` and puts the chains in the component groups (`beam_probe/transformations`) | Standard | [S7] | whole layout |
| <a id="d3"></a>D3 | The scanner frame is the central frame | Vendor offsets and scan angles are given relative to the scanner: "The Scan Angle parameter defines the degree of rotation between the axis upon which the scanner travels and the scanner's x-axis" | Vendor | [V1] | `scanner_frame` |
| <a id="d4"></a>D4 | Scanner origin: "undeflected piezo position" or "calibrated piezo position" | The calibration can determine the centre and the axes of the scanner frame, which may differ from the zero-voltage position | Team | — | `scanner_frame/origin` |
| <a id="d5"></a>D5 | Positive rotation about `z` is counter-clockwise when viewed from `+z` (from the probe side) | "In a right-handed coordinate system, positive rotation about an axis is counter-clockwise when looking from a point on the positive axis towards its origin" | Standard | [S2] | overview, `scan_angleAXIS` |
| <a id="d6"></a>D6 | One scan angle `θ`: `scan_angle_x` and `scan_angle_y` must be equal, `scan_angle_x` alone is enough | Vendor files store one angle (Nanonis `:SCAN_ANGLE:` = `1.351E+2`; Bruker `\Rotate Ang.`). The reader writes the same value to each axis (`nanonis_sxm_stm.py:248`) | Raw data | [R1], [R2], [C2] | `scan_region/scan_angleAXIS` |
| <a id="d7"></a>D7 | Scan offset as one translation per axis (`offset_x`, `offset_y`), not one translation along `o/|o|` | A transformation `vector` "should be normalized to unit length". `o/|o|` is undefined for `o = 0` | Standard | [S2] | `scan_region/transformations` |
| <a id="d8"></a>D8 | `depends_on` names the **next** transformation; the direction of a step is its `vector` | "For a chain of three transformations, where T₁ depends on T₂ and that in turn depends on T₃, the final transformation T_f is T_f = T₃ T₂ T₁" | Standard | [S2] | all chains |
| <a id="d9"></a>D9 | The last `depends_on` of a chain points to a transformation field or to `scanner_frame`, never to a component group such as `stage` | The `depends_on` attribute "Points to the path of a field defining the axis on which this instance of NXtransformations depends or the string ".". It can also point to an instance of ``NX_coordinate_system``" | Standard | [S2] | `mount_translation_z@depends_on` → `stage_z` |
| <a id="d10"></a>D10 | Probe frame origin at the clamped end on the chip, `x` from the chip towards the tip | Beam mechanics: "The cantilever is firmly clamped at one end and the tip is located at the other end", with the tip load "at position x = L" | Paper | [P1] | `NXspm_cantilever` |
| <a id="d11"></a>D11 | The tip position is not part of the probe frame; it is the scanner-frame point `p` | Tip–sample interaction is described in a frame with "the origin placed in the sample surface", i.e. the role of our scanner frame | Paper | [P2] | `NXspm_cantilever/transformations` doc |
| <a id="d12"></a>D12 | Tilt `α` is a rotation about `+y` (`vector=[0,1,0]`); positive when the tip end is lower than the chip end | **Geometry:** "These cantilevers are inclined at small angles (usually around 10◦ –15◦ ) to allow the tips of the cantilevers to access the sample surface without the cantilever holder making contact", so the tip end is the lowest point. **Instrument:** Bruker stores this angle as a positive number (`\Cantilever Angle: 12`), and its help confirms "the cantilever is at an angle relative to the surface", typically 12°–25°. **Sign:** with `x` from the chip to the tip and the right-hand rule, `R_y(α)` maps `x` to `(cos α, 0, −sin α)`, so a positive `α` lowers the tip end, matching the positive vendor value | Paper, Raw data, Vendor, Derived | [P4], [R2], [V7], [S2] | `NXafm/.../SPM_CANTILEVER/transformations/tilt` |
| <a id="d13"></a>D13 | `NXspm_cantilever` extends `NXcomponent` | `NXcomponent` provides `depends_on` and an `NXtransformations` group | Standard | [S3] | `NXspm_cantilever` |
| <a id="d14"></a>D14 | The stage is an `NXmanipulator` named `stage`, not an `NXpositioner` | `NXmanipulator`: "Base class to describe the use of manipulators and sample stages", with `NXpositioner` subgroups for "the motors that are used in the manipulator". `NXpositioner`: "A generic positioner such as a motor or piezo-electric transducer" (one `value`). `NXem` uses `stageID: NXmanipulator` | Standard | [S4], [S5], [S6] | `NXspm/ENTRY/INSTRUMENT/stage` |
| <a id="d15"></a>D15 | Stage positions are stored as `transformations/stage_x/y/z`; motor details in optional `stage_motorAXIS` | For stage values, "it is better to describe the reference frame … explicitly using instances of :ref:`NXtransformations` and respective instances of :ref:`NXcoordinate_system`" | Standard | [S6] | `stage/transformations`, `stage/stage_motorAXIS` |
| <a id="d16"></a>D16 | Stage `vector`s are not fixed; they depend on the instrument and the axis | Bruker Dimension Icon: "The XY stage permits micrometer-scale positioning of samples beneath the tip"; the motorized Z stage provides "tip engagement and approach". Nanonis: the coarse-motor approach direction is configured per instrument (`plus` or `minus`) | Vendor, Code | [V4], [C1] | `stage/transformations/*@vector` |
| <a id="d17"></a>D17 | Without stage data, the stage frame coincides with the scanner frame | No Nanonis `.sxm` or `.dat` header in the test data has a stage or coarse-motor position | Raw data | [R1] | `stage` doc, overview |
| <a id="d18"></a>D18 | Bruker stage values: unit assumed µm, open loop | `\Stage X/Y/Z` have no unit in the header, while `\Engage X Pos` is given in `um`. The stage "uses an open loop (unencoded) architecture" | Raw data, Vendor | [R2], [V5] | open question 6 |
| <a id="d19"></a>D19 | Bruker height sensor in force ramps increases towards the sample (opposite to scanner `z`) | During extend, `Height_Sensor_nm` rises from −1576 to +925 nm while the deflection jumps from about −51 to +22 nm at contact | Raw data | [R3] | open question 5 |
| <a id="d20"></a>D20 | Nanonis `Z (m)` sign stays open | Headers and accessible SPECS documents do not state it. A height-skewness test on the test images gave mixed signs and is not evidence | Raw data, Vendor | [R1], [V6] | open question 5 |
| <a id="d21"></a>D21 | Sample chain: `mount_rotation` → `mount_translation_x` → `_y` → `_z` → stage; no surface tilt | Kept simple; the rotation and translation are found from fiducials | Team | [P3] | `NXspm/ENTRY/SAMPLE/transformations` |
| <a id="d22"></a>D22 | Piezo sensor `x`, `y`, `z` are the position of the tip relative to the sample in the scanner frame; the group names the frame with its inherited `depends_on` | The scanner frame is the relative tip–sample displacement measured from the piezo zero (see [scanner frame](#1-scanner-frame-central)), so piezo readings are scanner-frame coordinates without a transformation. `NXspm_piezo_sensor` extends `NXsensor`, which already has `depends_on`, but its doc is still a `.. todo::` | Standard, Derived | [S8] | `NXspm_piezo_sensor`, `NXspm/ENTRY/INSTRUMENT/piezo_sensor` |
| <a id="d23"></a>D23 | Piezo sensor `z` is positive away from the sample; a vendor value that increases as the tip approaches the sample is stored with the opposite sign | Follows from the scanner frame's `z` (from the sample towards the probe). The Bruker height sensor in force ramps increases towards the sample ([D19](#d19)), so the rule is needed in practice | Derived, Raw data | [R3] | `NXspm_piezo_sensor/z` |
| <a id="d24"></a>D24 | `NXspm_piezo_config` gets its own `depends_on`; `tiltAXIS` is the instrument's slope-compensation angle, with the instrument's sign | `NXspm_piezo_config` extends `NXobject` and had no `depends_on`. Nanonis stores the tilt in the piezo configuration (`:Piezo Configuration>Tilt X (deg):` = `0.678395`). No source found for its sign | Raw data | [R1] | `NXspm_piezo_config/depends_on`, `tiltAXIS` |
| <a id="d25"></a>D25 | `spatial_location` in `NXspm_bias_spectroscopy` is an `NXspm_piezo_sensor` (a tip position), not an `NXcoordinate_system` | In `NXcoordinate_system`, `x`, `y`, `z` are basis vectors, not a position. Nanonis STS headers store the spectrum position as `X (m)`, `Y (m)`, `Z (m)`: `X`/`Y` share the origin of the scan offset (e.g. `X` = 153.514 nm inside a 4 nm scan field centred at 153.414 nm) and `Z (m)` equals `Z-Controller>Z (m)` (62.880 vs 62.850 nm). The reader already maps them to `piezo_sensor/x, y, z`. As a result, `scanner_frame` is the only `NXcoordinate_system` in all SPM definitions ([D1](#d1)) | Standard, Raw data, Code | [S1], [R4], [C4] | `NXspm_bias_spectroscopy/BIAS_SWEEP/spatial_location` |
| <a id="d26"></a>D26 | `scanner_frame/x_direction` and `y_direction` are recommended, not required | They are free text that readers rarely provide; making them required would reject otherwise complete files | Team | — | `NXspm/ENTRY/scanner_frame` |
| <a id="d27"></a>D27 | `calibratedAXIS`, `hv_gainAXIS` and `driftAXIS` describe the stored values instead of software behaviour ("automatically updated"); `driftAXIS` keeps `units="NX_ANY"` with the unit (m/s) in the doc | Nanonis stores `Calib. X (m/V)`, `HV Gain X` and `Drift X (m/s)` with `Drift correction status (on/off)` in the piezo configuration. No `Range` key exists in any test file, so no formula is stated, only that two of the three values determine the third. NeXus has no velocity unit category (no `NX_VELOCITY` in `nxdlTypes.xsd`); speeds such as `scan_speedAXIS` use `NX_ANY` | Raw data, Standard | [R1], [S9] | `NXspm_piezo_config/calibration` |

## Sources

Each source lists what we learned from it and the decisions (D…) it supports.

### NeXus definitions (read in the `nexus_definitions` repository)

- **[S1]** `base_classes/NXcoordinate_system.nxdl.xml`, lines 43 and 81. Fallback to a single `NXcoordinate_system`; advice on using one versus several. → [D1](#d1), [D25](#d25). [Manual][nx-cs]
- **[S2]** `base_classes/NXtransformations.nxdl.xml`: chain composition `T_f = T₃ T₂ T₁` (line 71), unit-length `vector` (line 153), right-hand rotation rule (line 175), targets of the `depends_on` attribute (line 202). → [D5](#d5), [D7](#d7), [D8](#d8), [D9](#d9). [Manual][nx-tr]
- **[S3]** `base_classes/NXcomponent.nxdl.xml`, lines 66 and 80. Provides `depends_on` and `NXtransformations` to every component. → [D13](#d13)
- **[S4]** `base_classes/NXmanipulator.nxdl.xml`, lines 26 and 221. "Base class to describe the use of manipulators and sample stages"; `NXpositioner` subgroups for its motors. → [D14](#d14)
- **[S5]** `base_classes/NXpositioner.nxdl.xml`, line 34. "A generic positioner such as a motor or piezo-electric transducer". → [D14](#d14)
- **[S6]** `base_classes/NXem_instrument.nxdl.xml`, line 162, and `applications/NXem.nxdl.xml`, line 964. Stage values should be described with `NXtransformations`; `stageID` is an `NXmanipulator`. → [D14](#d14), [D15](#d15)
- **[S8]** `base_classes/NXsensor.nxdl.xml`, line 161. `depends_on` exists (inherited by `NXspm_piezo_sensor`), but its doc is a `.. todo::` "Add a definition for the reference point of a sensor". → [D22](#d22)
- **[S9]** `nxdlTypes.xsd`. The list of NeXus unit categories; it has `NX_LENGTH`, `NX_TIME`, `NX_ANY`, but no velocity category. → [D27](#d27)
- **[S7]** `applications/NXxps.nxdl.xml`, line 52. One `xps_coordinate_system` under `NXentry`, chains in the component groups. → [D2](#d2)

### Vendor documentation

- **[V1]** Bruker NanoScope help, *Raster Scan Parameters*. Scan angle relative to the scanner's x-axis. → [D3](#d3). [Link][bruker-raster]
- **[V2]** Bruker NanoScope help, *Scan Panel*. "Controls the angle of the X (fast) scan relative to the sample". Offsets ±220 V. [Link][bruker-panel]
- **[V3]** Bruker NanoScope help, *Scan View Parameters Tips*. "These parameters use the sample as the position reference". Open question 4. [Link][bruker-tips]
- **[V4]** Bruker NanoScope help, *System Overview*. "The XY stage permits micrometer-scale positioning of samples beneath the tip"; the motorized Z stage provides "tip engagement and approach". → [D16](#d16). [Link][bruker-overview]
- **[V5]** Bruker NanoScope help, *Stage System*. The XY stage "uses an open loop (unencoded) architecture"; X decreases to the left, Y increases towards the rear. → [D18](#d18). [Link][bruker-stage]
- **[V7]** Bruker NanoScope help, *Ramp Parameter List*, X Rotate: "This is useful because the cantilever is at an angle relative to the surface"; the compensation angle "typically ranges between 12 and 25 degrees", "about 22.0 degrees". → [D12](#d12). [Link][bruker-ramp]
- **[V6]** SPECS, *Nanonis SPM Control System* (manual summary). Mentions TipLift and the Z controller, but no Z sign convention. → [D20](#d20). [Link][nanonis-manual]

### Papers

- **[P1]** Platz, Forchheimer, Tholén, Haviland, *Tip-surface interactions in dynamic atomic force microscopy* (arXiv 1301.7340), section 1.1. "The cantilever is firmly clamped at one end and the tip is located at the other end"; "x is the position coordinate along the cantilever beam"; tip load "at position x = L". → [D10](#d10). [Link][platz]
- **[P2]** *Quantitative dynamic force microscopy with inclined tip oscillation* (PMC9273987). Tip–sample forces in a frame with "the origin placed in the sample surface and the z-axis … perpendicular to the surface"; tilt as the inclination of the tip path from the surface normal. → [D11](#d11). [Link][inclined]
- **[P4]** R. S. Gates, *Experimental confirmation of the atomic force microscope cantilever stiffness tilt correction*, Rev. Sci. Instrum. 88, 123710 (2017), NIST. "The tilt angle (angle of repose) of an AFM cantilever relative to the surface it is interrogating affects the effective stiffness"; "These cantilevers are inclined at small angles (usually around 10◦ –15◦ ) to allow the tips of the cantilevers to access the sample surface without the cantilever holder making contact." → [D12](#d12). [Link][gates]
- **[P3]** Fiducial-based correlative microscopy (stage ↔ sample per loading). → [D21](#d21). [US 9368321][fiducial] · [nanoGPS, MST](https://iopscience.iop.org/article/10.1088/1361-6501/abce39)

### Code

- **[C1]** rusty-tip PR #29 (Nanonis control software). The coarse-motor approach direction is configured per instrument (`motor_z_approach`: `plus` or `minus`). → [D16](#d16). [Link][rusty-tip]
- **[C2]** pynxtools-spm, `src/pynxtools_spm/nxformatters/nanonis/nanonis_sxm_stm.py`, line 248. Writes one scan angle per axis. → [D6](#d6)
- **[C3]** pynxtools-spm, *Scan region, axes and scan direction*. Offset = centre of the scan area; stage keys never combined with the offset. [Link][repo-scan]
- **[C4]** pynxtools-spm, `src/pynxtools_spm/configs/nanonis/nanonis_dat_generic_sts.json`, lines 549–551. Maps the STS header keys `X (m)`, `Y (m)`, `Z (m)` to `piezo_sensor/x, y, z`. → [D25](#d25)

### Raw data (test files in this repository)

- **[R1]** Nanonis headers, e.g. `tests/data/nanonis/stm/v_gen_5_dflt_conf_down/Au_mica_2023_Y_A_diPAMY_195.sxm`: one `:SCAN_ANGLE:` value, no stage or coarse-motor keys in any `.sxm` or `.dat` file., piezo tilt in `:Piezo Configuration>Tilt X (deg):`, calibration `Calib. X (m/V)`, `HV Gain X`, `Drift X (m/s)` and a negative `Calib. Z (m/V)` = `-871E-12` in `tests/data/nanonis/afm/v_gen_4_dflt_conf_up/A151216.123306-02602.sxm`. → [D6](#d6), [D17](#d17), [D20](#d20), [D24](#d24), [D27](#d27)
- **[R2]** Bruker `.spm` headers, e.g. `tests/data/bruker/afm/spm_v_9_4_dflt_conf_up/tecky.0_00002.spm`: one `\Rotate Ang.`; `\Stage X/Y/Z` without a unit; `\Engage X Pos` in `um`; `\Scanner type: Dim 4000`; `\Cantilever Angle: 12` (two files) or `0` (one file). → [D6](#d6), [D12](#d12), [D18](#d18)
- **[R3]** Bruker force ramp `tests/data/bruker/afm/txt_dflt_conf/SB04-MG1.0_00000.spm.txt`: `Height_Sensor_nm` and `Defl_nm` in the extend (`_Ex`) and retract (`_Rt`) halves. → [D19](#d19)
- **[R4]** Nanonis STS files `tests/data/nanonis/sts/v_gen_5_descrb_nx_dt/Bias-Spectroscopy00015_20230420.dat` and `tests/data/nanonis/sts/v_gen_5e_dflt_conf/STS_nanonis_generic_5e_1.dat`: `X (m)`, `Y (m)`, `Z (m)`, `Scan>Scanfield`, `Z-Controller>Z (m)`. → [D25](#d25)

### Not yet read in full (seen only in search summaries)

- Lateral PFM, scan angle relative to the cantilever. [arXiv 2305.03864][lpfm]
- Torsional force microscopy, PNAS 2024. [PNAS](https://www.pnas.org/doi/10.1073/pnas.2314083121)
- Patent defining lab, cantilever and tilt angles. [US 11644478](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11644478)
- Cantilever clamped at `X = 0`, tip at `X = L`: *Coupled lateral bending–torsional vibration sensitivity of AFM cantilever*, Ultramicroscopy 2007 ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304399107002495), page not accessible). Would support D10.
- *Cantilever tilt compensation for variable-load AFM*, RSI 2005: `L` is "the length from the base of the lever to the tip axis" ([RSI](https://pubs.aip.org/aip/rsi/article-abstract/76/5/053706/1017654/Cantilever-tilt-compensation-for-variable-load), page not accessible). Would support D10.
- *Interfacing a Nanonis controller with a scanning tunneling microscope*, Cornell thesis ([PDF](https://ecommons.cornell.edu/bitstream/handle/1813/43642/jrr45.pdf?sequence=1&isAllowed=y), could not be fetched). Might answer D20.
- PTB metrological large-range SPM (stage + piezo + interferometers). [RSI 2004](https://pubs.aip.org/aip/rsi/article-abstract/75/4/962/466407/Metrological-large-range-scanning-probe-microscope) · [RSI 2009](https://pubs.aip.org/aip/rsi/article-abstract/80/4/043702/282343/A-metrological-large-range-atomic-force-microscope)
- NIST six-axis interferometer positioning for SPM. [PMC3926591](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3926591/)
- Topography-based navigation in an mK STM with position markers (stage ↔ sample). [arXiv 2606.04848](https://arxiv.org/html/2606.04848)
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
[bruker-overview]: https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/System%20Overview/System%20Overview.htm
[bruker-stage]: https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/Stage%20System/Stage%20System.htm
[platz]: https://arxiv.org/pdf/1301.7340
[inclined]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9273987
[rusty-tip]: https://github.com/kronberger-droid/rusty-tip/pull/29
[nanonis-manual]: https://manualzilla.com/doc/5829502/nanonis-spm-control-system
[gates]: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=921131
[bruker-ramp]: https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/Force%20Imaging/Ramp%20Parameter%20List.htm
