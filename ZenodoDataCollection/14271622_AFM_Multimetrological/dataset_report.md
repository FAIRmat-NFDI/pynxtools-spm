# Dataset Report: Zenodo Record 14271622

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Raw data for "AFM as a Multimetrological Platform" Manuscript |
| **DOI**    | [10.5281/zenodo.14271622](https://doi.org/10.5281/zenodo.14271622) |
| **Url**    | [https://zenodo.org/records/14271622](https://zenodo.org/records/14271622) |
| **Date**   | 2024-12-04 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Aslan, Husnu; Kaja, Khaled; Piquemal, François et al. |
| **Tags**   | AFM, multimetrological, dimensional, electrical, Kelvin probe, SPM |
| **Description** | Attached are the raw scanning probe microscopy data, collected with different instruments. Each instrument has its own data format and needs to be processed to represent the data properly. The processing often includes, false-colour scale assignment, tilt and rotational corrections, and levelling. After processing, the analysis helps extracting the necessary information from the data such as dimensional and electrical properties, which when calibrated can be presented as images, maps or spectroscopy graphs in respective units. |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — PeakForce QNM + KPFM, multi-instrument "multimetrological" study
- **Instrument**: Multiple instruments (Bruker `.spm` for the AFM subset)

## Sample

- **Material / chemical formula**: **GaAs** nanowires (non-passivated, sample C3275) → `GaAs`.
- **Conditions**: imaged by PeakForce QNM AFM under different illumination (dark, camera light
  up/down), part of a multi-instrument "multimetrological" SPM platform study.
- **Note**: the Bruker files also contain KPFM/LockIn2 channels (`Potential`, `Amplitude2`,
  `Phase2`) that pySPM 0.6.3 cannot scale; those are skipped (see Conversion).

## Dataset Contents

Raw SPM data collected with different instruments for a multimetrological AFM study. 28 objects: large zip (`Fig.2_3_6_7_8_9.zip`, 1.6 GB) extracted into folders, plus `Fig. 4.zip` and `Fig. 5.zip` extracted. Contains Bruker `.spm` files confirmed (e.g., `NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm`).

## File Format

- **Format**: Bruker `.spm` (confirmed), possibly other formats from different instruments
- **Parsability**: Bruker `.spm` files are parsable by `BrukerSpmAFM`. Other instrument files require format investigation.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14271622/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 28 files

**S3 key pattern**: `zenodo/14271622/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `NW_GaAs_non-passive_C3275_00000.0_00009.spm` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 1 | `zenodo/14271622/NW_GaAs_non-passive_C3275_00000.0_00009.spm/` | True | True |
| `NW_GaAs_non-passive_C3275_camLight-DOWN_00007.spm` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 2 | `zenodo/14271622/NW_GaAs_non-passive_C3275_camLight-DOWN_00007.spm/` | True | True |
| `NW_GaAs_non-passive_C3275_camLight-Up_00008.spm` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 3 | `zenodo/14271622/NW_GaAs_non-passive_C3275_camLight-Up_00008.spm/` | True | True |
| `NW_GaAs_non-passive_C3275_dark UP_00006.spm` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 4 | `zenodo/14271622/NW_GaAs_non-passive_C3275_dark UP_00006.spm/` | True | True |
| `NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 5 | `zenodo/14271622/NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm/` | True | True |
| `*.zip` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 1 | `zenodo/14271622/04-14-23_Vendredi.zip/` | — | — |
| `*.zip` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 1 | `zenodo/14271622/04_13_23_Jeudi.zip/` | — | — |
| `*.svg` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 1 | `zenodo/14271622/Fig. 4/` | — | — |
| `*.tiff` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 8 | `zenodo/14271622/Fig. 4/` | — | — |
| `*.tiff` | AFM | GaAs nanowires (non-passivated, C3275) | GaAs | 12 | `zenodo/14271622/Fig. 5/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08 with `pynxtools-spm` 0.2.5 / `pySPM` 0.6.3. License **`cc-by-4.0`** passes
the open-license gate. **All 5 native Bruker `.spm` converted, validated, and uploaded**
(`PS = True`, `Uploaded = True`). These PeakForce QNM files carry KPFM/LockIn2 channels
(`Potential`, `Amplitude2`, `Phase2`) stored under `@3:Image Data` that pySPM 0.6.3 cannot
scale — previously this aborted the whole parse. A fix in the pynxtools-spm Bruker parser
(override `pySPMBruker._get_layer_val` to raise `KeyError` for missing keys + per-channel guard)
now recovers the 5 usable `@2` channels (Topography, Peak Force Error, DMT Modulus, Adhesion,
Deformation) and skips the 3 KPFM channels. 10 NXdata groups, default `z_forward`; post-audit:
0 long units, 0 shape mismatches, 0 bad defaults. `citeID.description` carries the full Zenodo
description.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 5/5 `.spm` converted (`PS = True`)
- [x] Reference .nxs files generated and uploaded for all 5 files
