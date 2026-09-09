# Dataset Report: Zenodo Record 13595509

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Nucleation-Limited Kinetics of GaAs Nanostructures Grown by Selective Area Epitaxy |
| **DOI**    | [10.5281/zenodo.13595509](https://doi.org/10.5281/zenodo.13595509) |
| **Date**   | 2024-08-12 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Zendrini, Michele; Piazza, Valerio; Fontcuberta i Morral, Anna; Rudra, Alok et al. |
| **Tags**   | SAE, MOVPE, GaAs, Nanowires, Growth kinetics, AFM, SEM |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) + SEM
- **Instrument**: Bruker AFM (format: .spm via .xyz conversion noted in description)

## Dataset Contents

AFM and SEM datasets of GaAs nanowires (NWs) and nanomembranes (NMs) grown by selective area epitaxy at varying growth times (45–840 s and annealing). 269 objects organised by growth condition and nanostructure type.

## File Format

- **Format**: Bruker `.spm` (AFM) and `.tif` (SEM)
- **Parsability**: AFM files potentially parsable by `BrukerSpmAFM`. SEM `.tif` files not in scope.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/13595509/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 269 files

**S3 key pattern**: `zenodo/13595509/<folder>/<filename>/<filename>`

### AFM nanomembranes — 101 files ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/13595509/AFM_NMs_))

8 growth-time conditions (45s, 60s, 90s, 120s, 180s, 420s, 840s, Annealing); each zip → its own folder

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `AFM_NMs_45s/<file>.spm`       | AFM | 12 | `zenodo/13595509/AFM_NMs_45s/` |
| `AFM_NMs_60s/<file>.spm`       | AFM | 14 | `zenodo/13595509/AFM_NMs_60s/` |
| `AFM_NMs_90s/<file>.spm`       | AFM | 13 | `zenodo/13595509/AFM_NMs_90s/` |
| `AFM_NMs_120s/<file>.spm`      | AFM | 14 | `zenodo/13595509/AFM_NMs_120s/` |
| `AFM_NMs_180s/<file>.spm`      | AFM | 11 | `zenodo/13595509/AFM_NMs_180s/` |
| `AFM_NMs_420s/<file>.spm`      | AFM | 13 | `zenodo/13595509/AFM_NMs_420s/` |
| `AFM_NMs_840s/<file>.spm`      | AFM | 12 | `zenodo/13595509/AFM_NMs_840s/` |
| `AFM_NMs_Annealing/<file>.spm` | AFM | 12 | `zenodo/13595509/AFM_NMs_Annealing/` |

### AFM nanowires — 32 files ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/13595509/AFM_NWs_))

8 sample/condition folders (4 files each)

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `AFM_NWs_6913_Annealing/<file>.spm` | AFM | 4 | `zenodo/13595509/AFM_NWs_6913_Annealing/` |
| `AFM_NWs_6914_180s/<file>.spm`      | AFM | 4 | `zenodo/13595509/AFM_NWs_6914_180s/` |
| `AFM_NWs_6929_420s/<file>.spm`      | AFM | 4 | `zenodo/13595509/AFM_NWs_6929_420s/` |
| `AFM_NWs_6930_45s/<file>.spm`       | AFM | 4 | `zenodo/13595509/AFM_NWs_6930_45s/` |
| `AFM_NWs_6953_840s/<file>.spm`      | AFM | 4 | `zenodo/13595509/AFM_NWs_6953_840s/` |
| `AFM_NWs_6978_60s/<file>.spm`       | AFM | 4 | `zenodo/13595509/AFM_NWs_6978_60s/` |
| `AFM_NWs_6979_90s/<file>.spm`       | AFM | 4 | `zenodo/13595509/AFM_NWs_6979_90s/` |
| `AFM_NWs_6980_120s/<file>.spm`      | AFM | 4 | `zenodo/13595509/AFM_NWs_6980_120s/` |

### SEM nanomembranes — 97 files ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/13595509/SEM_NMs_))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `SEM_NMs_45s/<file>.tif`       | SEM | 12 | `zenodo/13595509/SEM_NMs_45s/` |
| `SEM_NMs_60s/<file>.tif`       | SEM | 12 | `zenodo/13595509/SEM_NMs_60s/` |
| `SEM_NMs_90s/<file>.tif`       | SEM | 12 | `zenodo/13595509/SEM_NMs_90s/` |
| `SEM_NMs_120s/<file>.tif`      | SEM | 12 | `zenodo/13595509/SEM_NMs_120s/` |
| `SEM_NMs_180s/<file>.tif`      | SEM | 12 | `zenodo/13595509/SEM_NMs_180s/` |
| `SEM_NMs_420s/<file>.tif`      | SEM | 13 | `zenodo/13595509/SEM_NMs_420s/` |
| `SEM_NMs_840s/<file>.tif`      | SEM | 12 | `zenodo/13595509/SEM_NMs_840s/` |
| `SEM_NMs_Annealing/<file>.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_Annealing/` |

### SEM nanowires — 36 files ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/13595509/SEM_NWs_))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `SEM_NWs_45s/<file>.tif`  | SEM | 4 | `zenodo/13595509/SEM_NWs_45s/` |
| `SEM_NWs_60s/<file>.tif`  | SEM | 4 | `zenodo/13595509/SEM_NWs_60s/` |
| `SEM_NWs_90s/<file>.tif`  | SEM | 4 | `zenodo/13595509/SEM_NWs_90s/` |
| `SEM_NWs_120s/<file>.tif` | SEM | 4 | `zenodo/13595509/SEM_NWs_120s/` |
| `SEM_NWs_180s/<file>.tif` | SEM | 4 | `zenodo/13595509/SEM_NWs_180s/` |
| `SEM_NWs_420s/<file>.tif` | SEM | 8 | `zenodo/13595509/SEM_NWs_420s/` |
| `SEM_NWs_840s/<file>.tif` | SEM | 8 | `zenodo/13595509/SEM_NWs_840s/` |

### Ancillary files — 3 files

| file | experiment | S3 key |
|------|------------|--------|
| `README.txt`                   | — | `zenodo/13595509/README.txt/README.txt` |
| `240812_NMs_data_Final.txt`    | AFM | `zenodo/13595509/240812_NMs_data_Final.txt/240812_NMs_data_Final.txt` |
| `240812_NWs_data_Final.txt`    | AFM | `zenodo/13595509/240812_NWs_data_Final.txt/240812_NWs_data_Final.txt` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
