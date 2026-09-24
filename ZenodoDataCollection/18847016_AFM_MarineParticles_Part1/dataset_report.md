# Dataset Report: Zenodo Record 18847016

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data for: Measurements of the size and physical properties of marine particles using atomic force microscopy (part 1) |
| **DOI**    | [10.5281/zenodo.18847016](https://doi.org/10.5281/zenodo.18847016) |
| **Date**   | 2026-03-03 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Yamada, Yosuke; Mochizuki, Toshiaki; Fukuda, Hideki; Nagata, Toshi et al. |
| **Tags**   | AFM, atomic force microscopy, marine particles, ocean, particle size, physical properties |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — marine particle characterisation
- **Instrument**: Bruker AFM (NanoScope `.spm` format, organised by date in YYMMDD_particle folders)

## Dataset Contents

Part 1 of a multi-part dataset of raw AFM images of marine particle samples. The single archive `Part 1.7z` (43.9 GB) was too large to download — download failed and was skipped. **Only the README.txt is present in S3.** Part 2 is in record 18847316.

## File Format

- **Format**: Bruker `.spm` (inside Part 1.7z — not downloaded)
- **Parsability**: Parsable by `BrukerSpmAFM` once the archive is obtained. Currently inaccessible — the 43.9 GB `.7z` archive failed to download.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/18847016/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 1 files

**S3 key pattern**: `zenodo/18847016/<filename>/<filename>`

| file | experiment | S3 key |
|------|------------|--------|
| `README.txt` | — | `zenodo/18847016/README.txt/README.txt` |

## Category

**Datasets of Interest**

## Notes

⚠️ **Incomplete upload.** `Part 1.7z` (43.9 GB) failed to download during the batch run. Only `README.txt` is in S3. Re-upload required with sufficient disk space and a longer timeout.

## Status

- [ ] Files partially uploaded to S3 (Part 1.7z missing — 43.9 GB download failed)
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
