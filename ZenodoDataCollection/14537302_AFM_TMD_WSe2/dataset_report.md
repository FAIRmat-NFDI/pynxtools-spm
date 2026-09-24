# Dataset Report: Zenodo Record 14537302

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Role of Chalcogen atoms in In-Situ Exfoliation of Large-Area 2D Semiconducting Transition Metal Dichalcogenides |
| **DOI**    | [10.5281/zenodo.14537302](https://doi.org/10.5281/zenodo.14537302) |
| **Date**   | 2024-12-20 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Grubisic-Cabo, Antonija |
| **Tags**   | 2D materials, Transition metal dichalcogenides, XPS, LEED, Exfoliation, AFM |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) + XPS + LEED + Optical Microscopy
- **Instrument**: Bruker AFM (NanoScope format, `.spm`)

## Dataset Contents

16 files for a WSe₂ in-situ exfoliation study: 1 Bruker `.spm` AFM file, XPS spectra (`.txt`), optical microscopy images (`.jpg`, `.png`), and LEED images.

## File Format

- **Format**: Bruker `.spm` (1 file), `.txt` (XPS), `.jpg`/`.png` (optical/LEED)
- **Parsability**: The single `.spm` file (`Figure4b_WSe2-Ag-S1.0_00000.spm`) is parsable by `BrukerSpmAFM`.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14537302/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 16 files

**S3 key pattern**: `zenodo/14537302/<filename>/<filename>`

Files uploaded flat (no zip extraction) ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14537302/))

| file | experiment | S3 key |
|------|------------|--------|
| `Figure4b_WSe2-Ag-S1.0_00000.spm`        | AFM | `zenodo/14537302/Figure4b_WSe2-Ag-S1.0_00000.spm/Figure4b_WSe2-Ag-S1.0_00000.spm` |
| `230418BD_WSe2_Au_Survey_Figure5a.txt`    | XPS | `zenodo/14537302/230418BD_WSe2_Au_Survey_Figure5a.txt/230418BD_WSe2_Au_Survey_Figure5a.txt` |
| `230418BD WSe2_W4f_Figure5b.txt`          | XPS | `zenodo/14537302/230418BD WSe2_W4f_Figure5b.txt/230418BD WSe2_W4f_Figure5b.txt` |
| `230418BD WSe2_Se3p_Figure5c.txt`         | XPS | `zenodo/14537302/230418BD WSe2_Se3p_Figure5c.txt/230418BD WSe2_Se3p_Figure5c.txt` |
| `Figure1f.jpg`                            | OM  | `zenodo/14537302/Figure1f.jpg/Figure1f.jpg` |
| `Figure2a_Sample1.jpg`                    | OM  | `zenodo/14537302/Figure2a_Sample1.jpg/Figure2a_Sample1.jpg` |
| `Figure2a_Sample2.jpg`                    | OM  | `zenodo/14537302/Figure2a_Sample2.jpg/Figure2a_Sample2.jpg` |
| `Figure2a_Sample3.jpg`                    | OM  | `zenodo/14537302/Figure2a_Sample3.jpg/Figure2a_Sample3.jpg` |
| `Figure2a_Sample4.jpg`                    | OM  | `zenodo/14537302/Figure2a_Sample4.jpg/Figure2a_Sample4.jpg` |
| `Figure2b_Sample1.jpg`                    | OM  | `zenodo/14537302/Figure2b_Sample1.jpg/Figure2b_Sample1.jpg` |
| `Figure2b_Sample2.jpg`                    | OM  | `zenodo/14537302/Figure2b_Sample2.jpg/Figure2b_Sample2.jpg` |
| `Figure2b_Sample3.jpg`                    | OM  | `zenodo/14537302/Figure2b_Sample3.jpg/Figure2b_Sample3.jpg` |
| `Figure2b_Sample4.jpg`                    | OM  | `zenodo/14537302/Figure2b_Sample4.jpg/Figure2b_Sample4.jpg` |
| `Figure3a.jpg`                            | OM  | `zenodo/14537302/Figure3a.jpg/Figure3a.jpg` |
| `Figure3b.jpg`                            | OM  | `zenodo/14537302/Figure3b.jpg/Figure3b.jpg` |
| `Figure4a.png`                            | OM  | `zenodo/14537302/Figure4a.png/Figure4a.png` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
