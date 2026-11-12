# Dataset Report: Zenodo Record 10443995

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Scanning Tunneling Microscope Images of Atomic Scale Defects in Tungsten Diselenide |
| **DOI**    | [10.5281/zenodo.10443995](https://doi.org/10.5281/zenodo.10443995) |
| **Url**    | [https://zenodo.org/records/10443995](https://zenodo.org/records/10443995) |
| **Date**   | 2023-12-30 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Smalley, Darian |
| **Tags**   | STM, scanning tunneling microscopy, WSe2, tungsten diselenide, defects, machine learning |
| **Description** | This dataset contains scanning tunneling microscope (STM) data of single crystal tungsten diselenide (WSe2) provided by the Hone-Barmak Group acquired in constant current mode from two STM systems: a Low Temperature STM (LT-STM) and a room temperature STM (RT-STM). The images are of various sizes and resolutions. 136 of the STM images have associated labels of atomic-scale defects in the form of bouding boxes and image label masks. 38 annotated images were selected to construct an augmented training dataset of images and label masks saved as numpy files for convientent model training. Original, raw STM data of WSe2 is also inculded. <br><br> Code on GitHub: <https://github.com/darianSmalley/ML-STM> |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: STM (Scanning Tunneling Microscopy) — constant current
- **Instrument**: Nanonis LT-STM and RT-STM (Hone-Barmak Group)

## Sample

- **Material / chemical formula**: single-crystal **tungsten diselenide (WSe₂)** → `WSe2`.
- **Study**: constant-current STM imaging of atomic-scale defects in WSe₂ (LT-STM and RT-STM),
  various sizes/resolutions; a subset carries atomic-defect bounding-box / mask labels.

## Dataset Contents

136 annotated STM images of WSe₂ atomic-scale defects plus 38 augmented training images (bounding boxes + masks). 983 files including `.sxm` raw STM data, `.npy` numpy arrays for ML training, annotation CSV/JSON, and JPEG images.

## File Format

- **Format**: Nanonis `.sxm` (raw STM data)
- **Parsability**: Supported by `NanonisSxmSTM` formatter. Files are inside `STM_data/` folder (extracted from `STM_data.zip`).

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/10443995/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 983 files

**S3 key pattern**: `zenodo/10443995/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `STM_WTip_WSe2-SL445_001.sxm` | STM | WSe2 single crystal | WSe2 | 1 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_001.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_002.sxm` | STM | WSe2 single crystal | WSe2 | 2 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_002.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_003.sxm` | STM | WSe2 single crystal | WSe2 | 3 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_003.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_004.sxm` | STM | WSe2 single crystal | WSe2 | 4 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_004.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_005.sxm` | STM | WSe2 single crystal | WSe2 | 5 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_005.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_006.sxm` | STM | WSe2 single crystal | WSe2 | 6 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_006.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_007.sxm` | STM | WSe2 single crystal | WSe2 | 7 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_007.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_008.sxm` | STM | WSe2 single crystal | WSe2 | 8 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_008.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_009.sxm` | STM | WSe2 single crystal | WSe2 | 9 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_009.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_010.sxm` | STM | WSe2 single crystal | WSe2 | 10 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_010.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_011.sxm` | STM | WSe2 single crystal | WSe2 | 11 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_011.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_012.sxm` | STM | WSe2 single crystal | WSe2 | 12 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_012.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_013.sxm` | STM | WSe2 single crystal | WSe2 | 13 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_013.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_014.sxm` | STM | WSe2 single crystal | WSe2 | 14 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_014.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_015.sxm` | STM | WSe2 single crystal | WSe2 | 15 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_015.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_016.sxm` | STM | WSe2 single crystal | WSe2 | 16 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_016.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_017.sxm` | STM | WSe2 single crystal | WSe2 | 17 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_017.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_018.sxm` | STM | WSe2 single crystal | WSe2 | 18 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_018.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_019.sxm` | STM | WSe2 single crystal | WSe2 | 19 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_019.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_020.sxm` | STM | WSe2 single crystal | WSe2 | 20 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_020.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_021.sxm` | STM | WSe2 single crystal | WSe2 | 21 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_021.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_022.sxm` | STM | WSe2 single crystal | WSe2 | 22 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_022.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_023.sxm` | STM | WSe2 single crystal | WSe2 | 23 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_023.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_024.sxm` | STM | WSe2 single crystal | WSe2 | 24 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_024.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_025.sxm` | STM | WSe2 single crystal | WSe2 | 25 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_025.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_026.sxm` | STM | WSe2 single crystal | WSe2 | 26 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_026.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_027.sxm` | STM | WSe2 single crystal | WSe2 | 27 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_027.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_028.sxm` | STM | WSe2 single crystal | WSe2 | 28 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_028.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_029.sxm` | STM | WSe2 single crystal | WSe2 | 29 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_029.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_030.sxm` | STM | WSe2 single crystal | WSe2 | 30 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_030.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_031.sxm` | STM | WSe2 single crystal | WSe2 | 31 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_031.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_032.sxm` | STM | WSe2 single crystal | WSe2 | 32 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_032.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_033.sxm` | STM | WSe2 single crystal | WSe2 | 33 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_033.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_034.sxm` | STM | WSe2 single crystal | WSe2 | 34 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_034.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_035.sxm` | STM | WSe2 single crystal | WSe2 | 35 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_035.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_036.sxm` | STM | WSe2 single crystal | WSe2 | 36 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_036.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_037.sxm` | STM | WSe2 single crystal | WSe2 | 37 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_037.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_038.sxm` | STM | WSe2 single crystal | WSe2 | 38 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_038.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_039.sxm` | STM | WSe2 single crystal | WSe2 | 39 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_039.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_040.sxm` | STM | WSe2 single crystal | WSe2 | 40 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_040.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_041.sxm` | STM | WSe2 single crystal | WSe2 | 41 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_041.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_042.sxm` | STM | WSe2 single crystal | WSe2 | 42 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_042.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_043.sxm` | STM | WSe2 single crystal | WSe2 | 43 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_043.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_044.sxm` | STM | WSe2 single crystal | WSe2 | 44 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_044.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_045.sxm` | STM | WSe2 single crystal | WSe2 | 45 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_045.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_046.sxm` | STM | WSe2 single crystal | WSe2 | 46 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_046.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_047.sxm` | STM | WSe2 single crystal | WSe2 | 47 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_047.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_048.sxm` | STM | WSe2 single crystal | WSe2 | 48 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_048.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_049.sxm` | STM | WSe2 single crystal | WSe2 | 49 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_049.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_050.sxm` | STM | WSe2 single crystal | WSe2 | 50 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_050.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_051.sxm` | STM | WSe2 single crystal | WSe2 | 51 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_051.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_052.sxm` | STM | WSe2 single crystal | WSe2 | 52 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_052.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_053.sxm` | STM | WSe2 single crystal | WSe2 | 53 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_053.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_054.sxm` | STM | WSe2 single crystal | WSe2 | 54 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_054.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_055.sxm` | STM | WSe2 single crystal | WSe2 | 55 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_055.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_056.sxm` | STM | WSe2 single crystal | WSe2 | 56 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_056.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_057.sxm` | STM | WSe2 single crystal | WSe2 | 57 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_057.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_058.sxm` | STM | WSe2 single crystal | WSe2 | 58 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_058.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_059.sxm` | STM | WSe2 single crystal | WSe2 | 59 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_059.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_060.sxm` | STM | WSe2 single crystal | WSe2 | 60 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_060.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_061.sxm` | STM | WSe2 single crystal | WSe2 | 61 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_061.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_062.sxm` | STM | WSe2 single crystal | WSe2 | 62 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_062.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_063.sxm` | STM | WSe2 single crystal | WSe2 | 63 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_063.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_064.sxm` | STM | WSe2 single crystal | WSe2 | 64 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_064.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_065.sxm` | STM | WSe2 single crystal | WSe2 | 65 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_065.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_066.sxm` | STM | WSe2 single crystal | WSe2 | 66 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_066.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_067.sxm` | STM | WSe2 single crystal | WSe2 | 67 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_067.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_068.sxm` | STM | WSe2 single crystal | WSe2 | 68 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_068.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_069.sxm` | STM | WSe2 single crystal | WSe2 | 69 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_069.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_070.sxm` | STM | WSe2 single crystal | WSe2 | 70 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_070.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_071.sxm` | STM | WSe2 single crystal | WSe2 | 71 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_071.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_072.sxm` | STM | WSe2 single crystal | WSe2 | 72 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_072.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_073.sxm` | STM | WSe2 single crystal | WSe2 | 73 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_073.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_074.sxm` | STM | WSe2 single crystal | WSe2 | 74 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_074.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_075.sxm` | STM | WSe2 single crystal | WSe2 | 75 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_075.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_076.sxm` | STM | WSe2 single crystal | WSe2 | 76 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_076.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_077.sxm` | STM | WSe2 single crystal | WSe2 | 77 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_077.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_078.sxm` | STM | WSe2 single crystal | WSe2 | 78 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_078.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_079.sxm` | STM | WSe2 single crystal | WSe2 | 79 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_079.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_080.sxm` | STM | WSe2 single crystal | WSe2 | 80 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_080.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_081.sxm` | STM | WSe2 single crystal | WSe2 | 81 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_081.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_082.sxm` | STM | WSe2 single crystal | WSe2 | 82 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_082.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_083.sxm` | STM | WSe2 single crystal | WSe2 | 83 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_083.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_084.sxm` | STM | WSe2 single crystal | WSe2 | 84 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_084.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_085.sxm` | STM | WSe2 single crystal | WSe2 | 85 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_085.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_086.sxm` | STM | WSe2 single crystal | WSe2 | 86 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_086.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_087.sxm` | STM | WSe2 single crystal | WSe2 | 87 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_087.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_088.sxm` | STM | WSe2 single crystal | WSe2 | 88 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_088.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_089.sxm` | STM | WSe2 single crystal | WSe2 | 89 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_089.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_090.sxm` | STM | WSe2 single crystal | WSe2 | 90 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_090.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_091.sxm` | STM | WSe2 single crystal | WSe2 | 91 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_091.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_092.sxm` | STM | WSe2 single crystal | WSe2 | 92 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_092.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_093.sxm` | STM | WSe2 single crystal | WSe2 | 93 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_093.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_094.sxm` | STM | WSe2 single crystal | WSe2 | 94 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_094.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_095.sxm` | STM | WSe2 single crystal | WSe2 | 95 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_095.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_096.sxm` | STM | WSe2 single crystal | WSe2 | 96 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_096.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_097.sxm` | STM | WSe2 single crystal | WSe2 | 97 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_097.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_098.sxm` | STM | WSe2 single crystal | WSe2 | 98 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_098.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_099.sxm` | STM | WSe2 single crystal | WSe2 | 99 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_099.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_100.sxm` | STM | WSe2 single crystal | WSe2 | 100 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_100.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_101.sxm` | STM | WSe2 single crystal | WSe2 | 101 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_101.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_102.sxm` | STM | WSe2 single crystal | WSe2 | 102 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_102.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_103.sxm` | STM | WSe2 single crystal | WSe2 | 103 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_103.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_104.sxm` | STM | WSe2 single crystal | WSe2 | 104 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_104.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_105.sxm` | STM | WSe2 single crystal | WSe2 | 105 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_105.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_106.sxm` | STM | WSe2 single crystal | WSe2 | 106 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_106.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_107.sxm` | STM | WSe2 single crystal | WSe2 | 107 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_107.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_108.sxm` | STM | WSe2 single crystal | WSe2 | 108 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_108.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_109.sxm` | STM | WSe2 single crystal | WSe2 | 109 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_109.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_110.sxm` | STM | WSe2 single crystal | WSe2 | 110 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_110.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_111.sxm` | STM | WSe2 single crystal | WSe2 | 111 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_111.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_112.sxm` | STM | WSe2 single crystal | WSe2 | 112 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_112.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_113.sxm` | STM | WSe2 single crystal | WSe2 | 113 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_113.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_114.sxm` | STM | WSe2 single crystal | WSe2 | 114 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_114.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_115.sxm` | STM | WSe2 single crystal | WSe2 | 115 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_115.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_116.sxm` | STM | WSe2 single crystal | WSe2 | 116 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_116.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_117.sxm` | STM | WSe2 single crystal | WSe2 | 117 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_117.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_118.sxm` | STM | WSe2 single crystal | WSe2 | 118 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_118.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_119.sxm` | STM | WSe2 single crystal | WSe2 | 119 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_119.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_120.sxm` | STM | WSe2 single crystal | WSe2 | 120 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_120.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_121.sxm` | STM | WSe2 single crystal | WSe2 | 121 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_121.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_122.sxm` | STM | WSe2 single crystal | WSe2 | 122 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_122.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_123.sxm` | STM | WSe2 single crystal | WSe2 | 123 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_123.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_124.sxm` | STM | WSe2 single crystal | WSe2 | 124 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_124.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_125.sxm` | STM | WSe2 single crystal | WSe2 | 125 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_125.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_126.sxm` | STM | WSe2 single crystal | WSe2 | 126 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_126.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_127.sxm` | STM | WSe2 single crystal | WSe2 | 127 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_127.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_128.sxm` | STM | WSe2 single crystal | WSe2 | 128 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_128.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_129.sxm` | STM | WSe2 single crystal | WSe2 | 129 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_129.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_130.sxm` | STM | WSe2 single crystal | WSe2 | 130 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_130.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_131.sxm` | STM | WSe2 single crystal | WSe2 | 131 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_131.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_132.sxm` | STM | WSe2 single crystal | WSe2 | 132 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_132.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_133.sxm` | STM | WSe2 single crystal | WSe2 | 133 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_133.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_134.sxm` | STM | WSe2 single crystal | WSe2 | 134 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_134.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_135.sxm` | STM | WSe2 single crystal | WSe2 | 135 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_135.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_136.sxm` | STM | WSe2 single crystal | WSe2 | 136 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_136.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_137.sxm` | STM | WSe2 single crystal | WSe2 | 137 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_137.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_138.sxm` | STM | WSe2 single crystal | WSe2 | 138 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_138.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_139.sxm` | STM | WSe2 single crystal | WSe2 | 139 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_139.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_140.sxm` | STM | WSe2 single crystal | WSe2 | 140 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_140.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_141.sxm` | STM | WSe2 single crystal | WSe2 | 141 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_141.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_142.sxm` | STM | WSe2 single crystal | WSe2 | 142 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_142.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_143.sxm` | STM | WSe2 single crystal | WSe2 | 143 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_143.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_144.sxm` | STM | WSe2 single crystal | WSe2 | 144 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_144.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_145.sxm` | STM | WSe2 single crystal | WSe2 | 145 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_145.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_146.sxm` | STM | WSe2 single crystal | WSe2 | 146 | `zenodo/10443995/STM_data/2021-11-18/STM_WTip_WSe2-SL445_146.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_032.sxm` | STM | WSe2 single crystal | WSe2 | 147 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_032.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_033.sxm` | STM | WSe2 single crystal | WSe2 | 148 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_033.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_034.sxm` | STM | WSe2 single crystal | WSe2 | 149 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_034.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_035.sxm` | STM | WSe2 single crystal | WSe2 | 150 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_035.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_036.sxm` | STM | WSe2 single crystal | WSe2 | 151 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_036.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_037.sxm` | STM | WSe2 single crystal | WSe2 | 152 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_037.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_038.sxm` | STM | WSe2 single crystal | WSe2 | 153 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_038.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_039.sxm` | STM | WSe2 single crystal | WSe2 | 154 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_039.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_040.sxm` | STM | WSe2 single crystal | WSe2 | 155 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_040.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_041.sxm` | STM | WSe2 single crystal | WSe2 | 156 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_041.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_042.sxm` | STM | WSe2 single crystal | WSe2 | 157 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_042.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_043.sxm` | STM | WSe2 single crystal | WSe2 | 158 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_043.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_044.sxm` | STM | WSe2 single crystal | WSe2 | 159 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_044.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_045.sxm` | STM | WSe2 single crystal | WSe2 | 160 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_045.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_046.sxm` | STM | WSe2 single crystal | WSe2 | 161 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_046.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_047.sxm` | STM | WSe2 single crystal | WSe2 | 162 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_047.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_048.sxm` | STM | WSe2 single crystal | WSe2 | 163 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_048.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_049.sxm` | STM | WSe2 single crystal | WSe2 | 164 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_049.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_050.sxm` | STM | WSe2 single crystal | WSe2 | 165 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_050.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_051.sxm` | STM | WSe2 single crystal | WSe2 | 166 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_051.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_052.sxm` | STM | WSe2 single crystal | WSe2 | 167 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_052.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_053.sxm` | STM | WSe2 single crystal | WSe2 | 168 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_053.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_054.sxm` | STM | WSe2 single crystal | WSe2 | 169 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_054.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_055.sxm` | STM | WSe2 single crystal | WSe2 | 170 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_055.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_056.sxm` | STM | WSe2 single crystal | WSe2 | 171 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_056.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_057.sxm` | STM | WSe2 single crystal | WSe2 | 172 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_057.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_058.sxm` | STM | WSe2 single crystal | WSe2 | 173 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_058.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_059.sxm` | STM | WSe2 single crystal | WSe2 | 174 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_059.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_060.sxm` | STM | WSe2 single crystal | WSe2 | 175 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_060.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_061.sxm` | STM | WSe2 single crystal | WSe2 | 176 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_061.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_062.sxm` | STM | WSe2 single crystal | WSe2 | 177 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_062.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_063.sxm` | STM | WSe2 single crystal | WSe2 | 178 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_063.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_064.sxm` | STM | WSe2 single crystal | WSe2 | 179 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_064.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_065.sxm` | STM | WSe2 single crystal | WSe2 | 180 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_065.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_066.sxm` | STM | WSe2 single crystal | WSe2 | 181 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_066.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_067.sxm` | STM | WSe2 single crystal | WSe2 | 182 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_067.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_068.sxm` | STM | WSe2 single crystal | WSe2 | 183 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_068.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_069.sxm` | STM | WSe2 single crystal | WSe2 | 184 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_069.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_070.sxm` | STM | WSe2 single crystal | WSe2 | 185 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_070.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_071.sxm` | STM | WSe2 single crystal | WSe2 | 186 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_071.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_072.sxm` | STM | WSe2 single crystal | WSe2 | 187 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_072.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_073.sxm` | STM | WSe2 single crystal | WSe2 | 188 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_073.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_074.sxm` | STM | WSe2 single crystal | WSe2 | 189 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_074.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_075.sxm` | STM | WSe2 single crystal | WSe2 | 190 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_075.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_076.sxm` | STM | WSe2 single crystal | WSe2 | 191 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_076.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_077.sxm` | STM | WSe2 single crystal | WSe2 | 192 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_077.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_078.sxm` | STM | WSe2 single crystal | WSe2 | 193 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_078.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_079.sxm` | STM | WSe2 single crystal | WSe2 | 194 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_079.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_080.sxm` | STM | WSe2 single crystal | WSe2 | 195 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_080.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_081.sxm` | STM | WSe2 single crystal | WSe2 | 196 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_081.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_082.sxm` | STM | WSe2 single crystal | WSe2 | 197 | `zenodo/10443995/STM_data/2021-11-19/STM_WTip_WSe2-SL445_082.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_083.sxm` | STM | WSe2 single crystal | WSe2 | 198 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_083.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_084.sxm` | STM | WSe2 single crystal | WSe2 | 199 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_084.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_085.sxm` | STM | WSe2 single crystal | WSe2 | 200 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_085.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_086.sxm` | STM | WSe2 single crystal | WSe2 | 201 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_086.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_087.sxm` | STM | WSe2 single crystal | WSe2 | 202 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_087.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_088.sxm` | STM | WSe2 single crystal | WSe2 | 203 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_088.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_089.sxm` | STM | WSe2 single crystal | WSe2 | 204 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_089.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_090.sxm` | STM | WSe2 single crystal | WSe2 | 205 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_090.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_091.sxm` | STM | WSe2 single crystal | WSe2 | 206 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_091.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_092.sxm` | STM | WSe2 single crystal | WSe2 | 207 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_092.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_093.sxm` | STM | WSe2 single crystal | WSe2 | 208 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_093.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_094.sxm` | STM | WSe2 single crystal | WSe2 | 209 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_094.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_095.sxm` | STM | WSe2 single crystal | WSe2 | 210 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_095.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_096.sxm` | STM | WSe2 single crystal | WSe2 | 211 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_096.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_097.sxm` | STM | WSe2 single crystal | WSe2 | 212 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_097.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_098.sxm` | STM | WSe2 single crystal | WSe2 | 213 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_098.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_099.sxm` | STM | WSe2 single crystal | WSe2 | 214 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_099.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_100.sxm` | STM | WSe2 single crystal | WSe2 | 215 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_100.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_101.sxm` | STM | WSe2 single crystal | WSe2 | 216 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_101.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_102.sxm` | STM | WSe2 single crystal | WSe2 | 217 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_102.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_103.sxm` | STM | WSe2 single crystal | WSe2 | 218 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_103.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_104.sxm` | STM | WSe2 single crystal | WSe2 | 219 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_104.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_105.sxm` | STM | WSe2 single crystal | WSe2 | 220 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_105.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_106.sxm` | STM | WSe2 single crystal | WSe2 | 221 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_106.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_107.sxm` | STM | WSe2 single crystal | WSe2 | 222 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_107.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_108.sxm` | STM | WSe2 single crystal | WSe2 | 223 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_108.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_109.sxm` | STM | WSe2 single crystal | WSe2 | 224 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_109.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_110.sxm` | STM | WSe2 single crystal | WSe2 | 225 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_110.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_111.sxm` | STM | WSe2 single crystal | WSe2 | 226 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_111.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_112.sxm` | STM | WSe2 single crystal | WSe2 | 227 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_112.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_113.sxm` | STM | WSe2 single crystal | WSe2 | 228 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_113.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_114.sxm` | STM | WSe2 single crystal | WSe2 | 229 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_114.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_115.sxm` | STM | WSe2 single crystal | WSe2 | 230 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_115.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_116.sxm` | STM | WSe2 single crystal | WSe2 | 231 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_116.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_117.sxm` | STM | WSe2 single crystal | WSe2 | 232 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_117.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_118.sxm` | STM | WSe2 single crystal | WSe2 | 233 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_118.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_119.sxm` | STM | WSe2 single crystal | WSe2 | 234 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_119.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_120.sxm` | STM | WSe2 single crystal | WSe2 | 235 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_120.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_121.sxm` | STM | WSe2 single crystal | WSe2 | 236 | `zenodo/10443995/STM_data/2021-11-20/STM_WTip_WSe2-SL445_121.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_001.sxm` | STM | WSe2 single crystal | WSe2 | 237 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_001.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_002.sxm` | STM | WSe2 single crystal | WSe2 | 238 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_002.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_003.sxm` | STM | WSe2 single crystal | WSe2 | 239 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_003.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_004.sxm` | STM | WSe2 single crystal | WSe2 | 240 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_004.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_005.sxm` | STM | WSe2 single crystal | WSe2 | 241 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_005.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_006.sxm` | STM | WSe2 single crystal | WSe2 | 242 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_006.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_007.sxm` | STM | WSe2 single crystal | WSe2 | 243 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_007.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_008.sxm` | STM | WSe2 single crystal | WSe2 | 244 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_008.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_009.sxm` | STM | WSe2 single crystal | WSe2 | 245 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_009.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_010.sxm` | STM | WSe2 single crystal | WSe2 | 246 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_010.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_011.sxm` | STM | WSe2 single crystal | WSe2 | 247 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_011.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_012.sxm` | STM | WSe2 single crystal | WSe2 | 248 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_012.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_013.sxm` | STM | WSe2 single crystal | WSe2 | 249 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_013.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_014.sxm` | STM | WSe2 single crystal | WSe2 | 250 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_014.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_015.sxm` | STM | WSe2 single crystal | WSe2 | 251 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_015.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_122.sxm` | STM | WSe2 single crystal | WSe2 | 252 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_122.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_123.sxm` | STM | WSe2 single crystal | WSe2 | 253 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_123.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_124.sxm` | STM | WSe2 single crystal | WSe2 | 254 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_124.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_125.sxm` | STM | WSe2 single crystal | WSe2 | 255 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_125.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_126.sxm` | STM | WSe2 single crystal | WSe2 | 256 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_126.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_127.sxm` | STM | WSe2 single crystal | WSe2 | 257 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_127.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_128.sxm` | STM | WSe2 single crystal | WSe2 | 258 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_128.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_129.sxm` | STM | WSe2 single crystal | WSe2 | 259 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_129.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_130.sxm` | STM | WSe2 single crystal | WSe2 | 260 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_130.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_131.sxm` | STM | WSe2 single crystal | WSe2 | 261 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_131.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_132.sxm` | STM | WSe2 single crystal | WSe2 | 262 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_132.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_133.sxm` | STM | WSe2 single crystal | WSe2 | 263 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_133.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_134.sxm` | STM | WSe2 single crystal | WSe2 | 264 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_134.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_135.sxm` | STM | WSe2 single crystal | WSe2 | 265 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_135.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_136.sxm` | STM | WSe2 single crystal | WSe2 | 266 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_136.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_137.sxm` | STM | WSe2 single crystal | WSe2 | 267 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_137.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_138.sxm` | STM | WSe2 single crystal | WSe2 | 268 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_138.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_139.sxm` | STM | WSe2 single crystal | WSe2 | 269 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_139.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_140.sxm` | STM | WSe2 single crystal | WSe2 | 270 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_140.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_141.sxm` | STM | WSe2 single crystal | WSe2 | 271 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_141.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_142.sxm` | STM | WSe2 single crystal | WSe2 | 272 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_142.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_143.sxm` | STM | WSe2 single crystal | WSe2 | 273 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_143.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_144.sxm` | STM | WSe2 single crystal | WSe2 | 274 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_144.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_145.sxm` | STM | WSe2 single crystal | WSe2 | 275 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_145.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_146.sxm` | STM | WSe2 single crystal | WSe2 | 276 | `zenodo/10443995/STM_data/2021-11-21/STM_WTip_WSe2-SL445_146.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_001.sxm` | STM | WSe2 single crystal | WSe2 | 277 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_001.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_002.sxm` | STM | WSe2 single crystal | WSe2 | 278 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_002.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_003.sxm` | STM | WSe2 single crystal | WSe2 | 279 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_003.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_004.sxm` | STM | WSe2 single crystal | WSe2 | 280 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_004.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_005.sxm` | STM | WSe2 single crystal | WSe2 | 281 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_005.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_006.sxm` | STM | WSe2 single crystal | WSe2 | 282 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_006.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_007.sxm` | STM | WSe2 single crystal | WSe2 | 283 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_007.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_008.sxm` | STM | WSe2 single crystal | WSe2 | 284 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_008.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_009.sxm` | STM | WSe2 single crystal | WSe2 | 285 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_009.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_010.sxm` | STM | WSe2 single crystal | WSe2 | 286 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_010.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_011.sxm` | STM | WSe2 single crystal | WSe2 | 287 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_011.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_012.sxm` | STM | WSe2 single crystal | WSe2 | 288 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_012.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_013.sxm` | STM | WSe2 single crystal | WSe2 | 289 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_013.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_014.sxm` | STM | WSe2 single crystal | WSe2 | 290 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_014.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_015.sxm` | STM | WSe2 single crystal | WSe2 | 291 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_015.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_016.sxm` | STM | WSe2 single crystal | WSe2 | 292 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_016.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_017.sxm` | STM | WSe2 single crystal | WSe2 | 293 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_017.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_018.sxm` | STM | WSe2 single crystal | WSe2 | 294 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_018.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_019.sxm` | STM | WSe2 single crystal | WSe2 | 295 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_019.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_020.sxm` | STM | WSe2 single crystal | WSe2 | 296 | `zenodo/10443995/STM_data/2021-11-22 -bak/STM_WTip_WSe2-SL445_020.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_016.sxm` | STM | WSe2 single crystal | WSe2 | 297 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_016.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_017.sxm` | STM | WSe2 single crystal | WSe2 | 298 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_017.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_018.sxm` | STM | WSe2 single crystal | WSe2 | 299 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_018.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_019.sxm` | STM | WSe2 single crystal | WSe2 | 300 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_019.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_020.sxm` | STM | WSe2 single crystal | WSe2 | 301 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_020.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_021.sxm` | STM | WSe2 single crystal | WSe2 | 302 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_021.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_022.sxm` | STM | WSe2 single crystal | WSe2 | 303 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_022.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_023.sxm` | STM | WSe2 single crystal | WSe2 | 304 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_023.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_024.sxm` | STM | WSe2 single crystal | WSe2 | 305 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_024.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_025.sxm` | STM | WSe2 single crystal | WSe2 | 306 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_025.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_026.sxm` | STM | WSe2 single crystal | WSe2 | 307 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_026.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_027.sxm` | STM | WSe2 single crystal | WSe2 | 308 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_027.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_028.sxm` | STM | WSe2 single crystal | WSe2 | 309 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_028.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_029.sxm` | STM | WSe2 single crystal | WSe2 | 310 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_029.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_030.sxm` | STM | WSe2 single crystal | WSe2 | 311 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_030.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_031.sxm` | STM | WSe2 single crystal | WSe2 | 312 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_031.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_032.sxm` | STM | WSe2 single crystal | WSe2 | 313 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_032.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_033.sxm` | STM | WSe2 single crystal | WSe2 | 314 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_033.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_034.sxm` | STM | WSe2 single crystal | WSe2 | 315 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_034.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_035.sxm` | STM | WSe2 single crystal | WSe2 | 316 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_035.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_036.sxm` | STM | WSe2 single crystal | WSe2 | 317 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_036.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_037.sxm` | STM | WSe2 single crystal | WSe2 | 318 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_037.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_038.sxm` | STM | WSe2 single crystal | WSe2 | 319 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_038.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_039.sxm` | STM | WSe2 single crystal | WSe2 | 320 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_039.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_040.sxm` | STM | WSe2 single crystal | WSe2 | 321 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_040.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_041.sxm` | STM | WSe2 single crystal | WSe2 | 322 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_041.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_042.sxm` | STM | WSe2 single crystal | WSe2 | 323 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_042.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_043.sxm` | STM | WSe2 single crystal | WSe2 | 324 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_043.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_044.sxm` | STM | WSe2 single crystal | WSe2 | 325 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_044.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_045.sxm` | STM | WSe2 single crystal | WSe2 | 326 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_045.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_046.sxm` | STM | WSe2 single crystal | WSe2 | 327 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_046.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_047.sxm` | STM | WSe2 single crystal | WSe2 | 328 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_047.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_048.sxm` | STM | WSe2 single crystal | WSe2 | 329 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_048.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_049.sxm` | STM | WSe2 single crystal | WSe2 | 330 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_049.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_050.sxm` | STM | WSe2 single crystal | WSe2 | 331 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_050.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_051.sxm` | STM | WSe2 single crystal | WSe2 | 332 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_051.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_052.sxm` | STM | WSe2 single crystal | WSe2 | 333 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_052.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_053.sxm` | STM | WSe2 single crystal | WSe2 | 334 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_053.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_054.sxm` | STM | WSe2 single crystal | WSe2 | 335 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_054.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_055.sxm` | STM | WSe2 single crystal | WSe2 | 336 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_055.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_056.sxm` | STM | WSe2 single crystal | WSe2 | 337 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_056.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_057.sxm` | STM | WSe2 single crystal | WSe2 | 338 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_057.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_058.sxm` | STM | WSe2 single crystal | WSe2 | 339 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_058.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_059.sxm` | STM | WSe2 single crystal | WSe2 | 340 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_059.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_060.sxm` | STM | WSe2 single crystal | WSe2 | 341 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_060.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_061.sxm` | STM | WSe2 single crystal | WSe2 | 342 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_061.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_062.sxm` | STM | WSe2 single crystal | WSe2 | 343 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_062.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_063.sxm` | STM | WSe2 single crystal | WSe2 | 344 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_063.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_064.sxm` | STM | WSe2 single crystal | WSe2 | 345 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_064.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_065.sxm` | STM | WSe2 single crystal | WSe2 | 346 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_065.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_066.sxm` | STM | WSe2 single crystal | WSe2 | 347 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_066.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_067.sxm` | STM | WSe2 single crystal | WSe2 | 348 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_067.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_068.sxm` | STM | WSe2 single crystal | WSe2 | 349 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_068.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_069.sxm` | STM | WSe2 single crystal | WSe2 | 350 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_069.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_070.sxm` | STM | WSe2 single crystal | WSe2 | 351 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_070.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_071.sxm` | STM | WSe2 single crystal | WSe2 | 352 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_071.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_072.sxm` | STM | WSe2 single crystal | WSe2 | 353 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_072.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_073.sxm` | STM | WSe2 single crystal | WSe2 | 354 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_073.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_074.sxm` | STM | WSe2 single crystal | WSe2 | 355 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_074.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_075.sxm` | STM | WSe2 single crystal | WSe2 | 356 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_075.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_076.sxm` | STM | WSe2 single crystal | WSe2 | 357 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_076.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_077.sxm` | STM | WSe2 single crystal | WSe2 | 358 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_077.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_078.sxm` | STM | WSe2 single crystal | WSe2 | 359 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_078.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_079.sxm` | STM | WSe2 single crystal | WSe2 | 360 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_079.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_080.sxm` | STM | WSe2 single crystal | WSe2 | 361 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_080.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_081.sxm` | STM | WSe2 single crystal | WSe2 | 362 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_081.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_082.sxm` | STM | WSe2 single crystal | WSe2 | 363 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_082.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_083.sxm` | STM | WSe2 single crystal | WSe2 | 364 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_083.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_084.sxm` | STM | WSe2 single crystal | WSe2 | 365 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_084.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_085.sxm` | STM | WSe2 single crystal | WSe2 | 366 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_085.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_086.sxm` | STM | WSe2 single crystal | WSe2 | 367 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_086.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_087.sxm` | STM | WSe2 single crystal | WSe2 | 368 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_087.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_088.sxm` | STM | WSe2 single crystal | WSe2 | 369 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_088.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_089.sxm` | STM | WSe2 single crystal | WSe2 | 370 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_089.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_090.sxm` | STM | WSe2 single crystal | WSe2 | 371 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_090.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_091.sxm` | STM | WSe2 single crystal | WSe2 | 372 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_091.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_092.sxm` | STM | WSe2 single crystal | WSe2 | 373 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_092.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_093.sxm` | STM | WSe2 single crystal | WSe2 | 374 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_093.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_094.sxm` | STM | WSe2 single crystal | WSe2 | 375 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_094.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_095.sxm` | STM | WSe2 single crystal | WSe2 | 376 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_095.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_096.sxm` | STM | WSe2 single crystal | WSe2 | 377 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_096.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_097.sxm` | STM | WSe2 single crystal | WSe2 | 378 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_097.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_098.sxm` | STM | WSe2 single crystal | WSe2 | 379 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_098.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_099.sxm` | STM | WSe2 single crystal | WSe2 | 380 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_099.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_100.sxm` | STM | WSe2 single crystal | WSe2 | 381 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_100.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_101.sxm` | STM | WSe2 single crystal | WSe2 | 382 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_101.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_102.sxm` | STM | WSe2 single crystal | WSe2 | 383 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_102.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_103.sxm` | STM | WSe2 single crystal | WSe2 | 384 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_103.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_104.sxm` | STM | WSe2 single crystal | WSe2 | 385 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_104.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_105.sxm` | STM | WSe2 single crystal | WSe2 | 386 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_105.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_106.sxm` | STM | WSe2 single crystal | WSe2 | 387 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_106.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_107.sxm` | STM | WSe2 single crystal | WSe2 | 388 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_107.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_108.sxm` | STM | WSe2 single crystal | WSe2 | 389 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_108.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_109.sxm` | STM | WSe2 single crystal | WSe2 | 390 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_109.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_110.sxm` | STM | WSe2 single crystal | WSe2 | 391 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_110.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_111.sxm` | STM | WSe2 single crystal | WSe2 | 392 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_111.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_112.sxm` | STM | WSe2 single crystal | WSe2 | 393 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_112.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_113.sxm` | STM | WSe2 single crystal | WSe2 | 394 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_113.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_114.sxm` | STM | WSe2 single crystal | WSe2 | 395 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_114.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_115.sxm` | STM | WSe2 single crystal | WSe2 | 396 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_115.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_116.sxm` | STM | WSe2 single crystal | WSe2 | 397 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_116.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_117.sxm` | STM | WSe2 single crystal | WSe2 | 398 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_117.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_118.sxm` | STM | WSe2 single crystal | WSe2 | 399 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_118.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_119.sxm` | STM | WSe2 single crystal | WSe2 | 400 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_119.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_120.sxm` | STM | WSe2 single crystal | WSe2 | 401 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_120.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_121.sxm` | STM | WSe2 single crystal | WSe2 | 402 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_121.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_122.sxm` | STM | WSe2 single crystal | WSe2 | 403 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_122.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_123.sxm` | STM | WSe2 single crystal | WSe2 | 404 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_123.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_124.sxm` | STM | WSe2 single crystal | WSe2 | 405 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_124.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_125.sxm` | STM | WSe2 single crystal | WSe2 | 406 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_125.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_126.sxm` | STM | WSe2 single crystal | WSe2 | 407 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_126.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_127.sxm` | STM | WSe2 single crystal | WSe2 | 408 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_127.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_128.sxm` | STM | WSe2 single crystal | WSe2 | 409 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_128.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_129.sxm` | STM | WSe2 single crystal | WSe2 | 410 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_129.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_130.sxm` | STM | WSe2 single crystal | WSe2 | 411 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_130.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_131.sxm` | STM | WSe2 single crystal | WSe2 | 412 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_131.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_132.sxm` | STM | WSe2 single crystal | WSe2 | 413 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_132.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_133.sxm` | STM | WSe2 single crystal | WSe2 | 414 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_133.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_134.sxm` | STM | WSe2 single crystal | WSe2 | 415 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_134.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_135.sxm` | STM | WSe2 single crystal | WSe2 | 416 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_135.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_136.sxm` | STM | WSe2 single crystal | WSe2 | 417 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_136.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_137.sxm` | STM | WSe2 single crystal | WSe2 | 418 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_137.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_138.sxm` | STM | WSe2 single crystal | WSe2 | 419 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_138.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_139.sxm` | STM | WSe2 single crystal | WSe2 | 420 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_139.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_140.sxm` | STM | WSe2 single crystal | WSe2 | 421 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_140.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_141.sxm` | STM | WSe2 single crystal | WSe2 | 422 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_141.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_142.sxm` | STM | WSe2 single crystal | WSe2 | 423 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_142.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_143.sxm` | STM | WSe2 single crystal | WSe2 | 424 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_143.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_144.sxm` | STM | WSe2 single crystal | WSe2 | 425 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_144.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_145.sxm` | STM | WSe2 single crystal | WSe2 | 426 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_145.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_146.sxm` | STM | WSe2 single crystal | WSe2 | 427 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_146.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_147.sxm` | STM | WSe2 single crystal | WSe2 | 428 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_147.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_148.sxm` | STM | WSe2 single crystal | WSe2 | 429 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_148.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_149.sxm` | STM | WSe2 single crystal | WSe2 | 430 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_149.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_150.sxm` | STM | WSe2 single crystal | WSe2 | 431 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_150.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_151.sxm` | STM | WSe2 single crystal | WSe2 | 432 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_151.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_152.sxm` | STM | WSe2 single crystal | WSe2 | 433 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_152.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_153.sxm` | STM | WSe2 single crystal | WSe2 | 434 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_153.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_154.sxm` | STM | WSe2 single crystal | WSe2 | 435 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_154.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_155.sxm` | STM | WSe2 single crystal | WSe2 | 436 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_155.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_156.sxm` | STM | WSe2 single crystal | WSe2 | 437 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_156.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_157.sxm` | STM | WSe2 single crystal | WSe2 | 438 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_157.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_158.sxm` | STM | WSe2 single crystal | WSe2 | 439 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_158.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_159.sxm` | STM | WSe2 single crystal | WSe2 | 440 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_159.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_160.sxm` | STM | WSe2 single crystal | WSe2 | 441 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_160.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_161.sxm` | STM | WSe2 single crystal | WSe2 | 442 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_161.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_162.sxm` | STM | WSe2 single crystal | WSe2 | 443 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_162.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_163.sxm` | STM | WSe2 single crystal | WSe2 | 444 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_163.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_164.sxm` | STM | WSe2 single crystal | WSe2 | 445 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_164.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_165.sxm` | STM | WSe2 single crystal | WSe2 | 446 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_165.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_166.sxm` | STM | WSe2 single crystal | WSe2 | 447 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_166.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_167.sxm` | STM | WSe2 single crystal | WSe2 | 448 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_167.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_168.sxm` | STM | WSe2 single crystal | WSe2 | 449 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_168.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_169.sxm` | STM | WSe2 single crystal | WSe2 | 450 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_169.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_170.sxm` | STM | WSe2 single crystal | WSe2 | 451 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_170.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_171.sxm` | STM | WSe2 single crystal | WSe2 | 452 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_171.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_172.sxm` | STM | WSe2 single crystal | WSe2 | 453 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_172.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_173.sxm` | STM | WSe2 single crystal | WSe2 | 454 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_173.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_174.sxm` | STM | WSe2 single crystal | WSe2 | 455 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_174.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_175.sxm` | STM | WSe2 single crystal | WSe2 | 456 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_175.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_176.sxm` | STM | WSe2 single crystal | WSe2 | 457 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_176.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_177.sxm` | STM | WSe2 single crystal | WSe2 | 458 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_177.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_178.sxm` | STM | WSe2 single crystal | WSe2 | 459 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_178.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_179.sxm` | STM | WSe2 single crystal | WSe2 | 460 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_179.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_180.sxm` | STM | WSe2 single crystal | WSe2 | 461 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_180.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_181.sxm` | STM | WSe2 single crystal | WSe2 | 462 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_181.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_182.sxm` | STM | WSe2 single crystal | WSe2 | 463 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_182.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_183.sxm` | STM | WSe2 single crystal | WSe2 | 464 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_183.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_184.sxm` | STM | WSe2 single crystal | WSe2 | 465 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_184.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_185.sxm` | STM | WSe2 single crystal | WSe2 | 466 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_185.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_186.sxm` | STM | WSe2 single crystal | WSe2 | 467 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_186.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_187.sxm` | STM | WSe2 single crystal | WSe2 | 468 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_187.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_188.sxm` | STM | WSe2 single crystal | WSe2 | 469 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_188.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_189.sxm` | STM | WSe2 single crystal | WSe2 | 470 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_189.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_190.sxm` | STM | WSe2 single crystal | WSe2 | 471 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_190.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_191.sxm` | STM | WSe2 single crystal | WSe2 | 472 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_191.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_192.sxm` | STM | WSe2 single crystal | WSe2 | 473 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_192.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_193.sxm` | STM | WSe2 single crystal | WSe2 | 474 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_193.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_194.sxm` | STM | WSe2 single crystal | WSe2 | 475 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_194.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_195.sxm` | STM | WSe2 single crystal | WSe2 | 476 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_195.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_196.sxm` | STM | WSe2 single crystal | WSe2 | 477 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_196.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_197.sxm` | STM | WSe2 single crystal | WSe2 | 478 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_197.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_198.sxm` | STM | WSe2 single crystal | WSe2 | 479 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_198.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_199.sxm` | STM | WSe2 single crystal | WSe2 | 480 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_199.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_200.sxm` | STM | WSe2 single crystal | WSe2 | 481 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_200.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_201.sxm` | STM | WSe2 single crystal | WSe2 | 482 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_201.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_202.sxm` | STM | WSe2 single crystal | WSe2 | 483 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_202.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_203.sxm` | STM | WSe2 single crystal | WSe2 | 484 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_203.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_204.sxm` | STM | WSe2 single crystal | WSe2 | 485 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_204.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_205.sxm` | STM | WSe2 single crystal | WSe2 | 486 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_205.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_206.sxm` | STM | WSe2 single crystal | WSe2 | 487 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_206.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_207.sxm` | STM | WSe2 single crystal | WSe2 | 488 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_207.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_208.sxm` | STM | WSe2 single crystal | WSe2 | 489 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_208.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_209.sxm` | STM | WSe2 single crystal | WSe2 | 490 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_209.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_210.sxm` | STM | WSe2 single crystal | WSe2 | 491 | `zenodo/10443995/STM_data/2021-11-22/STM_WTip_WSe2-SL445_210.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_001.sxm` | STM | WSe2 single crystal | WSe2 | 492 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_001.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_002.sxm` | STM | WSe2 single crystal | WSe2 | 493 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_002.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_003.sxm` | STM | WSe2 single crystal | WSe2 | 494 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_003.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_004.sxm` | STM | WSe2 single crystal | WSe2 | 495 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_004.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_005.sxm` | STM | WSe2 single crystal | WSe2 | 496 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_005.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_006.sxm` | STM | WSe2 single crystal | WSe2 | 497 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_006.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_007.sxm` | STM | WSe2 single crystal | WSe2 | 498 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_007.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_008.sxm` | STM | WSe2 single crystal | WSe2 | 499 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_008.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_009.sxm` | STM | WSe2 single crystal | WSe2 | 500 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_009.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_010.sxm` | STM | WSe2 single crystal | WSe2 | 501 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_010.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_011.sxm` | STM | WSe2 single crystal | WSe2 | 502 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_011.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_012.sxm` | STM | WSe2 single crystal | WSe2 | 503 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_012.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_013.sxm` | STM | WSe2 single crystal | WSe2 | 504 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_013.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_014.sxm` | STM | WSe2 single crystal | WSe2 | 505 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_014.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_015.sxm` | STM | WSe2 single crystal | WSe2 | 506 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_015.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_016.sxm` | STM | WSe2 single crystal | WSe2 | 507 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_016.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_017.sxm` | STM | WSe2 single crystal | WSe2 | 508 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_017.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_018.sxm` | STM | WSe2 single crystal | WSe2 | 509 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_018.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_019.sxm` | STM | WSe2 single crystal | WSe2 | 510 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_019.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_020.sxm` | STM | WSe2 single crystal | WSe2 | 511 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_020.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_021.sxm` | STM | WSe2 single crystal | WSe2 | 512 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_021.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_022.sxm` | STM | WSe2 single crystal | WSe2 | 513 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_022.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_023.sxm` | STM | WSe2 single crystal | WSe2 | 514 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_023.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_024.sxm` | STM | WSe2 single crystal | WSe2 | 515 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_024.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_025.sxm` | STM | WSe2 single crystal | WSe2 | 516 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_025.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_026.sxm` | STM | WSe2 single crystal | WSe2 | 517 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_026.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_027.sxm` | STM | WSe2 single crystal | WSe2 | 518 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_027.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_028.sxm` | STM | WSe2 single crystal | WSe2 | 519 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_028.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_029.sxm` | STM | WSe2 single crystal | WSe2 | 520 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_029.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_030.sxm` | STM | WSe2 single crystal | WSe2 | 521 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_030.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_031.sxm` | STM | WSe2 single crystal | WSe2 | 522 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_031.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_032.sxm` | STM | WSe2 single crystal | WSe2 | 523 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_032.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_033.sxm` | STM | WSe2 single crystal | WSe2 | 524 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_033.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_034.sxm` | STM | WSe2 single crystal | WSe2 | 525 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_034.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_035.sxm` | STM | WSe2 single crystal | WSe2 | 526 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_035.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_036.sxm` | STM | WSe2 single crystal | WSe2 | 527 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_036.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_037.sxm` | STM | WSe2 single crystal | WSe2 | 528 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_037.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_038.sxm` | STM | WSe2 single crystal | WSe2 | 529 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_038.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_039.sxm` | STM | WSe2 single crystal | WSe2 | 530 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_039.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_040.sxm` | STM | WSe2 single crystal | WSe2 | 531 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_040.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_041.sxm` | STM | WSe2 single crystal | WSe2 | 532 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_041.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_042.sxm` | STM | WSe2 single crystal | WSe2 | 533 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_042.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_043.sxm` | STM | WSe2 single crystal | WSe2 | 534 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_043.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_044.sxm` | STM | WSe2 single crystal | WSe2 | 535 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_044.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_045.sxm` | STM | WSe2 single crystal | WSe2 | 536 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_045.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_046.sxm` | STM | WSe2 single crystal | WSe2 | 537 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_046.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_047.sxm` | STM | WSe2 single crystal | WSe2 | 538 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_047.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_048.sxm` | STM | WSe2 single crystal | WSe2 | 539 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_048.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_049.sxm` | STM | WSe2 single crystal | WSe2 | 540 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_049.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_050.sxm` | STM | WSe2 single crystal | WSe2 | 541 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_050.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_051.sxm` | STM | WSe2 single crystal | WSe2 | 542 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_051.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_052.sxm` | STM | WSe2 single crystal | WSe2 | 543 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_052.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_053.sxm` | STM | WSe2 single crystal | WSe2 | 544 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_053.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_054.sxm` | STM | WSe2 single crystal | WSe2 | 545 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_054.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_055.sxm` | STM | WSe2 single crystal | WSe2 | 546 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_055.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_056.sxm` | STM | WSe2 single crystal | WSe2 | 547 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_056.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_057.sxm` | STM | WSe2 single crystal | WSe2 | 548 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_057.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_058.sxm` | STM | WSe2 single crystal | WSe2 | 549 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_058.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_059.sxm` | STM | WSe2 single crystal | WSe2 | 550 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_059.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_060.sxm` | STM | WSe2 single crystal | WSe2 | 551 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_060.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_061.sxm` | STM | WSe2 single crystal | WSe2 | 552 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_061.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_062.sxm` | STM | WSe2 single crystal | WSe2 | 553 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_062.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_063.sxm` | STM | WSe2 single crystal | WSe2 | 554 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_063.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_064.sxm` | STM | WSe2 single crystal | WSe2 | 555 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_064.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_065.sxm` | STM | WSe2 single crystal | WSe2 | 556 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_065.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_066.sxm` | STM | WSe2 single crystal | WSe2 | 557 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_066.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_067.sxm` | STM | WSe2 single crystal | WSe2 | 558 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_067.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_068.sxm` | STM | WSe2 single crystal | WSe2 | 559 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_068.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_069.sxm` | STM | WSe2 single crystal | WSe2 | 560 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_069.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_070.sxm` | STM | WSe2 single crystal | WSe2 | 561 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_070.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_071.sxm` | STM | WSe2 single crystal | WSe2 | 562 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_071.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_072.sxm` | STM | WSe2 single crystal | WSe2 | 563 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_072.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_073.sxm` | STM | WSe2 single crystal | WSe2 | 564 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_073.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_074.sxm` | STM | WSe2 single crystal | WSe2 | 565 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_074.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_075.sxm` | STM | WSe2 single crystal | WSe2 | 566 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_075.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_076.sxm` | STM | WSe2 single crystal | WSe2 | 567 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_076.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_077.sxm` | STM | WSe2 single crystal | WSe2 | 568 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_077.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_078.sxm` | STM | WSe2 single crystal | WSe2 | 569 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_078.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_079.sxm` | STM | WSe2 single crystal | WSe2 | 570 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_079.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_080.sxm` | STM | WSe2 single crystal | WSe2 | 571 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_080.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_081.sxm` | STM | WSe2 single crystal | WSe2 | 572 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_081.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_082.sxm` | STM | WSe2 single crystal | WSe2 | 573 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_082.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_083.sxm` | STM | WSe2 single crystal | WSe2 | 574 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_083.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_084.sxm` | STM | WSe2 single crystal | WSe2 | 575 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_084.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_085.sxm` | STM | WSe2 single crystal | WSe2 | 576 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_085.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_086.sxm` | STM | WSe2 single crystal | WSe2 | 577 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_086.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_087.sxm` | STM | WSe2 single crystal | WSe2 | 578 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_087.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_088.sxm` | STM | WSe2 single crystal | WSe2 | 579 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_088.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_089.sxm` | STM | WSe2 single crystal | WSe2 | 580 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_089.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_090.sxm` | STM | WSe2 single crystal | WSe2 | 581 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_090.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_091.sxm` | STM | WSe2 single crystal | WSe2 | 582 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_091.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_092.sxm` | STM | WSe2 single crystal | WSe2 | 583 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_092.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_093.sxm` | STM | WSe2 single crystal | WSe2 | 584 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_093.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_094.sxm` | STM | WSe2 single crystal | WSe2 | 585 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_094.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_095.sxm` | STM | WSe2 single crystal | WSe2 | 586 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_095.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_096.sxm` | STM | WSe2 single crystal | WSe2 | 587 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_096.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_097.sxm` | STM | WSe2 single crystal | WSe2 | 588 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_097.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_098.sxm` | STM | WSe2 single crystal | WSe2 | 589 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_098.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_099.sxm` | STM | WSe2 single crystal | WSe2 | 590 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_099.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_100.sxm` | STM | WSe2 single crystal | WSe2 | 591 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_100.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_101.sxm` | STM | WSe2 single crystal | WSe2 | 592 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_101.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_102.sxm` | STM | WSe2 single crystal | WSe2 | 593 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_102.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_103.sxm` | STM | WSe2 single crystal | WSe2 | 594 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_103.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_104.sxm` | STM | WSe2 single crystal | WSe2 | 595 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_104.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_105.sxm` | STM | WSe2 single crystal | WSe2 | 596 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_105.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_106.sxm` | STM | WSe2 single crystal | WSe2 | 597 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_106.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_107.sxm` | STM | WSe2 single crystal | WSe2 | 598 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_107.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_108.sxm` | STM | WSe2 single crystal | WSe2 | 599 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_108.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_109.sxm` | STM | WSe2 single crystal | WSe2 | 600 | `zenodo/10443995/STM_data/2021-11-23/STM_WTip_WSe2-SL445_109.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_001.sxm` | STM | WSe2 single crystal | WSe2 | 601 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_001.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_002.sxm` | STM | WSe2 single crystal | WSe2 | 602 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_002.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_003.sxm` | STM | WSe2 single crystal | WSe2 | 603 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_003.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_004.sxm` | STM | WSe2 single crystal | WSe2 | 604 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_004.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_005.sxm` | STM | WSe2 single crystal | WSe2 | 605 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_005.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_006.sxm` | STM | WSe2 single crystal | WSe2 | 606 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_006.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_007.sxm` | STM | WSe2 single crystal | WSe2 | 607 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_007.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_008.sxm` | STM | WSe2 single crystal | WSe2 | 608 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_008.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_009.sxm` | STM | WSe2 single crystal | WSe2 | 609 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_009.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_010.sxm` | STM | WSe2 single crystal | WSe2 | 610 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_010.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_011.sxm` | STM | WSe2 single crystal | WSe2 | 611 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_011.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_012.sxm` | STM | WSe2 single crystal | WSe2 | 612 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_012.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_013.sxm` | STM | WSe2 single crystal | WSe2 | 613 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_013.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_014.sxm` | STM | WSe2 single crystal | WSe2 | 614 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_014.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_015.sxm` | STM | WSe2 single crystal | WSe2 | 615 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_015.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_016.sxm` | STM | WSe2 single crystal | WSe2 | 616 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_016.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_017.sxm` | STM | WSe2 single crystal | WSe2 | 617 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_017.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_018.sxm` | STM | WSe2 single crystal | WSe2 | 618 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_018.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_019.sxm` | STM | WSe2 single crystal | WSe2 | 619 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_019.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_020.sxm` | STM | WSe2 single crystal | WSe2 | 620 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_020.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_021.sxm` | STM | WSe2 single crystal | WSe2 | 621 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_021.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_022.sxm` | STM | WSe2 single crystal | WSe2 | 622 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_022.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_023.sxm` | STM | WSe2 single crystal | WSe2 | 623 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_023.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_024.sxm` | STM | WSe2 single crystal | WSe2 | 624 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_024.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_025.sxm` | STM | WSe2 single crystal | WSe2 | 625 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_025.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_026.sxm` | STM | WSe2 single crystal | WSe2 | 626 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_026.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_027.sxm` | STM | WSe2 single crystal | WSe2 | 627 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_027.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_028.sxm` | STM | WSe2 single crystal | WSe2 | 628 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_028.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_029.sxm` | STM | WSe2 single crystal | WSe2 | 629 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_029.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_030.sxm` | STM | WSe2 single crystal | WSe2 | 630 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_030.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_031.sxm` | STM | WSe2 single crystal | WSe2 | 631 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_031.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_032.sxm` | STM | WSe2 single crystal | WSe2 | 632 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_032.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_033.sxm` | STM | WSe2 single crystal | WSe2 | 633 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_033.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_034.sxm` | STM | WSe2 single crystal | WSe2 | 634 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_034.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_035.sxm` | STM | WSe2 single crystal | WSe2 | 635 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_035.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_036.sxm` | STM | WSe2 single crystal | WSe2 | 636 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_036.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_037.sxm` | STM | WSe2 single crystal | WSe2 | 637 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_037.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_038.sxm` | STM | WSe2 single crystal | WSe2 | 638 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_038.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_039.sxm` | STM | WSe2 single crystal | WSe2 | 639 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_039.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_040.sxm` | STM | WSe2 single crystal | WSe2 | 640 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_040.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_041.sxm` | STM | WSe2 single crystal | WSe2 | 641 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_041.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_042.sxm` | STM | WSe2 single crystal | WSe2 | 642 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_042.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_043.sxm` | STM | WSe2 single crystal | WSe2 | 643 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_043.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_044.sxm` | STM | WSe2 single crystal | WSe2 | 644 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_044.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_045.sxm` | STM | WSe2 single crystal | WSe2 | 645 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_045.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_046.sxm` | STM | WSe2 single crystal | WSe2 | 646 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_046.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_047.sxm` | STM | WSe2 single crystal | WSe2 | 647 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_047.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_048.sxm` | STM | WSe2 single crystal | WSe2 | 648 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_048.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_049.sxm` | STM | WSe2 single crystal | WSe2 | 649 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_049.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_050.sxm` | STM | WSe2 single crystal | WSe2 | 650 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_050.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_051.sxm` | STM | WSe2 single crystal | WSe2 | 651 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_051.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_052.sxm` | STM | WSe2 single crystal | WSe2 | 652 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_052.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_053.sxm` | STM | WSe2 single crystal | WSe2 | 653 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_053.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_054.sxm` | STM | WSe2 single crystal | WSe2 | 654 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_054.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_055.sxm` | STM | WSe2 single crystal | WSe2 | 655 | `zenodo/10443995/STM_data/2021-11-26/STM_WTip_WSe2-SL445_055.sxm/` | True | True |
| `V-Spec_WTip_WSe2-SL445_001.dat` | STM | WSe2 single crystal | WSe2 | 656 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_001.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_002.dat` | STM | WSe2 single crystal | WSe2 | 657 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_002.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_003.dat` | STM | WSe2 single crystal | WSe2 | 658 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_003.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_004.dat` | STM | WSe2 single crystal | WSe2 | 659 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_004.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_005.dat` | STM | WSe2 single crystal | WSe2 | 660 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_005.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_006.dat` | STM | WSe2 single crystal | WSe2 | 661 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_006.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_007.dat` | STM | WSe2 single crystal | WSe2 | 662 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_007.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_008.dat` | STM | WSe2 single crystal | WSe2 | 663 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_008.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_009.dat` | STM | WSe2 single crystal | WSe2 | 664 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_009.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_010.dat` | STM | WSe2 single crystal | WSe2 | 665 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_010.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_011.dat` | STM | WSe2 single crystal | WSe2 | 666 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_011.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_012.dat` | STM | WSe2 single crystal | WSe2 | 667 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_012.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_013.dat` | STM | WSe2 single crystal | WSe2 | 668 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_013.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_014.dat` | STM | WSe2 single crystal | WSe2 | 669 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_014.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_015.dat` | STM | WSe2 single crystal | WSe2 | 670 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_015.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_016.dat` | STM | WSe2 single crystal | WSe2 | 671 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_016.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_017.dat` | STM | WSe2 single crystal | WSe2 | 672 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_017.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_018.dat` | STM | WSe2 single crystal | WSe2 | 673 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_018.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_019.dat` | STM | WSe2 single crystal | WSe2 | 674 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_019.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_020.dat` | STM | WSe2 single crystal | WSe2 | 675 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_020.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_021.dat` | STM | WSe2 single crystal | WSe2 | 676 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_021.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_022.dat` | STM | WSe2 single crystal | WSe2 | 677 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_022.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_023.dat` | STM | WSe2 single crystal | WSe2 | 678 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_023.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_024.dat` | STM | WSe2 single crystal | WSe2 | 679 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_024.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_025.dat` | STM | WSe2 single crystal | WSe2 | 680 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_025.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_026.dat` | STM | WSe2 single crystal | WSe2 | 681 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_026.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_027.dat` | STM | WSe2 single crystal | WSe2 | 682 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_027.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_028.dat` | STM | WSe2 single crystal | WSe2 | 683 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_028.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_029.dat` | STM | WSe2 single crystal | WSe2 | 684 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_029.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_030.dat` | STM | WSe2 single crystal | WSe2 | 685 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_030.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_031.dat` | STM | WSe2 single crystal | WSe2 | 686 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_031.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_032.dat` | STM | WSe2 single crystal | WSe2 | 687 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_032.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_033.dat` | STM | WSe2 single crystal | WSe2 | 688 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_033.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_034.dat` | STM | WSe2 single crystal | WSe2 | 689 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_034.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_035.dat` | STM | WSe2 single crystal | WSe2 | 690 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_035.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_036.dat` | STM | WSe2 single crystal | WSe2 | 691 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_036.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_037.dat` | STM | WSe2 single crystal | WSe2 | 692 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_037.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_038.dat` | STM | WSe2 single crystal | WSe2 | 693 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_038.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_039.dat` | STM | WSe2 single crystal | WSe2 | 694 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_039.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_040.dat` | STM | WSe2 single crystal | WSe2 | 695 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_040.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_041.dat` | STM | WSe2 single crystal | WSe2 | 696 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_041.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_042.dat` | STM | WSe2 single crystal | WSe2 | 697 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_042.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_043.dat` | STM | WSe2 single crystal | WSe2 | 698 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_043.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_044.dat` | STM | WSe2 single crystal | WSe2 | 699 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_044.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_045.dat` | STM | WSe2 single crystal | WSe2 | 700 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_045.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_046.dat` | STM | WSe2 single crystal | WSe2 | 701 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_046.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_047.dat` | STM | WSe2 single crystal | WSe2 | 702 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_047.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_048.dat` | STM | WSe2 single crystal | WSe2 | 703 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_048.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_049.dat` | STM | WSe2 single crystal | WSe2 | 704 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_049.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_050.dat` | STM | WSe2 single crystal | WSe2 | 705 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_050.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_051.dat` | STM | WSe2 single crystal | WSe2 | 706 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_051.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_052.dat` | STM | WSe2 single crystal | WSe2 | 707 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_052.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_053.dat` | STM | WSe2 single crystal | WSe2 | 708 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_053.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_054.dat` | STM | WSe2 single crystal | WSe2 | 709 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_054.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_055.dat` | STM | WSe2 single crystal | WSe2 | 710 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_055.dat/` | True | True |
| `V-Spec_WTip_WSe2-SL445_056.dat` | STM | WSe2 single crystal | WSe2 | 711 | `zenodo/10443995/STM_data/2021-11-26/V-Spec_WTip_WSe2-SL445_056.dat/` | True | True |
| `STM_WTip_WSe2-SL445_001.sxm` | STM | WSe2 single crystal | WSe2 | 712 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_001.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_002.sxm` | STM | WSe2 single crystal | WSe2 | 713 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_002.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_003.sxm` | STM | WSe2 single crystal | WSe2 | 714 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_003.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_004.sxm` | STM | WSe2 single crystal | WSe2 | 715 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_004.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_005.sxm` | STM | WSe2 single crystal | WSe2 | 716 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_005.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_006.sxm` | STM | WSe2 single crystal | WSe2 | 717 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_006.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_007.sxm` | STM | WSe2 single crystal | WSe2 | 718 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_007.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_008.sxm` | STM | WSe2 single crystal | WSe2 | 719 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_008.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_009.sxm` | STM | WSe2 single crystal | WSe2 | 720 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_009.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_010.sxm` | STM | WSe2 single crystal | WSe2 | 721 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_010.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_011.sxm` | STM | WSe2 single crystal | WSe2 | 722 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_011.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_012.sxm` | STM | WSe2 single crystal | WSe2 | 723 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_012.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_013.sxm` | STM | WSe2 single crystal | WSe2 | 724 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_013.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_014.sxm` | STM | WSe2 single crystal | WSe2 | 725 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_014.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_015.sxm` | STM | WSe2 single crystal | WSe2 | 726 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_015.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_016.sxm` | STM | WSe2 single crystal | WSe2 | 727 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_016.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_017.sxm` | STM | WSe2 single crystal | WSe2 | 728 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_017.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_018.sxm` | STM | WSe2 single crystal | WSe2 | 729 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_018.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_019.sxm` | STM | WSe2 single crystal | WSe2 | 730 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_019.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_020.sxm` | STM | WSe2 single crystal | WSe2 | 731 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_020.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_021.sxm` | STM | WSe2 single crystal | WSe2 | 732 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_021.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_022.sxm` | STM | WSe2 single crystal | WSe2 | 733 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_022.sxm/` | True | True |
| `STM_WTip_WSe2-SL445_023.sxm` | STM | WSe2 single crystal | WSe2 | 734 | `zenodo/10443995/STM_data/2021-11-27/STM_WTip_WSe2-SL445_023.sxm/` | True | True |
| `*.ini` | STM | WSe2 single crystal | WSe2 | 7 | `zenodo/10443995/STM_data/` | — | — |
| `*.zip` | STM | WSe2 single crystal | WSe2 | 2 | `zenodo/10443995/STM_data/` | — | — |
| `*.jpg` | STM | WSe2 single crystal | WSe2 | 236 | `zenodo/10443995/STM_images/` | — | — |
| `*.npy` | STM | WSe2 single crystal | WSe2 | 1 | `zenodo/10443995/WSe2-Defect-Training-Images_2023-05-01.npy/` | — | — |
| `*.npy` | STM | WSe2 single crystal | WSe2 | 1 | `zenodo/10443995/WSe2-Defect-Training-Labels_2023-05-01.npy/` | — | — |
| `*.csv` | STM | WSe2 single crystal | WSe2 | 1 | `zenodo/10443995/annotations.csv/` | — | — |
| `*.json` | STM | WSe2 single crystal | WSe2 | 1 | `zenodo/10443995/annotations.json/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08/09 with `pynxtools-spm` 0.2.5. License **`cc-by-4.0`** passes the
open-license gate. **All 678 `.sxm` STM + all 56 `.dat` STS files converted, validated, and
uploaded** (`PS = True`, `Uploaded = True`).

- **STM `.sxm` (678/678):** default `current_forward`; short units, 0 shape mismatches.
- **STS `.dat` (56/56):** genuine Nanonis STS (header `Experiment<TAB>bias spectroscopy`).
  Recovered with a **per-dataset `config.json`** (copied from `ElnExamples/nanonis_dat_sts` and
  edited so `raw_path` is a list — this dataset mixes averaged-sweep `Current [AVG]` and
  single-sweep `Current` channel names; the src default config was not touched). Default
  `current` (+ `current_grad` = numerical dI/dV).

Output `.nxs` named meaningfully as `WSe2_<raw_stem>.nxs`. `citeID.description` carries the full
Zenodo description + the original raw file name.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 678/678 `.sxm` + 56/56 `.dat` converted (`PS = True`)
- [x] Reference .nxs files generated and uploaded for all 734 files
