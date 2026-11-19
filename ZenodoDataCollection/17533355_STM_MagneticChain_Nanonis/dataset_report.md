# Dataset Report: Zenodo Record 17533355

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data underlying the paper "Direct signatures of d-level hybridization and dimerization in magnetic adatom chains on a superconductor" |
| **DOI**    | [10.5281/zenodo.17533355](https://doi.org/10.5281/zenodo.17533355) |
| **Url**    | [https://zenodo.org/records/17533355](https://zenodo.org/records/17533355) |
| **Date**   | 2025-11-05 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Rütten, Lisa M.; Liebhaber, Eva; Reecht, Gaël et al. |
| **Tags**   | Superconductivity, Scanning tunneling microscopy, magnetic chain |
| **Description** | Here, we provide all original data used in the manuscript  "Direct signatures of d-level hybridization and dimerization in magnetic adatom chains on a superconductor" |
| **Experiment information related files** | `directory.pdf` |

## Technique

- **Primary SPM technique**: STM/STS (Scanning Tunneling Microscopy/Spectroscopy)
- **Instrument**: Nanonis (`.sxm` / `.dat` format)

## Sample

- **Material / chemical formula**: **magnetic adatom chains on a superconductor** (STM/STS of
  d-level hybridization and dimerization). As an adatoms-on-substrate system with no single
  stoichiometry stated in the metadata, `chemical_formula` is left empty (`—`).

## Dataset Contents

638 objects extracted from `data.zip`, organised by figure (Fig1–Fig5, FigS1–FigS9). Contains Nanonis `.sxm` STM images and `.dat` STS spectroscopy files plus a PDF directory.

## File Format

- **Format**: Nanonis `.sxm` (STM), Nanonis `.dat` (STS)
- **Parsability**: STM `.sxm` files parsable by `NanonisSxmSTM`; STS `.dat` files parsable by `NanonisDatSTS`.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17533355/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 638 files

**S3 key pattern**: `zenodo/17533355/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `cloud_No08BA_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 1 | `zenodo/17533355/Fig1/cloud_No08BA_001.dat/` | True | True |
| `cloud_No08BA_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 2 | `zenodo/17533355/Fig1/cloud_No08BA_002.dat/` | True | True |
| `cloud_No08BA_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 3 | `zenodo/17533355/Fig1/cloud_No08BA_003.dat/` | True | True |
| `cloud_No08BO_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 4 | `zenodo/17533355/Fig1/cloud_No08BO_001.dat/` | True | True |
| `cloud_No08BO_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 5 | `zenodo/17533355/Fig1/cloud_No08BO_002.dat/` | True | True |
| `cloud_No08BR_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 6 | `zenodo/17533355/Fig1/cloud_No08BR_001.dat/` | True | True |
| `cloud_No08BR_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 7 | `zenodo/17533355/Fig1/cloud_No08BR_002.dat/` | True | True |
| `cloud_No08BR_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 8 | `zenodo/17533355/Fig1/cloud_No08BR_003.dat/` | True | True |
| `cloud_No08CB_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 9 | `zenodo/17533355/Fig1/cloud_No08CB_001.dat/` | True | True |
| `cloud_No08CB_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 10 | `zenodo/17533355/Fig1/cloud_No08CB_002.dat/` | True | True |
| `cloud_No08CB_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 11 | `zenodo/17533355/Fig1/cloud_No08CB_003.dat/` | True | True |
| `image_645.sxm` | STS | Magnetic adatom chains on a superconductor | — | 12 | `zenodo/17533355/Fig1/image_645.sxm/` | True | True |
| `image_712.sxm` | STS | Magnetic adatom chains on a superconductor | — | 13 | `zenodo/17533355/Fig1/image_712.sxm/` | True | True |
| `image_721.sxm` | STS | Magnetic adatom chains on a superconductor | — | 14 | `zenodo/17533355/Fig1/image_721.sxm/` | True | True |
| `image_745.sxm` | STS | Magnetic adatom chains on a superconductor | — | 15 | `zenodo/17533355/Fig1/image_745.sxm/` | True | True |
| `image_065.sxm` | STS | Magnetic adatom chains on a superconductor | — | 16 | `zenodo/17533355/Fig2/image_065.sxm/` | True | True |
| `image_069.sxm` | STS | Magnetic adatom chains on a superconductor | — | 17 | `zenodo/17533355/Fig2/image_069.sxm/` | True | True |
| `image_078.sxm` | STS | Magnetic adatom chains on a superconductor | — | 18 | `zenodo/17533355/Fig2/image_078.sxm/` | True | True |
| `image_084.sxm` | STS | Magnetic adatom chains on a superconductor | — | 19 | `zenodo/17533355/Fig2/image_084.sxm/` | True | True |
| `line_No14AA_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 20 | `zenodo/17533355/Fig2/line_No14AA_001.dat/` | True | True |
| `line_No14AA_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 21 | `zenodo/17533355/Fig2/line_No14AA_002.dat/` | True | True |
| `line_No14AA_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 22 | `zenodo/17533355/Fig2/line_No14AA_003.dat/` | True | True |
| `line_No14AA_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 23 | `zenodo/17533355/Fig2/line_No14AA_004.dat/` | True | True |
| `line_No14AA_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 24 | `zenodo/17533355/Fig2/line_No14AA_005.dat/` | True | True |
| `line_No14AA_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 25 | `zenodo/17533355/Fig2/line_No14AA_006.dat/` | True | True |
| `line_No14AA_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 26 | `zenodo/17533355/Fig2/line_No14AA_007.dat/` | True | True |
| `line_No14AA_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 27 | `zenodo/17533355/Fig2/line_No14AA_008.dat/` | True | True |
| `line_No14AA_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 28 | `zenodo/17533355/Fig2/line_No14AA_009.dat/` | True | True |
| `line_No14AA_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 29 | `zenodo/17533355/Fig2/line_No14AA_010.dat/` | True | True |
| `line_No14AA_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 30 | `zenodo/17533355/Fig2/line_No14AA_011.dat/` | True | True |
| `line_No14AA_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 31 | `zenodo/17533355/Fig2/line_No14AA_012.dat/` | True | True |
| `line_No14AA_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 32 | `zenodo/17533355/Fig2/line_No14AA_013.dat/` | True | True |
| `line_No14AA_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 33 | `zenodo/17533355/Fig2/line_No14AA_014.dat/` | True | True |
| `line_No14AA_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 34 | `zenodo/17533355/Fig2/line_No14AA_015.dat/` | True | True |
| `line_No14AA_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 35 | `zenodo/17533355/Fig2/line_No14AA_016.dat/` | True | True |
| `line_No14AA_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 36 | `zenodo/17533355/Fig2/line_No14AA_017.dat/` | True | True |
| `line_No14AA_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 37 | `zenodo/17533355/Fig2/line_No14AA_018.dat/` | True | True |
| `line_No14AA_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 38 | `zenodo/17533355/Fig2/line_No14AA_019.dat/` | True | True |
| `line_No14AA_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 39 | `zenodo/17533355/Fig2/line_No14AA_020.dat/` | True | True |
| `line_No14AA_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 40 | `zenodo/17533355/Fig2/line_No14AA_021.dat/` | True | True |
| `line_No14AA_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 41 | `zenodo/17533355/Fig2/line_No14AA_022.dat/` | True | True |
| `line_No14AA_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 42 | `zenodo/17533355/Fig2/line_No14AA_023.dat/` | True | True |
| `line_No14AA_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 43 | `zenodo/17533355/Fig2/line_No14AA_024.dat/` | True | True |
| `line_No14AA_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 44 | `zenodo/17533355/Fig2/line_No14AA_025.dat/` | True | True |
| `line_No14AA_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 45 | `zenodo/17533355/Fig2/line_No14AA_026.dat/` | True | True |
| `line_No14AA_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 46 | `zenodo/17533355/Fig2/line_No14AA_027.dat/` | True | True |
| `line_No14AA_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 47 | `zenodo/17533355/Fig2/line_No14AA_028.dat/` | True | True |
| `line_No14AA_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 48 | `zenodo/17533355/Fig2/line_No14AA_029.dat/` | True | True |
| `line_No14AA_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 49 | `zenodo/17533355/Fig2/line_No14AA_030.dat/` | True | True |
| `line_No14AA_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 50 | `zenodo/17533355/Fig2/line_No14AA_031.dat/` | True | True |
| `line_No14AA_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 51 | `zenodo/17533355/Fig2/line_No14AA_032.dat/` | True | True |
| `line_No14AA_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 52 | `zenodo/17533355/Fig2/line_No14AA_033.dat/` | True | True |
| `line_No14AA_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 53 | `zenodo/17533355/Fig2/line_No14AA_034.dat/` | True | True |
| `line_No14AA_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 54 | `zenodo/17533355/Fig2/line_No14AA_035.dat/` | True | True |
| `line_No14AA_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 55 | `zenodo/17533355/Fig2/line_No14AA_036.dat/` | True | True |
| `line_No14AA_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 56 | `zenodo/17533355/Fig2/line_No14AA_037.dat/` | True | True |
| `line_No14AA_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 57 | `zenodo/17533355/Fig2/line_No14AA_038.dat/` | True | True |
| `line_No14AA_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 58 | `zenodo/17533355/Fig2/line_No14AA_039.dat/` | True | True |
| `line_No14AA_040.dat` | STS | Magnetic adatom chains on a superconductor | — | 59 | `zenodo/17533355/Fig2/line_No14AA_040.dat/` | True | True |
| `line_No14AA_041.dat` | STS | Magnetic adatom chains on a superconductor | — | 60 | `zenodo/17533355/Fig2/line_No14AA_041.dat/` | True | True |
| `line_No14AA_042.dat` | STS | Magnetic adatom chains on a superconductor | — | 61 | `zenodo/17533355/Fig2/line_No14AA_042.dat/` | True | True |
| `line_No14AA_043.dat` | STS | Magnetic adatom chains on a superconductor | — | 62 | `zenodo/17533355/Fig2/line_No14AA_043.dat/` | True | True |
| `line_No14AD_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 63 | `zenodo/17533355/Fig2/line_No14AD_001.dat/` | True | True |
| `line_No14AD_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 64 | `zenodo/17533355/Fig2/line_No14AD_002.dat/` | True | True |
| `line_No14AD_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 65 | `zenodo/17533355/Fig2/line_No14AD_003.dat/` | True | True |
| `line_No14AD_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 66 | `zenodo/17533355/Fig2/line_No14AD_004.dat/` | True | True |
| `line_No14AD_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 67 | `zenodo/17533355/Fig2/line_No14AD_005.dat/` | True | True |
| `line_No14AD_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 68 | `zenodo/17533355/Fig2/line_No14AD_006.dat/` | True | True |
| `line_No14AD_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 69 | `zenodo/17533355/Fig2/line_No14AD_007.dat/` | True | True |
| `line_No14AD_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 70 | `zenodo/17533355/Fig2/line_No14AD_008.dat/` | True | True |
| `line_No14AD_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 71 | `zenodo/17533355/Fig2/line_No14AD_009.dat/` | True | True |
| `line_No14AD_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 72 | `zenodo/17533355/Fig2/line_No14AD_010.dat/` | True | True |
| `line_No14AD_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 73 | `zenodo/17533355/Fig2/line_No14AD_011.dat/` | True | True |
| `line_No14AD_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 74 | `zenodo/17533355/Fig2/line_No14AD_012.dat/` | True | True |
| `line_No14AD_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 75 | `zenodo/17533355/Fig2/line_No14AD_013.dat/` | True | True |
| `line_No14AD_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 76 | `zenodo/17533355/Fig2/line_No14AD_014.dat/` | True | True |
| `line_No14AD_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 77 | `zenodo/17533355/Fig2/line_No14AD_015.dat/` | True | True |
| `line_No14AD_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 78 | `zenodo/17533355/Fig2/line_No14AD_016.dat/` | True | True |
| `line_No14AD_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 79 | `zenodo/17533355/Fig2/line_No14AD_017.dat/` | True | True |
| `line_No14AD_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 80 | `zenodo/17533355/Fig2/line_No14AD_018.dat/` | True | True |
| `line_No14AD_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 81 | `zenodo/17533355/Fig2/line_No14AD_019.dat/` | True | True |
| `line_No14AD_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 82 | `zenodo/17533355/Fig2/line_No14AD_020.dat/` | True | True |
| `line_No14AD_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 83 | `zenodo/17533355/Fig2/line_No14AD_021.dat/` | True | True |
| `line_No14AD_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 84 | `zenodo/17533355/Fig2/line_No14AD_022.dat/` | True | True |
| `line_No14AD_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 85 | `zenodo/17533355/Fig2/line_No14AD_023.dat/` | True | True |
| `line_No14AD_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 86 | `zenodo/17533355/Fig2/line_No14AD_024.dat/` | True | True |
| `line_No14AD_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 87 | `zenodo/17533355/Fig2/line_No14AD_025.dat/` | True | True |
| `line_No14AD_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 88 | `zenodo/17533355/Fig2/line_No14AD_026.dat/` | True | True |
| `line_No14AD_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 89 | `zenodo/17533355/Fig2/line_No14AD_027.dat/` | True | True |
| `line_No14AD_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 90 | `zenodo/17533355/Fig2/line_No14AD_028.dat/` | True | True |
| `line_No14AD_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 91 | `zenodo/17533355/Fig2/line_No14AD_029.dat/` | True | True |
| `line_No14AD_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 92 | `zenodo/17533355/Fig2/line_No14AD_030.dat/` | True | True |
| `line_No14AD_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 93 | `zenodo/17533355/Fig2/line_No14AD_031.dat/` | True | True |
| `line_No14AD_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 94 | `zenodo/17533355/Fig2/line_No14AD_032.dat/` | True | True |
| `line_No14AD_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 95 | `zenodo/17533355/Fig2/line_No14AD_033.dat/` | True | True |
| `line_No14AD_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 96 | `zenodo/17533355/Fig2/line_No14AD_034.dat/` | True | True |
| `line_No14AD_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 97 | `zenodo/17533355/Fig2/line_No14AD_035.dat/` | True | True |
| `line_No14AD_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 98 | `zenodo/17533355/Fig2/line_No14AD_036.dat/` | True | True |
| `line_No14AD_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 99 | `zenodo/17533355/Fig2/line_No14AD_037.dat/` | True | True |
| `line_No14AD_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 100 | `zenodo/17533355/Fig2/line_No14AD_038.dat/` | True | True |
| `line_No14AD_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 101 | `zenodo/17533355/Fig2/line_No14AD_039.dat/` | True | True |
| `line_No14AD_040.dat` | STS | Magnetic adatom chains on a superconductor | — | 102 | `zenodo/17533355/Fig2/line_No14AD_040.dat/` | True | True |
| `line_No14AD_041.dat` | STS | Magnetic adatom chains on a superconductor | — | 103 | `zenodo/17533355/Fig2/line_No14AD_041.dat/` | True | True |
| `line_No14AD_042.dat` | STS | Magnetic adatom chains on a superconductor | — | 104 | `zenodo/17533355/Fig2/line_No14AD_042.dat/` | True | True |
| `line_No14AD_043.dat` | STS | Magnetic adatom chains on a superconductor | — | 105 | `zenodo/17533355/Fig2/line_No14AD_043.dat/` | True | True |
| `line_No14AD_044.dat` | STS | Magnetic adatom chains on a superconductor | — | 106 | `zenodo/17533355/Fig2/line_No14AD_044.dat/` | True | True |
| `line_No14AD_045.dat` | STS | Magnetic adatom chains on a superconductor | — | 107 | `zenodo/17533355/Fig2/line_No14AD_045.dat/` | True | True |
| `line_No14AD_046.dat` | STS | Magnetic adatom chains on a superconductor | — | 108 | `zenodo/17533355/Fig2/line_No14AD_046.dat/` | True | True |
| `line_No14AD_047.dat` | STS | Magnetic adatom chains on a superconductor | — | 109 | `zenodo/17533355/Fig2/line_No14AD_047.dat/` | True | True |
| `line_No14AK_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 110 | `zenodo/17533355/Fig2/line_No14AK_001.dat/` | True | True |
| `line_No14AK_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 111 | `zenodo/17533355/Fig2/line_No14AK_002.dat/` | True | True |
| `line_No14AK_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 112 | `zenodo/17533355/Fig2/line_No14AK_003.dat/` | True | True |
| `line_No14AK_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 113 | `zenodo/17533355/Fig2/line_No14AK_004.dat/` | True | True |
| `line_No14AK_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 114 | `zenodo/17533355/Fig2/line_No14AK_005.dat/` | True | True |
| `line_No14AK_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 115 | `zenodo/17533355/Fig2/line_No14AK_006.dat/` | True | True |
| `line_No14AK_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 116 | `zenodo/17533355/Fig2/line_No14AK_007.dat/` | True | True |
| `line_No14AK_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 117 | `zenodo/17533355/Fig2/line_No14AK_008.dat/` | True | True |
| `line_No14AK_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 118 | `zenodo/17533355/Fig2/line_No14AK_009.dat/` | True | True |
| `line_No14AK_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 119 | `zenodo/17533355/Fig2/line_No14AK_010.dat/` | True | True |
| `line_No14AK_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 120 | `zenodo/17533355/Fig2/line_No14AK_011.dat/` | True | True |
| `line_No14AK_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 121 | `zenodo/17533355/Fig2/line_No14AK_012.dat/` | True | True |
| `line_No14AK_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 122 | `zenodo/17533355/Fig2/line_No14AK_013.dat/` | True | True |
| `line_No14AK_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 123 | `zenodo/17533355/Fig2/line_No14AK_014.dat/` | True | True |
| `line_No14AK_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 124 | `zenodo/17533355/Fig2/line_No14AK_015.dat/` | True | True |
| `line_No14AK_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 125 | `zenodo/17533355/Fig2/line_No14AK_016.dat/` | True | True |
| `line_No14AK_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 126 | `zenodo/17533355/Fig2/line_No14AK_017.dat/` | True | True |
| `line_No14AK_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 127 | `zenodo/17533355/Fig2/line_No14AK_018.dat/` | True | True |
| `line_No14AK_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 128 | `zenodo/17533355/Fig2/line_No14AK_019.dat/` | True | True |
| `line_No14AK_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 129 | `zenodo/17533355/Fig2/line_No14AK_020.dat/` | True | True |
| `line_No14AK_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 130 | `zenodo/17533355/Fig2/line_No14AK_021.dat/` | True | True |
| `line_No14AK_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 131 | `zenodo/17533355/Fig2/line_No14AK_022.dat/` | True | True |
| `line_No14AK_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 132 | `zenodo/17533355/Fig2/line_No14AK_023.dat/` | True | True |
| `line_No14AK_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 133 | `zenodo/17533355/Fig2/line_No14AK_024.dat/` | True | True |
| `line_No14AK_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 134 | `zenodo/17533355/Fig2/line_No14AK_025.dat/` | True | True |
| `line_No14AK_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 135 | `zenodo/17533355/Fig2/line_No14AK_026.dat/` | True | True |
| `line_No14AK_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 136 | `zenodo/17533355/Fig2/line_No14AK_027.dat/` | True | True |
| `line_No14AK_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 137 | `zenodo/17533355/Fig2/line_No14AK_028.dat/` | True | True |
| `line_No14AK_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 138 | `zenodo/17533355/Fig2/line_No14AK_029.dat/` | True | True |
| `line_No14AK_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 139 | `zenodo/17533355/Fig2/line_No14AK_030.dat/` | True | True |
| `line_No14AK_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 140 | `zenodo/17533355/Fig2/line_No14AK_031.dat/` | True | True |
| `line_No14AK_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 141 | `zenodo/17533355/Fig2/line_No14AK_032.dat/` | True | True |
| `line_No14AK_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 142 | `zenodo/17533355/Fig2/line_No14AK_033.dat/` | True | True |
| `line_No14AK_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 143 | `zenodo/17533355/Fig2/line_No14AK_034.dat/` | True | True |
| `line_No14AK_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 144 | `zenodo/17533355/Fig2/line_No14AK_035.dat/` | True | True |
| `line_No14AK_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 145 | `zenodo/17533355/Fig2/line_No14AK_036.dat/` | True | True |
| `line_No14AN_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 146 | `zenodo/17533355/Fig2/line_No14AN_001.dat/` | True | True |
| `line_No14AN_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 147 | `zenodo/17533355/Fig2/line_No14AN_002.dat/` | True | True |
| `line_No14AN_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 148 | `zenodo/17533355/Fig2/line_No14AN_003.dat/` | True | True |
| `line_No14AN_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 149 | `zenodo/17533355/Fig2/line_No14AN_004.dat/` | True | True |
| `line_No14AN_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 150 | `zenodo/17533355/Fig2/line_No14AN_005.dat/` | True | True |
| `line_No14AN_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 151 | `zenodo/17533355/Fig2/line_No14AN_006.dat/` | True | True |
| `line_No14AN_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 152 | `zenodo/17533355/Fig2/line_No14AN_007.dat/` | True | True |
| `line_No14AN_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 153 | `zenodo/17533355/Fig2/line_No14AN_008.dat/` | True | True |
| `line_No14AN_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 154 | `zenodo/17533355/Fig2/line_No14AN_009.dat/` | True | True |
| `line_No14AN_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 155 | `zenodo/17533355/Fig2/line_No14AN_010.dat/` | True | True |
| `line_No14AN_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 156 | `zenodo/17533355/Fig2/line_No14AN_011.dat/` | True | True |
| `line_No14AN_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 157 | `zenodo/17533355/Fig2/line_No14AN_012.dat/` | True | True |
| `line_No14AN_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 158 | `zenodo/17533355/Fig2/line_No14AN_013.dat/` | True | True |
| `line_No14AN_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 159 | `zenodo/17533355/Fig2/line_No14AN_014.dat/` | True | True |
| `line_No14AN_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 160 | `zenodo/17533355/Fig2/line_No14AN_015.dat/` | True | True |
| `line_No14AN_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 161 | `zenodo/17533355/Fig2/line_No14AN_016.dat/` | True | True |
| `line_No14AN_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 162 | `zenodo/17533355/Fig2/line_No14AN_017.dat/` | True | True |
| `line_No14AN_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 163 | `zenodo/17533355/Fig2/line_No14AN_018.dat/` | True | True |
| `line_No14AN_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 164 | `zenodo/17533355/Fig2/line_No14AN_019.dat/` | True | True |
| `line_No14AN_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 165 | `zenodo/17533355/Fig2/line_No14AN_020.dat/` | True | True |
| `line_No14AN_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 166 | `zenodo/17533355/Fig2/line_No14AN_021.dat/` | True | True |
| `line_No14AN_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 167 | `zenodo/17533355/Fig2/line_No14AN_022.dat/` | True | True |
| `line_No14AN_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 168 | `zenodo/17533355/Fig2/line_No14AN_023.dat/` | True | True |
| `line_No14AN_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 169 | `zenodo/17533355/Fig2/line_No14AN_024.dat/` | True | True |
| `line_No14AN_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 170 | `zenodo/17533355/Fig2/line_No14AN_025.dat/` | True | True |
| `line_No14AN_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 171 | `zenodo/17533355/Fig2/line_No14AN_026.dat/` | True | True |
| `line_No14AN_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 172 | `zenodo/17533355/Fig2/line_No14AN_027.dat/` | True | True |
| `line_No14AN_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 173 | `zenodo/17533355/Fig2/line_No14AN_028.dat/` | True | True |
| `line_No14AN_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 174 | `zenodo/17533355/Fig2/line_No14AN_029.dat/` | True | True |
| `line_No14AN_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 175 | `zenodo/17533355/Fig2/line_No14AN_030.dat/` | True | True |
| `line_No14AN_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 176 | `zenodo/17533355/Fig2/line_No14AN_031.dat/` | True | True |
| `line_No14AN_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 177 | `zenodo/17533355/Fig2/line_No14AN_032.dat/` | True | True |
| `line_No14AN_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 178 | `zenodo/17533355/Fig2/line_No14AN_033.dat/` | True | True |
| `line_No14AN_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 179 | `zenodo/17533355/Fig2/line_No14AN_034.dat/` | True | True |
| `line_No14AN_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 180 | `zenodo/17533355/Fig2/line_No14AN_035.dat/` | True | True |
| `line_No14AN_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 181 | `zenodo/17533355/Fig2/line_No14AN_036.dat/` | True | True |
| `line_No14AN_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 182 | `zenodo/17533355/Fig2/line_No14AN_037.dat/` | True | True |
| `line_No14AN_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 183 | `zenodo/17533355/Fig2/line_No14AN_038.dat/` | True | True |
| `line_No14AN_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 184 | `zenodo/17533355/Fig2/line_No14AN_039.dat/` | True | True |
| `const_dos_No14_001.sxm` | STS | Magnetic adatom chains on a superconductor | — | 185 | `zenodo/17533355/Fig3/const_dos_No14_001.sxm/` | True | True |
| `const_dos_No14_061.sxm` | STS | Magnetic adatom chains on a superconductor | — | 186 | `zenodo/17533355/Fig3/const_dos_No14_061.sxm/` | True | True |
| `const_dos_No14_077.sxm` | STS | Magnetic adatom chains on a superconductor | — | 187 | `zenodo/17533355/Fig3/const_dos_No14_077.sxm/` | True | True |
| `const_dos_No14_093.sxm` | STS | Magnetic adatom chains on a superconductor | — | 188 | `zenodo/17533355/Fig3/const_dos_No14_093.sxm/` | True | True |
| `image_264.sxm` | STS | Magnetic adatom chains on a superconductor | — | 189 | `zenodo/17533355/Fig3/image_264.sxm/` | True | True |
| `image_288.sxm` | STS | Magnetic adatom chains on a superconductor | — | 190 | `zenodo/17533355/Fig3/image_288.sxm/` | True | True |
| `image_295.sxm` | STS | Magnetic adatom chains on a superconductor | — | 191 | `zenodo/17533355/Fig3/image_295.sxm/` | True | True |
| `BiasSpec_049.dat` | STS | Magnetic adatom chains on a superconductor | — | 192 | `zenodo/17533355/Fig4/BiasSpec_049.dat/` | True | True |
| `image_055.sxm` | STS | Magnetic adatom chains on a superconductor | — | 193 | `zenodo/17533355/Fig4/image_055.sxm/` | True | True |
| `image_060.sxm` | STS | Magnetic adatom chains on a superconductor | — | 194 | `zenodo/17533355/Fig4/image_060.sxm/` | True | True |
| `image_214.sxm` | STS | Magnetic adatom chains on a superconductor | — | 195 | `zenodo/17533355/Fig4/image_214.sxm/` | True | True |
| `image_215.sxm` | STS | Magnetic adatom chains on a superconductor | — | 196 | `zenodo/17533355/Fig4/image_215.sxm/` | True | True |
| `line_No03DB_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 197 | `zenodo/17533355/Fig4/line_No03DB_001.dat/` | True | True |
| `line_No03DB_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 198 | `zenodo/17533355/Fig4/line_No03DB_002.dat/` | True | True |
| `line_No03DB_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 199 | `zenodo/17533355/Fig4/line_No03DB_003.dat/` | True | True |
| `line_No03DB_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 200 | `zenodo/17533355/Fig4/line_No03DB_004.dat/` | True | True |
| `line_No03DB_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 201 | `zenodo/17533355/Fig4/line_No03DB_005.dat/` | True | True |
| `line_No03DB_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 202 | `zenodo/17533355/Fig4/line_No03DB_006.dat/` | True | True |
| `line_No03DB_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 203 | `zenodo/17533355/Fig4/line_No03DB_007.dat/` | True | True |
| `line_No03DB_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 204 | `zenodo/17533355/Fig4/line_No03DB_008.dat/` | True | True |
| `line_No03DB_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 205 | `zenodo/17533355/Fig4/line_No03DB_009.dat/` | True | True |
| `line_No03DB_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 206 | `zenodo/17533355/Fig4/line_No03DB_010.dat/` | True | True |
| `line_No03DB_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 207 | `zenodo/17533355/Fig4/line_No03DB_011.dat/` | True | True |
| `line_No03DB_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 208 | `zenodo/17533355/Fig4/line_No03DB_012.dat/` | True | True |
| `line_No03DB_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 209 | `zenodo/17533355/Fig4/line_No03DB_013.dat/` | True | True |
| `line_No03DB_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 210 | `zenodo/17533355/Fig4/line_No03DB_014.dat/` | True | True |
| `line_No03DB_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 211 | `zenodo/17533355/Fig4/line_No03DB_015.dat/` | True | True |
| `line_No03DB_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 212 | `zenodo/17533355/Fig4/line_No03DB_016.dat/` | True | True |
| `line_No03DB_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 213 | `zenodo/17533355/Fig4/line_No03DB_017.dat/` | True | True |
| `line_No03DB_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 214 | `zenodo/17533355/Fig4/line_No03DB_018.dat/` | True | True |
| `line_No03DB_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 215 | `zenodo/17533355/Fig4/line_No03DB_019.dat/` | True | True |
| `line_No03DB_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 216 | `zenodo/17533355/Fig4/line_No03DB_020.dat/` | True | True |
| `line_No03DB_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 217 | `zenodo/17533355/Fig4/line_No03DB_021.dat/` | True | True |
| `line_No03DB_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 218 | `zenodo/17533355/Fig4/line_No03DB_022.dat/` | True | True |
| `line_No03DB_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 219 | `zenodo/17533355/Fig4/line_No03DB_023.dat/` | True | True |
| `line_No03DB_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 220 | `zenodo/17533355/Fig4/line_No03DB_024.dat/` | True | True |
| `line_No03DB_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 221 | `zenodo/17533355/Fig4/line_No03DB_025.dat/` | True | True |
| `line_No03DB_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 222 | `zenodo/17533355/Fig4/line_No03DB_026.dat/` | True | True |
| `line_No03DB_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 223 | `zenodo/17533355/Fig4/line_No03DB_027.dat/` | True | True |
| `line_No03DB_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 224 | `zenodo/17533355/Fig4/line_No03DB_028.dat/` | True | True |
| `line_No03DB_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 225 | `zenodo/17533355/Fig4/line_No03DB_029.dat/` | True | True |
| `line_No03DB_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 226 | `zenodo/17533355/Fig4/line_No03DB_030.dat/` | True | True |
| `line_No03DB_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 227 | `zenodo/17533355/Fig4/line_No03DB_031.dat/` | True | True |
| `line_No03DB_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 228 | `zenodo/17533355/Fig4/line_No03DB_032.dat/` | True | True |
| `line_No03DB_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 229 | `zenodo/17533355/Fig4/line_No03DB_033.dat/` | True | True |
| `line_No03DB_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 230 | `zenodo/17533355/Fig4/line_No03DB_034.dat/` | True | True |
| `line_No03DB_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 231 | `zenodo/17533355/Fig4/line_No03DB_035.dat/` | True | True |
| `line_No03DB_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 232 | `zenodo/17533355/Fig4/line_No03DB_036.dat/` | True | True |
| `line_No03DB_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 233 | `zenodo/17533355/Fig4/line_No03DB_037.dat/` | True | True |
| `line_No03DB_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 234 | `zenodo/17533355/Fig4/line_No03DB_038.dat/` | True | True |
| `line_No03DB_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 235 | `zenodo/17533355/Fig4/line_No03DB_039.dat/` | True | True |
| `line_No03DB_040.dat` | STS | Magnetic adatom chains on a superconductor | — | 236 | `zenodo/17533355/Fig4/line_No03DB_040.dat/` | True | True |
| `line_No03DB_041.dat` | STS | Magnetic adatom chains on a superconductor | — | 237 | `zenodo/17533355/Fig4/line_No03DB_041.dat/` | True | True |
| `line_No03DB_042.dat` | STS | Magnetic adatom chains on a superconductor | — | 238 | `zenodo/17533355/Fig4/line_No03DB_042.dat/` | True | True |
| `line_No03DB_043.dat` | STS | Magnetic adatom chains on a superconductor | — | 239 | `zenodo/17533355/Fig4/line_No03DB_043.dat/` | True | True |
| `line_No03DB_044.dat` | STS | Magnetic adatom chains on a superconductor | — | 240 | `zenodo/17533355/Fig4/line_No03DB_044.dat/` | True | True |
| `line_No03DB_045.dat` | STS | Magnetic adatom chains on a superconductor | — | 241 | `zenodo/17533355/Fig4/line_No03DB_045.dat/` | True | True |
| `line_No03DB_046.dat` | STS | Magnetic adatom chains on a superconductor | — | 242 | `zenodo/17533355/Fig4/line_No03DB_046.dat/` | True | True |
| `line_No03DB_047.dat` | STS | Magnetic adatom chains on a superconductor | — | 243 | `zenodo/17533355/Fig4/line_No03DB_047.dat/` | True | True |
| `line_No03DB_048.dat` | STS | Magnetic adatom chains on a superconductor | — | 244 | `zenodo/17533355/Fig4/line_No03DB_048.dat/` | True | True |
| `line_No03DB_049.dat` | STS | Magnetic adatom chains on a superconductor | — | 245 | `zenodo/17533355/Fig4/line_No03DB_049.dat/` | True | True |
| `line_No03DB_050.dat` | STS | Magnetic adatom chains on a superconductor | — | 246 | `zenodo/17533355/Fig4/line_No03DB_050.dat/` | True | True |
| `line_No03DB_051.dat` | STS | Magnetic adatom chains on a superconductor | — | 247 | `zenodo/17533355/Fig4/line_No03DB_051.dat/` | True | True |
| `line_No03DB_052.dat` | STS | Magnetic adatom chains on a superconductor | — | 248 | `zenodo/17533355/Fig4/line_No03DB_052.dat/` | True | True |
| `line_No03DB_053.dat` | STS | Magnetic adatom chains on a superconductor | — | 249 | `zenodo/17533355/Fig4/line_No03DB_053.dat/` | True | True |
| `line_No03DB_054.dat` | STS | Magnetic adatom chains on a superconductor | — | 250 | `zenodo/17533355/Fig4/line_No03DB_054.dat/` | True | True |
| `line_No03DB_055.dat` | STS | Magnetic adatom chains on a superconductor | — | 251 | `zenodo/17533355/Fig4/line_No03DB_055.dat/` | True | True |
| `line_No03DB_056.dat` | STS | Magnetic adatom chains on a superconductor | — | 252 | `zenodo/17533355/Fig4/line_No03DB_056.dat/` | True | True |
| `line_No03DB_057.dat` | STS | Magnetic adatom chains on a superconductor | — | 253 | `zenodo/17533355/Fig4/line_No03DB_057.dat/` | True | True |
| `line_No03DE_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 254 | `zenodo/17533355/Fig4/line_No03DE_001.dat/` | True | True |
| `line_No03DE_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 255 | `zenodo/17533355/Fig4/line_No03DE_002.dat/` | True | True |
| `line_No03DE_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 256 | `zenodo/17533355/Fig4/line_No03DE_003.dat/` | True | True |
| `line_No03DE_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 257 | `zenodo/17533355/Fig4/line_No03DE_004.dat/` | True | True |
| `line_No03DE_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 258 | `zenodo/17533355/Fig4/line_No03DE_005.dat/` | True | True |
| `line_No03DE_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 259 | `zenodo/17533355/Fig4/line_No03DE_006.dat/` | True | True |
| `line_No03DE_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 260 | `zenodo/17533355/Fig4/line_No03DE_007.dat/` | True | True |
| `line_No03DE_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 261 | `zenodo/17533355/Fig4/line_No03DE_008.dat/` | True | True |
| `line_No03DE_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 262 | `zenodo/17533355/Fig4/line_No03DE_009.dat/` | True | True |
| `line_No03DE_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 263 | `zenodo/17533355/Fig4/line_No03DE_010.dat/` | True | True |
| `line_No03DE_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 264 | `zenodo/17533355/Fig4/line_No03DE_011.dat/` | True | True |
| `line_No03DE_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 265 | `zenodo/17533355/Fig4/line_No03DE_012.dat/` | True | True |
| `line_No03DE_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 266 | `zenodo/17533355/Fig4/line_No03DE_013.dat/` | True | True |
| `line_No03DE_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 267 | `zenodo/17533355/Fig4/line_No03DE_014.dat/` | True | True |
| `line_No03DE_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 268 | `zenodo/17533355/Fig4/line_No03DE_015.dat/` | True | True |
| `line_No03DE_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 269 | `zenodo/17533355/Fig4/line_No03DE_016.dat/` | True | True |
| `line_No03DE_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 270 | `zenodo/17533355/Fig4/line_No03DE_017.dat/` | True | True |
| `line_No03DE_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 271 | `zenodo/17533355/Fig4/line_No03DE_018.dat/` | True | True |
| `line_No03DE_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 272 | `zenodo/17533355/Fig4/line_No03DE_019.dat/` | True | True |
| `line_No03DE_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 273 | `zenodo/17533355/Fig4/line_No03DE_020.dat/` | True | True |
| `line_No03DE_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 274 | `zenodo/17533355/Fig4/line_No03DE_021.dat/` | True | True |
| `line_No03DE_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 275 | `zenodo/17533355/Fig4/line_No03DE_022.dat/` | True | True |
| `line_No03DE_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 276 | `zenodo/17533355/Fig4/line_No03DE_023.dat/` | True | True |
| `line_No03DE_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 277 | `zenodo/17533355/Fig4/line_No03DE_024.dat/` | True | True |
| `line_No03DE_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 278 | `zenodo/17533355/Fig4/line_No03DE_025.dat/` | True | True |
| `line_No03DE_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 279 | `zenodo/17533355/Fig4/line_No03DE_026.dat/` | True | True |
| `line_No03DE_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 280 | `zenodo/17533355/Fig4/line_No03DE_027.dat/` | True | True |
| `line_No03DE_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 281 | `zenodo/17533355/Fig4/line_No03DE_028.dat/` | True | True |
| `line_No03DE_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 282 | `zenodo/17533355/Fig4/line_No03DE_029.dat/` | True | True |
| `line_No03DE_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 283 | `zenodo/17533355/Fig4/line_No03DE_030.dat/` | True | True |
| `line_No03DE_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 284 | `zenodo/17533355/Fig4/line_No03DE_031.dat/` | True | True |
| `line_No03DE_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 285 | `zenodo/17533355/Fig4/line_No03DE_032.dat/` | True | True |
| `line_No03DE_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 286 | `zenodo/17533355/Fig4/line_No03DE_033.dat/` | True | True |
| `line_No03DE_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 287 | `zenodo/17533355/Fig4/line_No03DE_034.dat/` | True | True |
| `line_No03DE_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 288 | `zenodo/17533355/Fig4/line_No03DE_035.dat/` | True | True |
| `line_No03DE_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 289 | `zenodo/17533355/Fig4/line_No03DE_036.dat/` | True | True |
| `line_No03DE_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 290 | `zenodo/17533355/Fig4/line_No03DE_037.dat/` | True | True |
| `line_No03DE_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 291 | `zenodo/17533355/Fig4/line_No03DE_038.dat/` | True | True |
| `line_No03DE_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 292 | `zenodo/17533355/Fig4/line_No03DE_039.dat/` | True | True |
| `line_No03DE_040.dat` | STS | Magnetic adatom chains on a superconductor | — | 293 | `zenodo/17533355/Fig4/line_No03DE_040.dat/` | True | True |
| `line_No03DE_041.dat` | STS | Magnetic adatom chains on a superconductor | — | 294 | `zenodo/17533355/Fig4/line_No03DE_041.dat/` | True | True |
| `line_No03DE_042.dat` | STS | Magnetic adatom chains on a superconductor | — | 295 | `zenodo/17533355/Fig4/line_No03DE_042.dat/` | True | True |
| `line_No03DE_043.dat` | STS | Magnetic adatom chains on a superconductor | — | 296 | `zenodo/17533355/Fig4/line_No03DE_043.dat/` | True | True |
| `line_No03DE_044.dat` | STS | Magnetic adatom chains on a superconductor | — | 297 | `zenodo/17533355/Fig4/line_No03DE_044.dat/` | True | True |
| `line_No03DE_045.dat` | STS | Magnetic adatom chains on a superconductor | — | 298 | `zenodo/17533355/Fig4/line_No03DE_045.dat/` | True | True |
| `line_No03DE_046.dat` | STS | Magnetic adatom chains on a superconductor | — | 299 | `zenodo/17533355/Fig4/line_No03DE_046.dat/` | True | True |
| `line_No03DE_047.dat` | STS | Magnetic adatom chains on a superconductor | — | 300 | `zenodo/17533355/Fig4/line_No03DE_047.dat/` | True | True |
| `line_No03DE_048.dat` | STS | Magnetic adatom chains on a superconductor | — | 301 | `zenodo/17533355/Fig4/line_No03DE_048.dat/` | True | True |
| `line_No03DE_049.dat` | STS | Magnetic adatom chains on a superconductor | — | 302 | `zenodo/17533355/Fig4/line_No03DE_049.dat/` | True | True |
| `line_No03DE_050.dat` | STS | Magnetic adatom chains on a superconductor | — | 303 | `zenodo/17533355/Fig4/line_No03DE_050.dat/` | True | True |
| `line_No03DE_051.dat` | STS | Magnetic adatom chains on a superconductor | — | 304 | `zenodo/17533355/Fig4/line_No03DE_051.dat/` | True | True |
| `line_No03DE_052.dat` | STS | Magnetic adatom chains on a superconductor | — | 305 | `zenodo/17533355/Fig4/line_No03DE_052.dat/` | True | True |
| `line_No03DE_053.dat` | STS | Magnetic adatom chains on a superconductor | — | 306 | `zenodo/17533355/Fig4/line_No03DE_053.dat/` | True | True |
| `line_No03DE_054.dat` | STS | Magnetic adatom chains on a superconductor | — | 307 | `zenodo/17533355/Fig4/line_No03DE_054.dat/` | True | True |
| `line_No03DE_055.dat` | STS | Magnetic adatom chains on a superconductor | — | 308 | `zenodo/17533355/Fig4/line_No03DE_055.dat/` | True | True |
| `line_No03DE_056.dat` | STS | Magnetic adatom chains on a superconductor | — | 309 | `zenodo/17533355/Fig4/line_No03DE_056.dat/` | True | True |
| `line_No03DE_057.dat` | STS | Magnetic adatom chains on a superconductor | — | 310 | `zenodo/17533355/Fig4/line_No03DE_057.dat/` | True | True |
| `line_No03DE_058.dat` | STS | Magnetic adatom chains on a superconductor | — | 311 | `zenodo/17533355/Fig4/line_No03DE_058.dat/` | True | True |
| `line_No03DE_059.dat` | STS | Magnetic adatom chains on a superconductor | — | 312 | `zenodo/17533355/Fig4/line_No03DE_059.dat/` | True | True |
| `line_No03DE_060.dat` | STS | Magnetic adatom chains on a superconductor | — | 313 | `zenodo/17533355/Fig4/line_No03DE_060.dat/` | True | True |
| `line_No03DE_061.dat` | STS | Magnetic adatom chains on a superconductor | — | 314 | `zenodo/17533355/Fig4/line_No03DE_061.dat/` | True | True |
| `image_272.sxm` | STS | Magnetic adatom chains on a superconductor | — | 315 | `zenodo/17533355/Fig5/image_272.sxm/` | True | True |
| `image_559.sxm` | STS | Magnetic adatom chains on a superconductor | — | 316 | `zenodo/17533355/Fig5/image_559.sxm/` | True | True |
| `line_No03BW_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 317 | `zenodo/17533355/Fig5/line_No03BW_001.dat/` | True | True |
| `line_No03BW_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 318 | `zenodo/17533355/Fig5/line_No03BW_002.dat/` | True | True |
| `line_No03BW_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 319 | `zenodo/17533355/Fig5/line_No03BW_003.dat/` | True | True |
| `line_No03BW_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 320 | `zenodo/17533355/Fig5/line_No03BW_004.dat/` | True | True |
| `line_No03BW_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 321 | `zenodo/17533355/Fig5/line_No03BW_005.dat/` | True | True |
| `line_No03BW_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 322 | `zenodo/17533355/Fig5/line_No03BW_006.dat/` | True | True |
| `line_No03BW_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 323 | `zenodo/17533355/Fig5/line_No03BW_007.dat/` | True | True |
| `line_No03BW_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 324 | `zenodo/17533355/Fig5/line_No03BW_008.dat/` | True | True |
| `line_No03BW_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 325 | `zenodo/17533355/Fig5/line_No03BW_009.dat/` | True | True |
| `line_No03BW_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 326 | `zenodo/17533355/Fig5/line_No03BW_010.dat/` | True | True |
| `line_No03BW_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 327 | `zenodo/17533355/Fig5/line_No03BW_011.dat/` | True | True |
| `line_No03BW_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 328 | `zenodo/17533355/Fig5/line_No03BW_012.dat/` | True | True |
| `line_No03BW_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 329 | `zenodo/17533355/Fig5/line_No03BW_013.dat/` | True | True |
| `line_No03BW_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 330 | `zenodo/17533355/Fig5/line_No03BW_014.dat/` | True | True |
| `line_No03BW_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 331 | `zenodo/17533355/Fig5/line_No03BW_015.dat/` | True | True |
| `line_No03BW_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 332 | `zenodo/17533355/Fig5/line_No03BW_016.dat/` | True | True |
| `line_No03BW_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 333 | `zenodo/17533355/Fig5/line_No03BW_017.dat/` | True | True |
| `line_No03BW_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 334 | `zenodo/17533355/Fig5/line_No03BW_018.dat/` | True | True |
| `line_No03BW_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 335 | `zenodo/17533355/Fig5/line_No03BW_019.dat/` | True | True |
| `line_No03BW_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 336 | `zenodo/17533355/Fig5/line_No03BW_020.dat/` | True | True |
| `line_No03BW_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 337 | `zenodo/17533355/Fig5/line_No03BW_021.dat/` | True | True |
| `line_No03BW_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 338 | `zenodo/17533355/Fig5/line_No03BW_022.dat/` | True | True |
| `line_No03BW_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 339 | `zenodo/17533355/Fig5/line_No03BW_023.dat/` | True | True |
| `line_No03BW_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 340 | `zenodo/17533355/Fig5/line_No03BW_024.dat/` | True | True |
| `line_No03BW_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 341 | `zenodo/17533355/Fig5/line_No03BW_025.dat/` | True | True |
| `line_No03BW_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 342 | `zenodo/17533355/Fig5/line_No03BW_026.dat/` | True | True |
| `line_No03BW_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 343 | `zenodo/17533355/Fig5/line_No03BW_027.dat/` | True | True |
| `line_No03BW_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 344 | `zenodo/17533355/Fig5/line_No03BW_028.dat/` | True | True |
| `line_No03BW_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 345 | `zenodo/17533355/Fig5/line_No03BW_029.dat/` | True | True |
| `line_No03BW_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 346 | `zenodo/17533355/Fig5/line_No03BW_030.dat/` | True | True |
| `line_No03BW_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 347 | `zenodo/17533355/Fig5/line_No03BW_031.dat/` | True | True |
| `line_No03BW_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 348 | `zenodo/17533355/Fig5/line_No03BW_032.dat/` | True | True |
| `line_No03BW_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 349 | `zenodo/17533355/Fig5/line_No03BW_033.dat/` | True | True |
| `line_No03BW_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 350 | `zenodo/17533355/Fig5/line_No03BW_034.dat/` | True | True |
| `line_No03BW_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 351 | `zenodo/17533355/Fig5/line_No03BW_035.dat/` | True | True |
| `line_No03BW_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 352 | `zenodo/17533355/Fig5/line_No03BW_036.dat/` | True | True |
| `line_No03BW_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 353 | `zenodo/17533355/Fig5/line_No03BW_037.dat/` | True | True |
| `line_No03BW_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 354 | `zenodo/17533355/Fig5/line_No03BW_038.dat/` | True | True |
| `line_No03BW_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 355 | `zenodo/17533355/Fig5/line_No03BW_039.dat/` | True | True |
| `line_No03BW_040.dat` | STS | Magnetic adatom chains on a superconductor | — | 356 | `zenodo/17533355/Fig5/line_No03BW_040.dat/` | True | True |
| `line_No03BW_041.dat` | STS | Magnetic adatom chains on a superconductor | — | 357 | `zenodo/17533355/Fig5/line_No03BW_041.dat/` | True | True |
| `line_No03BW_042.dat` | STS | Magnetic adatom chains on a superconductor | — | 358 | `zenodo/17533355/Fig5/line_No03BW_042.dat/` | True | True |
| `line_No03BW_043.dat` | STS | Magnetic adatom chains on a superconductor | — | 359 | `zenodo/17533355/Fig5/line_No03BW_043.dat/` | True | True |
| `line_No03BW_044.dat` | STS | Magnetic adatom chains on a superconductor | — | 360 | `zenodo/17533355/Fig5/line_No03BW_044.dat/` | True | True |
| `line_No03BW_045.dat` | STS | Magnetic adatom chains on a superconductor | — | 361 | `zenodo/17533355/Fig5/line_No03BW_045.dat/` | True | True |
| `line_No03BW_046.dat` | STS | Magnetic adatom chains on a superconductor | — | 362 | `zenodo/17533355/Fig5/line_No03BW_046.dat/` | True | True |
| `line_No03BW_047.dat` | STS | Magnetic adatom chains on a superconductor | — | 363 | `zenodo/17533355/Fig5/line_No03BW_047.dat/` | True | True |
| `line_No03BW_048.dat` | STS | Magnetic adatom chains on a superconductor | — | 364 | `zenodo/17533355/Fig5/line_No03BW_048.dat/` | True | True |
| `line_No03BW_049.dat` | STS | Magnetic adatom chains on a superconductor | — | 365 | `zenodo/17533355/Fig5/line_No03BW_049.dat/` | True | True |
| `line_No03BW_050.dat` | STS | Magnetic adatom chains on a superconductor | — | 366 | `zenodo/17533355/Fig5/line_No03BW_050.dat/` | True | True |
| `line_No03BW_051.dat` | STS | Magnetic adatom chains on a superconductor | — | 367 | `zenodo/17533355/Fig5/line_No03BW_051.dat/` | True | True |
| `line_No03BW_052.dat` | STS | Magnetic adatom chains on a superconductor | — | 368 | `zenodo/17533355/Fig5/line_No03BW_052.dat/` | True | True |
| `line_No03BW_053.dat` | STS | Magnetic adatom chains on a superconductor | — | 369 | `zenodo/17533355/Fig5/line_No03BW_053.dat/` | True | True |
| `line_No03CA_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 370 | `zenodo/17533355/Fig5/line_No03CA_001.dat/` | True | True |
| `line_No03CA_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 371 | `zenodo/17533355/Fig5/line_No03CA_002.dat/` | True | True |
| `line_No03CA_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 372 | `zenodo/17533355/Fig5/line_No03CA_003.dat/` | True | True |
| `line_No03CA_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 373 | `zenodo/17533355/Fig5/line_No03CA_004.dat/` | True | True |
| `line_No03CA_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 374 | `zenodo/17533355/Fig5/line_No03CA_005.dat/` | True | True |
| `line_No03CA_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 375 | `zenodo/17533355/Fig5/line_No03CA_006.dat/` | True | True |
| `line_No03CA_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 376 | `zenodo/17533355/Fig5/line_No03CA_007.dat/` | True | True |
| `line_No03CA_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 377 | `zenodo/17533355/Fig5/line_No03CA_008.dat/` | True | True |
| `line_No03CA_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 378 | `zenodo/17533355/Fig5/line_No03CA_009.dat/` | True | True |
| `line_No03CA_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 379 | `zenodo/17533355/Fig5/line_No03CA_010.dat/` | True | True |
| `line_No03CA_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 380 | `zenodo/17533355/Fig5/line_No03CA_011.dat/` | True | True |
| `line_No03CA_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 381 | `zenodo/17533355/Fig5/line_No03CA_012.dat/` | True | True |
| `line_No03CA_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 382 | `zenodo/17533355/Fig5/line_No03CA_013.dat/` | True | True |
| `line_No03CA_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 383 | `zenodo/17533355/Fig5/line_No03CA_014.dat/` | True | True |
| `line_No03CA_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 384 | `zenodo/17533355/Fig5/line_No03CA_015.dat/` | True | True |
| `line_No03CA_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 385 | `zenodo/17533355/Fig5/line_No03CA_016.dat/` | True | True |
| `line_No03CA_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 386 | `zenodo/17533355/Fig5/line_No03CA_017.dat/` | True | True |
| `line_No03CA_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 387 | `zenodo/17533355/Fig5/line_No03CA_018.dat/` | True | True |
| `line_No03CA_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 388 | `zenodo/17533355/Fig5/line_No03CA_019.dat/` | True | True |
| `line_No03CA_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 389 | `zenodo/17533355/Fig5/line_No03CA_020.dat/` | True | True |
| `line_No03CA_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 390 | `zenodo/17533355/Fig5/line_No03CA_021.dat/` | True | True |
| `line_No03CA_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 391 | `zenodo/17533355/Fig5/line_No03CA_022.dat/` | True | True |
| `line_No03CA_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 392 | `zenodo/17533355/Fig5/line_No03CA_023.dat/` | True | True |
| `line_No03CA_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 393 | `zenodo/17533355/Fig5/line_No03CA_024.dat/` | True | True |
| `line_No03CA_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 394 | `zenodo/17533355/Fig5/line_No03CA_025.dat/` | True | True |
| `line_No03CA_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 395 | `zenodo/17533355/Fig5/line_No03CA_026.dat/` | True | True |
| `line_No03CA_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 396 | `zenodo/17533355/Fig5/line_No03CA_027.dat/` | True | True |
| `line_No03CA_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 397 | `zenodo/17533355/Fig5/line_No03CA_028.dat/` | True | True |
| `line_No03CA_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 398 | `zenodo/17533355/Fig5/line_No03CA_029.dat/` | True | True |
| `line_No03CA_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 399 | `zenodo/17533355/Fig5/line_No03CA_030.dat/` | True | True |
| `line_No03CA_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 400 | `zenodo/17533355/Fig5/line_No03CA_031.dat/` | True | True |
| `line_No03CA_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 401 | `zenodo/17533355/Fig5/line_No03CA_032.dat/` | True | True |
| `line_No03CA_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 402 | `zenodo/17533355/Fig5/line_No03CA_033.dat/` | True | True |
| `line_No03CA_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 403 | `zenodo/17533355/Fig5/line_No03CA_034.dat/` | True | True |
| `line_No03CA_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 404 | `zenodo/17533355/Fig5/line_No03CA_035.dat/` | True | True |
| `line_No03CA_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 405 | `zenodo/17533355/Fig5/line_No03CA_036.dat/` | True | True |
| `line_No03CA_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 406 | `zenodo/17533355/Fig5/line_No03CA_037.dat/` | True | True |
| `line_No03CA_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 407 | `zenodo/17533355/Fig5/line_No03CA_038.dat/` | True | True |
| `line_No03CA_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 408 | `zenodo/17533355/Fig5/line_No03CA_039.dat/` | True | True |
| `line_No03CA_040.dat` | STS | Magnetic adatom chains on a superconductor | — | 409 | `zenodo/17533355/Fig5/line_No03CA_040.dat/` | True | True |
| `line_No03CA_041.dat` | STS | Magnetic adatom chains on a superconductor | — | 410 | `zenodo/17533355/Fig5/line_No03CA_041.dat/` | True | True |
| `line_No03CA_042.dat` | STS | Magnetic adatom chains on a superconductor | — | 411 | `zenodo/17533355/Fig5/line_No03CA_042.dat/` | True | True |
| `line_No03CA_043.dat` | STS | Magnetic adatom chains on a superconductor | — | 412 | `zenodo/17533355/Fig5/line_No03CA_043.dat/` | True | True |
| `line_No03CA_044.dat` | STS | Magnetic adatom chains on a superconductor | — | 413 | `zenodo/17533355/Fig5/line_No03CA_044.dat/` | True | True |
| `line_No03CA_045.dat` | STS | Magnetic adatom chains on a superconductor | — | 414 | `zenodo/17533355/Fig5/line_No03CA_045.dat/` | True | True |
| `line_No03CA_046.dat` | STS | Magnetic adatom chains on a superconductor | — | 415 | `zenodo/17533355/Fig5/line_No03CA_046.dat/` | True | True |
| `line_No03CA_047.dat` | STS | Magnetic adatom chains on a superconductor | — | 416 | `zenodo/17533355/Fig5/line_No03CA_047.dat/` | True | True |
| `line_No03CA_048.dat` | STS | Magnetic adatom chains on a superconductor | — | 417 | `zenodo/17533355/Fig5/line_No03CA_048.dat/` | True | True |
| `line_No03CA_049.dat` | STS | Magnetic adatom chains on a superconductor | — | 418 | `zenodo/17533355/Fig5/line_No03CA_049.dat/` | True | True |
| `line_No03CA_050.dat` | STS | Magnetic adatom chains on a superconductor | — | 419 | `zenodo/17533355/Fig5/line_No03CA_050.dat/` | True | True |
| `line_No03CA_051.dat` | STS | Magnetic adatom chains on a superconductor | — | 420 | `zenodo/17533355/Fig5/line_No03CA_051.dat/` | True | True |
| `line_No03CA_052.dat` | STS | Magnetic adatom chains on a superconductor | — | 421 | `zenodo/17533355/Fig5/line_No03CA_052.dat/` | True | True |
| `line_No03CA_053.dat` | STS | Magnetic adatom chains on a superconductor | — | 422 | `zenodo/17533355/Fig5/line_No03CA_053.dat/` | True | True |
| `line_No03CA_054.dat` | STS | Magnetic adatom chains on a superconductor | — | 423 | `zenodo/17533355/Fig5/line_No03CA_054.dat/` | True | True |
| `line_No03CA_055.dat` | STS | Magnetic adatom chains on a superconductor | — | 424 | `zenodo/17533355/Fig5/line_No03CA_055.dat/` | True | True |
| `line_No03CA_056.dat` | STS | Magnetic adatom chains on a superconductor | — | 425 | `zenodo/17533355/Fig5/line_No03CA_056.dat/` | True | True |
| `line_No03CA_057.dat` | STS | Magnetic adatom chains on a superconductor | — | 426 | `zenodo/17533355/Fig5/line_No03CA_057.dat/` | True | True |
| `line_No03CA_058.dat` | STS | Magnetic adatom chains on a superconductor | — | 427 | `zenodo/17533355/Fig5/line_No03CA_058.dat/` | True | True |
| `line_No03CA_059.dat` | STS | Magnetic adatom chains on a superconductor | — | 428 | `zenodo/17533355/Fig5/line_No03CA_059.dat/` | True | True |
| `line_No03CA_060.dat` | STS | Magnetic adatom chains on a superconductor | — | 429 | `zenodo/17533355/Fig5/line_No03CA_060.dat/` | True | True |
| `line_No03CA_061.dat` | STS | Magnetic adatom chains on a superconductor | — | 430 | `zenodo/17533355/Fig5/line_No03CA_061.dat/` | True | True |
| `line_No03CA_062.dat` | STS | Magnetic adatom chains on a superconductor | — | 431 | `zenodo/17533355/Fig5/line_No03CA_062.dat/` | True | True |
| `line_No03CA_063.dat` | STS | Magnetic adatom chains on a superconductor | — | 432 | `zenodo/17533355/Fig5/line_No03CA_063.dat/` | True | True |
| `line_No03CA_064.dat` | STS | Magnetic adatom chains on a superconductor | — | 433 | `zenodo/17533355/Fig5/line_No03CA_064.dat/` | True | True |
| `line_No03CA_065.dat` | STS | Magnetic adatom chains on a superconductor | — | 434 | `zenodo/17533355/Fig5/line_No03CA_065.dat/` | True | True |
| `line_No03CA_066.dat` | STS | Magnetic adatom chains on a superconductor | — | 435 | `zenodo/17533355/Fig5/line_No03CA_066.dat/` | True | True |
| `dIdV_No08_029.sxm` | STS | Magnetic adatom chains on a superconductor | — | 436 | `zenodo/17533355/FigS1/dIdV_No08_029.sxm/` | True | True |
| `dIdV_No08_035.sxm` | STS | Magnetic adatom chains on a superconductor | — | 437 | `zenodo/17533355/FigS1/dIdV_No08_035.sxm/` | True | True |
| `cloud_No01AC_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 438 | `zenodo/17533355/FigS2/cloud_No01AC_001.dat/` | True | True |
| `cloud_No01AC_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 439 | `zenodo/17533355/FigS2/cloud_No01AC_002.dat/` | True | True |
| `cloud_No01AE_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 440 | `zenodo/17533355/FigS2/cloud_No01AE_001.dat/` | True | True |
| `cloud_No01AE_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 441 | `zenodo/17533355/FigS2/cloud_No01AE_002.dat/` | True | True |
| `cloud_No01AE_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 442 | `zenodo/17533355/FigS2/cloud_No01AE_003.dat/` | True | True |
| `cloud_No01AE_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 443 | `zenodo/17533355/FigS2/cloud_No01AE_004.dat/` | True | True |
| `image_051.sxm` | STS | Magnetic adatom chains on a superconductor | — | 444 | `zenodo/17533355/FigS2/image_051.sxm/` | True | True |
| `image_059.sxm` | STS | Magnetic adatom chains on a superconductor | — | 445 | `zenodo/17533355/FigS2/image_059.sxm/` | True | True |
| `image_078.sxm` | STS | Magnetic adatom chains on a superconductor | — | 446 | `zenodo/17533355/FigS3/image_078.sxm/` | True | True |
| `image_084.sxm` | STS | Magnetic adatom chains on a superconductor | — | 447 | `zenodo/17533355/FigS3/image_084.sxm/` | True | True |
| `line_No14AL_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 448 | `zenodo/17533355/FigS3/line_No14AL_001.dat/` | True | True |
| `line_No14AL_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 449 | `zenodo/17533355/FigS3/line_No14AL_018.dat/` | True | True |
| `line_No14AO_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 450 | `zenodo/17533355/FigS3/line_No14AO_001.dat/` | True | True |
| `line_No14AO_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 451 | `zenodo/17533355/FigS3/line_No14AO_019.dat/` | True | True |
| `line_No14AO_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 452 | `zenodo/17533355/FigS3/line_No14AO_024.dat/` | True | True |
| `const_dos_No14_001.sxm` | STS | Magnetic adatom chains on a superconductor | — | 453 | `zenodo/17533355/FigS4/const_dos_No14_001.sxm/` | True | True |
| `const_dos_No14_002.sxm` | STS | Magnetic adatom chains on a superconductor | — | 454 | `zenodo/17533355/FigS4/const_dos_No14_002.sxm/` | True | True |
| `const_dos_No14_003.sxm` | STS | Magnetic adatom chains on a superconductor | — | 455 | `zenodo/17533355/FigS4/const_dos_No14_003.sxm/` | True | True |
| `const_dos_No14_008.sxm` | STS | Magnetic adatom chains on a superconductor | — | 456 | `zenodo/17533355/FigS4/const_dos_No14_008.sxm/` | True | True |
| `const_dos_No14_019.sxm` | STS | Magnetic adatom chains on a superconductor | — | 457 | `zenodo/17533355/FigS4/const_dos_No14_019.sxm/` | True | True |
| `const_dos_No14_061.sxm` | STS | Magnetic adatom chains on a superconductor | — | 458 | `zenodo/17533355/FigS4/const_dos_No14_061.sxm/` | True | True |
| `const_dos_No14_063.sxm` | STS | Magnetic adatom chains on a superconductor | — | 459 | `zenodo/17533355/FigS4/const_dos_No14_063.sxm/` | True | True |
| `const_dos_No14_067.sxm` | STS | Magnetic adatom chains on a superconductor | — | 460 | `zenodo/17533355/FigS4/const_dos_No14_067.sxm/` | True | True |
| `const_dos_No14_076.sxm` | STS | Magnetic adatom chains on a superconductor | — | 461 | `zenodo/17533355/FigS4/const_dos_No14_076.sxm/` | True | True |
| `const_dos_No14_077.sxm` | STS | Magnetic adatom chains on a superconductor | — | 462 | `zenodo/17533355/FigS4/const_dos_No14_077.sxm/` | True | True |
| `const_dos_No14_078.sxm` | STS | Magnetic adatom chains on a superconductor | — | 463 | `zenodo/17533355/FigS4/const_dos_No14_078.sxm/` | True | True |
| `const_dos_No14_079.sxm` | STS | Magnetic adatom chains on a superconductor | — | 464 | `zenodo/17533355/FigS4/const_dos_No14_079.sxm/` | True | True |
| `const_dos_No14_083.sxm` | STS | Magnetic adatom chains on a superconductor | — | 465 | `zenodo/17533355/FigS4/const_dos_No14_083.sxm/` | True | True |
| `const_dos_No14_093.sxm` | STS | Magnetic adatom chains on a superconductor | — | 466 | `zenodo/17533355/FigS4/const_dos_No14_093.sxm/` | True | True |
| `image_264.sxm` | STS | Magnetic adatom chains on a superconductor | — | 467 | `zenodo/17533355/FigS4/image_264.sxm/` | True | True |
| `image_288.sxm` | STS | Magnetic adatom chains on a superconductor | — | 468 | `zenodo/17533355/FigS4/image_288.sxm/` | True | True |
| `image_295.sxm` | STS | Magnetic adatom chains on a superconductor | — | 469 | `zenodo/17533355/FigS4/image_295.sxm/` | True | True |
| `const_dos_No03_001.sxm` | STS | Magnetic adatom chains on a superconductor | — | 470 | `zenodo/17533355/FigS5/const_dos_No03_001.sxm/` | True | True |
| `const_dos_No03_002.sxm` | STS | Magnetic adatom chains on a superconductor | — | 471 | `zenodo/17533355/FigS5/const_dos_No03_002.sxm/` | True | True |
| `const_dos_No03_003.sxm` | STS | Magnetic adatom chains on a superconductor | — | 472 | `zenodo/17533355/FigS5/const_dos_No03_003.sxm/` | True | True |
| `const_dos_No03_004.sxm` | STS | Magnetic adatom chains on a superconductor | — | 473 | `zenodo/17533355/FigS5/const_dos_No03_004.sxm/` | True | True |
| `const_dos_No03_006.sxm` | STS | Magnetic adatom chains on a superconductor | — | 474 | `zenodo/17533355/FigS5/const_dos_No03_006.sxm/` | True | True |
| `const_dos_No03_009.sxm` | STS | Magnetic adatom chains on a superconductor | — | 475 | `zenodo/17533355/FigS5/const_dos_No03_009.sxm/` | True | True |
| `const_dos_No03_028.sxm` | STS | Magnetic adatom chains on a superconductor | — | 476 | `zenodo/17533355/FigS5/const_dos_No03_028.sxm/` | True | True |
| `const_dos_No03_031.sxm` | STS | Magnetic adatom chains on a superconductor | — | 477 | `zenodo/17533355/FigS5/const_dos_No03_031.sxm/` | True | True |
| `const_dos_No03_033.sxm` | STS | Magnetic adatom chains on a superconductor | — | 478 | `zenodo/17533355/FigS5/const_dos_No03_033.sxm/` | True | True |
| `const_dos_No03_035.sxm` | STS | Magnetic adatom chains on a superconductor | — | 479 | `zenodo/17533355/FigS5/const_dos_No03_035.sxm/` | True | True |
| `const_dos_No03_036.sxm` | STS | Magnetic adatom chains on a superconductor | — | 480 | `zenodo/17533355/FigS5/const_dos_No03_036.sxm/` | True | True |
| `const_dos_No03_039.sxm` | STS | Magnetic adatom chains on a superconductor | — | 481 | `zenodo/17533355/FigS5/const_dos_No03_039.sxm/` | True | True |
| `const_dos_No03_040.sxm` | STS | Magnetic adatom chains on a superconductor | — | 482 | `zenodo/17533355/FigS5/const_dos_No03_040.sxm/` | True | True |
| `image_220.sxm` | STS | Magnetic adatom chains on a superconductor | — | 483 | `zenodo/17533355/FigS5/image_220.sxm/` | True | True |
| `image_230.sxm` | STS | Magnetic adatom chains on a superconductor | — | 484 | `zenodo/17533355/FigS5/image_230.sxm/` | True | True |
| `image_234.sxm` | STS | Magnetic adatom chains on a superconductor | — | 485 | `zenodo/17533355/FigS5/image_234.sxm/` | True | True |
| `cloud_No02AY_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 486 | `zenodo/17533355/FigS6/cloud_No02AY_001.dat/` | True | True |
| `cloud_No02AY_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 487 | `zenodo/17533355/FigS6/cloud_No02AY_002.dat/` | True | True |
| `cloud_No02AY_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 488 | `zenodo/17533355/FigS6/cloud_No02AY_003.dat/` | True | True |
| `cloud_No08CB_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 489 | `zenodo/17533355/FigS6/cloud_No08CB_001.dat/` | True | True |
| `cloud_No08CB_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 490 | `zenodo/17533355/FigS6/cloud_No08CB_002.dat/` | True | True |
| `cloud_No08CB_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 491 | `zenodo/17533355/FigS6/cloud_No08CB_003.dat/` | True | True |
| `cloud_No08CC_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 492 | `zenodo/17533355/FigS6/cloud_No08CC_001.dat/` | True | True |
| `cloud_No08CC_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 493 | `zenodo/17533355/FigS6/cloud_No08CC_002.dat/` | True | True |
| `cloud_No08CC_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 494 | `zenodo/17533355/FigS6/cloud_No08CC_003.dat/` | True | True |
| `cloud_No08CC_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 495 | `zenodo/17533355/FigS6/cloud_No08CC_004.dat/` | True | True |
| `cloud_No08CC_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 496 | `zenodo/17533355/FigS6/cloud_No08CC_005.dat/` | True | True |
| `cloud_No08CC_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 497 | `zenodo/17533355/FigS6/cloud_No08CC_006.dat/` | True | True |
| `cloud_No08CC_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 498 | `zenodo/17533355/FigS6/cloud_No08CC_007.dat/` | True | True |
| `cloud_No08CC_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 499 | `zenodo/17533355/FigS6/cloud_No08CC_008.dat/` | True | True |
| `cloud_No08CC_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 500 | `zenodo/17533355/FigS6/cloud_No08CC_009.dat/` | True | True |
| `image_074.sxm` | STS | Magnetic adatom chains on a superconductor | — | 501 | `zenodo/17533355/FigS6/image_074.sxm/` | True | True |
| `image_745.sxm` | STS | Magnetic adatom chains on a superconductor | — | 502 | `zenodo/17533355/FigS6/image_745.sxm/` | True | True |
| `line_No02AZ_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 503 | `zenodo/17533355/FigS6/line_No02AZ_001.dat/` | True | True |
| `line_No02AZ_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 504 | `zenodo/17533355/FigS6/line_No02AZ_002.dat/` | True | True |
| `line_No02AZ_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 505 | `zenodo/17533355/FigS6/line_No02AZ_003.dat/` | True | True |
| `line_No02AZ_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 506 | `zenodo/17533355/FigS6/line_No02AZ_004.dat/` | True | True |
| `line_No02AZ_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 507 | `zenodo/17533355/FigS6/line_No02AZ_005.dat/` | True | True |
| `line_No02AZ_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 508 | `zenodo/17533355/FigS6/line_No02AZ_006.dat/` | True | True |
| `line_No02AZ_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 509 | `zenodo/17533355/FigS6/line_No02AZ_007.dat/` | True | True |
| `line_No02AZ_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 510 | `zenodo/17533355/FigS6/line_No02AZ_008.dat/` | True | True |
| `line_No02AZ_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 511 | `zenodo/17533355/FigS6/line_No02AZ_009.dat/` | True | True |
| `line_No02AZ_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 512 | `zenodo/17533355/FigS6/line_No02AZ_010.dat/` | True | True |
| `line_No02AZ_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 513 | `zenodo/17533355/FigS6/line_No02AZ_011.dat/` | True | True |
| `line_No02AZ_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 514 | `zenodo/17533355/FigS6/line_No02AZ_012.dat/` | True | True |
| `line_No02AZ_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 515 | `zenodo/17533355/FigS6/line_No02AZ_013.dat/` | True | True |
| `line_No02AZ_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 516 | `zenodo/17533355/FigS6/line_No02AZ_014.dat/` | True | True |
| `line_No02AZ_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 517 | `zenodo/17533355/FigS6/line_No02AZ_015.dat/` | True | True |
| `line_No02AZ_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 518 | `zenodo/17533355/FigS6/line_No02AZ_016.dat/` | True | True |
| `line_No02AZ_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 519 | `zenodo/17533355/FigS6/line_No02AZ_017.dat/` | True | True |
| `line_No02AZ_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 520 | `zenodo/17533355/FigS6/line_No02AZ_018.dat/` | True | True |
| `line_No02AZ_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 521 | `zenodo/17533355/FigS6/line_No02AZ_019.dat/` | True | True |
| `line_No02AZ_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 522 | `zenodo/17533355/FigS6/line_No02AZ_020.dat/` | True | True |
| `line_No02AZ_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 523 | `zenodo/17533355/FigS6/line_No02AZ_021.dat/` | True | True |
| `line_No02AZ_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 524 | `zenodo/17533355/FigS6/line_No02AZ_022.dat/` | True | True |
| `line_No02AZ_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 525 | `zenodo/17533355/FigS6/line_No02AZ_023.dat/` | True | True |
| `line_No02AZ_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 526 | `zenodo/17533355/FigS6/line_No02AZ_024.dat/` | True | True |
| `line_No02AZ_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 527 | `zenodo/17533355/FigS6/line_No02AZ_025.dat/` | True | True |
| `line_No02AZ_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 528 | `zenodo/17533355/FigS6/line_No02AZ_026.dat/` | True | True |
| `line_No02AZ_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 529 | `zenodo/17533355/FigS6/line_No02AZ_027.dat/` | True | True |
| `line_No02AZ_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 530 | `zenodo/17533355/FigS6/line_No02AZ_028.dat/` | True | True |
| `line_No02AZ_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 531 | `zenodo/17533355/FigS6/line_No02AZ_029.dat/` | True | True |
| `line_No02AZ_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 532 | `zenodo/17533355/FigS6/line_No02AZ_030.dat/` | True | True |
| `line_No02AZ_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 533 | `zenodo/17533355/FigS6/line_No02AZ_031.dat/` | True | True |
| `line_No02AZ_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 534 | `zenodo/17533355/FigS6/line_No02AZ_032.dat/` | True | True |
| `line_No02AZ_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 535 | `zenodo/17533355/FigS6/line_No02AZ_033.dat/` | True | True |
| `line_No02AZ_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 536 | `zenodo/17533355/FigS6/line_No02AZ_034.dat/` | True | True |
| `line_No02AZ_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 537 | `zenodo/17533355/FigS6/line_No02AZ_035.dat/` | True | True |
| `line_No02AZ_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 538 | `zenodo/17533355/FigS6/line_No02AZ_036.dat/` | True | True |
| `line_No02AZ_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 539 | `zenodo/17533355/FigS6/line_No02AZ_037.dat/` | True | True |
| `line_No02AZ_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 540 | `zenodo/17533355/FigS6/line_No02AZ_038.dat/` | True | True |
| `line_No02AZ_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 541 | `zenodo/17533355/FigS6/line_No02AZ_039.dat/` | True | True |
| `BiasSpec_042.dat` | STS | Magnetic adatom chains on a superconductor | — | 542 | `zenodo/17533355/FigS8/BiasSpec_042.dat/` | True | True |
| `BiasSpec_046.dat` | STS | Magnetic adatom chains on a superconductor | — | 543 | `zenodo/17533355/FigS8/BiasSpec_046.dat/` | True | True |
| `cloud_No08AS_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 544 | `zenodo/17533355/FigS8/cloud_No08AS_004.dat/` | True | True |
| `cloud_No08AY_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 545 | `zenodo/17533355/FigS8/cloud_No08AY_002.dat/` | True | True |
| `image_120.sxm` | STS | Magnetic adatom chains on a superconductor | — | 546 | `zenodo/17533355/FigS8/image_120.sxm/` | True | True |
| `image_123.sxm` | STS | Magnetic adatom chains on a superconductor | — | 547 | `zenodo/17533355/FigS8/image_123.sxm/` | True | True |
| `image_165.sxm` | STS | Magnetic adatom chains on a superconductor | — | 548 | `zenodo/17533355/FigS8/image_165.sxm/` | True | True |
| `image_166.sxm` | STS | Magnetic adatom chains on a superconductor | — | 549 | `zenodo/17533355/FigS8/image_166.sxm/` | True | True |
| `image_168.sxm` | STS | Magnetic adatom chains on a superconductor | — | 550 | `zenodo/17533355/FigS8/image_168.sxm/` | True | True |
| `image_192.sxm` | STS | Magnetic adatom chains on a superconductor | — | 551 | `zenodo/17533355/FigS8/image_192.sxm/` | True | True |
| `image_194.sxm` | STS | Magnetic adatom chains on a superconductor | — | 552 | `zenodo/17533355/FigS8/image_194.sxm/` | True | True |
| `cloud_No08EH_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 553 | `zenodo/17533355/FigS9/cloud_No08EH_001.dat/` | True | True |
| `cloud_No08EH_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 554 | `zenodo/17533355/FigS9/cloud_No08EH_002.dat/` | True | True |
| `cloud_No08EH_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 555 | `zenodo/17533355/FigS9/cloud_No08EH_003.dat/` | True | True |
| `cloud_No08EH_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 556 | `zenodo/17533355/FigS9/cloud_No08EH_004.dat/` | True | True |
| `cloud_No08EH_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 557 | `zenodo/17533355/FigS9/cloud_No08EH_005.dat/` | True | True |
| `cloud_No08EH_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 558 | `zenodo/17533355/FigS9/cloud_No08EH_006.dat/` | True | True |
| `cloud_No08EH_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 559 | `zenodo/17533355/FigS9/cloud_No08EH_007.dat/` | True | True |
| `cloud_No08EH_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 560 | `zenodo/17533355/FigS9/cloud_No08EH_008.dat/` | True | True |
| `cloud_No08EH_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 561 | `zenodo/17533355/FigS9/cloud_No08EH_009.dat/` | True | True |
| `cloud_No08EH_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 562 | `zenodo/17533355/FigS9/cloud_No08EH_010.dat/` | True | True |
| `cloud_No08EH_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 563 | `zenodo/17533355/FigS9/cloud_No08EH_011.dat/` | True | True |
| `cloud_No08EH_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 564 | `zenodo/17533355/FigS9/cloud_No08EH_012.dat/` | True | True |
| `cloud_No08EH_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 565 | `zenodo/17533355/FigS9/cloud_No08EH_013.dat/` | True | True |
| `cloud_No08EH_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 566 | `zenodo/17533355/FigS9/cloud_No08EH_014.dat/` | True | True |
| `cloud_No08EH_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 567 | `zenodo/17533355/FigS9/cloud_No08EH_015.dat/` | True | True |
| `cloud_No08EH_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 568 | `zenodo/17533355/FigS9/cloud_No08EH_016.dat/` | True | True |
| `cloud_No08EH_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 569 | `zenodo/17533355/FigS9/cloud_No08EH_017.dat/` | True | True |
| `cloud_No08EH_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 570 | `zenodo/17533355/FigS9/cloud_No08EH_018.dat/` | True | True |
| `cloud_No08EH_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 571 | `zenodo/17533355/FigS9/cloud_No08EH_019.dat/` | True | True |
| `cloud_No08EH_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 572 | `zenodo/17533355/FigS9/cloud_No08EH_020.dat/` | True | True |
| `cloud_No08EH_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 573 | `zenodo/17533355/FigS9/cloud_No08EH_021.dat/` | True | True |
| `cloud_No08EH_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 574 | `zenodo/17533355/FigS9/cloud_No08EH_022.dat/` | True | True |
| `cloud_No08EH_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 575 | `zenodo/17533355/FigS9/cloud_No08EH_023.dat/` | True | True |
| `cloud_No08EH_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 576 | `zenodo/17533355/FigS9/cloud_No08EH_024.dat/` | True | True |
| `cloud_No08EH_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 577 | `zenodo/17533355/FigS9/cloud_No08EH_025.dat/` | True | True |
| `cloud_No08EH_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 578 | `zenodo/17533355/FigS9/cloud_No08EH_026.dat/` | True | True |
| `cloud_No08EH_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 579 | `zenodo/17533355/FigS9/cloud_No08EH_027.dat/` | True | True |
| `cloud_No08EH_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 580 | `zenodo/17533355/FigS9/cloud_No08EH_028.dat/` | True | True |
| `cloud_No08EH_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 581 | `zenodo/17533355/FigS9/cloud_No08EH_029.dat/` | True | True |
| `cloud_No08EH_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 582 | `zenodo/17533355/FigS9/cloud_No08EH_030.dat/` | True | True |
| `cloud_No08EH_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 583 | `zenodo/17533355/FigS9/cloud_No08EH_031.dat/` | True | True |
| `cloud_No08EH_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 584 | `zenodo/17533355/FigS9/cloud_No08EH_032.dat/` | True | True |
| `cloud_No08EH_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 585 | `zenodo/17533355/FigS9/cloud_No08EH_033.dat/` | True | True |
| `cloud_No08EH_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 586 | `zenodo/17533355/FigS9/cloud_No08EH_034.dat/` | True | True |
| `cloud_No08EH_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 587 | `zenodo/17533355/FigS9/cloud_No08EH_035.dat/` | True | True |
| `cloud_No08EH_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 588 | `zenodo/17533355/FigS9/cloud_No08EH_036.dat/` | True | True |
| `cloud_No08EH_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 589 | `zenodo/17533355/FigS9/cloud_No08EH_037.dat/` | True | True |
| `cloud_No08EH_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 590 | `zenodo/17533355/FigS9/cloud_No08EH_038.dat/` | True | True |
| `cloud_No08EH_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 591 | `zenodo/17533355/FigS9/cloud_No08EH_039.dat/` | True | True |
| `cloud_No08EH_040.dat` | STS | Magnetic adatom chains on a superconductor | — | 592 | `zenodo/17533355/FigS9/cloud_No08EH_040.dat/` | True | True |
| `cloud_No08EH_041.dat` | STS | Magnetic adatom chains on a superconductor | — | 593 | `zenodo/17533355/FigS9/cloud_No08EH_041.dat/` | True | True |
| `cloud_No08EI_001.dat` | STS | Magnetic adatom chains on a superconductor | — | 594 | `zenodo/17533355/FigS9/cloud_No08EI_001.dat/` | True | True |
| `cloud_No08EI_002.dat` | STS | Magnetic adatom chains on a superconductor | — | 595 | `zenodo/17533355/FigS9/cloud_No08EI_002.dat/` | True | True |
| `cloud_No08EI_003.dat` | STS | Magnetic adatom chains on a superconductor | — | 596 | `zenodo/17533355/FigS9/cloud_No08EI_003.dat/` | True | True |
| `cloud_No08EI_004.dat` | STS | Magnetic adatom chains on a superconductor | — | 597 | `zenodo/17533355/FigS9/cloud_No08EI_004.dat/` | True | True |
| `cloud_No08EI_005.dat` | STS | Magnetic adatom chains on a superconductor | — | 598 | `zenodo/17533355/FigS9/cloud_No08EI_005.dat/` | True | True |
| `cloud_No08EI_006.dat` | STS | Magnetic adatom chains on a superconductor | — | 599 | `zenodo/17533355/FigS9/cloud_No08EI_006.dat/` | True | True |
| `cloud_No08EI_007.dat` | STS | Magnetic adatom chains on a superconductor | — | 600 | `zenodo/17533355/FigS9/cloud_No08EI_007.dat/` | True | True |
| `cloud_No08EI_008.dat` | STS | Magnetic adatom chains on a superconductor | — | 601 | `zenodo/17533355/FigS9/cloud_No08EI_008.dat/` | True | True |
| `cloud_No08EI_009.dat` | STS | Magnetic adatom chains on a superconductor | — | 602 | `zenodo/17533355/FigS9/cloud_No08EI_009.dat/` | True | True |
| `cloud_No08EI_010.dat` | STS | Magnetic adatom chains on a superconductor | — | 603 | `zenodo/17533355/FigS9/cloud_No08EI_010.dat/` | True | True |
| `cloud_No08EI_011.dat` | STS | Magnetic adatom chains on a superconductor | — | 604 | `zenodo/17533355/FigS9/cloud_No08EI_011.dat/` | True | True |
| `cloud_No08EI_012.dat` | STS | Magnetic adatom chains on a superconductor | — | 605 | `zenodo/17533355/FigS9/cloud_No08EI_012.dat/` | True | True |
| `cloud_No08EI_013.dat` | STS | Magnetic adatom chains on a superconductor | — | 606 | `zenodo/17533355/FigS9/cloud_No08EI_013.dat/` | True | True |
| `cloud_No08EI_014.dat` | STS | Magnetic adatom chains on a superconductor | — | 607 | `zenodo/17533355/FigS9/cloud_No08EI_014.dat/` | True | True |
| `cloud_No08EI_015.dat` | STS | Magnetic adatom chains on a superconductor | — | 608 | `zenodo/17533355/FigS9/cloud_No08EI_015.dat/` | True | True |
| `cloud_No08EI_016.dat` | STS | Magnetic adatom chains on a superconductor | — | 609 | `zenodo/17533355/FigS9/cloud_No08EI_016.dat/` | True | True |
| `cloud_No08EI_017.dat` | STS | Magnetic adatom chains on a superconductor | — | 610 | `zenodo/17533355/FigS9/cloud_No08EI_017.dat/` | True | True |
| `cloud_No08EI_018.dat` | STS | Magnetic adatom chains on a superconductor | — | 611 | `zenodo/17533355/FigS9/cloud_No08EI_018.dat/` | True | True |
| `cloud_No08EI_019.dat` | STS | Magnetic adatom chains on a superconductor | — | 612 | `zenodo/17533355/FigS9/cloud_No08EI_019.dat/` | True | True |
| `cloud_No08EI_020.dat` | STS | Magnetic adatom chains on a superconductor | — | 613 | `zenodo/17533355/FigS9/cloud_No08EI_020.dat/` | True | True |
| `cloud_No08EI_021.dat` | STS | Magnetic adatom chains on a superconductor | — | 614 | `zenodo/17533355/FigS9/cloud_No08EI_021.dat/` | True | True |
| `cloud_No08EI_022.dat` | STS | Magnetic adatom chains on a superconductor | — | 615 | `zenodo/17533355/FigS9/cloud_No08EI_022.dat/` | True | True |
| `cloud_No08EI_023.dat` | STS | Magnetic adatom chains on a superconductor | — | 616 | `zenodo/17533355/FigS9/cloud_No08EI_023.dat/` | True | True |
| `cloud_No08EI_024.dat` | STS | Magnetic adatom chains on a superconductor | — | 617 | `zenodo/17533355/FigS9/cloud_No08EI_024.dat/` | True | True |
| `cloud_No08EI_025.dat` | STS | Magnetic adatom chains on a superconductor | — | 618 | `zenodo/17533355/FigS9/cloud_No08EI_025.dat/` | True | True |
| `cloud_No08EI_026.dat` | STS | Magnetic adatom chains on a superconductor | — | 619 | `zenodo/17533355/FigS9/cloud_No08EI_026.dat/` | True | True |
| `cloud_No08EI_027.dat` | STS | Magnetic adatom chains on a superconductor | — | 620 | `zenodo/17533355/FigS9/cloud_No08EI_027.dat/` | True | True |
| `cloud_No08EI_028.dat` | STS | Magnetic adatom chains on a superconductor | — | 621 | `zenodo/17533355/FigS9/cloud_No08EI_028.dat/` | True | True |
| `cloud_No08EI_029.dat` | STS | Magnetic adatom chains on a superconductor | — | 622 | `zenodo/17533355/FigS9/cloud_No08EI_029.dat/` | True | True |
| `cloud_No08EI_030.dat` | STS | Magnetic adatom chains on a superconductor | — | 623 | `zenodo/17533355/FigS9/cloud_No08EI_030.dat/` | True | True |
| `cloud_No08EI_031.dat` | STS | Magnetic adatom chains on a superconductor | — | 624 | `zenodo/17533355/FigS9/cloud_No08EI_031.dat/` | True | True |
| `cloud_No08EI_032.dat` | STS | Magnetic adatom chains on a superconductor | — | 625 | `zenodo/17533355/FigS9/cloud_No08EI_032.dat/` | True | True |
| `cloud_No08EI_033.dat` | STS | Magnetic adatom chains on a superconductor | — | 626 | `zenodo/17533355/FigS9/cloud_No08EI_033.dat/` | True | True |
| `cloud_No08EI_034.dat` | STS | Magnetic adatom chains on a superconductor | — | 627 | `zenodo/17533355/FigS9/cloud_No08EI_034.dat/` | True | True |
| `cloud_No08EI_035.dat` | STS | Magnetic adatom chains on a superconductor | — | 628 | `zenodo/17533355/FigS9/cloud_No08EI_035.dat/` | True | True |
| `cloud_No08EI_036.dat` | STS | Magnetic adatom chains on a superconductor | — | 629 | `zenodo/17533355/FigS9/cloud_No08EI_036.dat/` | True | True |
| `cloud_No08EI_037.dat` | STS | Magnetic adatom chains on a superconductor | — | 630 | `zenodo/17533355/FigS9/cloud_No08EI_037.dat/` | True | True |
| `cloud_No08EI_038.dat` | STS | Magnetic adatom chains on a superconductor | — | 631 | `zenodo/17533355/FigS9/cloud_No08EI_038.dat/` | True | True |
| `cloud_No08EI_039.dat` | STS | Magnetic adatom chains on a superconductor | — | 632 | `zenodo/17533355/FigS9/cloud_No08EI_039.dat/` | True | True |
| `cloud_No08EI_040.dat` | STS | Magnetic adatom chains on a superconductor | — | 633 | `zenodo/17533355/FigS9/cloud_No08EI_040.dat/` | True | True |
| `cloud_No08EI_041.dat` | STS | Magnetic adatom chains on a superconductor | — | 634 | `zenodo/17533355/FigS9/cloud_No08EI_041.dat/` | True | True |
| `cloud_No08EI_042.dat` | STS | Magnetic adatom chains on a superconductor | — | 635 | `zenodo/17533355/FigS9/cloud_No08EI_042.dat/` | True | True |
| `image_531.sxm` | STS | Magnetic adatom chains on a superconductor | — | 636 | `zenodo/17533355/FigS9/image_531.sxm/` | True | True |
| `image_540.sxm` | STS | Magnetic adatom chains on a superconductor | — | 637 | `zenodo/17533355/FigS9/image_540.sxm/` | True | True |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `directory.pdf` | STS | 1 | `zenodo/17533355/directory.pdf/` |

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08/09 with `pynxtools-spm` 0.2.5. License **`cc-by-4.0`** passes the
open-license gate. **All 71 `.sxm` STM + all 566 `.dat` STS files converted, validated, and
uploaded** (`PS = True`, `Uploaded = True`).

- **STM `.sxm` (71/71):** 69 single-pass (default `current_forward`) + 2 multi-pass
  (`dIdV_No08_029/035.sxm`, `[Pn]_` channels) recovered via a per-dataset `config.json` (copied
  from `ElnExamples/nanonis_sxm_stm` and edited to add `[P1]_`/`[P2]_` channel groups; the src
  default config was not touched). Output `MagAdatomChain_<raw_stem>.nxs`.
- **STS `.dat` (566/566):** genuine Nanonis STS (header `Experiment<TAB>bias spectroscopy`);
  `NanonisDatSTS`, default `current` (with `current_grad` = numerical dI/dV). Output
  `MagAdatomChain_<raw_stem>.nxs`.

Short units, 0 shape mismatches. `citeID.description` carries the full Zenodo description + the
original raw file name.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 71/71 `.sxm` + 566/566 `.dat` converted (`PS = True`)
- [x] Reference .nxs files generated and uploaded for all 637 files
