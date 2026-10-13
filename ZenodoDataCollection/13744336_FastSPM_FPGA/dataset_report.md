# Dataset Report: Zenodo Record 13744336

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset supplementing journal article "Design of an FPGA-Based Controller for Fast Scanning Probe Microscopy" in Sensors 2024 |
| **DOI**    | [10.5281/zenodo.13744336](https://doi.org/10.5281/zenodo.13744336) |
| **Url**    | [https://zenodo.org/records/13744336](https://zenodo.org/records/13744336) |
| **Date**   | 2024-09-11 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Gregorat, Leonardo; Cautero, Marco; Carrato, Sergio et al. |
| **Tags**   | fast SPM, FPGA, STM, AFM, scanning probe microscopy |
| **Description** | Dataset supplementing journal article "Design of an FPGA-Based Controller for Fast Scanning Probe Microscopy" in Sensors 2024. <br><br> Fast imaging measurements showed in Figure 9 of the article:  <br><br> 9a: Fast STM of a static Pt5 cluster on a Fe3O4(001) magnetite surface, taken at room temperature in a UHV chamber with an Omicron VT-AFM microscope at 4 frames/s; pixel resolution 100x100 pixels; image size 8x8 nm2. <br><br> 9b: Fast STM of a Pd-octaethylporphyrin monolayer on a Au(111) surface under electrolyte (phosphate buffer, pH= 7, Ar-saturated), taken with a Beetle-type EC-STM at 12 frames/s (EWE = +0.65 vs RHE, Ub = +0.4 V vs WE); pixel resolution 120x120 pixels; image size 8x8 nm2. <br><br> 9c: Fast AFM images of a Mikromasch TGX1 test grating with a 3 μm pitch and a 130 nm height, taken in contact mode with an Asylum Research/Oxford Instruments MFP-3D microscope (Mikromasch NSC36 probe - 0.6 N/m cantilever) at 4 frames/s; pixel resolution 100x100 pixels. |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: STM + AFM (fast imaging)
- **Instrument**: Omicron VT-AFM (fast STM), Beetle-type EC-STM, MFP-3D (fast AFM)

## Dataset Contents

Fast imaging datasets: (9a) fast STM of Pt5 cluster on Fe₃O₄(001) at 4 fps; (9b) fast EC-STM of Pd-porphyrin on Au(111) at 12 fps; (9c) fast AFM of TGX1 grating at 4 fps. 24 objects extracted from data.zip.

## File Format

- **Format**: `.h5` / `.h5_meta` (Omicron fast SPM proprietary HDF5 variant)
- **Parsability**: Not supported. Format is `.h56` / `.h5_meta` from Omicron VT-AFM fast controller. No parser implemented.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/13744336/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 24 files

**S3 key pattern**: `zenodo/13744336/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `*.h5` | STM | 3 | `zenodo/13744336/data/` | — | — |
| `*.log` | STM | 3 | `zenodo/13744336/data/` | — | — |
| `*.mp4` | STM | 3 | `zenodo/13744336/data/` | — | — |
| `*.png` | STM | 12 | `zenodo/13744336/data/` | — | — |
| `*.txt` | STM | 3 | `zenodo/13744336/data/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Unknown/Unsupported Format**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
