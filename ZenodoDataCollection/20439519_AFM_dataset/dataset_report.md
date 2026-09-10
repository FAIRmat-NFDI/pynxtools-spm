# Dataset Report: Zenodo Record 20439519

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset - Autonomous scanning electrochemical cell microscopy enables rapid exploration of large compositionally complex material spaces |
| **DOI**    | [10.5281/zenodo.20439519](https://doi.org/10.5281/zenodo.20439519) |
| **Url**    | [https://zenodo.org/records/20439519](https://zenodo.org/records/20439519) |
| **Date**   | 2026-05-28 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Thelen, Felix; Kim, Moonjoo; de Oliveira, Geovane Arruda et al. |
| **Tags**   | Hydrogen evolution reaction, Active learning, Electrochemistry, Materials science, Magetron sputtering, Scanning electrochemical cell microscopy, Gaussian process regression, Electrocatalysis, Materials libraries, High-throughput characterization |
| **Description** | This dataset contains all experimental and computational data associated with the autonomous Scanning Electrochemical Cell Microscopy (SECCM) platform described in the accompanying publication. The platform combines robotic SECCM with active learning and multi-output Gaussian process (GP) modeling for high-throughput electrochemical characterization of compositionally complex thin-film materials libraries, validated on the Au-Ir-Rh ternary system as a model case for hydrogen evolution reaction (HER) electrocatalyst discovery. <br><br> Three Au-Ir-Rh thin-film materials libraries were fabricated by magnetron co-sputtering onto 100 mm diameter Sapphire wafers and are referred to throughout as Au-rich, Ir-rich, and Rh-rich according to their position in the ternary composition space. All characterization techniques share a unified measurement grid of 342 measurement areas distributed across each library at 4.5 mm spacing. A coordinates file providing the x, y positions of all 342 MAs is included. <br><br> Dataset contents: <br><br> Energy-Dispersive X-ray Spectroscopy (EDX) Volume compositions (Au, Ir, Rh in at.%) at all 342 MAs for each of the three libraries. Provided in .csv format. X-ray Photoelectron Spectroscopy (XPS) Due to the lower throughput of XPS, 13 localized surface composition measurements were performed per library. The full set of measurement areas were predicted using a Gaussian process regression model (method described here (https://doi.org/10.1002/aidi.202500062)). Two files are provided per library: one containing the measured XPS compositions and one containing the GP-predicted values. In addition to Au, Ir, and Rh, the XPS dataset includes surface contents of oxygen (O), carbon (C), native Rh oxide, and Rh hydroxide. Provided in .csv format. <br><br> - X-ray Diffraction (XRD) Diffractograms (2θ position vs. intensity in counts) at all 342 areas for each library. Provided in .csv format. Atomic Force Microscopy (AFM) Raw data from 15 localized AFM measurements (5 per library), recorded in Bruker NanoScope raw data format. Representative images are shown in the Supporting Information of the accompanying paper. SECCM Linear sweep voltammograms (LSVs) acquired at each area for all three libraries. Due to collision risk of the environmental chamber, 20 areas per library were excluded, yielding 322 LSVs per library. Each LSV file contains three columns: potential vs. the reversible hydrogen electrode (RHE, in V), mean current density (in A/cm^2), and the standard deviation of the current density, computed from three individually recorded LSVs that are averaged per measurement area. An additional file contains the parameters extracted by fitting the averaged LSVs to an analytical equation described in the publication: the limiting current density I_lim (A/cm^2), the transfer coefficient α (dimensionless), and the standard rate constant k^0 (cm/s). Provided in .csv format. Active Learning Animations: Two animations (.mp4 format) illustrating the active learning process applied to the Au-Ir-Rh composition space. Each frame corresponds to one iteration of the algorithm and displays the current LSV data, the extracted fit parameters, the GP model predictions across the ternary space, and the acquisition function values used to select the next measurement. One animation corresponds to the baseline GP implementation; the second corresponds to the noise-aware GP variant, which incorporates per-area measurement uncertainty derived from the standard deviations of the individual LSV fit parameters prior to averaging. Measurement Video: (.mp4) of the measurement process of the first 400 measurements/training iterations. It shows the robotic transfer, the environmental chamber and visual capillary approach and the electrocatalytic measurements. |
| **Experiment information related files** | `DataSetnote.txt`, `LSV_fit_parameters.csv` |

## Technique

- **Primary SPM technique**: Atomic Force Microscopy (AFM, PeakForce Tapping)
- **Instrument vendor**: Bruker (NanoScope raw format, firmware `0x05120000` ≈ v5.12; files have
  **no extension**)
- **Additional techniques in dataset**: EDX, XPS, XRD, SECCM

## Sample

- **Material / chemical formula**: **Au-Ir-Rh** ternary thin-film **materials library**
  (composition-spread) → `Au-Ir-Rh` (no single fixed stoichiometry; three regions: Au-rich,
  Ir-rich, Rh-rich).
- **Substrate / preparation**: fabricated by **magnetron co-sputtering** onto a 100 mm sapphire
  wafer; a composition-spread library screened for the hydrogen evolution reaction by autonomous
  SECCM (+ AFM, EDX, XPS, XRD).

## Dataset Contents

15 AFM measurements (5 per Au-Ir-Rh ternary library: Au-rich, Ir-rich, Rh-rich) on thin-film
materials libraries fabricated by magnetron co-sputtering on 100 mm Sapphire wafers.
Files use Bruker NanoScope raw format without `.spm` extension.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/20439519/`  
**Upload date**: 2026-06-25  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 2018 files

**S3 key pattern**: `zenodo/20439519/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

**Skipped**: 3 `.mp4` animation/video files (~550 MB total) — not SPM data.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `Au-Ir-Rh_Au-rich_AFM_area_168.002` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 1 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_168.002/` | True | True |
| `Au-Ir-Rh_Au-rich_AFM_area_178.004` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 2 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_178.004/` | True | True |
| `Au-Ir-Rh_Au-rich_AFM_area_20.003` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 3 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_20.003/` | True | True |
| `Au-Ir-Rh_Au-rich_AFM_area_313.000` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 4 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_313.000/` | True | True |
| `Au-Ir-Rh_Au-rich_AFM_area_55.005` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 5 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_55.005/` | True | True |
| `Au-Ir-Rh_Ir-rich_AFM_area_13.000` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 6 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_13.000/` | True | True |
| `Au-Ir-Rh_Ir-rich_AFM_area_168.001` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 7 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_168.001/` | True | True |
| `Au-Ir-Rh_Ir-rich_AFM_area_178.002` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 8 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_178.002/` | True | True |
| `Au-Ir-Rh_Ir-rich_AFM_area_315.003` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 9 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_315.003/` | True | True |
| `Au-Ir-Rh_Ir-rich_AFM_area_342.004` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 10 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Ir-rich_AFM_area_342.004/` | True | True |
| `Au-Ir-Rh_Rh-rich_AFM_area_16.005` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 11 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_16.005/` | True | True |
| `Au-Ir-Rh_Rh-rich_AFM_area_168.008` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 12 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_168.008/` | True | True |
| `Au-Ir-Rh_Rh-rich_AFM_area_200.010` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 13 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_200.010/` | True | True |
| `Au-Ir-Rh_Rh-rich_AFM_area_240.006` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 14 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_240.006/` | True | True |
| `Au-Ir-Rh_Rh-rich_AFM_area_297.009` | AFM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 15 | `zenodo/20439519/AFM_dataset/Au-Ir-Rh_Rh-rich_AFM_area_297.009/` | True | True |
| `*.csv` | EDX | Au-Ir-Rh thin-film library | Au-Ir-Rh | 3 | `zenodo/20439519/EDX_dataset/` | — | — |
| `*.csv` | SECCM | Au-Ir-Rh thin-film library | Au-Ir-Rh | 966 | `zenodo/20439519/SECCM_dataset/` | — | — |
| `*.csv` | XPS | Au-Ir-Rh thin-film library | Au-Ir-Rh | 6 | `zenodo/20439519/XPS_dataset/` | — | — |
| `*.xy` | XRD | Au-Ir-Rh thin-film library | Au-Ir-Rh | 1026 | `zenodo/20439519/XRD_dataset/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `DataSetnote.txt` | AFM | 1 | `zenodo/20439519/AFM_dataset/DataSetnote.txt/` |
| `LSV_fit_parameters.csv` | SECCM | 2 | `zenodo/20439519/SECCM_dataset/LSV_fit_parameters.csv/` |

## Conversion (CONTEXT 2)

Processed 2026-07-08 with `pynxtools-spm` 0.2.5 / `pySPM` 0.6.3. License **`cc-by-4.0`** passes
the open-license gate. The 15 AFM files have **no extension**, so each was copied to a temporary
`.spm`-named file so the reader could classify it, then converted; the `eln_data.yaml`,
`config.json`, and `.nxs` were uploaded into each file's **original** (extensionless) S3 folder.
**All 15 converted, validated, and uploaded** (`PS = True`, `Uploaded = True`). PeakForce QNM
(PeakForce config, scientific titles); 4 NXdata groups (Topography, Peak Force Error × fwd/bwd),
default `z_forward`; post-audit: **0 long units, 0 shape mismatches, 0 bad defaults**.
`citeID.description` carries the full Zenodo description. The EDX/XPS/SECCM/XRD files are other
techniques (grouped rows, not converted).

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 15/15 AFM files converted (`PS = True`)
- [x] Reference .nxs files generated and uploaded for all 15 AFM files
