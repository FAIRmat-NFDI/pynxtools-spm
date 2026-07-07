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

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — multiple modes including dimensional, electrical, Kelvin probe
- **Instrument**: Multiple instruments (Bruker .spm confirmed for some files)

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

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `NW_GaAs_non-passive_C3275_00000.0_00009.spm` | AFM | 1 | `zenodo/14271622/NW_GaAs_non-passive_C3275_00000.0_00009.spm/` | — | — |
| `NW_GaAs_non-passive_C3275_camLight-DOWN_00007.spm` | AFM | 2 | `zenodo/14271622/NW_GaAs_non-passive_C3275_camLight-DOWN_00007.spm/` | — | — |
| `NW_GaAs_non-passive_C3275_camLight-Up_00008.spm` | AFM | 3 | `zenodo/14271622/NW_GaAs_non-passive_C3275_camLight-Up_00008.spm/` | — | — |
| `NW_GaAs_non-passive_C3275_dark UP_00006.spm` | AFM | 4 | `zenodo/14271622/NW_GaAs_non-passive_C3275_dark UP_00006.spm/` | — | — |
| `NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm` | AFM | 5 | `zenodo/14271622/NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm/` | — | — |
| `*.zip` | AFM | 1 | `zenodo/14271622/04-14-23_Vendredi.zip/` | — | — |
| `*.zip` | AFM | 1 | `zenodo/14271622/04_13_23_Jeudi.zip/` | — | — |
| `*.svg` | AFM | 1 | `zenodo/14271622/Fig. 4/` | — | — |
| `*.tiff` | AFM | 8 | `zenodo/14271622/Fig. 4/` | — | — |
| `*.tiff` | AFM | 12 | `zenodo/14271622/Fig. 5/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
