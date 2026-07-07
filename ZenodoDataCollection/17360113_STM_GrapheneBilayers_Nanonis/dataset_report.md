# Dataset Report: Zenodo Record 17360113

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | STM image of quasiparticle interferences on twisted graphene bilayers |
| **DOI**    | [10.5281/zenodo.17360113](https://doi.org/10.5281/zenodo.17360113) |
| **Url**    | [https://zenodo.org/records/17360113](https://zenodo.org/records/17360113) |
| **Date**   | 2025-10-15 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Renard, Vincent |
| **Tags**   | STM, scanning tunneling microscopy, quasiparticle interference, twisted graphene bilayer, topography, dI/dV |
| **Description** | The dataset contains the STM measurements of quasiparticle interferences near a defect. <br><br> Each image contains three channels : topography, dI/dV and current (bothforward and backward).  <br><br> Each image contains metadata indicating the measurement conditions |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: STM (Scanning Tunneling Microscopy) — topography + dI/dV + current channels
- **Instrument**: Nanonis (`.sxm` format)

## Dataset Contents

15 objects: Nanonis `.sxm` STM images extracted from `STM_images.zip`. Each image contains three channels (topography, dI/dV, current — forward and backward) with acquisition metadata.

## File Format

- **Format**: Nanonis `.sxm`
- **Parsability**: Supported by `NanonisSxmSTM`. Multi-channel files with topography and dI/dV.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17360113/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 15 files

**S3 key pattern**: `zenodo/17360113/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `SiCCAO#C012_300mV.sxm` | STM | 1 | `zenodo/17360113/STM_images/SiCCAO#C012_300mV.sxm/` | — | — |
| `SiCCAO#C013_500mV.sxm` | STM | 2 | `zenodo/17360113/STM_images/SiCCAO#C013_500mV.sxm/` | — | — |
| `SiCCAO#C014_350mV.sxm` | STM | 3 | `zenodo/17360113/STM_images/SiCCAO#C014_350mV.sxm/` | — | — |
| `SiCCAO#C015_425mV.sxm` | STM | 4 | `zenodo/17360113/STM_images/SiCCAO#C015_425mV.sxm/` | — | — |
| `SiCCAO#C016_325.sxm` | STM | 5 | `zenodo/17360113/STM_images/SiCCAO#C016_325.sxm/` | — | — |
| `SiCCAO#C017_400mV.sxm` | STM | 6 | `zenodo/17360113/STM_images/SiCCAO#C017_400mV.sxm/` | — | — |
| `SiCCAO#C018_275mV.sxm` | STM | 7 | `zenodo/17360113/STM_images/SiCCAO#C018_275mV.sxm/` | — | — |
| `SiCCAO#C019_375.sxm` | STM | 8 | `zenodo/17360113/STM_images/SiCCAO#C019_375.sxm/` | — | — |
| `SiCCAO#C020_200mV.sxm` | STM | 9 | `zenodo/17360113/STM_images/SiCCAO#C020_200mV.sxm/` | — | — |
| `SiCCAO#C021_450mV.sxm` | STM | 10 | `zenodo/17360113/STM_images/SiCCAO#C021_450mV.sxm/` | — | — |
| `SiCCAO#C022_362mV.sxm` | STM | 11 | `zenodo/17360113/STM_images/SiCCAO#C022_362mV.sxm/` | — | — |
| `SiCCAO#C023_388mV.sxm` | STM | 12 | `zenodo/17360113/STM_images/SiCCAO#C023_388mV.sxm/` | — | — |
| `SiCCAO#C024_300mV.sxm` | STM | 13 | `zenodo/17360113/STM_images/SiCCAO#C024_300mV.sxm/` | — | — |
| `SiCCAO#C025_475mV.sxm` | STM | 14 | `zenodo/17360113/STM_images/SiCCAO#C025_475mV.sxm/` | — | — |
| `SiCCAO#C031_150mV.sxm` | STM | 15 | `zenodo/17360113/STM_images/SiCCAO#C031_150mV.sxm/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
