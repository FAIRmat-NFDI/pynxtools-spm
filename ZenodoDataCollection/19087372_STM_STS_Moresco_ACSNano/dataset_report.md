# Dataset Report: Zenodo Record 19087372

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Supplementary data to publication https://pubs.acs.org/doi/10.1021/acsnano.5c17283 |
| **DOI**    | [10.5281/zenodo.19087372](https://doi.org/10.5281/zenodo.19087372) |
| **Url** | PlaceHolder: Full dataset URL from the zenodo record. |
| **Date**   | 2026-03-18 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Moresco, Francesca |
| **Tags**   | STM, STS, scanning tunneling microscopy, subphthalocyanine, single-molecule machines, Au(111) |
| **Description** | PlaceHolder: Full dataset description file from the zenodo record. |
| **Experiment information related files** | PlaceHolder: List of the files that contain other information related with the experiment, e.g., chemical formulas, experiment temperatures etc. |


## Technique

- **Primary SPM technique**: STM/STS (Scanning Tunneling Microscopy/Spectroscopy)
- **Instrument**: Nanonis (`.dat` format — STM images and STS spectroscopy)

## Dataset Contents

78 Nanonis `.dat` STM/STS files (prefixed A or B) for a study of subphthalocyanine single-molecule machines on Au(111). Files span multiple sessions from 2024-03 to 2025-02. Supplementary to ACS Nano publication.

## File Format

- **Format**: Nanonis `.dat` (STM images and STS spectra)
- **Parsability**: Parsable by `NanonisDatSTS` for spectroscopy files. STM image `.dat` files may use a different Nanonis sub-format.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/19087372/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 78 files

**S3 key pattern**: `zenodo/19087372/<filename>/<filename>`

Files uploaded flat ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/19087372/))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `A*.dat` / `B*.dat` | STM/STS | 78 | `zenodo/19087372/` |

**Information Files**:
| file | experiment | count | S3 key|
|------|------------|-------|---------------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
