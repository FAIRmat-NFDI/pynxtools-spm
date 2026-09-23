# Scan region in Bruker NanoScope `.spm`

How a NanoScope `.spm` file states the scanned area, and how the reader turns it
into NeXus under [the scan region convention](../scan-region-conventions.md).

## Raw keys

| Raw key | Meaning | How the reader uses it |
|---|---|---|
| `\X Offset`, `\Y Offset` | Centre position of the scan | `scan_offset_value_x`, `_y` |
| `\Scan Size` | Edge length of the frame | `scan_range_x`; y is divided by `\Aspect Ratio` |
| `\Aspect Ratio` | Ratio of x to y range | Malformed values fall back to `1:1` with a warning |
| `\Samps/line`, `\Lines` | Pixels per line, number of lines | `scan_points_x`, `_y` |
| `\Frame direction` | `Up` or `Down`, the slow direction | Sign of the slow axis |
| `\Rotate Ang.` | Rotation of the frame | `scan_angle_x`, not applied |

Trace and Retrace layers are both stored, so the fast axis stays unsigned.
`\X Position` and the coarse stage `\Stage X` are **not** used for the scan
region: the stage is a different frame of reference.

**Open question.** No Bruker document states the order in which the rows are
stored, so the image orientation rests on how Gwyddion reads the format. A
document stating the row order, or an openly licensed Up and Down scan of one
area, would settle it.
## Evidence

The centre reading is graded **vendor manual**: the NanoScope 6.13 User Guide
defines the parameters on the Scan Controls panel as "X offset, Y offset:
Controls the center position of the scan in the X and Y directions,
respectively" (p. 60), and adds that "each volt of X or Y offset reduces the
maximum scan size by 2V" (p. 85), which only a centred frame does. See
[how the evidence is graded](../scan-region-conventions.md#grades).
