# Bruker AFM — PeakForce QNM Experiment Analysis

**Source file:** `raw_data/SB04-MG1.0_00000.spm.txt`
**Date analysed:** 2026-06-22
**Instrument date:** 2023-05-15 (from file header)

---

## What is this file?

`SB04-MG1.0_00000.spm.txt` is a **self-contained ASCII text file** — it contains both the full instrument metadata header AND the actual force-distance curve data as tab-separated columns. It does **not** require a separate binary `.spm` file to be useful.

**File structure:**

```
Lines 1 – 1172   │  Header sections  (instrument parameters, calibrations,
                  │  channel descriptions — all the \Key: Value lines)
Line  1172        │  \*Force file list end         ← header ends here
Line  1173        │  Column header row             ← 32 named columns
Lines 1174 – end  │  Data rows (9728 rows, one per Z-step)
```

The `Data offset` and `Data length` fields inside the header describe how an equivalent Bruker binary `.spm` file would encode the same data — they are format documentation, not pointers into this text file.

> **How we know this file is ASCII text:** There is no explicit `Format: ASCII` declaration anywhere in the header. The format is identified by observation: the file has a `.txt` extension, every line is human-readable, the column header row contains plain text names, and data values are written as scientific notation strings (e.g. `-4.792500e-001`). Line-counting with `wc -l` returns 10,901 — which only works on text files. The format is inferred, not declared.

In the pynxtools-spm codebase, this file is parsed by `bruker_txt.py` which reads both the header metadata and the ASCII data columns.

---

## Experiment Type

**Technique:** AFM — Atomic Force Microscopy
**Specific flavor:** **PeakForce Quantitative Nanomechanical Mapping (PeakForce QNM)**
**Measurement mode:** Force-Volume (FV) — a 2D grid of force-distance curves

### Key identifiers in the file

| Parameter | Value | Significance |
|---|---|---|
| `\?Force file list` | line 1 | Declares this as a Bruker force file |
| `\Start context: FOL` | line 4 | FOL = Force Object List (Bruker's force context) |
| `\Operating mode: Force` | line 164 | Instrument in force (not imaging) mode |
| `\@MicroscopeList: AFMMode "Contact"` | line 434 | AFM contact mechanics feedback |
| `\PFT Freq: 2 kHz` | line 358 | PeakForce oscillation at 2 kHz |
| `\QNM Calibration: DefaultByZ` | line 314 | QNM calibration via Z sensor |
| `\Modulus Fit Model: Hertzian (Spherical)` | line 336 | Contact mechanics fit model |
| `\*Ciao force list` | line 877 | Force measurement parameters section |
| `\*Ciao force image list` | line 972 | Force image data channel metadata |

---

## Scan Geometry: 2D Grid (not single-point, not a raster image)

This is a **2D spatial grid of force-distance curves** — each grid point has a full Z-approach and Z-retract curve recorded.

### Grid layout

| Parameter | Value | Line | Meaning |
|---|---|---|---|
| `Columns: 5` | 5 | 915 | Grid columns |
| `Rows: 5` | 5 | 916 | Grid rows |
| `Column step: 1000` | 1000 nm | 917 | Lateral spacing between columns |
| `Row step: 1000` | 1000 nm | 918 | Lateral spacing between rows |
| `X Offset: -2000 nm` | −2000 nm | 171 | Grid origin X |
| `Y Offset: -2000 nm` | −2000 nm | 172 | Grid origin Y |
| **Total positions** | **25** | — | 5 × 5 measurement points |

**Grid area:**
```
Width  = (5 − 1) × 1000 nm = 4000 nm = 4 µm
Height = (5 − 1) × 1000 nm = 4000 nm = 4 µm

X spans: −2000 nm → +2000 nm   (centered on sample origin)
Y spans: −2000 nm → +2000 nm
```

**One file per grid point (inferred, not confirmed from documentation):**

The `_00000` suffix in the filename strongly suggests this is a sequentially numbered file in a multi-point export series. The prediction of 25 total files comes from combining two pieces of evidence:

| Evidence | Source | Type |
|---|---|---|
| Grid has 5 × 5 = 25 positions | `Columns: 5` / `Rows: 5` in the file (lines 915–916) | Direct — read from file |
| `_00000` indicates position index 0 | Common Bruker multi-point naming convention | Inferred — not stated in this file |
| Therefore files `_00000` to `_00024` exist | Combination of the above | Inferred — unverified |

Only `_00000` is present in the test data folder; the existence of the remaining 24 files cannot be confirmed from this file alone.

> **Note on documentation:** Bruker does not publicly release the NanoScope file format specification — it is proprietary. The most complete community-documented reverse-engineering of the format is in the **Gwyddion** SPM analysis software documentation at `http://gwyddion.net/documentation/user-guide-en/file-formats.html` (search "NanoScope"). The `pySPM` library used in this codebase is also based on community reverse-engineering.

**Each file carries its own exact XY position in the header.** For `_00000`:

| Line | Field | Value | Role |
|---|---|---|---|
| 169 | `X Position` | 0 | Scan centre X |
| 170 | `Y Position` | 0 | Scan centre Y |
| 171 | `X Offset` | −2000 nm | Actual X of this grid point |
| 172 | `Y Offset` | −2000 nm | Actual Y of this grid point |
| 174 | `Stage X` | −9797.5 µm | Absolute motor encoder position |
| 175 | `Stage Y` | −42233.8 µm | Absolute motor encoder position |

`X Offset` and `Y Offset` are the fields that change between files. The stage coordinates give the absolute position on the sample in the lab frame.

**Reconstructed XY coordinates for all 25 files:**

```
X = −2000 + (column_index × 1000) nm
Y = −2000 + (row_index    × 1000) nm
```

| File | Col | Row | X (nm) | Y (nm) |
|---|---|---|---|---|
| `_00000` | 0 | 0 | −2000 | −2000 |
| `_00001` | 1 | 0 | −1000 | −2000 |
| `_00002` | 2 | 0 | 0 | −2000 |
| `_00003` | 3 | 0 | +1000 | −2000 |
| `_00004` | 4 | 0 | +2000 | −2000 |
| `_00005` | 0 | 1 | −2000 | −1000 |
| `_00006` | 1 | 1 | −1000 | −1000 |
| `_00007` | 2 | 1 | 0 | −1000 |
| `_00008` | 3 | 1 | +1000 | −1000 |
| `_00009` | 4 | 1 | +2000 | −1000 |
| `_00010` | 0 | 2 | −2000 | 0 |
| `_00011` | 1 | 2 | −1000 | 0 |
| `_00012` | 2 | 2 | 0 | 0 |
| `_00013` | 3 | 2 | +1000 | 0 |
| `_00014` | 4 | 2 | +2000 | 0 |
| `_00015` | 0 | 3 | −2000 | +1000 |
| `_00016` | 1 | 3 | −1000 | +1000 |
| `_00017` | 2 | 3 | 0 | +1000 |
| `_00018` | 3 | 3 | +1000 | +1000 |
| `_00019` | 4 | 3 | +2000 | +1000 |
| `_00020` | 0 | 4 | −2000 | +2000 |
| `_00021` | 1 | 4 | −1000 | +2000 |
| `_00022` | 2 | 4 | 0 | +2000 |
| `_00023` | 3 | 4 | +1000 | +2000 |
| `_00024` | 4 | 4 | +2000 | +2000 |

### Force curve parameters (per grid point)

| Parameter | Value | Meaning |
|---|---|---|
| `Samps/line: 9728 9728` | 9728 | Data points per approach / retract curve |
| `Ramp Size: 2500 nm` | 2.5 µm | Total Z travel per curve |
| `FV Line Direction: Bidirection` | both | Approach AND retract recorded |
| `force/line: 16` | 16 | Force curves per scan line (??)|
| `X Type: Height Sensor` | Z sensor | X-axis of force curve is true Z position |
| `Spring Constant: 0.0538362 N/m` | ~54 mN/m | Cantilever stiffness (very soft — suitable for biological samples) |

---

## Force-Distance Curve Calculations

All values are derived from the file header. No assumptions — every number traces back to a specific line in the raw file.

**Input constants from file:**

| Constant | Value | Source line |
|---|---|---|
| Samples per direction (N) | 9728 | line 882 |
| Ramp size (L) | 2500 nm | line 1019 |
| Sample period (T_s) | 16 µs | line 958 |
| Spring constant (k) | 0.0538362 N/m | line 993 |
| Deflection sensitivity (S_defl) | 105.4528 nm/V | line 526 |
| Deflection voltage resolution | 0.0003662 V/LSB | line 639 |
| Z sensor sensitivity (S_z) | 17.9493 nm/V | line 157 |
| PeakForce frequency (f_PF) | 2 kHz | line 358 |
| Grid columns / rows | 5 × 5 | lines 915–916 |
| Grid step size | 1000 nm | lines 917–918 |
| Bytes per pixel | 2 | line 975 |

---

### 1. Z spatial resolution — step size per data point

```
Δz = L / N = 2500 nm / 9728 = 0.257 nm per point
```

The tip Z position is sampled every **0.26 nm** — sub-atomic resolution along the indentation axis.

---

### 2. Duration of one approach (or retract)

```
t_half = N × T_s = 9728 × 16 µs = 155,648 µs ≈ 155.6 ms
```

---

### 3. Full approach + retract cycle duration

```
t_cycle = 2 × t_half = 2 × 155.6 ms = 311.3 ms ≈ 0.31 s per grid point
```

---

### 4. Actual tip velocity during Z ramp

Derived from ramp size and duration — not from the raw `Forward vel.` field, which is a Bruker internal normalized parameter:

```
v_tip = L / t_half = 2500 nm / 0.1556 s = 16,060 nm/s ≈ 16.1 µm/s
```

> The file records `Forward vel.: 56.1125` — this is Bruker's internal scan-rate-normalized unit, not SI nm/s. The true physical velocity is calculated above.

---

### 5. PeakForce oscillation cycles captured per curve

At f_PF = 2 kHz each oscillation cycle lasts 0.5 ms:

```
N_cycles = t_half / (1 / f_PF) = 155.6 ms / 0.5 ms = 311 cycles per direction

Full curve (approach + retract) = 311 × 2 = 622 PeakForce cycles
```

Each individual PeakForce oscillation cycle is one complete tip–sample interaction event from which modulus, adhesion, deformation, and dissipation are extracted in real time.

---

### 6. Minimum detectable force (force resolution)

The deflection calibration chain converts DAC bits → voltage → cantilever deflection → force:

```
line 635
Step 1 — minimum detectable deflection:
  δ_min = 0.0003662 V/LSB × 105.4528 nm/V = 0.0386 nm per LSB

Step 2 — minimum detectable force:
  F_min = k × δ_min = 0.0538362 N/m × 0.0386×10⁻⁹ m ≈ 2.08 pN per LSB
```

The instrument can theoretically resolve forces down to **~2 pN per digital step**.

---

### 7. ASCII data columns — what the file actually stores

The data section (starting at line 1173) contains **32 tab-separated columns** and **9,728 rows** (one row per Z-step).

**Column layout:**

| Columns | Signal | Units stored | Direction |
|---|---|---|---|
| 1 | Time | s | approach (Ex) |
| 2 | Time | s | retract (Rt) |
| 3 | Calculated Z ramp | nm | approach |
| 4 | Calculated Z ramp | nm | retract |
| 5–6 | Cantilever deflection | V | Ex / Rt |
| 7–8 | Cantilever deflection | nm | Ex / Rt |
| 9–10 | Force | pN | Ex / Rt |
| 11–12 | Deflection | raw LSB | Ex / Rt |
| 13–14 | Z height sensor | V | Ex / Rt |
| 15–16 | Z height sensor | nm | Ex / Rt |
| 17–18 | Z height sensor | raw LSB | Ex / Rt |
| 19–32 | **Second force curve** — same 14 signals repeated | | Ex / Rt |

The suffix `_Ex` = Extension (approach); `_Rt` = Retraction. Each physical signal is stored in multiple calibrated unit forms (V, nm, pN, and raw LSB) so that downstream analysis can use whichever representation is needed without re-applying calibrations.

**Why 32 columns and not 18?** Columns 19–32 are a **confirmed redundant duplicate** of columns 5–18, verified by comparing all 9,728 rows programmatically:

| Col A | Col B | Signal | Max difference | Verdict |
|---|---|---|---|---|
| 5 | 19 | `Defl_V_Ex` | 0.000000 | Exact duplicate |
| 6 | 20 | `Defl_V_Rt` | 0.000000 | Exact duplicate |
| 7 | 21 | `Defl_nm_Ex` | 0.000000 | Exact duplicate |
| 8 | 22 | `Defl_nm_Rt` | 0.000000 | Exact duplicate |
| 9 | 23 | `Defl_pN_Ex` | 0.000000 | Exact duplicate |
| 10 | 24 | `Defl_pN_Rt` | 0.000000 | Exact duplicate |
| 11 | 25 | `Defl_Lsb_Ex` | 0.000000 | Exact duplicate |
| 12 | 26 | `Defl_Lsb_Rt` | 0.000000 | Exact duplicate |
| 13 | 27 | `Height_Sensor_V_Ex` | 0.000000 | Exact duplicate |
| 14 | 28 | `Height_Sensor_V_Rt` | 0.000000 | Exact duplicate |
| **15** | **29** | **`Height_Sensor_nm_Ex`** | **0.001 nm** | Rounding only |
| **16** | **30** | **`Height_Sensor_nm_Rt`** | **0.001 nm** | Rounding only |
| 17 | 31 | `Height_Sensor_Lsb_Ex` | 0.000000 | Exact duplicate |
| 18 | 32 | `Height_Sensor_Lsb_Rt` | 0.000000 | Exact duplicate |

The two `Height_Sensor_nm` pairs show differences of ≤ 0.001 nm (1 pm) in 3,441–3,434 out of 9,728 rows. This is a **text serialisation rounding artefact**: the raw LSB columns (17/31 and 18/32) are exactly identical, confirming the underlying data is the same. The nm values are derived by multiplying voltage by the Z-sensor sensitivity (17.9493 nm/V); writing that product as limited-precision text introduces last-digit variation. At 0.001 nm the difference is 250× smaller than the Z spatial resolution of 0.257 nm — physically meaningless.

The differences are both positive and negative with no systematic trend, ruling out any real data distinction between the two column sets.

**Conclusion: columns 19–32 are redundant duplicates of columns 5–18 across all 9,728 rows. This file holds exactly one force curve for one grid position. The duplication is a Bruker `.spm.txt` export artefact, likely mirroring the structure of the 4 `*Ciao force image list` header sections.**

**Data points per column — verified by line count:**

```
Total lines in file : 10,901
Column header row   : line 1,173
Data rows           : 10,901 − 1,173 = 9,728
```

Every one of the 32 columns contains exactly **9,728 data points** — matching `Samps/line: 9728` from the header exactly.

Each row represents one Z-step. Approach (`_Ex`) and retract (`_Rt`) are stored **side-by-side in the same row**, so a single row simultaneously records the tip position and deflection at the same Z-index for both directions. This is why 9,728 rows cover the full ramp even though the tip travels 9,728 steps in each direction.

**Total data volume (ASCII):**

| Item | Calculation | Result |
|---|---|---|
| Data rows (Z steps) | 10,901 total lines − 1,173 header lines | **9,728** |
| Columns | 32 | 32 |
| Total data values | 9,728 × 32 | **311,296** |
| File size | 9,728 rows × 32 cols × ~15 chars/value | **~4.4 MB** ✓ |

**What the 4 `*Ciao force image list` header sections describe:**

The 4 sections in the header (lines 972, 1022, 1072, 1122) document how the **equivalent binary `.spm` file** would store the same data (?? are there two equivalent files in differnt format binary and txt files)? — they describe channels in binary format (deflection error and height sensor, approach and retrace). Their `Data offset / Data length` fields are not pointers into this text file. They are retained in the `.spm.txt` header for completeness and software compatibility.

---

### 8. Spatial area covered by the grid

```
Width  = (Columns − 1) × step = (5 − 1) × 1000 nm = 4000 nm = 4 µm
Height = (Rows    − 1) × step = (5 − 1) × 1000 nm = 4000 nm = 4 µm
```

The force-volume map covers a **4 µm × 4 µm** area of the sample surface.

---

### Summary of calculated quantities

| Quantity | Value |
|---|---|
| Z spatial resolution per data point | **0.257 nm** |
| Duration per approach or retract | **155.6 ms** |
| Duration of full approach+retract cycle | **311.3 ms** |
| Tip Z velocity during ramp | **16.1 µm/s** |
| PeakForce cycles per full curve | **622** |
| Minimum detectable force | **~2 pN** |
| Data points per column (verified by line count) | **9,728** (10,901 total lines − 1,173 header lines) |
| Data columns | **32** (time + Z ramp + 2 signals × 3 units × 2 directions × 2 curves) |
| Total data values | **311,296** (9,728 × 32) |
| File size | **~4.4 MB** (consistent with 9,728 × 32 × ~15 chars/value) |
| Spatial area mapped | **4 µm × 4 µm** |

---

## Physical Properties Measured

The Hertzian contact model is fitted to the approach–retract curve at each grid point to extract the following **nanomechanical properties**:

| Property | Unit | Physical meaning |
|---|---|---|
| **Young's modulus (E*)** | Pa | Elastic stiffness — how hard or soft the surface is |
| **Adhesion force** | nN | Attractive force between tip and sample during retract |
| **Deformation** | nm | Depth of tip indentation into the sample |
| **Dissipation** | eV | Energy lost per oscillation cycle (viscous/plastic losses) |
| **Stiffness** | N/m | Local contact spring constant |
| **Storage modulus** | Pa | Elastic (in-phase) component of viscoelastic response |
| **Loss modulus** | Pa | Viscous (out-of-phase) component of viscoelastic response |
| **Loss tangent** | dimensionless | tan(δ) = Loss mod / Storage mod — damping ratio |

All of these are confirmed by the sensitivity definitions in the file:
```
\@Sens. FVModulusSens, FVForceSens, FVStiffnessSens,
        FVCRStorageModSens, FVCRLossModSens, FVCRLossTanSens
```

### Scientific applications

- Nanomechanical mapping of heterogeneous materials (polymers, composites, biomaterials)
- Stiffness contrast imaging across phase-separated regions
- Cell mechanics: membrane stiffness, cytoskeletal organization
- Adhesion mapping between functional groups and surfaces (chemical force mapping)
- Characterization of thin films, grain boundaries, polymer blends

---

## PeakForce QNM — Technical Details

PeakForce QNM is Bruker's proprietary implementation of force-volume that differs from classical force-volume in the following ways:

| Aspect | Classical Force-Volume | PeakForce QNM |
|---|---|---|
| Tip oscillation | Static Z ramp | Sinusoidal at fixed frequency (2 kHz here) |
| Feedback signal | Deflection setpoint | Peak force per cycle |
| Data extraction | Post-processing | Real-time, per oscillation cycle |
| Speed | Slow (minutes per map) | Much faster |
| Force control | Open-loop Z ramp | Closed-loop force control |

### Key PeakForce QNM parameters in this file

| Parameter | Value |
|---|---|
| PeakForce frequency | 2 kHz |
| Peak Force Amplitude | 100 nm |
| PFT Feedback Type | Peak Force |
| PFT Deflection Setpoint | 0.2 V |
| PFT Deflection Igain / Pgain | 20 / 40 |
| ScanAsyst Auto Control | On (AI-assisted optimization) |

### Contact mechanics: Hertz model

The **Hertzian (Spherical)** model assumes:
- The tip is a sphere of radius R (here R = 3000 nm = 3 µm)
- The sample is an elastic half-space
- Contact is frictionless and purely elastic

$$F = \frac{4}{3} E^* \sqrt{R} \cdot \delta^{3/2}$$

where F is the applied force, E* is the reduced modulus, R is the tip radius, and δ is the indentation depth.

The file also has the **Sneddon model** sensitivity defined (`SneddonModulusSens`) which handles conical tip geometry — a more accurate model for sharp tips.

---

## Instruments and Hardware

| Component | Model / Value | Role |
|---|---|---|
| AFM platform | **Bruker Dimension Icon** | Main instrument |
| Scanner | Dim 4000 (serial `1b818`) | Closed-loop XY piezo scanner |
| Head type | `SG` | ScanAsyst-compatible, optical beam-deflection head |
| Cantilever type | `100W` | Wide-leg, very soft cantilever |
| Spring constant | 0.054 N/m | Ultra-soft — ideal for biological / soft-matter samples |
| Tip radius | 3000 nm (3 µm) | Relatively blunt — used with Hertz spherical model |
| Cantilever resonance | ~87 kHz | (Not used in PeakForce mode) |
| Z sensor | Closed-loop capacitive, sensitivity 17.9–493 nm/V | `Z Closed Loop: On` — true Z displacement |
| XY sensor | Optical (OptoXY), sensitivity ~350 nm/V | Closed-loop lateral positioning |
| Operating temperature | 23 °C | Room temperature |
| Fluid cell | No | Dry measurement in air |
| Vision system | uEye UI148xLE-C #1 | Optical camera for sample navigation |

---

## References

- **PeakForce QNM:** Pittenger, B. et al. *Quantitative Mechanical Property Mapping at the Nanoscale with PeakForce QNM.* Bruker Application Note AN128 (2010).
- **Force spectroscopy overview:** [Wikipedia — AFM Force Spectroscopy](https://en.wikipedia.org/wiki/Atomic_force_microscopy#Force_spectroscopy)
- **Hertz contact model:** [Wikipedia — Contact Mechanics](https://en.wikipedia.org/wiki/Contact_mechanics)
- **Bruker Dimension Icon:** [Bruker product page](https://www.bruker.com/en/products-and-solutions/microscopes/materials-afm/dimension-icon-afm.html)
- **PeakForce QNM technique page:** [Bruker PeakForce QNM](https://www.bruker.com/en/products-and-solutions/microscopes/materials-afm/peakforce-qnm.html)

---

## Relation to pynxtools-spm

In this codebase, the `.spm.txt` file is processed by:

| Layer | File | Role |
|---|---|---|
| Parser | `src/pynxtools_spm/parsers/bruker_txt.py` | Reads this `.txt` file → flat dict |
| Formatter | `src/pynxtools_spm/nxformatters/bruker/` | Maps dict → NeXus template |
| Config | `src/pynxtools_spm/configs/bruker/` | JSON mapping of raw keys → NeXus paths |
| Reader | `src/pynxtools_spm/reader.py` | Entry point; dispatches to `BrukerSpmAFM` for `AFM + spm` |

The ELN file accompanying this measurement must contain `experiment_technique: AFM` — this is mandatory for `SPMReader.read()`.
