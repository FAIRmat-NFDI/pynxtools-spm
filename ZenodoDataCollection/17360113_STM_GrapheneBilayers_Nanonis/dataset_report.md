# Dataset Report: Zenodo Record 17360113

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | STM image of quasiparticle interferences on twisted graphene bilayers |
| **DOI**    | [10.5281/zenodo.17360113](https://doi.org/10.5281/zenodo.17360113) |
| **Date**   | 2025-10-15 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Renard, Vincent |
| **Tags**   | STM, scanning tunneling microscopy, quasiparticle interference, twisted graphene bilayer, topography, dI/dV |

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

**S3 key pattern**: `zenodo/17360113/STM_images/<filename>/<filename>`

Source zip: `STM_images.zip` → `STM_images/` ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/17360113/STM_images/)) — 15 Nanonis `.sxm` files (topography + dI/dV + current channels, fwd/bwd)

| file | experiment | S3 key |
|------|------------|--------|
| `SiCCAO#C012_300mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C012_300mV.sxm/SiCCAO#C012_300mV.sxm` |
| `SiCCAO#C013_500mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C013_500mV.sxm/SiCCAO#C013_500mV.sxm` |
| `SiCCAO#C014_350mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C014_350mV.sxm/SiCCAO#C014_350mV.sxm` |
| `SiCCAO#C015_425mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C015_425mV.sxm/SiCCAO#C015_425mV.sxm` |
| `SiCCAO#C016_325.sxm`   | STM | `zenodo/17360113/STM_images/SiCCAO#C016_325.sxm/SiCCAO#C016_325.sxm` |
| `SiCCAO#C017_400mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C017_400mV.sxm/SiCCAO#C017_400mV.sxm` |
| `SiCCAO#C018_275mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C018_275mV.sxm/SiCCAO#C018_275mV.sxm` |
| `SiCCAO#C019_375.sxm`   | STM | `zenodo/17360113/STM_images/SiCCAO#C019_375.sxm/SiCCAO#C019_375.sxm` |
| `SiCCAO#C020_200mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C020_200mV.sxm/SiCCAO#C020_200mV.sxm` |
| `SiCCAO#C021_450mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C021_450mV.sxm/SiCCAO#C021_450mV.sxm` |
| `SiCCAO#C022_362mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C022_362mV.sxm/SiCCAO#C022_362mV.sxm` |
| `SiCCAO#C023_388mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C023_388mV.sxm/SiCCAO#C023_388mV.sxm` |
| `SiCCAO#C024_300mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C024_300mV.sxm/SiCCAO#C024_300mV.sxm` |
| `SiCCAO#C025_475mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C025_475mV.sxm/SiCCAO#C025_475mV.sxm` |
| `SiCCAO#C031_150mV.sxm` | STM | `zenodo/17360113/STM_images/SiCCAO#C031_150mV.sxm/SiCCAO#C031_150mV.sxm` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
