# Dataset Report: Zenodo Record 14780459

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data related to "Inverse melting and re-entrant transformations of the vortex lattice in amorphous Re₆Zr thin film" |
| **DOI**    | [10.5281/zenodo.14780459](https://doi.org/10.5281/zenodo.14780459) |
| **Date**   | 2025-01-31 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Duhan, Rishabh; Sengupta, Subhamita; Jesudasan, John; Basistha, Somak et al. |
| **Tags**   | STM, STS, scanning tunneling spectroscopy, superconductor, vortex lattice, Re6Zr |

## Technique

- **Primary SPM technique**: STS (Scanning Tunneling Spectroscopy) — conductance maps at low temperature
- **Instrument**: Nanonis (`.sxm` format) low-temperature STM/STS

## Dataset Contents

318 Nanonis `.sxm` conductance maps organised by figure (Fig 1 & 2, Fig 3) showing vortex lattice states at varying magnetic field and temperature in Re₆Zr thin film. Transport data in `.opju` (Origin). PNG summary image included.

## File Format

- **Format**: Nanonis `.sxm` (STS conductance maps), `.opju` (Origin transport data), `.png`
- **Parsability**: Nanonis `.sxm` files are parsable. Technique is STS (conductance maps), so `NanonisSxmSTM` would apply. Transport `.opju` files are not in scope.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14780459/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 318 files

**S3 key pattern**: `zenodo/14780459/<folder>/<filename>/<filename>`

### STS / STM conductance maps — 316 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14780459/STM%20data/))

Source zip: `STM data.zip` — Nanonis `.sxm` vortex-lattice conductance maps

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `STM data/Fig 1 and 2/<file>.sxm` | STS | 220 | `zenodo/14780459/STM data/Fig 1 and 2/` |
| `STM data/Fig3/<file>.sxm`        | STS |  96 | `zenodo/14780459/STM data/Fig3/` |

### Ancillary files — 2 files

| file | experiment | S3 key |
|------|------------|--------|
| `Transport Data.opju`    | — | `zenodo/14780459/Transport Data.opju/Transport Data.opju` |
| `raw_image_addition.png` | — | `zenodo/14780459/raw_image_addition.png/raw_image_addition.png` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
