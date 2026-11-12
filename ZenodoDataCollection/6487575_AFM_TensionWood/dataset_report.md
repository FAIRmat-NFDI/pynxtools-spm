# Dataset Report: Zenodo Record 6487575

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Mechanical characterisation of the developing cell wall layers of tension wood fibres by Atomic Force Microscopy |
| **DOI**    | [10.5281/zenodo.6487575](https://doi.org/10.5281/zenodo.6487575) |
| **Url**    | [https://zenodo.org/records/6487575](https://zenodo.org/records/6487575) |
| **Date**   | 2022-01-26 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Arnould, Olivier; Capron, Marie; Ramonda, Michel et al. |
| **Tags**   | Atomic Force Microscopy, Cell wall, G-layer, Indentation modulus, Maturation, Poplar, Stiffening, Tension wood, Thickening |
| **Description** | This dataset corresponds to the Arnould et al. (2022) paper (available at https://www.biorxiv.org/content/10.1101/2021.09.23.461481v1.full) on the mechanical characterization of developing cell wall layers of tension wood fibers by Atomic Force Microscopy. It contains all raw AFM files (Bruker format .spm, readable by the free software Gwyddion for example) corresponding to mechanical measurements of poplar reaction wood cells (clone 717-1B4) along 3 radial lines/rows, starting from the cambium. Each cell is identified by its "macroscopic" distance from the cambium (value in µm in the name of each file corresponding to the displacement of the sample in the AFM) which was corrected after using the AFM optical image captures. Some files, with a -z extension after the distance value, correspond to a zoom into the cell wall. The data also contain measurements made for mechanical calibration on epoxy embedded Kevlar fibers, controlled measurements in the embedding resin between each radial line and measurements in normal wood cells. Two csv files containing final data extracted from AFM measurements that give the value of the indentation modulus and the relative thickness to cell diameter ratio (by AFM and by phase contrast optical microscopy) in each cell wall layer as a function of cambium distance are also provided. |
| **Experiment information related files** | `readme.rtf` |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — mechanical indentation mapping
- **Instrument**: Bruker AFM (NanoScope `.spm` format)

## Dataset Contents

195 objects: Bruker `.spm` AFM files of poplar tension wood cell walls at varying cambium distances (extracted from `AFM files.zip`, 309 MB), optical microscopy images (`Optical files.zip`, 320 MB), and two CSV files with extracted modulus and thickness data.

## File Format

- **Format**: Bruker `.spm` (AFM indentation maps), `.csv`, `.rtf`
- **Parsability**: Parsable by `BrukerSpmAFM`. Mechanical channels (indentation modulus) may require extended channel support.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/6487575/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 195 files

**S3 key pattern**: `zenodo/6487575/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `714-1B4-resine3.0_00001.spm` | AFM | 1 | `zenodo/6487575/AFM files/embedding resin outside/714-1B4-resine3.0_00001.spm/` | True | True |
| `717-1B4-resine1.0_00001.spm` | AFM | 2 | `zenodo/6487575/AFM files/embedding resin outside/717-1B4-resine1.0_00001.spm/` | True | True |
| `717-1B4-resine1.0_00002.spm` | AFM | 3 | `zenodo/6487575/AFM files/embedding resin outside/717-1B4-resine1.0_00002.spm/` | False | — |
| `717-1B4-resine2.0_00002.spm` | AFM | 4 | `zenodo/6487575/AFM files/embedding resin outside/717-1B4-resine2.0_00002.spm/` | True | True |
| `fib-kev.0_00000.spm` | AFM | 5 | `zenodo/6487575/AFM files/kevlar fibre calibration/fib-kev.0_00000.spm/` | True | True |
| `fib-kev2.0_00001.spm` | AFM | 6 | `zenodo/6487575/AFM files/kevlar fibre calibration/fib-kev2.0_00001.spm/` | True | True |
| `fib-kev3.0_00002.spm` | AFM | 7 | `zenodo/6487575/AFM files/kevlar fibre calibration/fib-kev3.0_00002.spm/` | True | True |
| `717-1B4-BN2.0_00001.spm` | AFM | 8 | `zenodo/6487575/AFM files/normal wood/717-1B4-BN2.0_00001.spm/` | True | True |
| `717-1B4-BN3.0_00002.spm` | AFM | 9 | `zenodo/6487575/AFM files/normal wood/717-1B4-BN3.0_00002.spm/` | False | — |
| `717-1B4-BN9.0_00001.spm` | AFM | 10 | `zenodo/6487575/AFM files/normal wood/717-1B4-BN9.0_00001.spm/` | True | True |
| `717-1B4-1_0.0_00001.spm` | AFM | 11 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_0.0_00001.spm/` | False | — |
| `717-1B4-1_0Bis.0_00001.spm` | AFM | 12 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_0Bis.0_00001.spm/` | True | True |
| `717-1B4-1_0Tier.0_00002.spm` | AFM | 13 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_0Tier.0_00002.spm/` | False | — |
| `717-1B4-1_1000um.0_00000.spm` | AFM | 14 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_1000um.0_00000.spm/` | True | True |
| `717-1B4-1_1000um.0_00003.spm` | AFM | 15 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_1000um.0_00003.spm/` | True | True |
| `717-1B4-1_1100um.0_00001.spm` | AFM | 16 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_1100um.0_00001.spm/` | True | True |
| `717-1B4-1_1200um.0_00001.spm` | AFM | 17 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_1200um.0_00001.spm/` | True | True |
| `717-1B4-1_120um.0_00001.spm` | AFM | 18 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_120um.0_00001.spm/` | True | True |
| `717-1B4-1_1300um-z.0_00002.spm` | AFM | 19 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_1300um-z.0_00002.spm/` | True | True |
| `717-1B4-1_1300um.0_00001.spm` | AFM | 20 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_1300um.0_00001.spm/` | True | True |
| `717-1B4-1_1400um.0_00001.spm` | AFM | 21 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_1400um.0_00001.spm/` | True | True |
| `717-1B4-1_150um.0_00001.spm` | AFM | 22 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_150um.0_00001.spm/` | False | — |
| `717-1B4-1_1700um.0_00001.spm` | AFM | 23 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_1700um.0_00001.spm/` | True | True |
| `717-1B4-1_200um.0_00001.spm` | AFM | 24 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_200um.0_00001.spm/` | True | True |
| `717-1B4-1_210um.0_00002.spm` | AFM | 25 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_210um.0_00002.spm/` | False | — |
| `717-1B4-1_230um.0_00001.spm` | AFM | 26 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_230um.0_00001.spm/` | False | — |
| `717-1B4-1_260um.0_00001.spm` | AFM | 27 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_260um.0_00001.spm/` | True | True |
| `717-1B4-1_30um.0_00000.spm` | AFM | 28 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_30um.0_00000.spm/` | False | — |
| `717-1B4-1_320um-z.0_00001.spm` | AFM | 29 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_320um-z.0_00001.spm/` | True | True |
| `717-1B4-1_320um-z.0_00002.spm` | AFM | 30 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_320um-z.0_00002.spm/` | True | True |
| `717-1B4-1_320um.0_00001.spm` | AFM | 31 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_320um.0_00001.spm/` | True | True |
| `717-1B4-1_380um-z.0_00002.spm` | AFM | 32 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_380um-z.0_00002.spm/` | True | True |
| `717-1B4-1_380um.0_00001.spm` | AFM | 33 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_380um.0_00001.spm/` | True | True |
| `717-1B4-1_440um.0_00001.spm` | AFM | 34 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_440um.0_00001.spm/` | True | True |
| `717-1B4-1_500um.0_00001.spm` | AFM | 35 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_500um.0_00001.spm/` | True | True |
| `717-1B4-1_600um.0_00001.spm` | AFM | 36 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_600um.0_00001.spm/` | True | True |
| `717-1B4-1_60um.0_00000.spm` | AFM | 37 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_60um.0_00000.spm/` | True | True |
| `717-1B4-1_700um.0_00001.spm` | AFM | 38 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_700um.0_00001.spm/` | True | True |
| `717-1B4-1_800um-z.0_00001.spm` | AFM | 39 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_800um-z.0_00001.spm/` | True | True |
| `717-1B4-1_800um.0_00001.spm` | AFM | 40 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_800um.0_00001.spm/` | True | True |
| `717-1B4-1_900um.0_00001.spm` | AFM | 41 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_900um.0_00001.spm/` | True | True |
| `717-1B4-1_90um.0_00001.spm` | AFM | 42 | `zenodo/6487575/AFM files/radial ligne #1/717-1B4-1_90um.0_00001.spm/` | False | — |
| `717-1B4-0Fin.0_00001.spm` | AFM | 43 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-0Fin.0_00001.spm/` | True | True |
| `717-1B4-2_0.0_00001.spm` | AFM | 44 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_0.0_00001.spm/` | True | True |
| `717-1B4-2_0Bis.0_00001.spm` | AFM | 45 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_0Bis.0_00001.spm/` | True | True |
| `717-1B4-2_1000.0_00001.spm` | AFM | 46 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_1000.0_00001.spm/` | True | True |
| `717-1B4-2_1100.0_00001.spm` | AFM | 47 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_1100.0_00001.spm/` | True | True |
| `717-1B4-2_1150.0_00001.spm` | AFM | 48 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_1150.0_00001.spm/` | True | True |
| `717-1B4-2_120.0_00001.spm` | AFM | 49 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_120.0_00001.spm/` | True | True |
| `717-1B4-2_1200.0_00001.spm` | AFM | 50 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_1200.0_00001.spm/` | True | True |
| `717-1B4-2_1300.0_00001.spm` | AFM | 51 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_1300.0_00001.spm/` | True | True |
| `717-1B4-2_1400.0_00001.spm` | AFM | 52 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_1400.0_00001.spm/` | True | True |
| `717-1B4-2_1700.0_00001.spm` | AFM | 53 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_1700.0_00001.spm/` | True | True |
| `717-1B4-2_180.0_00001.spm` | AFM | 54 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_180.0_00001.spm/` | True | True |
| `717-1B4-2_200.0_00001.spm` | AFM | 55 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_200.0_00001.spm/` | True | True |
| `717-1B4-2_230.0_00001.spm` | AFM | 56 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_230.0_00001.spm/` | True | True |
| `717-1B4-2_260.0_00001.spm` | AFM | 57 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_260.0_00001.spm/` | True | True |
| `717-1B4-2_30.0_00001.spm` | AFM | 58 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_30.0_00001.spm/` | True | True |
| `717-1B4-2_320.0_00001.spm` | AFM | 59 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_320.0_00001.spm/` | True | True |
| `717-1B4-2_380.0_00001.spm` | AFM | 60 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_380.0_00001.spm/` | True | True |
| `717-1B4-2_440.0_00001.spm` | AFM | 61 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_440.0_00001.spm/` | True | True |
| `717-1B4-2_500.0_00001.spm` | AFM | 62 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_500.0_00001.spm/` | True | True |
| `717-1B4-2_60.0_00001.spm` | AFM | 63 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_60.0_00001.spm/` | True | True |
| `717-1B4-2_600.0_00001.spm` | AFM | 64 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_600.0_00001.spm/` | True | True |
| `717-1B4-2_700.0_00001.spm` | AFM | 65 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_700.0_00001.spm/` | True | True |
| `717-1B4-2_800.0_00001.spm` | AFM | 66 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_800.0_00001.spm/` | True | True |
| `717-1B4-2_90.0_00001.spm` | AFM | 67 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_90.0_00001.spm/` | True | True |
| `717-1B4-2_900.0_00001.spm` | AFM | 68 | `zenodo/6487575/AFM files/radial ligne #2/717-1B4-2_900.0_00001.spm/` | True | True |
| `714-1B4-3_0Bis.0_00001.spm` | AFM | 69 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_0Bis.0_00001.spm/` | True | True |
| `714-1B4-3_1000um.0_00001.spm` | AFM | 70 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_1000um.0_00001.spm/` | True | True |
| `714-1B4-3_1200um.0_00001.spm` | AFM | 71 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_1200um.0_00001.spm/` | True | True |
| `714-1B4-3_1400um.0_00001.spm` | AFM | 72 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_1400um.0_00001.spm/` | True | True |
| `714-1B4-3_1700um.0_00002.spm` | AFM | 73 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_1700um.0_00002.spm/` | True | True |
| `714-1B4-3_300um.0_00001.spm` | AFM | 74 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_300um.0_00001.spm/` | True | True |
| `714-1B4-3_400um.0_00001.spm` | AFM | 75 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_400um.0_00001.spm/` | True | True |
| `714-1B4-3_500um.0_00001.spm` | AFM | 76 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_500um.0_00001.spm/` | True | True |
| `714-1B4-3_600um.0_00001.spm` | AFM | 77 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_600um.0_00001.spm/` | True | True |
| `714-1B4-3_800um.0_00001.spm` | AFM | 78 | `zenodo/6487575/AFM files/radial ligne #3/714-1B4-3_800um.0_00001.spm/` | True | True |
| `717-1B4-3_0.0_00001.spm` | AFM | 79 | `zenodo/6487575/AFM files/radial ligne #3/717-1B4-3_0.0_00001.spm/` | True | True |
| `717-1B4-3_100um.0_00001.spm` | AFM | 80 | `zenodo/6487575/AFM files/radial ligne #3/717-1B4-3_100um.0_00001.spm/` | True | True |
| `717-1B4-3_200um.0_00001.spm` | AFM | 81 | `zenodo/6487575/AFM files/radial ligne #3/717-1B4-3_200um.0_00001.spm/` | True | True |
| `*.tif` | AFM | 67 | `zenodo/6487575/AFM files/` | — | — |
| `*.tif` | AFM | 44 | `zenodo/6487575/Optical files/` | — | — |
| `*.csv` | AFM | 1 | `zenodo/6487575/modulus.csv/` | — | — |
| `*.csv` | AFM | 1 | `zenodo/6487575/thickness.csv/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `readme.rtf` | AFM | 1 | `zenodo/6487575/readme.rtf/` |

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-07 with `pynxtools-spm` 0.2.5 / `pySPM` 0.6.3. **72 of 81 `.spm` files
converted, validated, and uploaded (`PS = True`, `Uploaded = True`); the 9 ISO/TC 201 files
are unsupported (`PS = False`).** For each of the 72 files, `eln_data.yaml`, `config.json`, and
`<stem>.nxs` were uploaded into the file's own S3 folder. See `conversion.log` for the full run.

Fixes required to convert these files (NanoScope firmware `0x09200201` ≈ v9.2, PeakForce QNM),
all landed and covered by tests:

- **Scan origin (formatter).** `BrukerSpmAFM.construct_region_region_grp` now uses
  `start = position` when `X_Position`/`Y_Position` exists, else `start = Stage_X/Y + offset`,
  and strips embedded units from string values like `'-3750 nm'` via `pint`. (These v9.2 files
  lack an absolute position and store unit-bearing offsets.)
- **NXdata axis shapes (formatter).** Each NXdata axis is sized from its own signal dimension
  (`y = shape[0]`, `x = shape[1]`) so partial/interrupted scans (e.g. 114×512) keep x/y aligned
  with `@axes = ['y','x']` instead of swapping.
- **PeakForce channels + scientific titles (per-dataset `config.json`).** Added `/Height`,
  `/DMTModulus`, `/Adhesion`, `/Deformation`, `/Dissipation`, `/Peak_Force_Error` channel
  mappings (the default config only covers TappingMode channels), with concise titles
  (`Topography (Forward)`, `DMT Modulus (Backward)`, …). Default plot = `height_forward`.

The **9 ISO/TC 201-exported `.spm` files** (`717-1B4-resine1.0_00002`, `717-1B4-BN3.0_00002`,
`717-1B4-1_0.0_00001`, `717-1B4-1_0Tier.0_00002`, `717-1B4-1_150um.0_00001`,
`717-1B4-1_210um.0_00002`, `717-1B4-1_230um.0_00001`, `717-1B4-1_30um.0_00000`,
`717-1B4-1_90um.0_00001`) are not native Bruker files; pySPM's `Bruker.__init__` infinite-loops
on them (no `*File list end` terminator), so they are skipped. Raw files kept in `s3_data/`.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 72/81 `.spm` converted (`PS = True`); 9 ISO/TC 201 files
      unsupported (`PS = False`)
- [x] Reference .nxs files generated and uploaded for all 72 converted files
