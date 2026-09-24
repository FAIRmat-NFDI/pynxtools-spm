# Dataset Report: Zenodo Record 18847316

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data for: Measurements of the size and physical properties of marine particles using atomic force microscopy (part 2) |
| **DOI**    | [10.5281/zenodo.18847316](https://doi.org/10.5281/zenodo.18847316) |
| **Date**   | 2026-03-03 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Yamada, Yosuke; Mochizuki, Toshiaki; Fukuda, Hideki; Nagata, Toshi et al. |
| **Tags**   | AFM, atomic force microscopy, marine particles, ocean, particle size, physical properties |

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

**S3 key pattern**: `zenodo/18847316/<filename>/<filename>`

Files uploaded flat ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/18847316/))

| file | experiment | S3 key |
|------|------------|--------|
| `210816 particle.7z` | AFM | `zenodo/18847316/210816 particle.7z/210816 particle.7z` |
| `210818 particle.7z` | AFM | `zenodo/18847316/210818 particle.7z/210818 particle.7z` |
| `210830 particle.7z` | AFM | `zenodo/18847316/210830 particle.7z/210830 particle.7z` |
| `210901 particle.7z` | AFM | `zenodo/18847316/210901 particle.7z/210901 particle.7z` |
| `210906 particle.7z` | AFM | `zenodo/18847316/210906 particle.7z/210906 particle.7z` |
| `210913 particle.7z` | AFM | `zenodo/18847316/210913 particle.7z/210913 particle.7z` |
| `210915 particle.7z` | AFM | `zenodo/18847316/210915 particle.7z/210915 particle.7z` |
| `210922 particle.7z` | AFM | `zenodo/18847316/210922 particle.7z/210922 particle.7z` |
| `210927 particle.7z` | AFM | `zenodo/18847316/210927 particle.7z/210927 particle.7z` |
| `210929 particle.7z` | AFM | `zenodo/18847316/210929 particle.7z/210929 particle.7z` |
| `211004 particle.7z` | AFM | `zenodo/18847316/211004 particle.7z/211004 particle.7z` |
| `211006 particle.7z` | AFM | `zenodo/18847316/211006 particle.7z/211006 particle.7z` |
| `README.txt`         | —   | `zenodo/18847316/README.txt/README.txt` |

## Category

**Datasets of Interest**

## Notes

⚠️ Archives are in `.7z` format. The batch upload script only extracts `.zip` files; `.7z` files were uploaded as-is. Each archive must be extracted locally to access the Bruker `.spm` files inside.

## Status

- [x] Files uploaded to S3 (as .7z archives, not extracted)
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
