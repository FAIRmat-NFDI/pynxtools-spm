# Dataset Report: Zenodo Record 15326266

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Force Volume Atomic Force Microscopy-Infrared for Simultaneous Nanoscale Chemical and Mechanical Spectromicroscopy |
| **DOI**    | [10.5281/zenodo.15326266](https://doi.org/10.5281/zenodo.15326266) |
| **Date**   | 2025-05-05 |
| **Access** | Open |
| **License**| CC BY-NC-ND 4.0 |
| **Authors**| Wagner, Martin; Hu, Qichi; Hu, Shuiqing; Phillips, Cassandra et al. |
| **Tags**   | AFM-IR, photothermal, force volume, nanomechanical, contact resonance, infrared spectroscopy |

## Technique

- **Primary SPM technique**: AFM-IR (Force Volume mode) — combined AFM and infrared spectroscopy
- **Instrument**: Bruker NanoScope (`.spm` force volume files)

## Dataset Contents

44 files for an AFM-IR force-volume study on polymer thin films (PS-b-PMMA, PS-LDPE, purple membrane). Includes Bruker `.spm` force volume files (up to 1.6 GB each) and `.txt` spectral data, organised by figure.

## File Format

- **Format**: Bruker `.spm` (force volume AFM-IR), `.txt` (spectra), `.PNG`
- **Parsability**: Parsable by `BrukerSpmAFM` for standard channels. Force-volume specific channels may require extended support.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/15326266/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 44 files

**S3 key pattern**: `zenodo/15326266/<filename>/<filename>`

Files uploaded flat (no subfolders) — one S3 prefix per file ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/15326266/))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `Fig1 <desc>.spm`   | AFM-IR | 2 | `zenodo/15326266/Fig1 …/` |
| `Fig2 <desc>.spm`   | AFM-IR | 2 | `zenodo/15326266/Fig2 …/` |
| `Fig3 <desc>.spm`   | AFM-IR | 1 | `zenodo/15326266/Fig3 purple mem …/` |
| `Fig3 spectrum *.txt` | AFM-IR | 2 | `zenodo/15326266/Fig3 spectrum …/` |
| `Fig4 <desc>.spm`   | AFM-IR | 3 | `zenodo/15326266/Fig4 PS-LDPE …/` |
| `Fig4 *.txt`        | AFM-IR | 2 | `zenodo/15326266/Fig4 …txt/` |
| `Fig5 <desc>.spm`   | AFM-IR | 1 | `zenodo/15326266/Fig5 dPS-b-PMMA …/` |
| `Fig6 <freq> 1720cm.spm` | AFM-IR | 6 | `zenodo/15326266/Fig6 …/` |
| `Fig6 curves panel *.txt` | AFM-IR | 2 | `zenodo/15326266/Fig6 curves …/` |
| `Fig7 spectra REFV and SSFV.txt` | AFM-IR | 1 | `zenodo/15326266/Fig7 …/` |
| `FigS1 *.spm`       | AFM-IR | 3 | `zenodo/15326266/FigS1 …/` |
| `FigS2 *.spm`       | AFM-IR | 4 | `zenodo/15326266/FigS2 …spm/` |
| `FigS2 *.txt`       | AFM-IR | 4 | `zenodo/15326266/FigS2 …txt/` |
| `FigS3 *.spm`       | AFM-IR | 5 | `zenodo/15326266/FigS3 …spm/` |
| `FigS3 graph data.txt` | AFM-IR | 1 | `zenodo/15326266/FigS3 graph data.txt/` |
| `FigS3 *.PNG`       | AFM-IR | 1 | `zenodo/15326266/FigS3 …PNG/` |
| `FigS4 <desc>.spm`  | AFM-IR | 1 | `zenodo/15326266/FigS4 …/` |
| `FigS5 *.spm`       | AFM-IR | 2 | `zenodo/15326266/FigS5 …/` |
| `FigS9 <desc>.spm`  | AFM-IR | 1 | `zenodo/15326266/FigS9 …/` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
