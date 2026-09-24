# Dataset Report: Zenodo Record 17533355

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data underlying "Direct signatures of d-level hybridization and dimerization in magnetic adatom chains on a superconductor" |
| **DOI**    | [10.5281/zenodo.17533355](https://doi.org/10.5281/zenodo.17533355) |
| **Date**   | 2025-11-05 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Rütten, Lisa M.; Liebhaber, Eva; Reecht, Gaël; Rossnagel, Kai et al. |
| **Tags**   | STM, STS, scanning tunneling microscopy, superconductivity, magnetic adatom chains, d-level hybridization |

## Technique

- **Primary SPM technique**: STM/STS (Scanning Tunneling Microscopy/Spectroscopy)
- **Instrument**: Nanonis (`.sxm` / `.dat` format)

## Dataset Contents

638 objects extracted from `data.zip`, organised by figure (Fig1–Fig5, FigS1–FigS9). Contains Nanonis `.sxm` STM images and `.dat` STS spectroscopy files plus a PDF directory.

## File Format

- **Format**: Nanonis `.sxm` (STM), Nanonis `.dat` (STS)
- **Parsability**: STM `.sxm` files parsable by `NanonisSxmSTM`; STS `.dat` files parsable by `NanonisDatSTS`.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17533355/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 638 files

**S3 key pattern**: `zenodo/17533355/<figure>/<filename>/<filename>`

Source zip: `data.zip` → 13 figure folders + 1 PDF ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/17533355/))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `Fig1/<file>.sxm / .dat`  | STM/STS |  15 | `zenodo/17533355/Fig1/` |
| `Fig2/<file>.sxm / .dat`  | STM/STS | 169 | `zenodo/17533355/Fig2/` |
| `Fig3/<file>.sxm / .dat`  | STM/STS |   7 | `zenodo/17533355/Fig3/` |
| `Fig4/<file>.sxm / .dat`  | STM/STS | 123 | `zenodo/17533355/Fig4/` |
| `Fig5/<file>.sxm / .dat`  | STM/STS | 121 | `zenodo/17533355/Fig5/` |
| `FigS1/<file>.sxm / .dat` | STM/STS |   2 | `zenodo/17533355/FigS1/` |
| `FigS2/<file>.sxm / .dat` | STM/STS |   8 | `zenodo/17533355/FigS2/` |
| `FigS3/<file>.sxm / .dat` | STM/STS |   7 | `zenodo/17533355/FigS3/` |
| `FigS4/<file>.sxm / .dat` | STM/STS |  17 | `zenodo/17533355/FigS4/` |
| `FigS5/<file>.sxm / .dat` | STM/STS |  16 | `zenodo/17533355/FigS5/` |
| `FigS6/<file>.sxm / .dat` | STM/STS |  56 | `zenodo/17533355/FigS6/` |
| `FigS8/<file>.sxm / .dat` | STM/STS |  11 | `zenodo/17533355/FigS8/` |
| `FigS9/<file>.sxm / .dat` | STM/STS |  85 | `zenodo/17533355/FigS9/` |
| `directory.pdf`            | —       |   1 | `zenodo/17533355/directory.pdf/directory.pdf` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
