# Scan region in Nanonis `.sxm`

How a Nanonis `.sxm` file states the scanned area, and how the reader turns it
into NeXus under [the scan region convention](../scan-region-conventions.md).

## Raw keys

| Raw key | Meaning | How the reader uses it |
|---|---|---|
| `:SCAN_OFFSET:` | Centre of the scan frame, x and y | `scan_offset_value_x`, `_y` |
| `:SCAN_RANGE:` | Width and height | `scan_range_x`, `_y` |
| `:SCAN_PIXELS:` | Pixels per line, number of lines | `scan_points_x`, `_y` |
| `:SCAN_DIR:` | `up` or `down`, the slow direction | Sign of the slow axis; orients the image |
| `:SCAN_ANGLE:` | Rotation of the frame | `scan_angle_x`, `_y`, not applied |

Both passes of the fast axis are stored (`DATA_INFO` `Direction` is `both`), so
the fast axis stays unsigned. The header repeats the same geometry in
`:Scan>Scanfield:` as `centre_x;centre_y;width;height;angle`; the reader does not
read that key.

**Open question.** That `SCAN_OFFSET` is the centre follows from what Nanonis
writes into the file and from how other readers treat it, not from a statement by
SPECS. The Nanonis TCP Protocol Document, which defines the scan frame directly,
needs a MySPECS account and has not been checked.
## Evidence

The centre reading is graded **vendor file content and third-party readers**: it
follows from the `:Scan>Scanfield:` key that Nanonis itself writes and from
Gwyddion's `nanonis.c`, which places the frame origin at
`SCAN_OFFSET - 0.5 * SCAN_RANGE`. See
[how the evidence is graded](../scan-region-conventions.md#grades).
