# Dataset Report: Zenodo Record 11234725

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Atomic Force Microscopy image of coagulation factor Va in liquid |
| **DOI**    | [10.5281/zenodo.11234725](https://doi.org/10.5281/zenodo.11234725) |
| **Url**    | [https://zenodo.org/records/11234725](https://zenodo.org/records/11234725) |
| **Date**   | 2014-09-04 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Pellequer |
| **Tags**   | AFM, coagulation factor Va, peak force tapping, liquid imaging |
| **Description** | Original raw and corrected AFM images of isolated coagulation factor Va (FVa). The image was acquired in liquid with an OTR8 cantilever using the peak force tapping mode of a multimode V microscope. The image size is 1 x 1 µm² with 1024 x 1024 pixels². The corrected image was obtained using Gwyddion (.gwy file) from the raw image file (.spm). This image was the experimental data used to assemble the A trimer and the two C domains of FVa using the AFMAssembly pipeline described in Chaves et al. (2014): http://dx.doi.org/10.1160/TH14-06-0481. The paper can be downloaded from the HAL repository (https://hal.archives-ouvertes.fr/hal-01146300v1). |
| **Experiment information related files** | None |

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

**S3 key pattern**: `zenodo/11234725/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `11s4_fva_e6_1,5nM_mgcl2_liquid_otr8_z1_1um.003.spm` | AFM | 1 | `zenodo/11234725/FVa/11s4_fva_e6_1,5nM_mgcl2_liquid_otr8_z1_1um.003.spm/` | — | — |
| `*.gwy` | AFM | 1 | `zenodo/11234725/FVa/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
