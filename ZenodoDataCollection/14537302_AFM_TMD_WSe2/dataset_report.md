# Dataset Report: Zenodo Record 14537302

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Role of Chalcogen atoms in In-Situ Exfoliation of Large-Area 2D Semiconducting Transition Metal Dichalcogenides |
| **DOI**    | [10.5281/zenodo.14537302](https://doi.org/10.5281/zenodo.14537302) |
| **Url**    | [https://zenodo.org/records/14537302](https://zenodo.org/records/14537302) |
| **Date**   | 2024-12-20 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Grubisic-Cabo, Antonija |
| **Tags**   | 2D materials, Transition metal dichalcogenides, XPS, LEED, Exfoliation, KISS |
| **Description** | Datasets for "Role of Chalcogen atoms in In Situ Exfoliation of Large-Area 2D Semiconducting Transition Metal Dichalcogenides" publication. <br><br> Optical microscopy, atomic force microscopy (AFM), low-energy electron diffraction (LEED) and X-ray photoelectron spectrocopy measurements (XPS). Measurements were conducted at the Zernike Institute for Advanced Materials in Groningen, The Netherlands. All measurements were performed at room temperature. LEED measurements are obtained using electron energy of 125 eV, while XPS measurements were performed using photon energy of 1486.6 eV (Al anode). <br><br> Experimental data are provided in jpeg format (optical microsopy images, LEED data), spm (AFM data) and txt (XPS data). |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy, TappingMode) + XPS + LEED + Optical Microscopy
- **Instrument**: Bruker AFM (NanoScope format, `.spm`)

## Sample

- **Material / chemical formula**: **WSe₂** (tungsten diselenide), a 2D semiconducting transition
  metal dichalcogenide → `WSe2`.
- **Substrate**: silver (**Ag**); the AFM file `Figure4b_WSe2-Ag-S1` is WSe₂ on Ag.
- **Preparation**: large-area WSe₂ exfoliated in situ from a bulk crystal by the KISS
  ("Kinetic in situ single-layer synthesis") method. Study also includes XPS, LEED, and optical
  microscopy (measured at the Zernike Institute, Groningen; room temperature).

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

**S3 key pattern**: `zenodo/14537302/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `Figure4b_WSe2-Ag-S1.0_00000.spm` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure4b_WSe2-Ag-S1.0_00000.spm/` | True | True |
| `*.txt` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/230418BD WSe2_Se3p_Figure5c.txt/` | — | — |
| `*.txt` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/230418BD WSe2_W4f_Figure5b.txt/` | — | — |
| `*.txt` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/230418BD_WSe2_Au_Survey_Figure5a.txt/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure1f.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure2a_Sample1.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure2a_Sample2.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure2a_Sample3.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure2a_Sample4.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure2b_Sample1.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure2b_Sample2.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure2b_Sample3.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure2b_Sample4.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure3a.jpg/` | — | — |
| `*.jpg` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure3b.jpg/` | — | — |
| `*.png` | AFM | WSe2 (2D TMD, on Ag) | WSe2 | 1 | `zenodo/14537302/Figure4a.png/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08 with `pynxtools-spm` 0.2.5 / `pySPM` 0.6.3. License **`cc-by-4.0`** passes
the open-license gate. **The 1 native Bruker `.spm` converted, validated, and uploaded**
(`PS = True`, `Uploaded = True`) with `eln_data.yaml` + `config.json` + `.nxs` in its S3 folder.
TappingMode (default config, scientific titles); 6 NXdata groups (Topography, Amplitude Error,
Phase × fwd/bwd), default `z_forward`; short units, no shape mismatch. The XPS `.txt` and
optical `.jpg` files are out of scope. `citeID.description` carries the full Zenodo description.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 1/1 `.spm` converted (`PS = True`)
- [x] Reference .nxs file generated and uploaded
