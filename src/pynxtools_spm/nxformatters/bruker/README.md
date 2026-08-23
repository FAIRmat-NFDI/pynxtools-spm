# Bruker SPMLab conventions (`.FLT`)

How the lateral (Y) grid, the Z values and the feedback gains are read for the
SPMLab `.FLT` format. Every rule below is traced to a source; where no primary
specification exists that is stated explicitly.

## `.FLT` (SPMLab)

The format comes from the TopoMetrix → ThermoMicroscopes → Veeco → Bruker lineage and is
identified by the header `Program=SPMLab`. **No public specification exists.** The only reference
implementation is Gwyddion's [`spmlabf.c`][spmlabf]; everything below is its
reverse-engineered behaviour, not documented fact.

The writing instrument is the Veeco → Bruker **Innova** family running SPMLab
(SPMLab-V): AtomicJ files this header dialect under [`readers/innova`][atomicj],
`XLinOn`/`YLinOn` are the Innova's switchable closed-loop scan linearization, and
the gain defaults of the [Innova operating notes][innova] match those in the
reference file. Its own manual (*Veeco DiInnova User Manual-B*, 004-1005-000) is
not publicly retrievable, so it could not be consulted.

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

## Feedback gains — `Gain*` and `XLinGain*`/`YLinGain*`

```ini
GainP=0.800000 (1000.000000)      XLinGainI=12.000000 (1200.000000)
```

- `GainP`/`GainI`/`GainD` are the P, I, D terms of the **Z (topography) feedback
  loop**, in SPMLab's dimensionless GUI units.
- `XLinGain*`/`YLinGain*` are the P, I, D terms of the **X and Y closed-loop scan
  linearization servos** (the "Lin" loops), active here because `XLinOn=TRUE` and
  `YLinOn=TRUE`. They are separate controllers from the Z loop, which is why they
  carry their own PID triplet.

The **first number is the value the operator set**. The Innova operating notes
give SPMLab's TappingMode default as *"P.I.D. gain of 1.0, 0.3, 0.0"* and its
contact mode default as *"4~8, 1~3, 0"*, unstable above I≈5 ([Innova Operation
Notes][innova], p. 1–2); the reference file's `0.8 / 0.3 / 0.0` sits on exactly
that scale, so the leading float is the feedback panel gain and not a raw
register value.

### The number in parentheses — undocumented, but constrained

**No specification, manual or reader defines it.** What can be established:

1. It is **constant per loop, not per channel**: `1000.0` for all three Z gains and
   `1200.0` for all six XY linearization gains, identical across `SIG_TOPO` and
   `SIG_USER2` and across `FRW` and `BKW` of one session. So it is a property of
   the controller, not of the data or of the gain value.
2. **No reader interprets it.** Gwyddion's [`spmlabf.c`][spmlabf] lists
   `GainP`…`YLinGainD` in `add_metadata()` and stores each as an uninterpreted
   string; [SpectraFox][spectrafox] and [AtomicJ][atomicj] ignore the gain keys
   entirely.
3. Neither the product nor the ratio of the pair is consistent across the file
   (`0.8·1000 = 800` against `12·1200 = 14400`), so it is not a scale factor
   applied to the displayed value in any way this sample supports.

The likeliest reading — **unverified** — is a per loop full scale or
normalization constant: the maximum settable gain, or the scale mapping the
displayed gain onto controller units. Two constants for two servo boards (Z
against XY linearization) fits that. One file recorded with deliberately changed
Z gains settles it: if the constant stays `1000.0` it is a range, if it tracks the
gain it is derived.

Because `K_p`, `K_i` and `K_d` are `NX_NUMBER` in `NXpid_controller`, the parser
keeps only the leading float (`GAIN_WITH_CONSTANT` in `parsers/bruker_flt.py`) and
drops the constant.

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
[innova]: https://www.shyue.idv.tw/SPM%20notes.pdf
[spectrafox]: https://github.com/spectrafox/spectrafox/blob/master/sourcecode/SpectroscopyManager/SpectroscopyManager/ImportMethods/Bruker/cFileImportBrukerFLT.vb
[atomicj]: https://github.com/pawelHerm/AtomicJ/tree/master/AtomicJ/src/atomicJ/readers/innova

- [NanoScope Software 8.10 User Guide][ns810] — Frame Up/Down (p. 23)
- [Bruker Dimension Icon online help — Raster Scan Parameters][raster]
- [Gwyddion `modules/file/spmlabf.c`][spmlabf] — `.FLT` reference implementation
- [Gwyddion `modules/file/nanoscope.c`][nanoscope] — `.spm` reference implementation,
  cited only as corroborating evidence for the stored row order
- [Gwyddion `GwyDataField` reference][gwydf] — `gwy_data_field_invert` semantics
- [Veeco Innova Operation Notes][innova] — SPMLab feedback gain defaults (p. 1–2)
- [SpectraFox `cFileImportBrukerFLT.vb`][spectrafox] and [AtomicJ `readers/innova`][atomicj]
  — the other two `.FLT` readers; both ignore the gain keys
