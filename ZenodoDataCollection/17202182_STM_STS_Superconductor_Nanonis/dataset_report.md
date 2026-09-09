# Dataset Report: Zenodo Record 17202182

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Revealing band-hybrid Cooper pairs on the surface of a superconductor with spin-orbit coupling |
| **DOI**    | [10.5281/zenodo.17202182](https://doi.org/10.5281/zenodo.17202182) |
| **Date**   | 2025-09-25 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Pascual, Jose Ignacio |
| **Tags**   | STM, STS, scanning tunneling microscopy, spectroscopy, superconductor, spin-orbit coupling, Cooper pairs, quasiparticle interference |

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

**S3 key pattern**: `zenodo/17202182/<folder>/<filename>/<filename>`

Source zip: `BQPI.zip` → 3 figure folders ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/17202182/))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `Fig2-QPI/<file>.sxm`  | STM | 10 | `zenodo/17202182/Fig2-QPI/` |
| `Fig3-BQPI/<file>.sxm` | STS |  3 | `zenodo/17202182/Fig3-BQPI/` |
| `Fig4-FFT/<file>.sxm`  | STS |  4 | `zenodo/17202182/Fig4-FFT/` |
| `Information.txt`       | —   |  1 | `zenodo/17202182/Information.txt/Information.txt` |
| `QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf` | — | 1 | `zenodo/17202182/QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf/QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf` |
| `QPI_visualization_of_Interband_Pairing-SM.pdf`         | — | 1 | `zenodo/17202182/QPI_visualization_of_Interband_Pairing-SM.pdf/QPI_visualization_of_Interband_Pairing-SM.pdf` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
