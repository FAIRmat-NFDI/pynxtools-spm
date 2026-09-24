# Dataset Report: Zenodo Record 10443995

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Scanning Tunneling Microscope Images of Atomic Scale Defects in Tungsten Diselenide |
| **DOI**    | [10.5281/zenodo.10443995](https://doi.org/10.5281/zenodo.10443995) |
| **Date**   | 2023-12-30 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Smalley, Darian |
| **Tags**   | STM, scanning tunneling microscopy, WSe2, tungsten diselenide, defects, machine learning |

## Technique

- **Primary SPM technique**: STM (Scanning Tunneling Microscopy)
- **Instrument**: LT-STM and RT-STM (Hone-Barmak Group)

## Dataset Contents

136 annotated STM images of WSe₂ atomic-scale defects plus 38 augmented training images (bounding boxes + masks). 983 files including `.sxm` raw STM data, `.npy` numpy arrays for ML training, annotation CSV/JSON, and JPEG images.

## File Format

- **Format**: Nanonis `.sxm` (raw STM data)
- **Parsability**: Supported by `NanonisSxmSTM` formatter. Files are inside `STM_data/` folder (extracted from `STM_data.zip`).

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/10443995/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 983 files (743 STM_data + 236 STM_images + 4 ancillary)

**S3 key pattern**: `zenodo/10443995/<folder>/<filename>/<filename>`

### STM data — 743 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/10443995/STM_data/))

Source zip: `STM_data.zip` — Nanonis files organized by session date (2021-11-18 to 2021-11-27)

| file | experiment | count | S3 key pattern |
|------|------------|-------|----------------|
| `STM_data/<date>/<file>.sxm` | STM | 658 | `zenodo/10443995/STM_data/<date>/<file>.sxm/<file>.sxm` |
| `STM_data/<date>/<file>.dat` | STM | 56  | `zenodo/10443995/STM_data/<date>/<file>.dat/<file>.dat` |
| `STM_data/<date>/Nanonis-Session.ini` | — | 6  | `zenodo/10443995/STM_data/<date>/Nanonis-Session.ini/…` |
| `STM_data/<date>/<file>.zip` | — | 2  | `zenodo/10443995/STM_data/<date>/<file>.zip/<file>.zip` |

### STM images — 236 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/10443995/STM_images/))

Source zip: `STM_images.zip` — processed JPEG images of WSe₂ defects

| file | experiment | count | S3 key pattern |
|------|------------|-------|----------------|
| `STM_images/<file>.jpg` | STM | 236 | `zenodo/10443995/STM_images/<file>.jpg/<file>.jpg` |

### Ancillary files — 4 files

| file | experiment | S3 key |
|------|------------|--------|
| `annotations.csv` | STM | `zenodo/10443995/annotations.csv/annotations.csv` |
| `annotations.json` | STM | `zenodo/10443995/annotations.json/annotations.json` |
| `WSe2-Defect-Training-Images_2023-05-01.npy` | ML | `zenodo/10443995/WSe2-Defect-Training-Images_2023-05-01.npy/WSe2-Defect-Training-Images_2023-05-01.npy` |
| `WSe2-Defect-Training-Labels_2023-05-01.npy` | ML | `zenodo/10443995/WSe2-Defect-Training-Labels_2023-05-01.npy/WSe2-Defect-Training-Labels_2023-05-01.npy` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
