# Dataset Report: Zenodo Record 17360113

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | STM image of quasiparticle interferences on twisted graphene bilayers |
| **DOI**    | [10.5281/zenodo.17360113](https://doi.org/10.5281/zenodo.17360113) |
| **Url**    | [https://zenodo.org/records/17360113](https://zenodo.org/records/17360113) |
| **Date**   | 2025-10-15 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Renard, Vincent |
| **Tags**   | STM, scanning tunneling microscopy, quasiparticle interference, twisted graphene bilayer, topography, dI/dV |
| **Description** | The dataset contains the STM measurements of quasiparticle interferences near a defect. <br><br> Each image contains three channels : topography, dI/dV and current (bothforward and backward).  <br><br> Each image contains metadata indicating the measurement conditions |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: STM (Scanning Tunneling Microscopy) — topography + dI/dV + current channels
- **Instrument**: Nanonis (`.sxm` format)

## Sample

- **Material / chemical formula**: **twisted bilayer graphene** → `C` (carbon).
- **Study**: STM imaging of quasiparticle interference (QPI) near a defect; each `.sxm` holds
  topography (z), current and dI/dV channels (forward and backward), with acquisition metadata.

## Dataset Contents

15 objects: Nanonis `.sxm` STM images extracted from `STM_images.zip`. Each image contains three channels (topography, dI/dV, current — forward and backward) with acquisition metadata.

## File Format

- **Format**: Nanonis `.sxm`
- **Parsability**: Supported by `NanonisSxmSTM`. Multi-channel files with topography and dI/dV.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17360113/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 15 files

**S3 key pattern**: `zenodo/17360113/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `SiCCAO#C012_300mV.sxm` | STM | Twisted bilayer graphene | C | 1 | `zenodo/17360113/STM_images/SiCCAO#C012_300mV.sxm/` | True | True |
| `SiCCAO#C013_500mV.sxm` | STM | Twisted bilayer graphene | C | 2 | `zenodo/17360113/STM_images/SiCCAO#C013_500mV.sxm/` | True | True |
| `SiCCAO#C014_350mV.sxm` | STM | Twisted bilayer graphene | C | 3 | `zenodo/17360113/STM_images/SiCCAO#C014_350mV.sxm/` | True | True |
| `SiCCAO#C015_425mV.sxm` | STM | Twisted bilayer graphene | C | 4 | `zenodo/17360113/STM_images/SiCCAO#C015_425mV.sxm/` | True | True |
| `SiCCAO#C016_325.sxm` | STM | Twisted bilayer graphene | C | 5 | `zenodo/17360113/STM_images/SiCCAO#C016_325.sxm/` | True | True |
| `SiCCAO#C017_400mV.sxm` | STM | Twisted bilayer graphene | C | 6 | `zenodo/17360113/STM_images/SiCCAO#C017_400mV.sxm/` | True | True |
| `SiCCAO#C018_275mV.sxm` | STM | Twisted bilayer graphene | C | 7 | `zenodo/17360113/STM_images/SiCCAO#C018_275mV.sxm/` | True | True |
| `SiCCAO#C019_375.sxm` | STM | Twisted bilayer graphene | C | 8 | `zenodo/17360113/STM_images/SiCCAO#C019_375.sxm/` | True | True |
| `SiCCAO#C020_200mV.sxm` | STM | Twisted bilayer graphene | C | 9 | `zenodo/17360113/STM_images/SiCCAO#C020_200mV.sxm/` | True | True |
| `SiCCAO#C021_450mV.sxm` | STM | Twisted bilayer graphene | C | 10 | `zenodo/17360113/STM_images/SiCCAO#C021_450mV.sxm/` | True | True |
| `SiCCAO#C022_362mV.sxm` | STM | Twisted bilayer graphene | C | 11 | `zenodo/17360113/STM_images/SiCCAO#C022_362mV.sxm/` | True | True |
| `SiCCAO#C023_388mV.sxm` | STM | Twisted bilayer graphene | C | 12 | `zenodo/17360113/STM_images/SiCCAO#C023_388mV.sxm/` | True | True |
| `SiCCAO#C024_300mV.sxm` | STM | Twisted bilayer graphene | C | 13 | `zenodo/17360113/STM_images/SiCCAO#C024_300mV.sxm/` | True | True |
| `SiCCAO#C025_475mV.sxm` | STM | Twisted bilayer graphene | C | 14 | `zenodo/17360113/STM_images/SiCCAO#C025_475mV.sxm/` | True | True |
| `SiCCAO#C031_150mV.sxm` | STM | Twisted bilayer graphene | C | 15 | `zenodo/17360113/STM_images/SiCCAO#C031_150mV.sxm/` | True | True |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08 with `pynxtools-spm` 0.2.5. License **`cc-by-4.0`** passes the open-license
gate. **All 15 Nanonis `.sxm` STM files converted, validated, and uploaded** (`PS = True`,
`Uploaded = True`); `eln_data.yaml` + `config.json` + `.nxs` in each file's S3 folder. 4 NXdata
groups per file (current, z × forward/backward), default `current_forward`; short units
(`A, V, m, s, °`); 0 shape mismatches. `citeID.description` carries the full Zenodo description.
Required a small `pynxtools-spm` fix — `NanonisDatSTS._construct_linear_sweep_grp` (borrowed by
the sxm STM formatter) now guards against `None` bias-sweep values so STM images without bias
spectroscopy no longer crash on `None - None`.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 15/15 `.sxm` converted (`PS = True`)
- [x] Reference .nxs files generated and uploaded for all 15 files
