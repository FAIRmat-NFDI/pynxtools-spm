# Dataset Report: Zenodo Record 17202182

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Revealing band-hybrid Cooper pairs on the surface of a superconductor with spin-orbit coupling |
| **DOI**    | [10.5281/zenodo.17202182](https://doi.org/10.5281/zenodo.17202182) |
| **Url**    | [https://zenodo.org/records/17202182](https://zenodo.org/records/17202182) |
| **Date**   | 2025-09-25 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Pascual, Jose Ignacio |
| **Tags**   | STM, STS, scanning tunneling microscopy, spectroscopy, superconductor, spin-orbit coupling, Cooper pairs, quasiparticle interference |
| **Description** | OPEN DATASET of the publication "Revealing band-hybrid Cooper pairs on the surface of a superconductor with spin-orbit coupling" including  Scanning Tunneling Microscopy and Spectroscopy results. |
| **Experiment information related files** | `Information.txt`, `QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf`, `QPI_visualization_of_Interband_Pairing-SM.pdf` |

## Technique

- **Primary SPM technique**: STM/STS (Scanning Tunneling Microscopy/Spectroscopy) — quasiparticle interference maps
- **Instrument**: Nanonis (`.sxm` format inferred from folder structure)

## Dataset Contents

20 objects for a QPI (Quasiparticle Interference) study on a superconductor with spin-orbit coupling. Data organised in Fig2-QPI, Fig3-BQPI, Fig4-FFT folders plus PDF manuscript and supplemental. Readable with Gwyddion.

## File Format

- **Format**: Nanonis `.sxm` (STM/STS QPI maps), `.pdf`
- **Parsability**: Nanonis `.sxm` files parsable by `NanonisSxmSTM`. QPI maps are conductance images — use STS/STM technique.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17202182/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 20 files

**S3 key pattern**: `zenodo/17202182/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `T190613_004.sxm` | STS | 1 | `zenodo/17202182/Fig2-QPI/T190613_004.sxm/` | — | — |
| `T180729_002.sxm` | STS | 2 | `zenodo/17202182/Fig3-BQPI/T180729_002.sxm/` | — | — |
| `T180817_001.sxm` | STS | 3 | `zenodo/17202182/Fig3-BQPI/T180817_001.sxm/` | — | — |
| `T190202_007.sxm` | STS | 4 | `zenodo/17202182/Fig3-BQPI/T190202_007.sxm/` | — | — |
| `T190322_005.sxm` | STS | 5 | `zenodo/17202182/Fig4-FFT/T190322_005.sxm/` | — | — |
| `*.stp` | STS | 9 | `zenodo/17202182/Fig2-QPI/` | — | — |
| `*.stp` | STS | 3 | `zenodo/17202182/Fig4-FFT/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `Information.txt` | STS | 1 | `zenodo/17202182/Information.txt/` |
| `QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf` | STS | 2 | `zenodo/17202182/QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf/` |
| `QPI_visualization_of_Interband_Pairing-SM.pdf` | STS | 3 | `zenodo/17202182/QPI_visualization_of_Interband_Pairing-SM.pdf/` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
