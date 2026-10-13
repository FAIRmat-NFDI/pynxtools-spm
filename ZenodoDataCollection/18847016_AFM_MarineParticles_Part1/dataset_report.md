# Dataset Report: Zenodo Record 18847016

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data for: Measurements of the size and physical properties of marine particles using atomic force microscopy (part 1) |
| **DOI**    | [10.5281/zenodo.18847016](https://doi.org/10.5281/zenodo.18847016) |
| **Url**    | [https://zenodo.org/records/18847016](https://zenodo.org/records/18847016) |
| **Date**   | 2026-03-03 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Yamada, Yosuke; Mochizuki, Toshiaki; Fukuda, Hideki et al. |
| **Tags**   | AFM, atomic force microscopy, marine particles, ocean, particle size, physical properties |
| **Description** | This dataset contains raw atomic force microscopy (AFM) image data of marine particle samples used in the associated manuscript submitted to Geophysical Research Letters. <br><br> The data are organized by measurement date using the folder naming convention YYMMDD_particle. Each subfolder corresponds to AFM measurements conducted on a specific date and contains original instrument files (.spm). Each file represents an individual AFM scan. <br><br> This record is Part 1 of a multi-part dataset. The complete dataset is distributed across multiple Zenodo records due to file size considerations. All quantitative results of particle properties reported in the associated manuscript were derived from these raw AFM image files. <br><br> Detailed file organization and additional information are provided in the accompanying README file. |
| **Experiment information related files** | `README.txt` |

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

**S3 key pattern**: `zenodo/18847016/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `README.txt` | AFM | 1 | `zenodo/18847016/README.txt/` |

## Notes

⚠️ **Incomplete upload.** `Part 1.7z` (43.9 GB) failed to download during the batch run. Only `README.txt` is in S3. Re-upload required with sufficient disk space and a longer timeout.

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
