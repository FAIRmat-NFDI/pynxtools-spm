# Dataset Report: Zenodo Record 17831280

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for 'Living Fiber Dispersions from Mycelium as a New Sustainable Platform for Advanced Materials' |
| **DOI**    | [10.5281/zenodo.17831280](https://doi.org/10.5281/zenodo.17831280) |
| **Url**    | [https://zenodo.org/records/17831280](https://zenodo.org/records/17831280) |
| **Date**   | 2025-12-05 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Nystrom, Gustav |
| **Tags**   | AFM, mycelium, biopolymers, living materials, sustainable materials, mechanical properties |
| **Description** | Functional biopolymeric fibers are key building blocks for developing sustainable materials within the growing bioeconomy. However, their flexible use in emerging advanced materials with smart properties typically requires processing methods that may compromise sustainability. Here, a sustainable route to generate living fiber dispersions (LFD) from mycelium that combines the excellent material-forming properties of biopolymeric fibers, and the highly dynamic properties of living materials is proposed. This is showcased by using industrially available liquid culture and mechanical defibrillation methods to generate well-dispersed living mycelium fibers. These fibers can form materials where precursors with good dispersibility and network formation properties are paramount and can harness dynamic properties through growth even in the absence of added nutrients. This is demonstrated in unique living emulsions with 3.6x slower phase separation and in living films with 2.5x higher tensile strength upon growth, the latter vastly outperforming the strongest pure mycelium materials to date. Further, humidity can be used to modulate mechanical properties and to trigger the superhydrophobic patterning of substrates, mechanical actuation, and degradation of lignocellulosic consumer goods at their end of life. In the future, combining synthetic biology with this promising platform for smart materials can expand the horizons for sustainable material manufacturing. |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy)
- **Instrument**: Bruker AFM (`.spm` format)

## Dataset Contents

18 files for a mycelium living fiber dispersion study. Contains 3 Bruker `.spm` AFM files (Fig2_HPB.spm 320 MB, Fig2_SPG.spm 43 MB, Fig2_SPG+HPB.spm 760 KB) and 15 Origin `.opju` data files for mechanical and wettability analysis.

## File Format

- **Format**: Bruker `.spm` (3 files), Origin `.opju` (15 files)
- **Parsability**: The three `.spm` files are parsable by `BrukerSpmAFM`. Origin `.opju` files are not in scope.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17831280/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 18 files

**S3 key pattern**: `zenodo/17831280/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `Fig2_HPB.spm` | AFM | 1 | `zenodo/17831280/Fig2_HPB.spm/` | — | — |
| `Fig2_SPG+HPB.spm` | AFM | 2 | `zenodo/17831280/Fig2_SPG+HPB.spm/` | — | — |
| `Fig2_SPG.spm` | AFM | 3 | `zenodo/17831280/Fig2_SPG.spm/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig2_PhaseSeparationAnalysis.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig3_ GrowthVNoGrowthVsAligned_Final.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig3_DVS.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig3_HumidityEffect.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig3_ModulusComparison.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig3_WCA1.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig3_WCAS2.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig4_DirectedGrowth.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig4_HumidityResponse.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/Fig4_PaperDegradation.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/SI22_WCALongTerm.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/SI23_HyphaOnTape.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/SI24Abrasion WCA.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/SI24immersion WCA.opju/` | — | — |
| `*.opju` | AFM | 1 | `zenodo/17831280/SI39_PaperDegradationFTIR.opju/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
