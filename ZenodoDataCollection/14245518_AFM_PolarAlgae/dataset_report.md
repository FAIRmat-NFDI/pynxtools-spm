# Dataset Report: Zenodo Record 14245518

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Heating by Dissipation of Energy from Absorbed Light: Molecular Mechanisms Underlying the Survival Strategy of Polar Algae |
| **DOI**    | [10.5281/zenodo.14245518](https://doi.org/10.5281/zenodo.14245518) |
| **Date**   | 2024-11-29 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Zubik-Duda, Monika; Grudzinski, Wojciech; Luchowski, Rafal; Janik, Sebastian et al. |
| **Tags**   | AFM, fluorescence microscopy, FLIM, HPLC, Raman, polar algae, Pediastrum orientale |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) + FLIM + Raman + HPLC + Fluorescence
- **Instrument**: JPK NanoWizard 3 (Bruker) with JPKSPM data processing software

## Dataset Contents

Multi-technique dataset for polar alga *Pediastrum orientale* collected from Reindeer Lake, Spitsbergen. AFM data is in `_AFM.ZIP` (JPK/Bruker format). Also contains FLIM (7 GB, FLIM.ZIP — download failed), Raman (4.5 GB, RAMAN.ZIP), HPLC, Microscope_Fluo, and Fluo data. 115 objects in S3.

## File Format

- **Format**: `.jpk` (JPK/Bruker NanoWizard proprietary). **Note:** `_AFM.ZIP` was uploaded as-is (not extracted) because the script only extracts lowercase `.zip`; `RAMAN.ZIP`, `HPLC.ZIP` similarly. `FLIM.ZIP` (7 GB) failed to download — not in S3.
- **Parsability**: Not supported. `.jpk` format (NanoWizard 3) is not in the dispatch table. Different from the NanoRacer `.jpk` in record 19254504 but same general format family.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14245518/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 115 files

**S3 key pattern**: `zenodo/14245518/<folder>/<filename>/<filename>`

⚠️ `_AFM.ZIP`, `HPLC.ZIP`, `RAMAN.ZIP` were uploaded as raw zip files (uppercase `.ZIP` bypassed extraction). `FLIM.ZIP` (7 GB) failed to download — absent from S3.

### AFM data — 1 file ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14245518/_AFM.ZIP/))

| file | experiment | S3 key |
|------|------------|--------|
| `_AFM.ZIP` | AFM | `zenodo/14245518/_AFM.ZIP/_AFM.ZIP` |

### Fluorescence spectroscopy — 84 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14245518/Fluo/))

Source zip: `Fluo.zip`

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `Fluo/Camera_/<file>` | Fluo | 84 | `zenodo/14245518/Fluo/Camera_/` |

### Fluorescence lifetime (FLIM) — 26 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14245518/Lifetime/))

Source zip: `Lifetime.zip`

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `Lifetime/2024-04-25/<file>` | FLIM | 26 | `zenodo/14245518/Lifetime/2024-04-25/` |

### Confocal microscopy — 2 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14245518/Microscope_Fluo/))

Source zip: `Microscope_Fluo.zip`

| file | experiment | S3 key |
|------|------------|--------|
| `Experiment-427_Zstack_LSM_dobra fluo-LSM Plus Processing-01.czi` | FM | `zenodo/14245518/Microscope_Fluo/Experiment-427_…-01.czi/Experiment-427_…-01.czi` |
| `Experiment-450 Z-stack_Airy_488_63x_4komorki_2024_10_21_do czapek (Position List) _ film 3d.czi` | FM | `zenodo/14245518/Microscope_Fluo/Experiment-450…3d.czi/Experiment-450…3d.czi` |

### Ancillary zipped archives — 2 files

| file | experiment | S3 key |
|------|------------|--------|
| `HPLC.ZIP`  | HPLC  | `zenodo/14245518/HPLC.ZIP/HPLC.ZIP` |
| `RAMAN.ZIP` | Raman | `zenodo/14245518/RAMAN.ZIP/RAMAN.ZIP` |

## Category

**Datasets of Interest**

## Notes

⚠️ `FLIM.ZIP` (7 GB) failed to download — not present in S3. `_AFM.ZIP`, `HPLC.ZIP`, `RAMAN.ZIP` were uploaded as raw zip files (not extracted) due to uppercase `.ZIP` extension not matching the unzip condition in the batch script.

## Status

- [ ] Files partially uploaded to S3 (FLIM.ZIP missing)
- [ ] Parser not implemented (.jpk format)
- [ ] Reference .nxs file not generated
