# Dataset Report: Zenodo Record 18060234

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | PiF-IR data of PMIS-C8 monolayer films on nanostructured and planar Au substrates, complementary AFM, FTIR/ATR and BAM data |
| **DOI**    | [10.5281/zenodo.18060234](https://doi.org/10.5281/zenodo.18060234) |
| **Date**   | 2025-12-26 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| James, Ayona; Ali, Maryam; Ye, Zekai; Schneider, Robin et al. |
| **Tags**   | AFM, PiF-IR, photo-induced force microscopy, infrared spectroscopy, monolayer, gold nanostructure, PMIS-C8 |

## Technique

- **Primary SPM technique**: PiF-IR (Photo-induced Force Microscopy Infrared) + AFM
- **Instrument**: Unknown PiF-IR instrument (`.FLT`, `.SIG` files) + Bruker AFM for complementary images

## Dataset Contents

1141 objects: PiF-IR hyperspectral and single-frequency scans, AFM images, BAM (Brewster Angle Microscopy), ATR-FTIR spectra, and calculated IR spectra for PMIS-C8 monolayer films on Au substrates.

## File Format

- **Format**: `.FLT` and `.SIG_HEIGHT_SENSOR_BKW.FLT` (PiF-IR proprietary), AFM images in unknown format
- **Parsability**: Not supported. PiF-IR `.FLT`/`.SIG` files have no parser. AFM component may be Bruker-compatible but format confirmation needed.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/18060234/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 1141 files

**S3 key pattern**: `zenodo/18060234/<folder>/<filename>/<filename>`

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `AFM/<file>` | AFM | 66 | `zenodo/18060234/AFM/` |
| `ATR-FTIR/<file>` | ATR-FTIR | 7 | `zenodo/18060234/ATR-FTIR/` |
| `PiF-IR_PMISC8_evaporated-Au_hypir/<file>` | PiF-IR | 54 | `zenodo/18060234/PiF-IR_PMISC8_evaporated-Au_hypir/` |
| `250618_PMIS-C8_0001_spectra/<file>` | PiF-IR | 56 | `zenodo/18060234/250618_PMIS-C8_0001_spectra/` |
| `250618_PMIS-C8_0002-3_scans/<file>` | PiF-IR | 90 | `zenodo/18060234/250618_PMIS-C8_0002-3_scans/` |
| `250619_PMIS-C8_0001_spectra/<file>` | PiF-IR | 55 | `zenodo/18060234/250619_PMIS-C8_0001_spectra/` |
| `250619_PMIS-C8_0002-3_scans/<file>` | PiF-IR | 90 | `zenodo/18060234/250619_PMIS-C8_0002-3_scans/` |
| `251120_PMIS-C8_0001_spectra/<file>` | PiF-IR | 53 | `zenodo/18060234/251120_PMIS-C8_0001_spectra/` |
| `251120_PMIS-C8_0002_scan/<file>`    | PiF-IR | 32 | `zenodo/18060234/251120_PMIS-C8_0002_scan/` |
| `251120_PMIS-C8_0003_hypir/<file>`   | PiF-IR | 54 | `zenodo/18060234/251120_PMIS-C8_0003_hypir/` |
| `251121_PMIS-C8_0001_spectra/<file>` | PiF-IR | 68 | `zenodo/18060234/251121_PMIS-C8_0001_spectra/` |
| `251121_PMIS-C8_0002-4_scans/<file>` | PiF-IR | 141 | `zenodo/18060234/251121_PMIS-C8_0002-4_scans/` |
| `IR_Analysis_Report-20251022/<file>` | — | 353 | `zenodo/18060234/IR_Analysis_Report-20251022/` |
| `20250527_Deposition_LB_Monolayer_PMIS2C8_…/<file>` | BAM | 22 | `zenodo/18060234/20250527_Deposition_LB_Monolayer_PMIS2C8_…/` |

## Category

**Unknown/Unsupported Format**

## Status

- [x] Files uploaded to S3
- [ ] Parser not implemented (PiF-IR .FLT format)
- [ ] Reference .nxs file not generated
