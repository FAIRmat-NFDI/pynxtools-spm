# Scan region in Omicron / RHK `.sm4`

How an `.sm4` file from an Omicron microscope with an RHK controller states the
scanned area, and how the reader turns it into NeXus under [the scan region convention](../scan-region-conventions.md).

## Raw keys

| Raw key | Meaning | How the reader uses it |
|---|---|---|
| `RHK_Xoffset`, `RHK_Yoffset` | Centre of the scan area | `scan_offset_value_x`, `_y` |
| `RHK_Xscale`, `RHK_Yscale` | Signed distance between adjacent pixels | `\|scale\|` is the pixel pitch; the sign of `RHK_Yscale` is the slow direction |
| `RHK_Xsize`, `RHK_Ysize` | Pixels per line, number of lines | `scan_points_x`, `_y` |
| `RHK_X/@unit`, `RHK_Y/@unit` | Unit of the lateral axes | Unit of offset, range, start, end and step |
| `RHK_ScanType` | Names the Forward and Backward pass | Channel naming; one scan control group per page |
| `RHK_Angle` | Rotation of the frame | `scan_angle_x`, `_y`, not applied |

No range is stored: it is `range = N × |scale|`, the edge-to-edge width, counting
`N` pitches and not `N - 1`.

**How the scan direction was decided.** The slow direction comes from the sign of
`RHK_Yscale`, positive for an upward scan and negative for a downward one. The
fast axis stays unsigned: `RHK_ScanType` names the Forward and the Backward pass,
but it does not say which way either ran, and `RHK_Xscale` carries the same sign
on both pages, so it describes the coordinate mapping of the stored array rather
than the travel of the tip. An RHK document defining `RHK_ScanType`, or two scans
of one area with opposite `RHK_ScanType` and a feature that fixes the direction,
would settle it.
## Evidence

The centre reading is graded **vendor manual and empirical test on vendor data**.
The RHK R9 User Manual states that "Move to Center: moves the Scan Area to the
center of the Scan Range by setting the XY Offsets to 0" (p. 195), so the XY
offset is the position of the scan-area centre within the scanner range and may
take any value in it. The page header stores the same quantity: in
`Figure_6c.SM4` the embedded R9 parameter block gives `X offset ::1.5773e-007 m`
against a header `RHK_Xoffset` of `1.6301e-07 m`, within 5 to 9 nm, where a
first-pixel reading would put them about 50 nm apart.

Scan pairs confirm it. The
[method](../scan-region-conventions.md#how-the-empirical-test-works) and the
[data](../scan-region-conventions.md#data-used) are described centrally.

| Pair, identical offsets | Correlation peak / next | Measured | Centre predicts | First pixel predicts |
|---|---|---|---|---|
| `VT231211_A1_0064` (10 nm) in `_0065` (30 nm) | 0.71 / 0.54 | (0.53, 0.41) nm | (0.00, 0.00) nm | (9.96, 9.96) nm |
| `VT231205_A1_0064` (up) and `_0063` (down), 20 nm | 0.44 / 0.38 | (0.94, 4.26) nm | (0.00, 0.00) nm | (0.00, 19.96) nm |

The 10 nm scan sits in the middle of the 30 nm one. The up and the down scan
overlap, which the first-pixel reading forbids: with `RHK_Yscale` of opposite
sign it would put one scan in the 20 nm below `RHK_Yoffset` and the other in the
20 nm above it, two strips that never meet. Three further pairs with different
offsets agree as well.

Gwyddion's `rhk-sm4.c` reads the offsets and never applies them, and spym drops
them for image pages; RHK's own "SM4 Data File Format" document is not publicly
available.
