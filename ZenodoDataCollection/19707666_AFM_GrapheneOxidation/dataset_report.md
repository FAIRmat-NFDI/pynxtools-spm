# Dataset Report: Zenodo Record 19707666

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for 'Layer-dependent oxidation spreading in multilayer graphene during AFM local anodic oxidation' |
| **DOI**    | [10.5281/zenodo.19707666](https://doi.org/10.5281/zenodo.19707666) |
| **Date**   | 2026-04-23 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Vymazal, Jan; Konečný, Martin; Piastek, Jakub; Mach, Jindrich et al. |
| **Tags**   | AFM, atomic force microscopy, graphene, local anodic oxidation, LAO, oxidation, multilayer graphene |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — local anodic oxidation (LAO) and imaging
- **Instrument**: Bruker AFM (NanoScope `.spm` format)

## Dataset Contents

99 objects extracted from `Data.zip`, organised by figures (Figures 2–12) and COMSOL simulations. Contains Bruker `.spm` AFM files for individual figures in the graphene layer-dependent oxidation spreading study.

## File Format

- **Format**: Bruker `.spm`
- **Parsability**: Parsable by `BrukerSpmAFM`.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/19707666/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 99 files

**S3 key pattern**: `zenodo/19707666/Data/<Figure folder>/<filename>/<filename>`

Source zip `Data.zip` extracted into `Data/` ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/19707666/Data/))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `Data/Figure 2/<file>` | AFM | 2 | `zenodo/19707666/Data/Figure 2/` |
| `Data/Figure 3/<file>` | AFM | 12 | `zenodo/19707666/Data/Figure 3/` |
| `Data/Figure 4/<file>` | AFM | 12 | `zenodo/19707666/Data/Figure 4/` |
| `Data/Figure 5/<file>` | AFM | 2 | `zenodo/19707666/Data/Figure 5/` |
| `Data/Figure 6/<file>` | Raman | 11 | `zenodo/19707666/Data/Figure 6/` |
| `Data/Figure 7/<file>` | AFM | 6 | `zenodo/19707666/Data/Figure 7/` |
| `Data/Figure 8/<file>` | AFM | 6 | `zenodo/19707666/Data/Figure 8/` |
| `Data/Figure 9/<file>` | AFM | 12 | `zenodo/19707666/Data/Figure 9/` |
| `Data/Figure 10/<file>` | — | 6 | `zenodo/19707666/Data/Figure 10/` |
| `Data/Figure 11/<file>` | — | 9 | `zenodo/19707666/Data/Figure 11/` |
| `Data/Figure 12/<file>` | — | 2 | `zenodo/19707666/Data/Figure 12/` |
| `Data/COMSOL simulations/<file>` | — | 19 | `zenodo/19707666/Data/COMSOL simulations/` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
