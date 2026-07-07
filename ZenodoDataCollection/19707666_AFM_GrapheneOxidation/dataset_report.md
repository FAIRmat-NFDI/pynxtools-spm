# Dataset Report: Zenodo Record 19707666

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for 'Layer-dependent oxidation spreading in multilayer graphene during AFM local anodic oxidation' |
| **DOI**    | [10.5281/zenodo.19707666](https://doi.org/10.5281/zenodo.19707666) |
| **Url**    | [https://zenodo.org/records/19707666](https://zenodo.org/records/19707666) |
| **Date**   | 2026-04-23 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Vymazal, Jan; Konečný, Martin; Piastek, Jakub et al. |
| **Tags**   | AFM, atomic force microscopy, graphene, local anodic oxidation, LAO, oxidation, multilayer graphene |
| **Description** | Individual files used for Figures 2-12 are assembled in the folders. The COMSOL Multiphysics files are provided in the folder "COMSOL Simulations". |
| **Experiment information related files** | None |

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

**S3 key pattern**: `zenodo/19707666/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `tecky.0_00000.spm` | AFM | 1 | `zenodo/19707666/Data/Figure 3/tecky.0_00000.spm/` | — | — |
| `tecky.0_00002.spm` | AFM | 2 | `zenodo/19707666/Data/Figure 3/tecky.0_00002.spm/` | — | — |
| `tecky.0_00000.spm` | AFM | 3 | `zenodo/19707666/Data/Figure 4/tecky.0_00000.spm/` | — | — |
| `tecky.0_00002.spm` | AFM | 4 | `zenodo/19707666/Data/Figure 4/tecky.0_00002.spm/` | — | — |
| `tecky.0_00001.spm` | AFM | 5 | `zenodo/19707666/Data/Figure 7/tecky.0_00001.spm/` | — | — |
| `tecky.0_00002.spm` | AFM | 6 | `zenodo/19707666/Data/Figure 7/tecky.0_00002.spm/` | — | — |
| `oxid.0_00008.spm` | AFM | 7 | `zenodo/19707666/Data/Figure 9/oxid.0_00008.spm/` | — | — |
| `*.mdt` | AFM | 6 | `zenodo/19707666/Data/` | — | — |
| `*.mph` | AFM | 19 | `zenodo/19707666/Data/` | — | — |
| `*.png` | AFM | 34 | `zenodo/19707666/Data/` | — | — |
| `*.py` | AFM | 6 | `zenodo/19707666/Data/` | — | — |
| `*.svg` | AFM | 6 | `zenodo/19707666/Data/` | — | — |
| `*.svg` | RAMAN | 1 | `zenodo/19707666/Data/` | — | — |
| `*.txt` | AFM | 17 | `zenodo/19707666/Data/` | — | — |
| `*.wip` | AFM | 3 | `zenodo/19707666/Data/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
