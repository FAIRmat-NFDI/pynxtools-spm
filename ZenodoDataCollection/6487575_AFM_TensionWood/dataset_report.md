# Dataset Report: Zenodo Record 6487575

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Mechanical characterisation of the developing cell wall layers of tension wood fibres by Atomic Force Microscopy |
| **DOI**    | [10.5281/zenodo.6487575](https://doi.org/10.5281/zenodo.6487575) |
| **Date**   | 2022-01-26 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Arnould, Olivier; Capron, Marie; Ramonda, Michel; Laurans, Françoise et al. |
| **Tags**   | AFM, atomic force microscopy, cell wall, tension wood, poplar, indentation modulus, G-layer |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — mechanical indentation mapping
- **Instrument**: Bruker AFM (NanoScope `.spm` format)

## Dataset Contents

195 objects: Bruker `.spm` AFM files of poplar tension wood cell walls at varying cambium distances (extracted from `AFM files.zip`, 309 MB), optical microscopy images (`Optical files.zip`, 320 MB), and two CSV files with extracted modulus and thickness data.

## File Format

- **Format**: Bruker `.spm` (AFM indentation maps), `.csv`, `.rtf`
- **Parsability**: Parsable by `BrukerSpmAFM`. Mechanical channels (indentation modulus) may require extended channel support.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/6487575/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 195 files (148 AFM + 44 Optical + 3 ancillary)

**S3 key pattern**: `zenodo/6487575/<folder>/<filename>/<filename>`

### AFM files — 148 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/6487575/AFM%20files/))

Source zip: `AFM files.zip` — Bruker NanoScope `.spm` mechanical indentation maps, grouped by sample type

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `embedding resin outside/<file>.spm` | AFM | 5  | `zenodo/6487575/AFM files/embedding resin outside/` |
| `kevlar fibre calibration/<file>.spm` | AFM | 3  | `zenodo/6487575/AFM files/kevlar fibre calibration/` |
| `normal wood/<file>.spm`             | AFM | 6  | `zenodo/6487575/AFM files/normal wood/` |
| `radial ligne #1/<file>.spm`         | AFM | 57 | `zenodo/6487575/AFM files/radial ligne #1/` |
| `radial ligne #2/<file>.spm`         | AFM | 52 | `zenodo/6487575/AFM files/radial ligne #2/` |
| `radial ligne #3/<file>.spm`         | AFM | 25 | `zenodo/6487575/AFM files/radial ligne #3/` |

### Optical files — 44 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/6487575/Optical%20files/))

Source zip: `Optical files.zip` — optical microscopy TIFF images

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `<file>.tif` | OM | 44 | `zenodo/6487575/Optical files/` |

### Ancillary files — 3 files

| file | experiment | S3 key |
|------|------------|--------|
| `modulus.csv`  | AFM | `zenodo/6487575/modulus.csv/modulus.csv` |
| `thickness.csv` | AFM | `zenodo/6487575/thickness.csv/thickness.csv` |
| `readme.rtf`   | —   | `zenodo/6487575/readme.rtf/readme.rtf` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
