# Dataset Report: Zenodo Record 19086147

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Supplementary data to publication https://doi.org/10.1002/anie.202424715 |
| **DOI**    | [10.5281/zenodo.19086147](https://doi.org/10.5281/zenodo.19086147) |
| **Url**    | [https://zenodo.org/records/19086147](https://zenodo.org/records/19086147) |
| **Date**   | 2026-03-18 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Moresco, Francesca |
| **Tags**   | STM, STS, scanning tunneling microscopy, NHC, thiophene, Au(111), chiral adsorption, molecular rotation |
| **Description** | Supplementary row STM data to the publication N. Khera, N. Sun, S. Park, P. Das, K. H. Au-Yeung, S. Sarkar, F. Plate, R. Robles, N. Lorente, F. S.-C. Lissel, F. Moresco, N-Heterocyclic Carbene vs. Thiophene – Chiral Adsorption and Unidirectional Rotation on Au(111), Angew. Chem. Int. Ed. 64, e202424715 (2025). <br><br> The data can be read and analyzed by a standard SPM data visualization and analysis software like Gwyddion. |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: STM/STS (Scanning Tunneling Microscopy/Spectroscopy)
- **Instrument**: Nanonis (`.dat` format — Nanonis `.dat` STM images and `.VERT` STS spectra)

## Dataset Contents

57 files: Nanonis `.dat` STM image files and `.VERT` STS spectroscopy files from STM experiments on NHC/thiophene molecules on Au(111). Supplementary data for Angew. Chem. publication on chiral adsorption and unidirectional rotation.

## File Format

- **Format**: Nanonis `.dat` (STM images), `.VERT` (STS spectra), `.jpeg` (reference images)
- **Parsability**: Nanonis `.dat` files parsable by `NanonisDatSTS` (for spectroscopy). `.VERT` files are Nanonis vertical spectroscopy — may need format investigation.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/19086147/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 57 files

**S3 key pattern**: `zenodo/19086147/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `A230904.105012.dat` | STS | 1 | `zenodo/19086147/A230904.105012.dat/` | — | — |
| `A230911.155843.dat` | STS | 2 | `zenodo/19086147/A230911.155843.dat/` | — | — |
| `A230911.161018.dat` | STS | 3 | `zenodo/19086147/A230911.161018.dat/` | — | — |
| `A230912.145204.dat` | STS | 4 | `zenodo/19086147/A230912.145204.dat/` | — | — |
| `A230912.145452.dat` | STS | 5 | `zenodo/19086147/A230912.145452.dat/` | — | — |
| `A230912.145708.dat` | STS | 6 | `zenodo/19086147/A230912.145708.dat/` | — | — |
| `A230912.145950.dat` | STS | 7 | `zenodo/19086147/A230912.145950.dat/` | — | — |
| `A230912.150618.dat` | STS | 8 | `zenodo/19086147/A230912.150618.dat/` | — | — |
| `A230912.151314.dat` | STS | 9 | `zenodo/19086147/A230912.151314.dat/` | — | — |
| `A230912.151609.dat` | STS | 10 | `zenodo/19086147/A230912.151609.dat/` | — | — |
| `A230912.152256.dat` | STS | 11 | `zenodo/19086147/A230912.152256.dat/` | — | — |
| `A230912.152834.dat` | STS | 12 | `zenodo/19086147/A230912.152834.dat/` | — | — |
| `A230913.142225.dat` | STS | 13 | `zenodo/19086147/A230913.142225.dat/` | — | — |
| `A230913.142717.dat` | STS | 14 | `zenodo/19086147/A230913.142717.dat/` | — | — |
| `A230913.143212.dat` | STS | 15 | `zenodo/19086147/A230913.143212.dat/` | — | — |
| `A230913.143745.dat` | STS | 16 | `zenodo/19086147/A230913.143745.dat/` | — | — |
| `A230913.144607.dat` | STS | 17 | `zenodo/19086147/A230913.144607.dat/` | — | — |
| `A230913.145056.dat` | STS | 18 | `zenodo/19086147/A230913.145056.dat/` | — | — |
| `A230913.145530.dat` | STS | 19 | `zenodo/19086147/A230913.145530.dat/` | — | — |
| `A230914.140344.dat` | STS | 20 | `zenodo/19086147/A230914.140344.dat/` | — | — |
| `A230918.114723.dat` | STS | 21 | `zenodo/19086147/A230918.114723.dat/` | — | — |
| `A230918.114915.dat` | STS | 22 | `zenodo/19086147/A230918.114915.dat/` | — | — |
| `A230918.115113.dat` | STS | 23 | `zenodo/19086147/A230918.115113.dat/` | — | — |
| `A230918.115237.dat` | STS | 24 | `zenodo/19086147/A230918.115237.dat/` | — | — |
| `A230918.115336.dat` | STS | 25 | `zenodo/19086147/A230918.115336.dat/` | — | — |
| `A230918.115432.dat` | STS | 26 | `zenodo/19086147/A230918.115432.dat/` | — | — |
| `A230918.115538.dat` | STS | 27 | `zenodo/19086147/A230918.115538.dat/` | — | — |
| `A230918.115711.dat` | STS | 28 | `zenodo/19086147/A230918.115711.dat/` | — | — |
| `A230918.115751.dat` | STS | 29 | `zenodo/19086147/A230918.115751.dat/` | — | — |
| `A230918.115845.dat` | STS | 30 | `zenodo/19086147/A230918.115845.dat/` | — | — |
| `A230918.124434.dat` | STS | 31 | `zenodo/19086147/A230918.124434.dat/` | — | — |
| `A241014.121242.dat` | STS | 32 | `zenodo/19086147/A241014.121242.dat/` | — | — |
| `A241105.160123.dat` | STS | 33 | `zenodo/19086147/A241105.160123.dat/` | — | — |
| `A241105.161247.dat` | STS | 34 | `zenodo/19086147/A241105.161247.dat/` | — | — |
| `A241105.162459.dat` | STS | 35 | `zenodo/19086147/A241105.162459.dat/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230912.145440.VERT/` | — | — |
| `*.jpeg` | STS | 1 | `zenodo/19086147/A230912.145655.VERT.jpeg/` | — | — |
| `*.jpeg` | STS | 1 | `zenodo/19086147/A230912.145942.VERT.jpeg/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230912.150234.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230912.151301.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230912.151555.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230912.152120.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230912.152644.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230913.142704.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230913.143144.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230913.143159.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.114823.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.115037.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.115212.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.115328.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.115421.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.115521.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.115657.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.115736.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A230918.115832.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A241105.161222.VERT/` | — | — |
| `*.vert` | STS | 1 | `zenodo/19086147/A241105.162355.VERT/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
