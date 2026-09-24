# Interpretation of Bruker SPM Metadata

This note summarizes the scan-area information extracted from the slash-separated
metadata file `spm_file_data_keys.txt`, which was generated from the Bruker SPM file
`VGEP-15m-.0_00000.spm`.

## Source of the Scan Geometry

The most reliable scan-geometry fields are the scanner-level entries:

- `/Scanner_list/0/Scan_Size: 20000 nm`
- `/Scanner_list/0/X_Position: 0`
- `/Scanner_list/0/Y_Position: 0`
- `/Scanner_list/0/X_Offset: 0 nm`
- `/Scanner_list/0/Y_Offset: 0 nm`
- `/Scanner_list/0/Rotate_Ang.: 1.5708`
- `/Scanner_list/0/Samps/line: 512`
- `/Scanner_list/0/Lines: 512`
- `/Scanner_list/0/Aspect_Ratio: 1:1`

These values are consistent with the per-channel scan blocks such as:

- `/Scan/Height_Sensor/forward/Scan_Size: 20 20 ~m`
- `/Scan/Height_Sensor/forward/Samps/line: 512`
- `/Scan/Height_Sensor/forward/Number_of_lines: 512`
- `/Scan/Height_Sensor/forward/Valid_data_start_X: 0`
- `/Scan/Height_Sensor/forward/Valid_data_len_X: 512`

## Lateral Scan Area

| Quantity | Value | Interpretation |
|----------|-------|----------------|
| Scan size | `20000 nm` | Lateral field of view is `20 um x 20 um` |
| X center | `0 nm` | Scan center along X |
| Y center | `0 nm` | Scan center along Y |
| X offset | `0 nm` | No additional X offset |
| Y offset | `0 nm` | No additional Y offset |
| Rotation | `1.5708 rad` | Approximately `90°` rotation |
| Samples per line | `512` | Number of X points |
| Number of lines | `512` | Number of Y points |
| Aspect ratio | `1:1` | Square scan |

## Derived Start and End Positions

Assuming the scan is centered at `(0, 0)` with zero offset and side length `20000 nm`:

- X start = `-10000 nm`
- X end = `+10000 nm`
- Y start = `-10000 nm`
- Y end = `+10000 nm`

The calculation is:

- `start = center - scan_size / 2`
- `end = center + scan_size / 2`

So the lateral scan box in scanner coordinates is:

| Axis | Start | End |
|------|-------|-----|
| X | `-10000 nm` | `+10000 nm` |
| Y | `-10000 nm` | `+10000 nm` |

## Effect of Non-Zero Offset

When offsets are non-zero, use:

- `start = center + offset - scan_size / 2`
- `end = center + offset + scan_size / 2`

Worked example for X axis with:

- `X_center = 0 nm`
- `X_offset = 100 nm`
- `scan_size = 20000 nm`

Then:

- `X_start = 0 + 100 - 10000 = -9900 nm`
- `X_end = 0 + 100 + 10000 = 10100 nm`

So a `+100 nm` X offset shifts the full X scan range by `+100 nm`:

- from `[-10000, +10000] nm`
- to `[-9900, +10100] nm`

## Lateral Sampling

The lateral sampling grid is `512 x 512`.

Two common ways to express the spacing are:

- Pixel size: `20000 / 512 = 39.0625 nm/pixel`
- Point-to-point interval: `20000 / (512 - 1) ≈ 39.14 nm`

For image data, `39.06 nm/pixel` is usually the more practical value.

## Valid Data Window

The per-channel metadata shows:

- `Valid_data_start_X = 0`
- `Valid_data_start_Y = 0`
- `Valid_data_len_X = 512`
- `Valid_data_len_Y = 512`

This indicates the full image is valid and no cropped subregion is defined.

## Stage Position

The absolute stage coordinates at acquisition time are:

- `Stage_X = 4061.25`
- `Stage_Y = 19872.8`
- `Stage_Z = -16797.4`

These are useful for locating the measurement on the sample, but they are not the
same as the scan-box start and end coordinates.

## Note on a Metadata Inconsistency

The scanner-level metadata also contains:

- `/Scanner_list/0/Y_disable: Enabled`

That conflicts with the presence of full `512 x 512` image channels in the same file.
For this file, the repeated per-channel image metadata and the `Scan_Size`, `Samps/line`,
and `Lines` fields are more trustworthy for reconstructing the lateral scan area.

## Summary

This Bruker SPM file describes a `20 um x 20 um` AFM image scan with:

- center at `(0, 0)`
- no X/Y offset
- lateral range from `-10000 nm` to `+10000 nm` on both axes
- `512` scan points along X
- `512` scan points along Y
- approximate lateral pixel size of `39.06 nm`
- scan frame rotated by about `90°`
