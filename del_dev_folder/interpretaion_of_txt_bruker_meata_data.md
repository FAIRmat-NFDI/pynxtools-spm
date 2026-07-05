# Interpretation of Bruker SPM `.txt` Metadata File

This document notes the interpretation of the parsed metadata keys from a Bruker `.spm.txt`
auxiliary file (e.g. `SB04-MG1.0_00000.spm.txt`), specifically for an AFM
**Force Spectroscopy (Force-Distance Curve)** experiment.

---

## Experiment Type

| Key | Value | Interpretation |
|-----|-------|----------------|
| `/Operating_mode` | `Force` | This is a force-distance (spectroscopy) measurement, **not** a 2D raster image scan |
| `/Parameter_select` | `Main` | Using the main parameter set |

---

## Scan Region Definition

### Centre / Origin

The scan region centre is defined by the **X/Y Position** (in instrument coordinates)
plus an **X/Y Offset** from the stage centre.

| Key | Value | Meaning |
|-----|-------|---------|
| `/X_Position` | `0` | X centre of the scan frame in instrument coordinates |
| `/Y_Position` | `0` | Y centre of the scan frame in instrument coordinates |
| `/X_Offset` | `-2000 nm` | X displacement from stage centre to scan origin |
| `/Y_Offset` | `-2000 nm` | Y displacement from stage centre to scan origin |

### Scan Area Size

| Key | Value | Meaning |
|-----|-------|---------|
| `/Scan_Size` | `0 nm` | Side length of the square scan area. **Zero** because no lateral 2D scanning is performed in force mode |
| `/Aspect_Ratio` | `1:1` | X and Y physical extents are equal (square scan frame) |
| `/Rotate_Ang.` | `0` | Scan frame rotation angle in degrees (no rotation) |

### Grid Resolution (Pixels)

| Key | Value | Meaning |
|-----|-------|---------|
| `/Samps/line` | `9728` | Data points sampled per ramp line — the X-axis resolution of the force curve |
| `/Lines` | `256` | Number of scan lines (Y-axis) — irrelevant here because `/Y_disable: Enabled` |
| `/Y_disable` | `Enabled` | Y-axis scanning is **off**; no lateral sweep, only Z |

> **Note**: Because `/Scan_Size = 0` and `/Y_disable = Enabled`, there is **no 2D scan area**.
> The tip is stationary at the X/Y offset position and sweeps only in Z.

### Start and End Points (Z-ramp / Force Curve)

| Key | Value | Meaning |
|-----|-------|---------|
| `/Start_size` | `13199.8 nm` | Z-ramp start position (tip far from surface) |
| `/@4: Ramp_End` | `0 nm` | Z-ramp end position (tip at/near surface) |

The ramp sweeps from `Start_size = 13199.8 nm` down to `Ramp_End = 0 nm` in the
extension phase, and then retracts back. See `force_spectroscopy_parameters.md` for
the column definitions of the resulting force-curve data arrays.

---

## Stage Absolute Position

These are the physical stage coordinates at the time of measurement (not the scan region,
but useful for reproducing the exact location on the sample).

| Key | Value |
|-----|-------|
| `/Stage_X` | `-9797.5` |
| `/Stage_Y` | `-42233.8` |
| `/Stage_Z` | `-13884.7` |
| `/Stage_Optics` | `-5781.29` |

---

## Sensor Sensitivities (Calibration)

These convert raw digital counts (LSB / Volts) to physical units.

| Key | Value | Meaning |
|-----|-------|---------|
| `/@Sens._Zsens` | `17.94930 nm/V` | Z-piezo sensitivity |
| `/@Sens._CurrentSens` | `10.00000 nA/V` | Current sensor sensitivity |
| `/@Sens._Xsensor` | `6265.256 nm/V` | X closed-loop sensor sensitivity |
| `/@Sens._Ysensor` | `6356.550 nm/V` | Y closed-loop sensor sensitivity |

---

## Key Observation and Summary

This `.txt` file accompanies a Bruker **Force Spectroscopy** `.spm` file.
The scan region has **no lateral extent** (`Scan_Size = 0`). The measurement is:

1. Tip positioned at absolute stage coordinates (`Stage_X`, `Stage_Y`)
2. Laterally offset by `X_Offset = -2000 nm`, `Y_Offset = -2000 nm` from centre
3. Z-ramp performed from `13199.8 nm` → `0 nm` (extension) then back (retraction)
4. `9728` data points collected per ramp direction

For a **2D image scan** the `/Scan_Size` would be non-zero, `/Y_disable` would be
`Disabled`, and `/Operating_mode` would be `Tapping` or `Contact`.
