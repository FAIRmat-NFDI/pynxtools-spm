# Bruker AFM — Au-Ir-Rh Au-rich Surface, Area 168 (File .002 ??does it mean it has other scan files with differrent numbers?)

**Source file:** `Au-Ir-Rh_Au-rich_AFM_area_168.002`
**Date analysed:** 2026-06-28
**Instrument date:** 2026-05-05 04:52:13 PM (from file header)
**Dataset note:** `DataSetnote.txt` (Zenodo record 20439519)

---

## Dataset Context

### What is the name of the experiment?

The AFM measurement is part of a multi-technique autonomous **Scanning Electrochemical Cell Microscopy (SECCM)** campaign described in the accompanying publication. The full platform combines robotic SECCM with active learning and multi-output Gaussian process (GP) modelling for high-throughput electrochemical characterisation of compositionally complex thin-film materials libraries, validated on the **Au-Ir-Rh ternary system** as a model case for hydrogen evolution reaction (HER) electrocatalyst discovery.

The AFM sub-experiment is titled:

> **Atomic Force Microscopy (AFM) characterisation of Au-Ir-Rh thin-film materials libraries**

It provides surface morphology data at selected measurement areas (MAs) from three libraries (Au-rich, Ir-rich, Rh-rich), which are correlated with EDX, XPS, XRD, and SECCM data at the same grid positions.

### How does the instrument collect data?

The dataset uses **two distinct scan modes** depending on the technique:

| Technique | Scan mode | Grid |
|---|---|---|
| **AFM** (this file) | **Raster scan** — tip traverses a 512 × 512 pixel grid over a fixed area (500 × 500 nm here) at each selected MA | 15 localised raster scans total (5 per library), selected from the 342-point grid |
| EDX / XRD | Point measurement at each of 342 MAs across the wafer (4.5 mm spacing) | Full 342-point grid |
| XPS | Point measurement at 13 selected MAs per library; remainder GP-predicted | 13-point sparse grid + GP |
| SECCM | Single-point linear sweep voltammogram (LSV) at each MA | 322 usable points per library |

For this AFM file specifically: the instrument performs a **2D raster scan** (`\Operating mode: Image`, `\Bidirectional Scan: Disabled`). The fast axis sweeps 512 points across 500 nm at 0.977 Hz while the slow axis steps 512 lines, producing a 512 × 512 image per channel. A single-point (non-raster) scan mode is not used here, but is possible on this instrument for force spectroscopy (`Operating mode: Force`).

---

## What is this file?

`Au-Ir-Rh_Au-rich_AFM_area_168.002` is a **Bruker Nanoscope binary SPM image file**. It stores two 512 × 512 pixel raster-scan images as signed 16-bit integer arrays in a binary block that follows a plain-text header. The file is self-contained: the header carries all calibration and metadata, and the binary blocks carry the raw pixel data for both channels.

**File structure:**

```
Bytes 0 – 40959    │  Plain-text header  (\*File list … \*File list end)
                   │  All \Key: Value parameter lines for the scan
Bytes 40960 – 565247   │  Channel 1 binary data: Height Sensor
                       │  512 × 512 pixels × 2 bytes = 524 288 bytes
Bytes 565248 – 1089535 │  Channel 2 binary data: Peak Force Error
                       │  512 × 512 pixels × 2 bytes = 524 288 bytes
```

**File size verification:**

| Segment | Offset | Length | Content |
|---|---|---|---|
| Header | 0 | 40 960 B (40 kB) | `\*File list` → `\*File list end` |
| Channel 1 | 40 960 | 524 288 B (512 kB) | Height Sensor image |
| Channel 2 | 565 248 | 524 288 B (512 kB) | Peak Force Error image |
| **Total** | — | **1 089 536 B ≈ 1.04 MB** | ✓ consistent with 1.1 MB on disk |

The `Data offset` and `Data length` fields in each `\*Ciao image list` section point directly into this same binary file.

---

## Experiment Type

**Technique:** AFM — Atomic Force Microscopy
**Specific mode:** **PeakForce Tapping / ScanAsyst** (Bruker's AI-assisted ScanAsyst autopilot)
**Measurement type:** 2D raster scan image — topography and force error simultaneously

### Key identifiers in the file

| Parameter | Value | Significance |
|---|---|---|
| `\*File list` | line 1 | Standard Bruker Nanoscope file header |
| `\Start context: OL2BIG` | header | OL = Offline; 2 = 2 channels; BIG = big-endian binary image |
| `\Operating mode: Image` | Ciao scan list | Raster image scan (not force-volume) |
| `\@MicroscopeList: "ScanAsyst"` | header | ScanAsyst autopilot with SoftHarmoniX |
| `\@SPMFeedbackList: "Peak Force"` | header (×2) | PeakForce feedback loop active |
| `\PFT Freq: 2 KHz` | header | PeakForce tapping oscillation frequency |
| `\ScanAsyst Auto Control: On` | header | Full autopilot (setpoint, gain, scan rate, Z limit) |
| `\Modulus Fit Model: Hertzian (Spherical)` | header | Contact mechanics fit in real-time |

---

## Sample

**Material system:** Au-Ir-Rh ternary alloy — Au-rich surface phase
**Area identifier:** 168
**File index within series:** .002 (third file; .000 and .001 likely precede this one at the same or adjacent areas)

The `Au-rich` label indicates this scan was taken on a region where the alloy surface is predominantly Au-terminated. The `.002` suffix follows Bruker's sequential numbering convention for successive scans on the same sample.

---

## Scan Geometry

This is a **standard 2D raster scan** — a single pass of the tip across a square grid of 512 × 512 points. No force-distance curves are recorded per pixel; only the instantaneous Z height and PeakForce error are captured at each point.

### Scan parameters

| Parameter | Value | Source |
|---|---|---|
| Scan size | 500 × 500 nm | `\Scan Size: 500 nm` |
| Pixels | 512 × 512 | `\Samps/line: 512` / `\Lines: 512` |
| Aspect ratio | 1:1 | `\Aspect Ratio: 1:1` |
| Scan rate | 0.976563 Hz (lines/s) | `\Scan Rate: 0.976563` |
| Bidirectional scan | Disabled | `\Bidirectional Scan: Disabled` |
| Captured direction | Retrace (right→left) | `\Line Direction: Retrace` (both channels) |
| X offset | 0 nm | `\X Offset: 0 nm` |
| Y offset | 0 nm | `\Y Offset: 0 nm` |
| Rotate angle | 0° | `\Rotate Ang.: 0` |

### Stage position at measurement

| Field | Value | Meaning |
|---|---|---|
| Stage X | −22 187 µm | Absolute motor position (X) |
| Stage Y | −40 500 µm | Absolute motor position (Y) |
| Engage X Pos (what is it?) | −19 783.4 µm | Approach position (X) |
| Engage Y Pos | −42 151.3 µm | Approach position (Y) |

---

## Quantitative Calculations

All values are derived directly from the file header. No external assumptions are made.

**Input constants from file:**

| Constant | Value | Source |
|---|---|---|
| Scan size (L) | 500 nm | `\Scan Size` |
| Pixels per line (N) | 512 | `\Samps/line` |
| Scan rate (f_scan) (?? each line) | 0.976563 Hz | `\Scan Rate` |
| Lines (M) | 512 | `\Lines` |
| PeakForce frequency (f_PF) | 2 kHz | `\PFT Freq` |
| Peak Force Amplitude (??cantiliver oscilator setup for finding peak force) | 150 nm | `\Peak Force Amplitude` |
| ZsensSens | 204.3017 nm/V | `\@Sens. ZsensSens` |
| Z scale (channel 1 (??max voltage)) | 24.57563 V | `\@2:Z scale` |
| Z magnify (channel 1) (??) | 0.001394189 | `\@Z magnify` |
| ForceDeflSens | 24.00 nN/V | `\@Sens. ForceDeflSens` |
| Z scale (channel 2 (max voltage)) | 24.57563 V | `\@2:Z scale` (ch2) |
| Z magnify (channel 2) | 0.0007290422 | `\@Z magnify` (ch2) |
| Bytes/pixel | 2 | `\Bytes/pixel` (both channels) |
| Tip radius | 5 nm | `\Tip Radius: 5` |

---

### 1. Lateral pixel size

```
Δx = L / N = 500 nm / 512 = 0.977 nm/pixel
```

Each image pixel represents a **0.977 nm × 0.977 nm** area on the surface.

---

### 2. Scan duration (one frame)

```
t_frame = M / f_scan = 512 lines / 0.976563 lines·s⁻¹ = 524.3 s ≈ 8.74 minutes
```

---

### 3. Tip lateral velocity during scan

```
v_tip = L × f_scan = 500 nm × 0.976563 Hz = 488.3 nm/s ≈ 0.49 µm/s
```

---

### 4. PeakForce cycles per scan line

At f_PF = 2 kHz, the line period is 1/f_scan = 1024 ms:

```
N_PF_per_line = f_PF × (1/f_scan) = 2000 Hz × 1.024 s = 2048 cycles/line
```

---

### 5. PeakForce cycles per pixel

```
N_PF_per_pixel = N_PF_per_line / N = 2048 / 512 = 4 cycles/pixel
```

At each pixel, the PeakForce feedback averages over **4 complete tip–sample interaction cycles**, improving noise rejection.

---

### 6. Effective Z range of the Height Sensor channel

```
Z_range = Z_magnify × Z_scale × ZsensSens
        = 0.001394189 × 24.57563 V × 204.3017 nm/V
        = 7.00 nm
```

The entire vertical dynamic range of this image spans only **7 nm** — consistent with an atomically smooth Au-rich alloy surface where step edges are sub-nm in height.

---

### 7. Z digital resolution (Height Sensor, 16-bit ADC)

```
δz = Z_range / 2¹⁶ = 7.00 nm / 65536 = 0.107 pm ≈ 0.11 pm
```

The theoretical digitisation step is **0.11 pm** — well below the physical noise floor of the instrument, confirming the ADC is not the resolution bottleneck.

---

### 8. Effective range of the Peak Force Error channel

```
F_range = Z_magnify(ch2) × Z_scale(ch2) × ForceDeflSens
        = 0.0007290422 × 24.57563 V × 24.00 nN/V
        = 0.430 nN = 430 pN
```

The Peak Force Error channel records deviations of the measured peak force from the setpoint over a ±430 pN window.

---

### 9. PeakForce oscillation amplitude verification

From the SoftHarmoniX drive:
- `DriveAmplitude3SoftHarmoniX` = 204.1372 mV
- `DriveAmplitude3Sens` = 734.8000 nm/V

```
Z_osc = 204.1372 mV × 0.001 V/mV × 734.8 nm/V = 149.96 nm ≈ 150 nm
```

This matches `\Peak Force Amplitude: 150` exactly — cross-validates the calibration chain. ✓

---

### 10. PeakForce setpoint force

The ScanAsyst autopilot maintains the peak force at a target value. The setpoint is stored as a voltage and converted via `ForceDeflSens`:

```
SoftHarmoniXSetpoint = 0.02737500 V  (from \@2:SoftHarmoniXSetpoint)
ForceDeflSens        = 24.00 nN/V    (from \@Sens. ForceDeflSens)

F_setpoint = 0.02737500 V × 24.00 nN/V = 0.657 nN ≈ 657 pN
```

The autopilot keeps the peak tip–sample force at **~660 pN** per PeakForce cycle. This is the primary parameter the ScanAsyst controller optimises in real time. As a cross-check, the `\@2:DigitalSetPoint` (0.2500 V × deflection sensitivity) gives a related but distinct value used for the digital feedback loop — the SoftHarmoniXSetpoint is the operative physical force target.

---

### Summary of calculated quantities

`scan_control` is inherited from **NXspm** into **NXafm**. It contains two sub-groups:
- `meshScan` — describes the raster grid parameters (how the tip sweeps the area)
- `scan_region` — describes the physical spatial extent and position of the scanned area

| Quantity | Value | Formula | Raw header fields used | NXafm `scan_control` concept |
|---|---|---|---|---|
| Lateral pixel size | **0.977 nm/pixel** | `\Scan Size` ÷ `\Samps/line` | 500 nm ÷ 512 | `meshScan/step_size` — step between adjacent pixels along both fast and slow axes |
| Scan frame duration | **524 s ≈ 8.74 min** | `\Lines` ÷ `\Scan Rate` | 512 ÷ 0.976563 Hz | `meshScan/frame_time` — total duration for one complete raster frame |
| Tip lateral velocity | **488 nm/s** | `\Scan Size` × `\Scan Rate` | 500 nm × 0.976563 Hz | `meshScan/scan_speed` — tip velocity along the fast scan axis |
| PeakForce cycles per line | **2048** | `\PFT Freq` × (1 ÷ `\Scan Rate`) | 2000 Hz × 1.024 s | `meshScan` context only — number of PeakForce tip–sample interactions per line; not a named NXafm field but derivable from `scan_speed` and PFT frequency |
| PeakForce cycles per pixel | **4** | PF cycles/line ÷ `\Samps/line` | 2048 ÷ 512 | `meshScan` context only — interactions averaged per pixel; not a named NXafm field |
| Height Sensor effective Z range | **7.00 nm** | `@Z magnify` × `@2:Z scale` × `@Sens. ZsensSens` | 0.001394189 × 24.57563 V × 204.3017 nm/V | `scan_region/z_range` — physical Z extent captured in this image; upper bound on surface roughness visible in the scan |
| Z digital resolution | **0.11 pm** | Z range ÷ 2^(`\Bytes/pixel` × 8) | 7.00 nm ÷ 65 536 | `scan_region` context — quantifies the digitisation step within the Z range; not a named NXafm field but characterises the precision of `z_range` |
| Peak Force Error range | **430 pN** | `@Z magnify`(ch2) × `@2:Z scale`(ch2) × `@Sens. ForceDeflSens` | 0.0007290422 × 24.57563 V × 24.00 nN/V | Not in `scan_control`; belongs to the channel data block (Peak Force Error detector calibration range) |
| PeakForce oscillation amplitude (verified) | **150 nm** | `@DriveAmplitude3SoftHarmoniX` × `@Sens. DriveAmplitude3Sens` = `\Peak Force Amplitude` | 204.1372 mV × 734.8000 nm/V = 150.00 nm ✓ | Not in `scan_control`; AFM-specific drive parameter — maps to NXafm `cantilever/oscillation_amplitude` |
| PeakForce setpoint force | **657 pN** | `@2:SoftHarmoniXSetpoint` × `@Sens. ForceDeflSens` | 0.02737500 V × 24.00 nN/V | Not in `scan_control`; force setpoint maintained by ScanAsyst autopilot per PeakForce cycle — maps to NXafm `cantilever/setpoint` |

**Direct `scan_control` field resolution from raw file:**

| NXafm field | Group | Value | Resolved from |
|---|---|---|---|
| `step_size` (x and y equal) | `meshScan` | 0.977 nm | calculated: `\Scan Size` ÷ `\Samps/line` |
| `number_of_lines` | `meshScan` | 512 | direct: `\Lines: 512` |
| `scan_points_per_line` | `meshScan` | 512 | direct: `\Samps/line: 512` |
| `scan_speed` | `meshScan` | 488 nm/s | calculated: `\Scan Size` × `\Scan Rate` |
| `line_time` | `meshScan` | 1024 ms | calculated: 1 ÷ `\Scan Rate` |
| `scan_direction` | `meshScan` | Retrace | direct: `\Line Direction: Retrace` |
| `bidirectional` | `meshScan` | False | direct: `\Bidirectional Scan: Disabled` |
| `scan_size_x`, `scan_size_y` | `scan_region` | 500 nm | direct: `\Scan Size: 500 nm` |
| `center_x`, `center_y` | `scan_region` | 0 nm, 0 nm | direct: `\X Offset: 0 nm`, `\Y Offset: 0 nm` |
| `rotation_angle` | `scan_region` | 0° | direct: `\Rotate Ang.: 0` |
| `z_range` | `scan_region` | 7.00 nm | calculated: `@Z magnify` × `@2:Z scale` × `@Sens. ZsensSens` |

---

## Data Channels

Two simultaneous channels are recorded, stored as consecutive binary blocks after the header.

| Channel | Name | Physical quantity | Sensitivity | Offset (B) | Size (B) |
|---|---|---|---|---|---|
| 1 | **Height Sensor** | Z piezo position | ZsensSens = 204.3 nm/V | 40 960 | 524 288 |
| 2 | **Peak Force Error** | Peak force deviation | ForceDeflSens = 24.00 nN/V | 565 248 | 524 288 |

Both channels: 512 × 512 pixels, 2 bytes/pixel (signed 16-bit integer, big-endian).

**Converting raw integers to physical units:**

```
Z_nm(i,j) = raw(i,j) × Z_magnify × (Z_scale_V / 32768) × ZsensSens_nm_per_V

For channel 1 (Height Sensor):
  Z_nm = raw × 0.001394189 × (24.57563 / 32768) × 204.3017
       = raw × 0.001394189 × 7.498 × 10⁻⁴ × 204.3017
       = raw × 2.133 × 10⁻⁴ nm

For channel 2 (Peak Force Error):
  F_nN = raw × 0.0007290422 × (24.57563 / 32768) × 24.00
       = raw × 1.311 × 10⁻⁵ nN = raw × 13.11 fN
```

> **Note:** Bruker binary data is big-endian signed 16-bit. The full Z_scale encodes the DAC full-scale range; the Z_magnify factor encodes how much of that range the instrument actually used during this scan.

---

## Instrument and Hardware
(?? verify if this is correct)
| Component | Model / Value | Role |
|---|---|---|
| AFM platform | **Bruker Dimension Icon** | Main instrument |
| Scanner | Dim 4000 (serial `1A00CD`) | Closed-loop XY piezo scanner |
| Head type | `SG` | ScanAsyst-compatible optical beam deflection head |
| Cantilever resonance | **81.597 kHz** | `\@2:CantFrequency` from thermal tune (range 1–100 kHz) |
| Cantilever phase at resonance | **−67.1°** | `\@2:CantPhase` — negative phase indicates tip is tracking the drive with a lag, consistent with operation below resonance in PeakForce mode |
| Cantilever drive amplitude | **1145 mV** | `\@2:CantDrive` — electrical drive to the acoustic piezo |
| Spring constant | **not stored** | No force calibration performed; PeakForce Tapping Imaging controls peak force directly without needing spring constant |
| Deflection sensitivity | **60 nm/V** | `\@Sens. DeflSens` — optical lever arm calibration |
| ForceDeflSens | **24.00 nN/V** | `\@Sens. ForceDeflSens` — used by PeakForce feedback to convert deflection voltage to force |
| Tip radius | **5 nm** | `\Tip Radius: 5` — sharp tip, resolution-optimised; used by real-time Hertz QNM engine |
| Tip half angle | **18.0°** | `\Tip Half Angle: 0.314159 rad` — used by Sneddon conical model as alternative to Hertz |
| Fluid cell | No | `\Fluid Cell: No` |
| Medium | Air | `\Medium: Air` |
| XY sensor | Optical (OptoXY) | Closed-loop: `\XY Closed Loop: On` |
| Z sensor | Capacitive, ZsensSens = 204.3 nm/V | Open-loop during scan: `\Z Closed Loop: Off` |
| Vision | uEye UI148xLE-C #1 | Optical navigation camera |
| Operating temperature | Room temperature | Not recorded explicitly |

**Z Closed Loop: Off** means the Z scanner is driven open-loop (no capacitive Z-position feedback during the scan). The `Height Sensor` channel still records the Z piezo position; the accuracy is limited by the piezo's mechanical linearity rather than a sensor.

**XY Closed Loop: On** means the lateral position is capacitively sensed and corrected in real time, giving accurate metric-scale lateral coordinates (no drift correction needed for XY).

---

## PeakForce Tapping / ScanAsyst — Technical Details
 (?? no need)
This measurement uses **PeakForce Tapping** (Bruker's sinusoidal Z-oscillation at 2 kHz) in **ScanAsyst autopilot** mode, not classical tapping mode (AM-AFM).

| Aspect | Classical Tapping (AM-AFM) | PeakForce Tapping (ScanAsyst) |
|---|---|---|
| Tip oscillation | Driven near resonance (~81.6 kHz here) | Sinusoidal at fixed off-resonance frequency (2 kHz) |
| Feedback signal | Amplitude setpoint | Peak force per cycle |
| Data per pixel | Amplitude + phase | Z height + force error (+ optional QNM channels) |
| Sample interaction | Intermittent, amplitude-controlled | Force-controlled peak interaction |
| ScanAsyst | Manual parameter setting | AI autopilot optimises gains, setpoint, scan rate |

### ScanAsyst autopilot settings
(?? no need)
| Control | State |
|---|---|
| `ScanAsyst Auto Control` | On |
| `ScanAsyst Auto Gain` | On |
| `ScanAsyst Auto Setpoint` | On |
| `ScanAsyst Auto Scan Rate` | On |
| `ScanAsyst Auto Z Limit` | On |
| `ScanAsyst Noise Threshold` | 0.15 |

All major scan parameters were auto-optimised in real time. The 0.976563 Hz scan rate (1/1.024 Hz) is therefore the AI-selected operating point for this surface.

### SoftHarmoniX
(??no need)

The `\@MicroscopeList: "ScanAsyst"` field maps to the `SoftHarmoniXAutoPilot` mode internally. SoftHarmoniX superimposes a slow sinusoidal Z modulation (Drive 3, at `\@2:DriveFrequency3SoftHarmoniX: 1.953125 kHz`, close to but offset from the 2 kHz PeakForce drive) on top of the PeakForce oscillation and uses lock-in detection of the cantilever response at that frequency to extract visco-elastic contrast in real time. Three lock-in channels are configured:

| Lock-in | Source (this scan) | Purpose |
|---|---|---|
| `LockIn1` | Enabled (Non-Contact mode), source: Vertical | Detects cantilever deflection at the SoftHarmoniX drive frequency — relates to elastic response |
| `LockIn2` | Disabled | Not used in this scan |
| `LockIn3` | Enabled, source: Vertical | Detects deflection at the PeakForce frequency (2 kHz) — the primary PeakForce control signal |

The LockIn1 output is the source of real-time storage modulus contrast; LockIn3 provides the peak force error for the Z feedback loop. Neither lock-in output is stored as an image channel in this file (only Height Sensor and Peak Force Error are written); they operate entirely as internal signals.

---

## PeakForce Tapping Imaging vs. PeakForce QNM
(?? is it possile a single file will store both image and force curves)
This file uses **PeakForce Tapping Imaging** mode — this must be distinguished from **PeakForce Quantitative Nanomechanical Mapping (PeakForce QNM)**, which is a related but distinct operating mode also available on the Bruker Dimension Icon.

| Aspect | PeakForce Tapping Imaging *(this file)* | PeakForce QNM (Force Volume) |
|---|---|---|
| `\Operating mode` | `Image` | `Force` |
| `\PeakForce Capture` | `Never` | Implicit in force file format |
| Data stored per pixel | Z height + Peak Force Error only | Full approach–retract force curve (64 points here) |
| QNM properties (modulus, adhesion…) | Computed on-board in real time per cycle, **not saved** | Fitted post-acquisition from stored curves, **saved** |
| File type in header | `\*Ciao image list` | `\*Ciao force list` / `\*Ciao force image list` |
| File size (512×512 scan) | **1.04 MB** (2 × 512 × 512 × 2 bytes) | ~34 MB (262 144 curves × 64 points × 2 bytes × 2 directions) |
| Spring constant required | No — force controlled directly via voltage setpoint | Yes — needed for force conversion (F = k × δ) |
| Example file in this repo | This file (`area_168.002`) | `Bruker_AFM_PeakForce_QNM/SB04-MG1.0_00000.spm.txt` |

**Consequence for this file:** All the QNM sensitivity definitions present in the header (`FVModulusSens`, `DeformationSens`, `DissipationSens`, etc.) describe channels that the on-board controller *could* compute and store, but which are suppressed by `PeakForce Capture: Never`. The Hertzian fit and deformation tracking happen inside the controller firmware at 2 kHz per pixel — only the two derived summary images exit to disk.

---

## Contact Mechanics — Real-Time QNM Engine
(?? after on wards no need)
Even though no force curves are stored in this file, the on-board QNM engine runs a complete contact mechanics fit at every PeakForce cycle (4 cycles per pixel, 2048 cycles per scan line). The configuration parameters for this engine are all present in the header.

### Hertzian (Spherical) model

The Bruker real-time QNM engine uses the **Hertz contact model** for a spherical indenter:

$$F = \frac{4}{3} E^{*} \sqrt{R} \cdot \delta^{3/2}$$

where:
- **F** is the applied peak force (maintained at 657 pN setpoint)
- **E\*** is the reduced Young's modulus (combined tip + sample elasticity)
- **R** is the tip radius (5 nm, from `\Tip Radius: 5`)
- **δ** is the indentation depth

The **reduced modulus** E* relates to the sample Young's modulus E_s and Poisson ratio ν_s (and the same quantities for the tip material) as:

$$\frac{1}{E^*} = \frac{1 - \nu_s^2}{E_s} + \frac{1 - \nu_{tip}^2}{E_{tip}}$$

For a diamond-like tip (E_tip ≈ 1000 GPa), the tip term is negligible for most samples, so E* ≈ E_s / (1 − ν_s²).

### QNM engine parameters from this file's header

| Parameter | Value | Header field | Role in QNM fit |
|---|---|---|---|
| Tip radius | **5 nm** | `\Tip Radius: 5` | R in Hertz model — determines force-to-modulus conversion sensitivity |
| Tip half angle | **18.0° (0.314 rad)** | `\Tip Half Angle: 0.314159` | Used by Sneddon conical model as an alternative to Hertz spherical |
| Fit model | **Hertzian (Spherical)** | `\Modulus Fit Model` | Selects Hertz over Sneddon; appropriate for rounded ScanAsyst tips |
| Adhesion algorithm | **Threshold Crossing** | `\Adhesion Algorithm` | Detects pull-off force as the point where the retract curve crosses a threshold |
| Adhesion fit % | **0.1%** | `\Adhesion Fit %` | Fraction of max force used as the threshold for adhesion detection |
| Deformation fit region | **98%** | `\Deformation Fit Region` | Uses 98% of the approach curve for deformation calculation, excluding the contact onset |
| Include adhesion in modulus fit | **Yes** | `\Include Adhesion Force` | DMT-style correction: adhesion force is added back to F before fitting |
| Force data points per cycle | **64** | `\Force Data Points: 64` | Digitisation of the 2 kHz cycle inside the controller (not saved, but determines fit resolution) |
| Sync Distance QNM | **81.6** | `\Sync Distance QNM` | Trigger offset (in nm) that aligns the PeakForce data acquisition window with the cantilever oscillation cycle — critical for correct contact point detection |
| QNM calibration method | **DefaultByZ** | `\QNM Calibration` | Uses the Z-sensor sensitivity (ZsensSens = 204.3 nm/V) to calibrate the indentation depth, rather than requiring a separate sensitivity calibration on a hard reference surface |

### Sneddon conical model (alternative, available but not selected)

The header also defines `\@Sens. SneddonModulusSens` and `\@1:SneddonModulusLimit`, confirming the Sneddon model is implemented but not active here. The Sneddon model for a conical tip is:

$$F = \frac{2}{\pi} E^{*} \tan(\alpha) \cdot \delta^{2}$$

where α is the tip half-angle (18° here). It is appropriate for very sharp tips where the apex is better approximated by a cone than a sphere.

### What QNM outputs would be stored if `PeakForce Capture` were enabled

| QNM Property | Sensitivity defined in header | Physical meaning | Units |
|---|---|---|---|
| **Young's modulus (E\*)** | `FVModulusSens: 1.000 Pa/Arb` | Elastic stiffness from Hertz fit | Pa |
| **Adhesion force** | `FVForceSens: 1.000 nN/Arb` | Peak pull-off force on retract | nN |
| **Deformation** | `DeformationSens: 3674 nm/V` | Depth of tip indentation at peak force | nm |
| **Dissipation** | `DissipationSens: 1.000 Arb/Arb` | Energy lost per PeakForce cycle (viscous/plastic) | eV |
| **Stiffness** | `StiffnessSens: 1.000 N/m*Arb` | Contact spring constant (slope of contact region) | N/m |
| **Sneddon modulus** | `SneddonModulusSens: 1.000 Arb/Arb` | Modulus via conical model (not used here) | Pa |
| **FV stiffness** | `FVStiffnessSens: 1.000 N/m*Arb` | Force-volume derived stiffness | N/m |

These channels are computed on-board at 2 kHz but suppressed at the output stage. With `PeakForce Capture: Always`, each would appear as an additional `\*Ciao image list` block in the file, adding ~262 kB per channel.

---

## Physical Properties Measured

### Stored channels (in this file)

| Channel | Property | Units | Physical meaning |
|---|---|---|---|
| **Height Sensor** | Surface topography | nm | Z piezo position tracking the surface; records morphology |
| **Peak Force Error** | Force servo error | nN | Deviation of the measured peak force from the 657 pN setpoint — qualitative contrast between regions of different stiffness or adhesion |

The 7 nm effective Z range indicates the imaged area has very low surface roughness, consistent with an Au-rich alloy surface expected to be close-packed and smooth.

### QNM-derived channels computed internally but not stored

The on-board Hertz-fit engine computes the following per pixel from the 4 PeakForce cycles, but discards them at the output stage (`PeakForce Capture: Never`):

| Property | Would reflect | Why absent from file |
|---|---|---|
| Young's modulus E* | Elastic stiffness of the Au-rich surface | `PeakForce Capture: Never`; no force curves saved |
| Adhesion force | Tip–surface pull-off (Au–tip van der Waals/contact) | Same |
| Deformation | Indentation depth at 657 pN peak force | Same |
| Dissipation | Viscoelastic energy loss per oscillation | Same |
| Storage / loss modulus | Elastic vs. viscous components via SoftHarmoniX LockIn1 | Same |

For the Au-rich alloy surface, these would all show very small contrast since a noble metal surface is mechanically homogeneous at the 500 nm scale — the Height Sensor and Peak Force Error channels are therefore sufficient for this morphological scan.

### Scientific context

Au-Ir-Rh ternary alloy surfaces are of interest in:
- Surface science: atomic-scale segregation of noble metals under annealing
- Catalysis: Au-rich terminations may modify adsorption energetics for Ir and Rh
- Surface alloy stability: understanding which face-centred cubic (FCC) stacking and surface composition is thermodynamically stable
- Hydrogen evolution reaction (HER) electrocatalyst discovery: this measurement area (MA 168) is one of 15 AFM-characterised positions in the SECCM campaign, providing morphology cross-validation for the electrochemical activity map

A 500 nm scan at sub-nm lateral resolution (~0.977 nm/pixel) on a Au-rich surface can resolve:
- Monoatomic step edges (~0.235 nm height for Au FCC (111) — detectable given the 7 nm Z range and 0.11 pm digital resolution)
- Surface reconstruction domains (Au(111) herringbone reconstruction has a ~63 × 22 Å unit cell — visible within this scan window)
- Nanoscale compositional heterogeneity via Peak Force Error contrast (harder Ir- or Rh-rich nano-inclusions would appear brighter in the error channel)

The 5 nm tip radius gives genuine sub-10 nm spatial resolution, making this scan suitable for resolving individual terraces and reconstruction domains. By contrast, the PeakForce QNM companion file (`SB04-MG1.0_00000.spm.txt`) uses a 3000 nm blunt tip optimised for soft-matter mechanical mapping — a trade-off between force resolution and lateral resolution.

---

## Questions about the Experiment

### Q1 — Does this file contain any single-point scans on a defined grid?

**No.** The header contains exactly **9 sections** and only **two data blocks**, both of type `\*Ciao image list`:

| Block | Channel | `Data offset` | `Data length` | Physical quantity |
|---|---|---|---|---|
| 1 | Height Sensor (`ZSensor`) | 40 960 B | 524 288 B | Z piezo position (nm) |
| 2 | Peak Force Error | 565 248 B | 524 288 B | Peak force deviation (nN) |

Total file size: `40 960 + 524 288 + 524 288 = 1 089 536 bytes` — which matches the actual file size on disk exactly. There is no remaining space for any additional data.

The header provides three corroborating confirmations that no single-point or force-curve data is present:

| Header key | Value | Meaning |
|---|---|---|
| `\Operating mode` | `Image` | The instrument ran a full-frame raster image scan, not a force-ramp or spectroscopy mode |
| `\PeakForce Capture` | `Never` | The raw per-pixel approach–retract force curves generated internally by PeakForce Tapping are explicitly **not saved to disk** |
| `\*Ciao force list` section | **absent** | No force-distance curve block exists in the file |

The `Force Data Points: 64`, `QNM Calibration`, and `Modulus Fit Model: Hertzian (Spherical)` entries in the header are configuration parameters for the **real-time on-board QNM engine**, not indicators of stored force data. They define how the controller fits each 2 kHz approach-retract cycle internally to derive the Peak Force Error signal before writing it to the image channel.

The macroscopic "342-point grid" mentioned in the dataset context refers to the wafer-level stage-motor grid used for positioning the tip between measurement areas (MAs). That grid is encoded in the `\Stage X` / `\Stage Y` header fields (`Stage X: −22 187 µm`, `Stage Y: −40 500 µm`) and in the companion SECCM/EDX datasets — it is **not** a data structure inside this file.

---

### Q2 — Is it possible to record a single-point scan on a grid using PeakForce Tapping mode?

**Yes.** The Bruker Dimension Icon platform offers three mechanisms for collecting force-resolved single-point data on a user-defined grid while operating in PeakForce Tapping mode:

#### Mechanism 1 — `PeakForce Capture: Grid` (sparse force-curve capture)

The header parameter `\PeakForce Capture` controls whether the raw per-pixel approach–retract curves are written to disk:

| `PeakForce Capture` value | Behaviour |
|---|---|
| `Never` *(this file)* | No force curves saved; only derived image channels (Height Sensor, Peak Force Error) are recorded |
| `Always` | A complete force curve (64 points by default — `\Force Data Points: 64`) is saved at **every** pixel, producing a much larger file |
| `Grid` | Force curves are saved only at a sparse user-defined sub-grid overlaid on the raster scan |

Switching to `Grid` mode would produce an output file containing both the two standard `*Ciao image list` channels and an additional `*Ciao force list` section holding the per-grid-point force curves. This is the most practical approach for combining full-field topography with spatially resolved mechanical mapping.

#### Mechanism 2 — Point & Shoot spectroscopy

The header entry `\Show Point & Shoot Button: Expanded Mode` confirms that the **Point & Shoot** button was present and accessible in the Nanoscope UI during this scan. Point & Shoot allows the operator to:
1. Park the raster scan.
2. Click on one or more XY positions in the live image.
3. Drive the tip to each position and record a single approach–retract force curve.

The resulting spectroscopy data is saved as a separate file (`.000`, `.001`, … extension in force mode) with a `*Ciao force list` section rather than a `*Ciao image list`. It is not embedded in the raster image file.

#### Mechanism 3 — Force Volume mode

On the Bruker Dimension Icon, selecting `\Operating mode: Force Volume` replaces the raster image scan with a pre-defined grid of force-ramp positions. At each grid point the tip records a full approach–retract curve. The header would then contain `*Ciao force list` sections for each recorded curve and corresponding derived image channels (Modulus, Adhesion, Deformation, Dissipation mapped from the Hertzian fit). This is the standard method for spatially resolved nanomechanical mapping when the real-time QNM output of PeakForce Tapping is insufficient.

#### Why none of these are used here

This file uses `\Operating mode: Image` with `\PeakForce Capture: Never`, which is the standard PeakForce Tapping imaging configuration. At 2 kHz PeakForce frequency and 0.977 Hz scan rate, storing force curves for all 512 × 512 pixels would require saving 262 144 curves × 64 points × 2 bytes ≈ **33.6 MB** additional data per frame — a 30-fold increase over the current 1 MB file. For this campaign the real-time derived Height Sensor and Peak Force Error channels are sufficient; per-pixel force data was not needed.

---

## File Series Context

The `.002` suffix indicates this is the **third file in a sequence** (0-indexed). Typical Bruker series conventions:

| File | Likely context |
|---|---|
| `...area_168.000` | First scan of area 168 |
| `...area_168.001` | Second scan (e.g. after parameter adjustment) |
| `...area_168.002` | This file — third scan |

Without access to the sibling files, it is unknown whether the series represents repeated scans of the same area (to check drift / stability) or a zoom-out sequence.

---

## Relation to pynxtools-spm

In this codebase, the binary `.spm` file is processed by:

| Layer | File | Role |
|---|---|---|
| Parser | `src/pynxtools_spm/parsers/bruker_spm.py` | Reads header + binary data → flat dict |
| Formatter | `src/pynxtools_spm/nxformatters/bruker/` | Maps dict → NeXus template |
| Config | `src/pynxtools_spm/configs/bruker/` | JSON mapping of raw keys → NeXus paths |
| Reader | `src/pynxtools_spm/reader.py` | Entry point; dispatches based on file type and `experiment_technique` |

The ELN file accompanying this measurement should contain `experiment_technique: AFM`.

---

## References

- **PeakForce Tapping / PeakForce QNM:** Pittenger, B. et al. *Quantitative Mechanical Property Mapping at the Nanoscale with PeakForce QNM.* Bruker Application Note AN128 (2010).
- **ScanAsyst / SoftHarmoniX:** Bruker ScanAsyst and PeakForce Tapping Application Notes.
- **Hertz contact model:** Johnson, K.L. *Contact Mechanics.* Cambridge University Press (1985). See also: [Wikipedia — Contact Mechanics](https://en.wikipedia.org/wiki/Contact_mechanics).
- **Sneddon conical indenter model:** Sneddon, I.N. *The relation between load and penetration in the axisymmetric Boussinesq problem for a punch of arbitrary profile.* Int. J. Eng. Sci. 3, 47–57 (1965).
- **DMT adhesion correction (used here via `Include Adhesion Force: Yes`):** Derjaguin, B.V., Muller, V.M., Toporov, Y.P. *Effect of contact deformations on the adhesion of particles.* J. Colloid Interface Sci. 53, 314–326 (1975).
- **Bruker Dimension Icon:** Bruker product page.
- **Nanoscope file format (community reverse-engineering):** Gwyddion SPM analysis software documentation, File Formats → NanoScope.
- **Au(111) surface reconstruction:** Barth, J.V. et al. *Scanning Tunneling Microscopy Observations on the Reconstructed Au(111) Surface.* Phys. Rev. B 42, 9307 (1990).
- **Au-Ir-Rh SECCM campaign (dataset source):** Zenodo record 20439519 (DOI linked to `DataSetnote.txt` in this directory).
