# Dataset Report: Zenodo Record 19087372

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Supplementary data to publication https://pubs.acs.org/doi/10.1021/acsnano.5c17283 |
| **DOI**    | [10.5281/zenodo.19087372](https://doi.org/10.5281/zenodo.19087372) |
| **Url**    | [https://zenodo.org/records/19087372](https://zenodo.org/records/19087372) |
| **Date**   | 2026-03-18 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Moresco, Francesca |
| **Tags**   | STM, STS, scanning tunneling microscopy, subphthalocyanine, single-molecule machines, Au(111) |
| **Description** | Supplementary row STM data to the publication Subphthalocyanine Platform for Single-Molecule Machines on Surface: Ligand-Directed Adsorption on Au(111) by <br><br> Franz Plate, Soyoung Park, Ebru Cihan, Natasha Khera, Ningwei Sun, Pranjit Das, Olga Guskova, Dmitry A. Ryndyk, Franziska Lissel, and Francesca Moresco <br><br> DOI: 10.1021/acsnano.5c17283 <br><br> The data can be read and analyzed by a standard SPM data visualization and analysis software like Gwyddion. |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: STM/STS (Scanning Tunneling Microscopy/Spectroscopy)
- **Instrument**: Nanonis (`.dat` format — STM images and STS spectroscopy)

## Dataset Contents

78 Nanonis `.dat` STM/STS files (prefixed A or B) for a study of subphthalocyanine single-molecule machines on Au(111). Files span multiple sessions from 2024-03 to 2025-02. Supplementary to ACS Nano publication.

## File Format

- **Format**: **`Paramco32`** STM images (NOT Nanonis). Despite the `.dat` extension, all 78
  files have the header `[Paramco32]` (a German STM control-software format) and store 2D STM
  scan images (`Num.X`/`Num.Y = 256`). This is **not** the Nanonis `.dat` spectroscopy format
  (which begins `Experiment<TAB>bias spectroscopy`).
- **Parsability**: **Not supported** — `Paramco32` is out of scope for the current
  `pynxtools-spm` parsers (like `.jpk`). `NanonisDatSTS` only handles genuine Nanonis STS `.dat`.
  `PS = —` (n/a) for all `.dat`; not attempted.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/19087372/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 78 files

**S3 key pattern**: `zenodo/19087372/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `A240328.114415.dat` | STS | 1 | `zenodo/19087372/A240328.114415.dat/` | — | — |
| `A240408.100048.dat` | STS | 2 | `zenodo/19087372/A240408.100048.dat/` | — | — |
| `A240408.161236.dat` | STS | 3 | `zenodo/19087372/A240408.161236.dat/` | — | — |
| `A240408.161506.dat` | STS | 4 | `zenodo/19087372/A240408.161506.dat/` | — | — |
| `A240408.161814.dat` | STS | 5 | `zenodo/19087372/A240408.161814.dat/` | — | — |
| `A240408.162055.dat` | STS | 6 | `zenodo/19087372/A240408.162055.dat/` | — | — |
| `A240408.162402.dat` | STS | 7 | `zenodo/19087372/A240408.162402.dat/` | — | — |
| `A240408.162608.dat` | STS | 8 | `zenodo/19087372/A240408.162608.dat/` | — | — |
| `A240408.163333.dat` | STS | 9 | `zenodo/19087372/A240408.163333.dat/` | — | — |
| `A240408.163521.dat` | STS | 10 | `zenodo/19087372/A240408.163521.dat/` | — | — |
| `A240409.123557.dat` | STS | 11 | `zenodo/19087372/A240409.123557.dat/` | — | — |
| `A240409.123828.dat` | STS | 12 | `zenodo/19087372/A240409.123828.dat/` | — | — |
| `A240411.131626.dat` | STS | 13 | `zenodo/19087372/A240411.131626.dat/` | — | — |
| `A240411.132935.dat` | STS | 14 | `zenodo/19087372/A240411.132935.dat/` | — | — |
| `A240419.142519.dat` | STS | 15 | `zenodo/19087372/A240419.142519.dat/` | — | — |
| `A240424.094722.dat` | STS | 16 | `zenodo/19087372/A240424.094722.dat/` | — | — |
| `A240424.095032.dat` | STS | 17 | `zenodo/19087372/A240424.095032.dat/` | — | — |
| `A240426.122915.dat` | STS | 18 | `zenodo/19087372/A240426.122915.dat/` | — | — |
| `A240722.104416.dat` | STS | 19 | `zenodo/19087372/A240722.104416.dat/` | — | — |
| `A240722.105730.dat` | STS | 20 | `zenodo/19087372/A240722.105730.dat/` | — | — |
| `A240722.134136.dat` | STS | 21 | `zenodo/19087372/A240722.134136.dat/` | — | — |
| `A240729.154544.dat` | STS | 22 | `zenodo/19087372/A240729.154544.dat/` | — | — |
| `A240729.154920.dat` | STS | 23 | `zenodo/19087372/A240729.154920.dat/` | — | — |
| `A240729.155120.dat` | STS | 24 | `zenodo/19087372/A240729.155120.dat/` | — | — |
| `A240729.155505.dat` | STS | 25 | `zenodo/19087372/A240729.155505.dat/` | — | — |
| `A240729.155833.dat` | STS | 26 | `zenodo/19087372/A240729.155833.dat/` | — | — |
| `A240729.160108.dat` | STS | 27 | `zenodo/19087372/A240729.160108.dat/` | — | — |
| `A240729.160600.dat` | STS | 28 | `zenodo/19087372/A240729.160600.dat/` | — | — |
| `A240729.160813.dat` | STS | 29 | `zenodo/19087372/A240729.160813.dat/` | — | — |
| `A240729.161404.dat` | STS | 30 | `zenodo/19087372/A240729.161404.dat/` | — | — |
| `A240729.161817.dat` | STS | 31 | `zenodo/19087372/A240729.161817.dat/` | — | — |
| `A240802.125932.dat` | STS | 32 | `zenodo/19087372/A240802.125932.dat/` | — | — |
| `A240802.131151.dat` | STS | 33 | `zenodo/19087372/A240802.131151.dat/` | — | — |
| `A240802.133241.dat` | STS | 34 | `zenodo/19087372/A240802.133241.dat/` | — | — |
| `A240802.134637.dat` | STS | 35 | `zenodo/19087372/A240802.134637.dat/` | — | — |
| `A240802.135926.dat` | STS | 36 | `zenodo/19087372/A240802.135926.dat/` | — | — |
| `A240802.150504.dat` | STS | 37 | `zenodo/19087372/A240802.150504.dat/` | — | — |
| `A240802.151316.dat` | STS | 38 | `zenodo/19087372/A240802.151316.dat/` | — | — |
| `A240802.151740.dat` | STS | 39 | `zenodo/19087372/A240802.151740.dat/` | — | — |
| `A240802.152028.dat` | STS | 40 | `zenodo/19087372/A240802.152028.dat/` | — | — |
| `A240802.152813.dat` | STS | 41 | `zenodo/19087372/A240802.152813.dat/` | — | — |
| `A240802.153335.dat` | STS | 42 | `zenodo/19087372/A240802.153335.dat/` | — | — |
| `A240802.153736.dat` | STS | 43 | `zenodo/19087372/A240802.153736.dat/` | — | — |
| `A240802.154152.dat` | STS | 44 | `zenodo/19087372/A240802.154152.dat/` | — | — |
| `A240802.154640.dat` | STS | 45 | `zenodo/19087372/A240802.154640.dat/` | — | — |
| `A240802.154749.dat` | STS | 46 | `zenodo/19087372/A240802.154749.dat/` | — | — |
| `A240802.154902.dat` | STS | 47 | `zenodo/19087372/A240802.154902.dat/` | — | — |
| `A240802.155023.dat` | STS | 48 | `zenodo/19087372/A240802.155023.dat/` | — | — |
| `A240802.155129.dat` | STS | 49 | `zenodo/19087372/A240802.155129.dat/` | — | — |
| `A240802.155740.dat` | STS | 50 | `zenodo/19087372/A240802.155740.dat/` | — | — |
| `A240802.160356.dat` | STS | 51 | `zenodo/19087372/A240802.160356.dat/` | — | — |
| `A240812.123508.dat` | STS | 52 | `zenodo/19087372/A240812.123508.dat/` | — | — |
| `A241128.100612.dat` | STS | 53 | `zenodo/19087372/A241128.100612.dat/` | — | — |
| `B241125.132144.dat` | STS | 54 | `zenodo/19087372/B241125.132144.dat/` | — | — |
| `B241127.154838.dat` | STS | 55 | `zenodo/19087372/B241127.154838.dat/` | — | — |
| `B250113.105108.dat` | STS | 56 | `zenodo/19087372/B250113.105108.dat/` | — | — |
| `B250113.150438.dat` | STS | 57 | `zenodo/19087372/B250113.150438.dat/` | — | — |
| `B250117.101724.dat` | STS | 58 | `zenodo/19087372/B250117.101724.dat/` | — | — |
| `B250204.113748.dat` | STS | 59 | `zenodo/19087372/B250204.113748.dat/` | — | — |
| `B250204.135625.dat` | STS | 60 | `zenodo/19087372/B250204.135625.dat/` | — | — |
| `B250204.150638.dat` | STS | 61 | `zenodo/19087372/B250204.150638.dat/` | — | — |
| `B250205.095632.dat` | STS | 62 | `zenodo/19087372/B250205.095632.dat/` | — | — |
| `B250205.110626.dat` | STS | 63 | `zenodo/19087372/B250205.110626.dat/` | — | — |
| `B250205.121510.dat` | STS | 64 | `zenodo/19087372/B250205.121510.dat/` | — | — |
| `B250205.132407.dat` | STS | 65 | `zenodo/19087372/B250205.132407.dat/` | — | — |
| `B250205.143732.dat` | STS | 66 | `zenodo/19087372/B250205.143732.dat/` | — | — |
| `B250205.144407.dat` | STS | 67 | `zenodo/19087372/B250205.144407.dat/` | — | — |
| `B250205.150250.dat` | STS | 68 | `zenodo/19087372/B250205.150250.dat/` | — | — |
| `B250205.153233.dat` | STS | 69 | `zenodo/19087372/B250205.153233.dat/` | — | — |
| `B250205.170423.dat` | STS | 70 | `zenodo/19087372/B250205.170423.dat/` | — | — |
| `B250206.094026.dat` | STS | 71 | `zenodo/19087372/B250206.094026.dat/` | — | — |
| `B250206.104940.dat` | STS | 72 | `zenodo/19087372/B250206.104940.dat/` | — | — |
| `B250206.115601.dat` | STS | 73 | `zenodo/19087372/B250206.115601.dat/` | — | — |
| `B250207.084826.dat` | STS | 74 | `zenodo/19087372/B250207.084826.dat/` | — | — |
| `B250207.091033.dat` | STS | 75 | `zenodo/19087372/B250207.091033.dat/` | — | — |
| `B250207.093342.dat` | STS | 76 | `zenodo/19087372/B250207.093342.dat/` | — | — |
| `B250207.095950.dat` | STS | 77 | `zenodo/19087372/B250207.095950.dat/` | — | — |
| `B250207.100258.dat` | STS | 78 | `zenodo/19087372/B250207.100258.dat/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
