# Dataset Report: Zenodo Record 17423992

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for Blue Laser for Production of Carbon Dots |
| **DOI**    | [10.5281/zenodo.17423992](https://doi.org/10.5281/zenodo.17423992) |
| **Date**   | 2024-10-03 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Cutroneo, Mariapompea |
| **Tags**   | AFM, carbon dots, Bruker Dimension ICON, ScanAsyst, thin film |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — ScanAsyst imaging mode
- **Instrument**: Bruker Dimension ICON (ScanAsyst mode in air)

## Dataset Contents

2 `.dat` files (Fig4 and Fig6) from Bruker Dimension ICON AFM measurements of carbon dot films on silicon. Data processed with NanoScope Analysis 1.80 (32-bit). Note: these are Bruker `.dat` export files, not Nanonis `.dat` files.

## File Format

- **Format**: `.dat` (Bruker NanoScope ASCII/binary export — not Nanonis format)
- **Parsability**: Not supported by current parsers. These `.dat` files are Bruker NanoScope exports, not Nanonis spectroscopy files. Format investigation needed.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17423992/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 2 files

**S3 key pattern**: `zenodo/17423992/<filename>/<filename>`

Files uploaded flat ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/17423992/))

| file | experiment | S3 key |
|------|------------|--------|
| `Fig4.dat` | AFM | `zenodo/17423992/Fig4.dat/Fig4.dat` |
| `Fig6.dat` | AFM | `zenodo/17423992/Fig6.dat/Fig6.dat` |

## Category

**Unknown/Unsupported Format**

## Status

- [x] Files uploaded to S3
- [ ] Format investigation needed
- [ ] Reference .nxs file not generated
