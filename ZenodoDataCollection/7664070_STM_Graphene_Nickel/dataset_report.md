# Dataset Report: Zenodo Record 7664070

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset of Scanning Tunneling Microscopy (STM) images of graphene on nickel |
| **DOI**    | [10.5281/zenodo.7664070](https://doi.org/10.5281/zenodo.7664070) |
| **Date**   | 2021-12-24 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Tommaso Rodani; Elda Osmenaj; Alberto Cazzaniga; Mirco Panighel et al. |
| **Tags**   | STM, scanning tunneling microscopy, graphene, nickel, CVD, surface, doping |

## Technique

- **Primary SPM technique**: STM (Scanning Tunneling Microscopy)
- **Instrument**: Omicron Variable Temperature STM (VT-STM), TASC laboratory CNR-IOM Trieste

## Dataset Contents

24983 objects: large STM dataset extracted from `STM.zip` (3.5 GB). Omicron VT-STM proprietary format (`.par`, `.tf`) files. Also includes `metadata.csv`, `provenance.json`, `md5sum.txt`.

## File Format

- **Format**: Omicron VT-STM proprietary (`.par`, `.tf`) — different from the Omicron `.sm4` format supported by `OmicronSM4STM`
- **Parsability**: Not supported. Omicron `.par`/`.tf` format is distinct from Omicron `.sm4`. A dedicated parser would be required.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/7664070/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 24983 files (24,980 STM + 3 ancillary)

**S3 key pattern**: `zenodo/7664070/<folder>/<filename>/<filename>`

### STM data — 24,980 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/7664070/STM/))

Source zip: `STM.zip` — Omicron VT-STM proprietary format; each scan produces 3 files (~8,327 scans total)

| file | experiment | count | S3 key pattern |
|------|------------|-------|----------------|
| `STM/data/<ID>.par` | STM | ~8,327 | `zenodo/7664070/STM/data/<ID>.par/<ID>.par` |
| `STM/data/<ID>.tb0` | STM | ~8,327 | `zenodo/7664070/STM/data/<ID>.tb0/<ID>.tb0` |
| `STM/data/<ID>.tf0` | STM | ~8,326 | `zenodo/7664070/STM/data/<ID>.tf0/<ID>.tf0` |

### Ancillary files — 3 files

| file | experiment | S3 key |
|------|------------|--------|
| `metadata.csv`    | — | `zenodo/7664070/metadata.csv/metadata.csv` |
| `provenance.json` | — | `zenodo/7664070/provenance.json/provenance.json` |
| `md5sum.txt`      | — | `zenodo/7664070/md5sum.txt/md5sum.txt` |

## Category

**Unknown/Unsupported Format**

## Status

- [x] Files uploaded to S3
- [ ] Parser not implemented (Omicron .par/.tf format)
- [ ] Reference .nxs file not generated
