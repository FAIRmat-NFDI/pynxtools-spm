# Dataset Report: Zenodo Record 18847316

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data for: Measurements of the size and physical properties of marine particles using atomic force microscopy (part 2) |
| **DOI**    | [10.5281/zenodo.18847316](https://doi.org/10.5281/zenodo.18847316) |
| **Url**    | [https://zenodo.org/records/18847316](https://zenodo.org/records/18847316) |
| **Date**   | 2026-03-03 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Yamada, Yosuke; Mochizuki, Toshiaki; Fukuda, Hideki et al. |
| **Tags**   | AFM, atomic force microscopy, marine particles, ocean, particle size, physical properties |
| **Description** | This dataset contains raw atomic force microscopy (AFM) image data of marine particle samples used in the associated manuscript submitted to Geophysical Research Letters. <br><br> The data are organized by measurement date using the folder naming convention YYMMDD_particle. Each subfolder corresponds to AFM measurements conducted on a specific date and contains original instrument files (.spm). Each file represents an individual AFM scan. <br><br> This record is Part 2 of a multi-part dataset. The complete dataset is distributed across multiple Zenodo records due to file size considerations. All quantitative results of particle properties reported in the associated manuscript were derived from these raw AFM image files. <br><br> Detailed file organization and additional information are provided in the accompanying README file. |
| **Experiment information related files** | `README.txt` |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — marine particle characterisation
- **Instrument**: Bruker AFM (NanoScope `.spm` format, organised by date in YYMMDD_particle folders)

## Dataset Contents

Part 2 of a multi-part marine particle AFM dataset. 13 `.7z` archives (one per measurement date, ~3 GB each, total ~40 GB) plus README. Each archive contains Bruker `.spm` AFM files in date-labelled folders. Archives were uploaded as-is (not extracted — `.7z` is not handled by the batch script).

## File Format

- **Format**: Bruker `.spm` (inside `.7z` archives — not extracted)
- **Parsability**: Parsable by `BrukerSpmAFM` once extracted from archives. The `.7z` archives must be extracted locally before parsing.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/18847316/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 13 files

**S3 key pattern**: `zenodo/18847316/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `*.7z` | AFM | 1 | `zenodo/18847316/210816 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210818 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210830 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210901 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210906 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210913 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210915 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210922 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210927 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/210929 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/211004 particle.7z/` | — | — |
| `*.7z` | AFM | 1 | `zenodo/18847316/211006 particle.7z/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `README.txt` | AFM | 1 | `zenodo/18847316/README.txt/` |

## Notes

⚠️ Archives are in `.7z` format. The batch upload script only extracts `.zip` files; `.7z` files were uploaded as-is. Each archive must be extracted locally to access the Bruker `.spm` files inside.

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
