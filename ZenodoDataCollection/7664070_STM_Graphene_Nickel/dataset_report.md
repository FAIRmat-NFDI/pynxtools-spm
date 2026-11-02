# Dataset Report: Zenodo Record 7664070

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset of Scanning Tunneling Microscopy (STM) images of graphene on nickel |
| **DOI**    | [10.5281/zenodo.7664070](https://doi.org/10.5281/zenodo.7664070) |
| **Url**    | [https://zenodo.org/records/7664070](https://zenodo.org/records/7664070) |
| **Date**   | 2021-12-24 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Tommaso Rodani; Elda Osmenaj; Alberto Cazzaniga et al. |
| **Tags**   | graphene, nickel, scanning tunneling microscopy, surface, chemical, vapour, deposition, doping, science |
| **Description** | STM images presented in the dataset were recorded by the STRAS research group using a Omicron Variable Temperature STM (VT-STM) microscope, in the TASC laboratory of the CNR-IOM in Trieste. |
| **Experiment information related files** | `metadata.csv`, `metadata.csv` |

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
**Total objects**: 24983 files

**S3 key pattern**: `zenodo/7664070/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `*.cs0` | STM | 29 | `zenodo/7664070/STM/` | — | — |
| `*.par` | STM | 7287 | `zenodo/7664070/STM/` | — | — |
| `*.tb0` | STM | 7287 | `zenodo/7664070/STM/` | — | — |
| `*.tb1` | STM | 2347 | `zenodo/7664070/STM/` | — | — |
| `*.tf0` | STM | 7287 | `zenodo/7664070/STM/` | — | — |
| `*.tf1` | STM | 741 | `zenodo/7664070/STM/` | — | — |
| `*.txt` | STM | 1 | `zenodo/7664070/STM/` | — | — |
| `*.txt` | STM | 1 | `zenodo/7664070/md5sum.txt/` | — | — |
| `*.json` | STM | 1 | `zenodo/7664070/provenance.json/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `metadata.csv` | STM | 1 | `zenodo/7664070/STM/metadata.csv/` |
| `metadata.csv` | STM | 2 | `zenodo/7664070/metadata.csv/` |

## Category

**Unknown/Unsupported Format**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
