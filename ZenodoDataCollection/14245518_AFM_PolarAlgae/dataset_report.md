# Dataset Report: Zenodo Record 14245518

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Heating by Dissipation of Energy from Absorbed Light: Molecular Mechanisms Underlying the Survival Strategy of Polar Algae |
| **DOI**    | [10.5281/zenodo.14245518](https://doi.org/10.5281/zenodo.14245518) |
| **Url**    | [https://zenodo.org/records/14245518](https://zenodo.org/records/14245518) |
| **Date**   | 2024-11-29 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Zubik-Duda, Monika; Grudzinski, Wojciech; Luchowski, Rafal et al. |
| **Tags**   | AFM, fluorescence microscopy, FLIM, HPLC, Raman, polar algae, Pediastrum orientale |
| **Description** | The original data, which served as the source material for the scientific article on the polar alga Pediastrum orientale, collected from Reindeer Lake on Spitsbergen. Consists of datasets obtained using various techniques: fluorescence microscopy (microscope_fluo), fluorescence lifetime microscopy (FLIM), high-performance liquid chromatography (HPLC), atomic force microscopy (AFM), Raman microspectroscopy (RAMAN), fluorescence lifitime spectroscopy (lifetime) and fluorescence spectroscopy (Fluo). <br><br> HPLC - Nexera LC-40 (Shimadzu, Japan) FLIM - OLYMPUS IX71 confocal microscope MicroTime 200 with SymPhoTime 64 software package (PicoQuant, GmbH, Germany) RAMAN - inVia Reflex confocal Raman microscope with the WiRE 5.5 software package (Renishaw, UK) AFM - JPK Nanowizard 3 system with JPKSMP data processing software (Bruker, USA) Lifetime - FluoTime 300 spectrometer with FluoFit Pro v 4.5.3.0 (PicoQuant, Germany) Microscope_Fluo - Zeiss LSM980 confocal microscope with Airy2 and Elyra7 detectors and ZEN 3.1 software (Zeiss, Germany) Fluo - OLYMPUS IX71 confocal microscope MicroTime 200 system with the spectrograph SR-163 and the Newton 970 EMCCD camera (Andor Technology) |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) + FLIM + Raman + HPLC + Fluorescence
- **Instrument**: JPK NanoWizard 3 (Bruker) with JPKSPM data processing software

## Dataset Contents

Multi-technique dataset for polar alga *Pediastrum orientale* collected from Reindeer Lake, Spitsbergen. AFM data is in `_AFM.ZIP` (JPK/Bruker format). Also contains FLIM (7 GB, FLIM.ZIP — download failed), Raman (4.5 GB, RAMAN.ZIP), HPLC, Microscope_Fluo, and Fluo data. 115 objects in S3.

## File Format

- **Format**: `.jpk` (JPK/Bruker NanoWizard proprietary). **Note:** `_AFM.ZIP` was uploaded as-is (not extracted) because the script only extracts lowercase `.zip`; `RAMAN.ZIP`, `HPLC.ZIP` similarly. `FLIM.ZIP` (7 GB) failed to download — not in S3.
- **Parsability**: Not supported. `.jpk` format (NanoWizard 3) is not in the dispatch table. Different from the NanoRacer `.jpk` in record 19254504 but same general format family.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14245518/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 115 files

**S3 key pattern**: `zenodo/14245518/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `KitonRed_11_5C_2skladowe.dat` | AFM | 1 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_11_5C_2skladowe.dat/` | — | — |
| `KitonRed_15_5C_2skladowe.dat` | AFM | 2 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_15_5C_2skladowe.dat/` | — | — |
| `KitonRed_20C_2skladowe.dat` | AFM | 3 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_20C_2skladowe.dat/` | — | — |
| `KitonRed_20C_B_2skladowe.dat` | AFM | 4 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_20C_B_2skladowe.dat/` | — | — |
| `KitonRed_23_8C_2skladowe.dat` | AFM | 5 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_23_8C_2skladowe.dat/` | — | — |
| `KitonRed_24_5C_2skladowe.dat` | AFM | 6 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_24_5C_2skladowe.dat/` | — | — |
| `KitonRed_25_2C_2skladowe.dat` | AFM | 7 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_25_2C_2skladowe.dat/` | — | — |
| `KitonRed_27_7C_2skladowe.dat` | AFM | 8 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_27_7C_2skladowe.dat/` | — | — |
| `KitonRed_29_8C_2skladowe.dat` | AFM | 9 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_29_8C_2skladowe.dat/` | — | — |
| `KitonRed_30C_2skladowe.dat` | AFM | 10 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_30C_2skladowe.dat/` | — | — |
| `KitonRed_35C_2skladowe.dat` | AFM | 11 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_35C_2skladowe.dat/` | — | — |
| `KitonRed_40C_2skladowe.dat` | AFM | 12 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_40C_2skladowe.dat/` | — | — |
| `KitonRed_45C_2skladowe.dat` | AFM | 13 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_45C_2skladowe.dat/` | — | — |
| `KitonRed_50C_2skladowe.dat` | AFM | 14 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_50C_2skladowe.dat/` | — | — |
| `KitonRed_55_5C_2skladowe.dat` | AFM | 15 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_55_5C_2skladowe.dat/` | — | — |
| `KitonRed_56C_2skladowe.dat` | AFM | 16 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_56C_2skladowe.dat/` | — | — |
| `KitonRed_65C_2skladowe.dat` | AFM | 17 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_65C_2skladowe.dat/` | — | — |
| `KitonRed_65_1C_2skladowe.dat` | AFM | 18 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_65_1C_2skladowe.dat/` | — | — |
| `KitonRed_70C_2skladowe.dat` | AFM | 19 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_70C_2skladowe.dat/` | — | — |
| `KitonRed_75C_2skladowe.dat` | AFM | 20 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_75C_2skladowe.dat/` | — | — |
| `KitonRed_7_7C_2skladowe.dat` | AFM | 21 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_7_7C_2skladowe.dat/` | — | — |
| `KitonRed_80C_2skladowe.dat` | AFM | 22 | `zenodo/14245518/Lifetime/2024-04-25/temp/KitonRed_80C_2skladowe.dat/` | — | — |
| `*.asc` | AFM | 41 | `zenodo/14245518/Fluo/` | — | — |
| `*.sif` | AFM | 43 | `zenodo/14245518/Fluo/` | — | — |
| `*.zip` | AFM | 1 | `zenodo/14245518/HPLC.ZIP/` | — | — |
| `*.etc` | AFM | 2 | `zenodo/14245518/Lifetime/` | — | — |
| `*.etf` | AFM | 1 | `zenodo/14245518/Lifetime/` | — | — |
| `*.etw` | AFM | 1 | `zenodo/14245518/Lifetime/` | — | — |
| `*.czi` | AFM | 2 | `zenodo/14245518/Microscope_Fluo/` | — | — |
| `*.zip` | RAMAN | 1 | `zenodo/14245518/RAMAN.ZIP/` | — | — |
| `*.zip` | AFM | 1 | `zenodo/14245518/_AFM.ZIP/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Notes

⚠️ `FLIM.ZIP` (7 GB) failed to download — not present in S3. `_AFM.ZIP`, `HPLC.ZIP`, `RAMAN.ZIP` were uploaded as raw zip files (not extracted) due to uppercase `.ZIP` extension not matching the unzip condition in the batch script.

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
