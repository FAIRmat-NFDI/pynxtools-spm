# Dataset Report: Zenodo Record 19086147

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Supplementary data to publication https://doi.org/10.1002/anie.202424715 |
| **DOI**    | [10.5281/zenodo.19086147](https://doi.org/10.5281/zenodo.19086147) |
| **Date**   | 2026-03-18 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Moresco, Francesca |
| **Tags**   | STM, STS, scanning tunneling microscopy, NHC, thiophene, Au(111), chiral adsorption, molecular rotation |

## Technique

- **Primary SPM technique**: STM/STS (Scanning Tunneling Microscopy/Spectroscopy)
- **Instrument**: Nanonis (`.dat` format — Nanonis `.dat` STM images and `.VERT` STS spectra)

## Dataset Contents

57 files: Nanonis `.dat` STM image files and `.VERT` STS spectroscopy files from STM experiments on NHC/thiophene molecules on Au(111). Supplementary data for Angew. Chem. publication on chiral adsorption and unidirectional rotation.

## File Format

- **Format**: Nanonis `.dat` (STM images), `.VERT` (STS spectra), `.jpeg` (reference images)
- **Parsability**: Nanonis `.dat` files parsable by `NanonisDatSTS` (for spectroscopy). `.VERT` files are Nanonis vertical spectroscopy — may need format investigation.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/19086147/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 57 files

**S3 key pattern**: `zenodo/19086147/<filename>/<filename>`

Files uploaded flat ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/19086147/))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `A*.dat` | STM/STS | 35 | `zenodo/19086147/` |
| `A*.VERT` | STS | 20 | `zenodo/19086147/` |
| `A*.VERT.jpeg` | — | 2 | `zenodo/19086147/` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
