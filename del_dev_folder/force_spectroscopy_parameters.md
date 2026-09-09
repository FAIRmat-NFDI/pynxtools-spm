# Force Spectroscopy Data Parameters

These are **Force Spectroscopy (Force-Distance Curve) data parameters** from the Ciao force list.

## Parameter Breakdown

| Parameter Group | Meaning |
|-----------------|---------|
| **Time_s_Ex / Time_s_Rt** | Time in seconds during extension / retraction phase |
| **Calc_Ramp_Ex/Rt_nm** | Calculated ramp (Z-piezo displacement) in nanometers for extension/retraction |
| **Defl_V_Ex/Rt** | Deflection signal in Volts for extension/retraction |
| **Defl_nm_Ex/Rt** | Deflection converted to nanometers for extension/retraction |
| **Defl_pN_Ex/Rt** | Deflection converted to picoNewtons (force) for extension/retraction |
| **Defl_Lsb_Ex/Rt** | Deflection in LSB (raw digital counts) for extension/retraction |
| **Height_Sensor_V_Ex/Rt** | Z-position (height) sensor voltage for extension/retraction |
| **Height_Sensor_nm_Ex/Rt** | Z-position (height) in nanometers for extension/retraction |
| **Height_Sensor_Lsb_Ex/Rt** | Z-position (height) in LSB (raw counts) for extension/retraction |

## Key Context

- **Ex (Extension)**: Tip approaching/pushing into sample
- **Rt (Retraction)**: Tip retracting/pulling away from sample
- **Duplicated columns**: The header appears twice, suggesting two channels or sets of measurements are being displayed together

## Related Acquisition Settings

From the file metadata:

| Setting | Value |
|---------|-------|
| **Ramp Size** | 2500 nm |
| **Forward velocity** | 56.1125 (units: TBD) |
| **Reverse velocity** | 56.1125 (units: TBD) |
| **Scan rate** | 0.201436 Hz |
| **Samples/line** | 9728 |
| **Spring Constant** | 0.0538362 |
| **Ramp Position** | -80.71881 V |
| **Sample Period** | 16.00000 us |

## Description

This data represents the actual **force-distance curve** used for mechanical property analysis of the sample. Each row contains a measurement point during the approach (extension) and withdrawal (retraction) phases of the force spectroscopy measurement.

The data includes:
- **Time information**: Sequential sampling during the ramp
- **Z-displacement**: Piezo movement during approach/retraction
- **Deflection signals**: Raw and calibrated force measurements
- **Height sensor data**: Z-position tracking during the measurement

This information is essential for determining:
- Sample stiffness
- Adhesion forces
- Surface interactions
- Mechanical properties at the nanoscale
