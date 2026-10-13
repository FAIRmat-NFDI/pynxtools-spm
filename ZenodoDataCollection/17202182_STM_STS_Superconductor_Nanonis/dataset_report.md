# Dataset Report: Zenodo Record 17202182

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Revealing band-hybrid Cooper pairs on the surface of a superconductor with spin-orbit coupling |
| **DOI**    | [10.5281/zenodo.17202182](https://doi.org/10.5281/zenodo.17202182) |
| **Url**    | [https://zenodo.org/records/17202182](https://zenodo.org/records/17202182) |
| **Date**   | 2025-09-25 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Pascual, Jose Ignacio |
| **Tags**   | STM, STS, scanning tunneling microscopy, spectroscopy, superconductor, spin-orbit coupling, Cooper pairs, quasiparticle interference |
| **Description** | OPEN DATASET of the publication "Revealing band-hybrid Cooper pairs on the surface of a superconductor with spin-orbit coupling" including  Scanning Tunneling Microscopy and Spectroscopy results. |
| **Experiment information related files** | `Information.txt`, `QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf`, `QPI_visualization_of_Interband_Pairing-SM.pdf` |

## Technique

- **Primary SPM technique**: STM/STS (Scanning Tunneling Microscopy/Spectroscopy) — quasiparticle interference maps
- **Instrument**: Nanonis (`.sxm` format inferred from folder structure)

## Sample

- **Material / chemical formula**: surface of a **superconductor with spin-orbit coupling**
  (study of band-hybrid Cooper pairs by STM/STS). The exact material is **not stated in the
  Zenodo metadata**, so `chemical_formula` is left empty (`—`).

## Dataset Contents

20 objects for a QPI (Quasiparticle Interference) study on a superconductor with spin-orbit coupling. Data organised in Fig2-QPI, Fig3-BQPI, Fig4-FFT folders plus PDF manuscript and supplemental. Readable with Gwyddion.

## File Format

- **Format**: Nanonis `.sxm` (STM/STS QPI maps), `.pdf`
- **Parsability**: Nanonis `.sxm` files parsable by `NanonisSxmSTM`. QPI maps are conductance images — use STS/STM technique.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17202182/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 20 files

**S3 key pattern**: `zenodo/17202182/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `T190613_004.sxm` | STS | Superconductor surface (spin-orbit coupled) | — | 1 | `zenodo/17202182/Fig2-QPI/T190613_004.sxm/` | True | True |
| `T180729_002.sxm` | STS | Superconductor surface (spin-orbit coupled) | — | 2 | `zenodo/17202182/Fig3-BQPI/T180729_002.sxm/` | True | True |
| `T180817_001.sxm` | STS | Superconductor surface (spin-orbit coupled) | — | 3 | `zenodo/17202182/Fig3-BQPI/T180817_001.sxm/` | True | True |
| `T190202_007.sxm` | STS | Superconductor surface (spin-orbit coupled) | — | 4 | `zenodo/17202182/Fig3-BQPI/T190202_007.sxm/` | True | True |
| `T190322_005.sxm` | STS | Superconductor surface (spin-orbit coupled) | — | 5 | `zenodo/17202182/Fig4-FFT/T190322_005.sxm/` | True | True |
| `*.stp` | STS | Superconductor surface (spin-orbit coupled) | — | 9 | `zenodo/17202182/Fig2-QPI/` | — | — |
| `*.stp` | STS | Superconductor surface (spin-orbit coupled) | — | 3 | `zenodo/17202182/Fig4-FFT/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `Information.txt` | STS | 1 | `zenodo/17202182/Information.txt/` |
| `QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf` | STS | 2 | `zenodo/17202182/QPI_visualization_of_Interband_Pairing-AcceptedMS.pdf/` |
| `QPI_visualization_of_Interband_Pairing-SM.pdf` | STS | 3 | `zenodo/17202182/QPI_visualization_of_Interband_Pairing-SM.pdf/` |

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08/09 with `pynxtools-spm` 0.2.5. License **`cc-by-4.0`** passes the
open-license gate. **All 5 `.sxm` files converted, validated, and uploaded** (`PS = True`).
`T190613_004` is single-pass (default `current_forward`); the other 4 are **multi-pass** files
whose channels are named `[P1]_Current`/`[P1]_Z`/`[P2]_…` (two measurement passes). These were
recovered by a **per-dataset `config.json`** (copied from `ElnExamples/nanonis_sxm_stm` and
edited to add `[P1]_`/`[P2]_` channel groups — the src default config was not touched), giving
8 NXdata groups (current/z × P1/P2 × fwd/bwd), default `current_p1_forward`; short units, no
shape mismatch. Output `.nxs` named `SOCsuperconductor_<raw_stem>.nxs`. This record has **no
`.dat`** — the STS spectroscopy is embedded in the `.sxm` (`.stp` files are Gwyddion exports,
grouped rows).

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 5/5 `.sxm` converted (`PS = True`; 4 multi-pass via edited config)
- [x] Reference .nxs files generated and uploaded for all 5 files
