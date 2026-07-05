# Dataset Report: Zenodo Record 20439519

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Autonomous scanning electrochemical cell microscopy enables rapid exploration of large compositionally complex material spaces |
| **DOI**    | [10.5281/zenodo.20439519](https://doi.org/10.5281/zenodo.20439519) |
| **Date**   | 2026-05-28 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Thelen, Felix; Kim, Moonjoo; de Oliveira, Geovane Arruda et al. |
| **Tags**   | Hydrogen evolution reaction, Active learning, Electrochemistry, Magnetron sputtering, SECCM, Gaussian process regression, Electrocatalysis |

## Technique

- **Primary SPM technique**: Atomic Force Microscopy (AFM)
- **Instrument vendor**: Bruker (NanoScope raw data format)
- **Additional techniques in dataset**: EDX, XPS, XRD, SECCM

## Dataset Contents

15 AFM measurements (5 per Au-Ir-Rh ternary library: Au-rich, Ir-rich, Rh-rich) on thin-film
materials libraries fabricated by magnetron co-sputtering on 100 mm Sapphire wafers.
Files use Bruker NanoScope raw format without `.spm` extension.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/20439519/`  
**Upload date**: 2026-06-25  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 2018 files (16 AFM + 3 EDX + 967 SECCM + 6 XPS + 1026 XRD)

Zips are extracted; each file is uploaded into its own subfolder so experiment metadata
(`eln_data.yaml`, converted `output.nxs`, etc.) can be added alongside the raw file later.

**S3 key pattern**: `zenodo/<record_id>/<dataset_folder>/<filename>/<filename>`

**Skipped**: 3 `.mp4` animation/video files (~550 MB total) — not SPM data.

### AFM dataset — 16 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/20439519/AFM_dataset/))

Source zip: `AFM_dataset.zip` — Bruker NanoScope raw format (no `.spm` extension)

| file | experiment | S3 key |
|------|------------|--------|
| `Au-Ir-Rh_Au-rich_AFM_area_168.002` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_168.002/Au-Ir-Rh_Au-rich_AFM_area_168.002` |
| `Au-Ir-Rh_Au-rich_AFM_area_178.004` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_178.004/Au-Ir-Rh_Au-rich_AFM_area_178.004` |
| `Au-Ir-Rh_Au-rich_AFM_area_20.003`  | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_20.003/Au-Ir-Rh_Au-rich_AFM_area_20.003` |
| `Au-Ir-Rh_Au-rich_AFM_area_313.000` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_313.000/Au-Ir-Rh_Au-rich_AFM_area_313.000` |
| `Au-Ir-Rh_Au-rich_AFM_area_55.005`  | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_55.005/Au-Ir-Rh_Au-rich_AFM_area_55.005` |
| `Au-Ir-Rh_Ir-rich_AFM_area_13.000`  | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_13.000/Au-Ir-Rh_Ir-rich_AFM_area_13.000` |
| `Au-Ir-Rh_Ir-rich_AFM_area_168.001` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_168.001/Au-Ir-Rh_Ir-rich_AFM_area_168.001` |
| `Au-Ir-Rh_Ir-rich_AFM_area_178.002` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_178.002/Au-Ir-Rh_Ir-rich_AFM_area_178.002` |
| `Au-Ir-Rh_Ir-rich_AFM_area_315.003` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_315.003/Au-Ir-Rh_Ir-rich_AFM_area_315.003` |
| `Au-Ir-Rh_Ir-rich_AFM_area_342.004` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_342.004/Au-Ir-Rh_Ir-rich_AFM_area_342.004` |
| `Au-Ir-Rh_Rh-rich_AFM_area_16.005`  | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_16.005/Au-Ir-Rh_Rh-rich_AFM_area_16.005` |
| `Au-Ir-Rh_Rh-rich_AFM_area_168.008` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_168.008/Au-Ir-Rh_Rh-rich_AFM_area_168.008` |
| `Au-Ir-Rh_Rh-rich_AFM_area_200.010` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_200.010/Au-Ir-Rh_Rh-rich_AFM_area_200.010` |
| `Au-Ir-Rh_Rh-rich_AFM_area_240.006` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_240.006/Au-Ir-Rh_Rh-rich_AFM_area_240.006` |
| `Au-Ir-Rh_Rh-rich_AFM_area_297.009` | AFM | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_297.009/Au-Ir-Rh_Rh-rich_AFM_area_297.009` |
| `DataSetnote.txt`                    | —   | `zenodo/20439519/AFM_dataset/DataSetnote.txt/DataSetnote.txt` |

### EDX dataset — 3 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/20439519/EDX_dataset/))

Source zip: `EDX_dataset.zip` — composition maps (CSV)

| file | experiment | S3 key |
|------|------------|--------|
| `Au-Ir-Rh_Au-rich_EDX.csv` | EDX | `zenodo/20439519/EDX_dataset/Au-Ir-Rh_Au-rich_EDX.csv/Au-Ir-Rh_Au-rich_EDX.csv` |
| `Au-Ir-Rh_Ir-rich_EDX.csv` | EDX | `zenodo/20439519/EDX_dataset/Au-Ir-Rh_Ir-rich_EDX.csv/Au-Ir-Rh_Ir-rich_EDX.csv` |
| `Au-Ir-Rh_Rh-rich_EDX.csv` | EDX | `zenodo/20439519/EDX_dataset/Au-Ir-Rh_Rh-rich_EDX.csv/Au-Ir-Rh_Rh-rich_EDX.csv` |

### XPS dataset — 6 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/20439519/XPS_dataset/))

Source zip: `XPS_dataset.zip` — surface composition CSVs (measured + predicted)

| file | experiment | S3 key |
|------|------------|--------|
| `Au-Ir-Rh_Au-rich_XPS.csv`           | XPS | `zenodo/20439519/XPS_dataset/Au-Ir-Rh_Au-rich_XPS.csv/Au-Ir-Rh_Au-rich_XPS.csv` |
| `Au-Ir-Rh_Au-rich_XPS_predicted.csv` | XPS | `zenodo/20439519/XPS_dataset/Au-Ir-Rh_Au-rich_XPS_predicted.csv/Au-Ir-Rh_Au-rich_XPS_predicted.csv` |
| `Au-Ir-Rh_Ir-rich_XPS.csv`           | XPS | `zenodo/20439519/XPS_dataset/Au-Ir-Rh_Ir-rich_XPS.csv/Au-Ir-Rh_Ir-rich_XPS.csv` |
| `Au-Ir-Rh_Ir-rich_XPS_predicted.csv` | XPS | `zenodo/20439519/XPS_dataset/Au-Ir-Rh_Ir-rich_XPS_predicted.csv/Au-Ir-Rh_Ir-rich_XPS_predicted.csv` |
| `Au-Ir-Rh_Rh-rich_XPS.csv`           | XPS | `zenodo/20439519/XPS_dataset/Au-Ir-Rh_Rh-rich_XPS.csv/Au-Ir-Rh_Rh-rich_XPS.csv` |
| `Au-Ir-Rh_Rh-rich_XPS_predicted.csv` | XPS | `zenodo/20439519/XPS_dataset/Au-Ir-Rh_Rh-rich_XPS_predicted.csv/Au-Ir-Rh_Rh-rich_XPS_predicted.csv` |

### SECCM dataset — 967 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/20439519/SECCM_dataset/))

Source zip: `SECCM_dataset.zip` — one LSV CSV per measurement area + fit-parameter summary

| file | experiment | count | S3 key pattern |
|------|------------|-------|----------------|
| `Au-Ir-Rh_Au-rich_SECCM_area_N_x=…_y=…_LSV.csv` | SECCM | 322 | `zenodo/20439519/SECCM_dataset/Au-Ir-Rh_Au-rich_SECCM_area_N_x=X_y=Y_LSV.csv/…` |
| `Au-Ir-Rh_Ir-rich_SECCM_area_N_x=…_y=…_LSV.csv` | SECCM | 322 | `zenodo/20439519/SECCM_dataset/Au-Ir-Rh_Ir-rich_SECCM_area_N_x=X_y=Y_LSV.csv/…` |
| `Au-Ir-Rh_Rh-rich_SECCM_area_N_x=…_y=…_LSV.csv` | SECCM | 322 | `zenodo/20439519/SECCM_dataset/Au-Ir-Rh_Rh-rich_SECCM_area_N_x=X_y=Y_LSV.csv/…` |
| `LSV_fit_parameters.csv`                          | SECCM |   1 | `zenodo/20439519/SECCM_dataset/LSV_fit_parameters.csv/LSV_fit_parameters.csv` |

### XRD dataset — 1026 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/20439519/XRD_dataset/))

Source zip: `XRD_dataset.zip` — one `.xy` diffractogram per measurement area

| file | experiment | count | S3 key pattern |
|------|------------|-------|----------------|
| `Au-Ir-Rh_Au-rich_XRD_area_NNN_diffractogram.xy` | XRD | 342 | `zenodo/20439519/XRD_dataset/Au-Ir-Rh_Au-rich_XRD_area_NNN_diffractogram.xy/…` |
| `Au-Ir-Rh_Ir-rich_XRD_area_NNN_diffractogram.xy` | XRD | 342 | `zenodo/20439519/XRD_dataset/Au-Ir-Rh_Ir-rich_XRD_area_NNN_diffractogram.xy/…` |
| `Au-Ir-Rh_Rh-rich_XRD_area_NNN_diffractogram.xy` | XRD | 342 | `zenodo/20439519/XRD_dataset/Au-Ir-Rh_Rh-rich_XRD_area_NNN_diffractogram.xy/…` |

## Parsability Assessment

- **Current parser compatibility**: Potentially parsable by the Bruker AFM parser (`BrukerSpmAFM`).
- **Complication**: AFM files have no `.spm` extension (named e.g. `Au-Ir-Rh_Au-rich_AFM_area_168.002`).
  The `SPMParser` dispatches on file extension, so these files would need to be renamed or
  the parser given an explicit format hint.
- **Next step**: Attempt to parse one file by renaming it with `.spm` and running
  `write_spm_raw_file_data()` to inspect the raw key-value dump.

## Status

- [x] Files uploaded to S3
- [ ] Parser test attempted
- [ ] Reference `.nxs` file generated
