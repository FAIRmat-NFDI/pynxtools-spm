# Bruker SPMLab axis conventions (`.FLT`)

How the lateral (Y) grid and the Z values are reconstructed for the SPMLab `.FLT`
format. Every rule below is traced to a source; where no primary specification
exists that is stated explicitly.

## `.FLT` (SPMLab)

The format comes from the TopoMetrix → ThermoMicroscopes → Veeco → Bruker lineage and is
identified by the header `Program=SPMLab`. **No public specification exists.** The only reference
implementation is Gwyddion's [`spmlabf.c`][spmlabf]; everything below is its
reverse-engineered behaviour, not documented fact.

### Y axis — offset treated as the **origin** (corner)

```python
y = linspace(OffsetY, OffsetY + ScanRangeY, ResolutionY)
```

Units come from `XYUnit` when present, otherwise they are parsed from the trailing text of
`ScanRangeY`.

> ⚠️ Unverified. In the sample files here `OffsetX == ScanRangeX == 1.0000` with no unit
> suffix, which looks more like a placeholder than a physical offset. Confirm against a
> file captured with a deliberately offset scan before relying on this.

### Z axis — single float multiply

Raw data are **float32 little-endian** (not integers):

```python
Z_physical = raw_float32 * ZTransferCoefficient
```

Units come from `ZUnit` when present. When absent, Gwyddion parses the trailing text of
`ZTransferCoefficient` and multiplies by `V` — so a bare coefficient such as `0.7731`
yields **volts**, and converting to nm still requires the instrument's Z sensitivity.

## Row order — fixed, independent of frame direction

`Frame Up` restarts the scan at the bottom of the frame and `Frame Down` at the top
([NanoScope 8.10][ns810], p. 23), but this affects only **acquisition order in time**, not
the stored raster. NanoScope normalises row order on write.

Evidence: Gwyddion applies one **unconditional** vertical flip to every image in both
formats — [`nanoscope.c`][nanoscope] L939 and [`spmlabf.c`][spmlabf] L210, both outside any
conditional — and `nanoscope.c` never reads a frame- or scan-direction key at all. Were the
stored order to track frame direction, roughly half of all files would render upside down.

```c
gwy_data_field_invert(dfield, TRUE, FALSE, FALSE);
```

The first flag is `yflipped`: *"TRUE to reflect Y, i.e. rows within the XY plane. The image
will be flipped upside down."* ([GwyDataField reference][gwydf])

Consequence: raw row 0 corresponds to the **bottom** edge of the image as NanoScope
displays it. Read as-is, the array origin is bottom-left and the row index increases toward
+Y. Do not encode this as an implicit convention — write the axis coordinates out
explicitly so orientation lives in the data.

The fast axis is a different matter: `ScanDirection=FORWARD`/`BACKWARD` (the `FRW`/`BKW`
channels) does genuinely reverse the X sampling order, per channel.

> **Not established by a primary source:** no Bruker document found states the stored
> raster order. The appendix documents header fields only, and the [Raster Scan
> Parameters][raster] help page defines fast/slow axis but is silent on the starting
> corner. This rests on reference-implementation behaviour. A test grating would settle it
> directly.

## Sources

[ns810]: https://nanoqam.ca/wiki/lib/exe/fetch.php?media=nanoscope_software_8.10_user_guide-d_004-1025-000_.pdf
[raster]: https://www.nanophys.kth.se/nanolab/afm/icon/bruker-help/Content/SPM%20Training%20Guide/Raster%20Scan%20Parameters.htm
[nanoscope]: https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/nanoscope.c
[spmlabf]: https://sourceforge.net/p/gwyddion/code/HEAD/tree/trunk/gwyddion/modules/file/spmlabf.c
[gwydf]: http://gwyddion.net/documentation/head/libgwyprocess/GwyDataField.php

- [NanoScope Software 8.10 User Guide][ns810] — Frame Up/Down (p. 23)
- [Bruker Dimension Icon online help — Raster Scan Parameters][raster]
- [Gwyddion `modules/file/spmlabf.c`][spmlabf] — `.FLT` reference implementation
- [Gwyddion `modules/file/nanoscope.c`][nanoscope] — `.spm` reference implementation,
  cited only as corroborating evidence for the stored row order
- [Gwyddion `GwyDataField` reference][gwydf] — `gwy_data_field_invert` semantics
