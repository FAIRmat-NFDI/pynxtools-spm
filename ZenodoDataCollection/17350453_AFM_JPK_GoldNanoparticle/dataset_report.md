# Dataset Report: Zenodo Record 17350453

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data set for the manuscript "Local Networks of Electrical Conductance in Hybrid Gold Nanoparticle-Polymer Films" |
| **DOI**    | [10.5281/zenodo.17350453](https://doi.org/10.5281/zenodo.17350453) |
| **Url**    | [https://zenodo.org/records/17350453](https://zenodo.org/records/17350453) |
| **Date**   | 2025-10-14 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Das, Sukanya; Bennewitz, Roland; Kraus, Tobias et al. |
| **Tags**   | AFM, cAFM, conductive AFM, gold nanoparticle, polymer film, JPK NanoWizard |
| **Description** | Atomic Force Microscopy (AFM) original data files for the figures in the paper indicated. All data is in the format of the manufacturer of the instrument NanoWizard3 (Bruker). Data can be edited for example by the open source software Gwyddion. |
| **Experiment information related files** | `README.txt` |

## Technique

- **Primary SPM technique**: cAFM (Conductive Atomic Force Microscopy)
- **Instrument**: JPK NanoWizard 3 (Bruker) — `.jpk` format

## Dataset Contents

8 cAFM files (`.jpk`) of gold nanoparticle-polymer films at varying PVA concentrations and bias voltages, plus README. Data acquired with JPK NanoWizard 3.

## File Format

- **Format**: `.jpk` (JPK/Bruker NanoWizard proprietary binary)
- **Parsability**: Not supported. `.jpk` is a zip-based format but requires a dedicated parser (not yet implemented).

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17350453/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 8 files

**S3 key pattern**: `zenodo/17350453/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `*.jpk` | AFM | 1 | `zenodo/17350453/10 vol% 99 pva_first batch_cafm -1.2 v 2.jpk/` | — | — |
| `*.jpk` | AFM | 1 | `zenodo/17350453/cafm_-1.2V_setpoint0.26V small area.jpk/` | — | — |
| `*.jpk` | AFM | 1 | `zenodo/17350453/figure1_130_99pva_save-2024.03.18-18.06.31.372.jpk/` | — | — |
| `*.jpk` | AFM | 1 | `zenodo/17350453/no pva ref_low conc ink sideways5.jpk/` | — | — |
| `*.jpk` | AFM | 1 | `zenodo/17350453/save-2024.07.26-16.03.36.852.jpk/` | — | — |
| `*.jpk` | AFM | 1 | `zenodo/17350453/save-2024.07.26-17.06.47.452.jpk/` | — | — |
| `*.jpk` | AFM | 1 | `zenodo/17350453/scan area2_second_save-2024.03.05-16.36.20.646.jpk/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `README.txt` | AFM | 1 | `zenodo/17350453/README.txt/` |

## Category

**Unknown/Unsupported Format**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
