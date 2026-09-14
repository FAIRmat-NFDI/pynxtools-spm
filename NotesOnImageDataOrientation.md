# Notes on Image Data Orientation
Bruker:
    AFM: 
        - Folder: default_config: Image Orientation is correct i.e., the origin starts at (0,0) at the top left corner of the image.
        - Folder: flt_default_config: Image Orientation is **not correct** i.e., the origin starts at (0,0) at the bottom left corner of the image.
        - Folder: flt_described_config: Image Orientation is **not correct** i.e., the origin starts at (0,0) at the bottom left corner of the image.

Nanonis:
    AFM:
        - Folder: version_gen_4_default_config: Image Orientation is correct
        - Folder: Version_gen_5_with_described_nxdata: Image Orientation is correct
    STM: 
        - Forder: version_gen_5e_with_described_nxdata: Image Orientation is correct#
        - Folder: Version_gen_5_with_default_config: Image Orientation is correct
        - Folder: Version_gen_5_with_described_nxdata: Image Orientation is correct
    STS:
        - All STS datasets are correct
Omicron:
    AFM:
        - Folder: default_config: Image Orientation **is not correct** i.e., the origin starts at (0,0) at the bottom left corner of the image.
---

## The convention

Row 0 of an NXdata signal is the **top** row of the image, and the slow axis
descends so that its first value labels that row.

The viewer draws row 0 at the top and ignores the axis values. That is not an
assumption: if it were axis-aware, a dataset with an ascending axis would have
its last row drawn on top and would display exactly what a descending one
displays, so the two groups above would look identical and no difference could
have been seen.

Writing a descending axis alongside top-row-first data keeps the two in
agreement, so the file renders the same way whether or not a viewer honours
axis direction.

## How to decide correct from wrong

Gwyddion reads every raw format in this test set (`nanonis` for .sxm,
`rhk-sm4` for .sm4, `nanoscope` for .spm, `spmlabf` for .FLT) and normalises
all of them to one orientation, so it works as a cross-vendor reference.

An image is correct exactly when its stored signal equals `np.flipud` of the
array `gwyddionpy.load(raw_file)` returns for the matching channel. Correlate
the two in all four flip orientations; the right one scores 1.0000 and the
others score near zero.

Each vendor puts its own flip in `rearrange_data_according_to_axes`, overridden
in its base formatter (`NanonisBase`, `OmicronBase`, `BrukerBase`). The
convention is shared; the flip that reaches it is vendor knowledge and stays
with the vendor.

## Status

- Omicron .sm4: **fixed**. `OmicronBase` now implements the orientation hook and
  the slow axis is reversed to match. The Z calibration was fixed at the same
  time: `spym` returns raw ADC counts and never applies `RHK_Zscale`, so every
  channel was stored as counts under a physical unit, and topography carried the
  wrong sign because that scale is negative.
- Bruker SPMLab .FLT: still open, same fix via `BrukerBase`.
- Note: the Omicron folder is `tests/data/omicron/stm/`, so it is STM, not AFM.
