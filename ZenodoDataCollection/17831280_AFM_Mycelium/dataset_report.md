# Dataset Report: Zenodo Record 17831280

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for 'Living Fiber Dispersions from Mycelium as a New Sustainable Platform for Advanced Materials' |
| **DOI**    | [10.5281/zenodo.17831280](https://doi.org/10.5281/zenodo.17831280) |
| **Date**   | 2025-12-05 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Nystrom, Gustav |
| **Tags**   | AFM, mycelium, biopolymers, living materials, sustainable materials, mechanical properties |

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

**S3 key pattern**: `zenodo/17831280/<filename>/<filename>`

Files uploaded flat ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/17831280/))

| file | experiment | S3 key |
|------|------------|--------|
| `Fig2_HPB.spm`                          | AFM | `zenodo/17831280/Fig2_HPB.spm/Fig2_HPB.spm` |
| `Fig2_SPG.spm`                          | AFM | `zenodo/17831280/Fig2_SPG.spm/Fig2_SPG.spm` |
| `Fig2_SPG+HPB.spm`                      | AFM | `zenodo/17831280/Fig2_SPG+HPB.spm/Fig2_SPG+HPB.spm` |
| `Fig2_PhaseSeparationAnalysis.opju`     | —   | `zenodo/17831280/Fig2_PhaseSeparationAnalysis.opju/Fig2_PhaseSeparationAnalysis.opju` |
| `Fig3_DVS.opju`                         | —   | `zenodo/17831280/Fig3_DVS.opju/Fig3_DVS.opju` |
| `Fig3_ GrowthVNoGrowthVsAligned_Final.opju` | — | `zenodo/17831280/Fig3_ GrowthVNoGrowthVsAligned_Final.opju/Fig3_ GrowthVNoGrowthVsAligned_Final.opju` |
| `Fig3_HumidityEffect.opju`              | —   | `zenodo/17831280/Fig3_HumidityEffect.opju/Fig3_HumidityEffect.opju` |
| `Fig3_ModulusComparison.opju`           | —   | `zenodo/17831280/Fig3_ModulusComparison.opju/Fig3_ModulusComparison.opju` |
| `Fig3_WCA1.opju`                        | —   | `zenodo/17831280/Fig3_WCA1.opju/Fig3_WCA1.opju` |
| `Fig3_WCAS2.opju`                       | —   | `zenodo/17831280/Fig3_WCAS2.opju/Fig3_WCAS2.opju` |
| `Fig4_DirectedGrowth.opju`              | —   | `zenodo/17831280/Fig4_DirectedGrowth.opju/Fig4_DirectedGrowth.opju` |
| `Fig4_HumidityResponse.opju`            | —   | `zenodo/17831280/Fig4_HumidityResponse.opju/Fig4_HumidityResponse.opju` |
| `Fig4_PaperDegradation.opju`            | —   | `zenodo/17831280/Fig4_PaperDegradation.opju/Fig4_PaperDegradation.opju` |
| `SI22_WCALongTerm.opju`                 | —   | `zenodo/17831280/SI22_WCALongTerm.opju/SI22_WCALongTerm.opju` |
| `SI23_HyphaOnTape.opju`                 | —   | `zenodo/17831280/SI23_HyphaOnTape.opju/SI23_HyphaOnTape.opju` |
| `SI24Abrasion WCA.opju`                 | —   | `zenodo/17831280/SI24Abrasion WCA.opju/SI24Abrasion WCA.opju` |
| `SI24immersion WCA.opju`                | —   | `zenodo/17831280/SI24immersion WCA.opju/SI24immersion WCA.opju` |
| `SI39_PaperDegradationFTIR.opju`        | —   | `zenodo/17831280/SI39_PaperDegradationFTIR.opju/SI39_PaperDegradationFTIR.opju` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
