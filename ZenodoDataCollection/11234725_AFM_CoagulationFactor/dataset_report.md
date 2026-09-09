# Dataset Report: Zenodo Record 11234725

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Atomic Force Microscopy image of coagulation factor Va in liquid |
| **DOI**    | [10.5281/zenodo.11234725](https://doi.org/10.5281/zenodo.11234725) |
| **Date**   | 2014-09-04 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Pellequer |
| **Tags**   | AFM, coagulation factor Va, peak force tapping, liquid imaging |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — Peak Force Tapping in liquid
- **Instrument**: Bruker Multimode V, OTR8 cantilever

## Dataset Contents

Single AFM image (1×1 µm², 1024×1024 px) of isolated coagulation factor Va (FVa) acquired in liquid with Peak Force Tapping. Includes raw `.spm` file and processed Gwyddion `.gwy` file.

## File Format

- **Format**: Bruker `.spm`
- **Parsability**: Potentially parsable by `BrukerSpmAFM`. Single file extracted from zip into `FVa/` folder.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/11234725/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 2 files

**S3 key pattern**: `zenodo/11234725/<folder>/<filename>/<filename>`

Source zip: `Data_AFM_Coagulation_FactorVa_PeakForce_Liquid_OTR8_2011.zip` → extracted into `FVa/` ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/11234725/FVa/))

| file | experiment | S3 key |
|------|------------|--------|
| `11s4_fva_e6_1,5nM_mgcl2_liquid_otr8_z1_1um.003.spm` | AFM | `zenodo/11234725/FVa/11s4_fva_e6_1,5nM_mgcl2_liquid_otr8_z1_1um.003.spm/11s4_fva_e6_1,5nM_mgcl2_liquid_otr8_z1_1um.003.spm` |
| `11s4_fva_e6_1,5nM_mgcl2_liquid_otr8_z1_1um.003.gwy` | AFM | `zenodo/11234725/FVa/11s4_fva_e6_1,5nM_mgcl2_liquid_otr8_z1_1um.003.gwy/11s4_fva_e6_1,5nM_mgcl2_liquid_otr8_z1_1um.003.gwy` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted
- [ ] Reference .nxs file not yet generated
