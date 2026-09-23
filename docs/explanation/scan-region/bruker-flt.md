# Scan region in Bruker SPMLab `.FLT`

How an SPMLab `.FLT` file states the scanned area, and how the reader turns it
into NeXus under [the scan region convention](../scan-region-conventions.md).

## Raw keys

| Raw key | Meaning | How the reader uses it |
|---|---|---|
| `OffsetX`, `OffsetY` | Centre of the scan frame | `scan_offset_value_x`, `_y` |
| `ScanRangeX`, `ScanRangeY` | Width and height | `scan_range_x`, `_y` |
| `ResolutionX`, `ResolutionY` | Pixels per line, number of lines | `scan_points_x`, `_y` |
| `ScanDirection` | `FORWARD` or `BACKWARD`, the fast direction | Sign of the fast axis |
| `Rotation` | Rotation of the frame | `scan_angle_x`, not applied |

A `.FLT` holds a single channel recorded in one direction, so the fast axis is
signed. The format records **no slow scan direction**, so the slow axis stays
bare. The `[Data]` block holds only the height values, `ResolutionX ×
ResolutionY` 32-bit floats; no axis coordinates are stored.

**Open question.** Because the slow direction is absent from the header, a bare
`Y` here states ignorance rather than an upward scan. An SPMLab or Innova manual,
or a pair of up and down scans of the same area, would settle it.
## Evidence

No vendor document defining `OffsetX` was found, so the centre reading is graded
**empirical test on vendor data**: a 5 µm scan and a 20 µm scan of the same
sample carry identical offsets, and the small scan was located inside the large
one by cross-correlation. The
[method](../scan-region-conventions.md#how-the-empirical-test-works) and the
[data](../scan-region-conventions.md#data-used) are described centrally.

| Pair | Correlation peak / next | Measured | Centre predicts | Corner predicts |
|---|---|---|---|---|
| `PMIS2-C8_ML2_p1_5` in `…_p1_20`, identical offsets | 0.54 / 0.10 | (10.00, 10.04) µm | (10.00, 10.00) µm | (2.50, 2.50) µm |

The 5 µm scan sits in the middle of the 20 µm one, one pixel (39 nm) from the
centre prediction and 10.6 µm from the corner prediction. Three further pairs of
the same record, with different offsets, agree to 0.02, 0.05 and 0.7 µm. The
match is found only with the rows read bottom row first, which also confirms the
image orientation.

Gwyddion's `spmlabf.c` reads the offset as a corner, without a cited source; the
test contradicts it.
