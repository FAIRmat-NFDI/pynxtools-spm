# Dataset Report: Zenodo Record 14271622

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Raw data for "AFM as a Multimetrological Platform" Manuscript |
| **DOI**    | [10.5281/zenodo.14271622](https://doi.org/10.5281/zenodo.14271622) |
| **Date**   | 2024-12-04 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Aslan, Husnu; Kaja, Khaled; Piquemal, François; Moran-Meza, Jose et al. |
| **Tags**   | AFM, multimetrological, dimensional, electrical, Kelvin probe, SPM |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — multiple modes including dimensional, electrical, Kelvin probe
- **Instrument**: Multiple instruments (Bruker .spm confirmed for some files)

## Dataset Contents

Raw SPM data collected with different instruments for a multimetrological AFM study. 28 objects: large zip (`Fig.2_3_6_7_8_9.zip`, 1.6 GB) extracted into folders, plus `Fig. 4.zip` and `Fig. 5.zip` extracted. Contains Bruker `.spm` files confirmed (e.g., `NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm`).

## File Format

- **Format**: Bruker `.spm` (confirmed), possibly other formats from different instruments
- **Parsability**: Bruker `.spm` files are parsable by `BrukerSpmAFM`. Other instrument files require format investigation.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14271622/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 28 files

**S3 key pattern**: `zenodo/14271622/<folder>/<filename>/<filename>`

### Bruker .spm AFM files — 5 files ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14271622/NW_GaAs_))

Source zip: `MultiMetrology_AFM_Manuscript_Fig.2_3_6_7_8_9.zip`

| file | experiment | S3 key |
|------|------------|--------|
| `NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm`  | AFM | `zenodo/14271622/NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm/NW_GaAs_non-passive_C3275_dark_DOWN_00005.spm` |
| `NW_GaAs_non-passive_C3275_dark UP_00006.spm`    | AFM | `zenodo/14271622/NW_GaAs_non-passive_C3275_dark UP_00006.spm/NW_GaAs_non-passive_C3275_dark UP_00006.spm` |
| `NW_GaAs_non-passive_C3275_camLight-DOWN_00007.spm` | AFM | `zenodo/14271622/NW_GaAs_non-passive_C3275_camLight-DOWN_00007.spm/NW_GaAs_non-passive_C3275_camLight-DOWN_00007.spm` |
| `NW_GaAs_non-passive_C3275_camLight-Up_00008.spm`  | AFM | `zenodo/14271622/NW_GaAs_non-passive_C3275_camLight-Up_00008.spm/NW_GaAs_non-passive_C3275_camLight-Up_00008.spm` |
| `NW_GaAs_non-passive_C3275_00000.0_00009.spm`    | AFM | `zenodo/14271622/NW_GaAs_non-passive_C3275_00000.0_00009.spm/NW_GaAs_non-passive_C3275_00000.0_00009.spm` |

### Figure 4 data — 9 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14271622/Fig.%204/))

Source zip: `MultiMetrology_AFM_Manuscript_Fig. 4.zip` — 1 SVG + 8 TIFF channel images (Z Height, NCM Amplitude, NCM Phase, Z Detector Corrected; fwd/bwd)

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `Fig. 4/MultmetrologicalAFM_Fig4.svg` | AFM | 1 | `zenodo/14271622/Fig. 4/MultmetrologicalAFM_Fig4.svg/` |
| `Fig. 4/Raw data/<channel>_<dir>.tiff` | AFM | 8 | `zenodo/14271622/Fig. 4/Raw data/` |

### Figure 5 data — 12 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/14271622/Fig.%205/))

Source zip: `MultiMetrology_AFM_Manuscript_Fig. 5.zip` — 12 TIFF channel images (NCM Phase, Z Height, Error Signal, EFM Amplitude/Phase/Quad; fwd/bwd)

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `Fig. 5/NWs Sample1_<timestamp>_<channel>_<dir>.tiff` | AFM | 12 | `zenodo/14271622/Fig. 5/` |

### Session archives — 2 files

| file | experiment | S3 key |
|------|------------|--------|
| `04_13_23_Jeudi.zip`   | AFM | `zenodo/14271622/04_13_23_Jeudi.zip/04_13_23_Jeudi.zip` |
| `04-14-23_Vendredi.zip` | AFM | `zenodo/14271622/04-14-23_Vendredi.zip/04-14-23_Vendredi.zip` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
