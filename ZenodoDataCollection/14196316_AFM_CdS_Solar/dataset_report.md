# Dataset Report: Zenodo Record 14196316

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for "An Alternative Chlorine-Assisted Optimization of CdS/Sb₂Se₃ Solar Cells" |
| **DOI**    | [10.5281/zenodo.14196316](https://doi.org/10.5281/zenodo.14196316) |
| **Date**   | 2024-11-21 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Kuliček, Jaroslav; Bouzek, Karel; Paušová, Šárka |
| **Tags**   | Kelvin probe, CdS/Sb2Se3, solar cells, AFM, surface photovoltage |

## Technique

- **Primary SPM technique**: AFM + Scanning Kelvin Probe + Surface Photovoltage
- **Instrument**: Unknown AFM vendor (`.Dat` files — Scanning Kelvin Probe data format)

## Dataset Contents

40 files (`.Dat`, `.txt`, `.jpg`) related to CdS/Sb₂Se₃ solar cell characterisation. Dat files contain Scanning Kelvin Probe and AFM measurements at different Cl⁻ concentrations.

## File Format

- **Format**: `.Dat` (Scanning Kelvin Probe format — unknown vendor), `.txt`, `.jpg`
- **Parsability**: Not directly supported. `.Dat` files may contain Kelvin probe or AFM data but the vendor format is unrecognised by the current parser.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14196316/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 40 files

**S3 key pattern**: `zenodo/14196316/<filename>/<filename>`

Files uploaded flat (no zip extraction): each file is its own top-level S3 key ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14196316/))

### Kelvin probe / AFM data — 35 .Dat files

| file | experiment | count | S3 key pattern |
|------|------------|-------|----------------|
| `VZ3_010_021_CVUT_D_NNNN_v1.Dat` | AFM | 35 | `zenodo/14196316/VZ3_010_021_CVUT_D_NNNN_v1.Dat/VZ3_010_021_CVUT_D_NNNN_v1.Dat` |

### Ancillary files — 5 files

| file | experiment | S3 key |
|------|------------|--------|
| `VZ3_010_021_CVUT_D_0001_v1.jpg` | AFM | `zenodo/14196316/VZ3_010_021_CVUT_D_0001_v1.jpg/VZ3_010_021_CVUT_D_0001_v1.jpg` |
| `VZ3_010_021_CVUT_D_0012_v1.jpg` | AFM | `zenodo/14196316/VZ3_010_021_CVUT_D_0012_v1.jpg/VZ3_010_021_CVUT_D_0012_v1.jpg` |
| `VZ3_010_021_CVUT_D_0013_v1.txt` | —   | `zenodo/14196316/VZ3_010_021_CVUT_D_0013_v1.txt/VZ3_010_021_CVUT_D_0013_v1.txt` |
| `VZ3_010_021_CVUT_D_0019_v1.txt` | —   | `zenodo/14196316/VZ3_010_021_CVUT_D_0019_v1.txt/VZ3_010_021_CVUT_D_0019_v1.txt` |
| `ReadMe_v2.txt`                   | —   | `zenodo/14196316/ReadMe_v2.txt/ReadMe_v2.txt` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Format investigation needed
- [ ] Reference .nxs file not generated
