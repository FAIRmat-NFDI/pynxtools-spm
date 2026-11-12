# Dataset Report: Zenodo Record 19254504

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Annexin V assembly dynamics on lipid bilayers by High-Speed AFM |
| **DOI**    | [10.5281/zenodo.19254504](https://doi.org/10.5281/zenodo.19254504) |
| **Url**    | [https://zenodo.org/records/19254504](https://zenodo.org/records/19254504) |
| **Date**   | 2026-03-27 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Heath, George R |
| **Tags**   | AFM, high-speed atomic force microscopy, atomic force microscopy, HS-AFM, annexin V, annexin, lipid bilayer, raw data |
| **Description** | This dataset contains curated high-speed atomic force microscopy (HS-AFM) videos capturing the dynamic assembly of Annexin V on supported lipid bilayers. Each movie is accompanied by a metadata table detailing key acquisition parameters and imaging conditions. <br><br> This dataset is released as an open resource and is made freely available to support reuse in high-speed AFM data analysis, algorithm development, machine learning applications, and studies of membrane protein assembly dynamics. <br><br> Methods Summary Membrane: DOPC:DOPS = 8:2 Protein: Annexin V (33 kDa, human placenta) in imaging solution Imaging Buffer: 10 mM HEPES (pH 7.4), 150 mM NaCl, 2 mMCaCl₂ AFM: NanoRacer (Bruker) Probe: USC-F1.2-k0.15 (NanoWorld) <br><br> Full method description  Annexin V (33 kDa, human placenta) was purchased from Sigma-Aldrich, and lipids dioleoyl-phosphatidylcholine (DOPC) and dioleoyl-phosphatidylserine (DOPS) were obtained from Avanti Polar Lipids. Lipids were mixed in chloroform at a molar ratio of DOPC:DOPS = 8:2. The solvent was evaporated under a nitrogen stream and further dried under vacuum for 2 hours. The resulting lipid film was resuspended in buffer (10 mM HEPES, pH 7.4, 150 mM NaCl, 2 mM CaCl₂) to form multilamellar vesicles. These were subsequently tip-sonicated for 10 minutes to produce small unilamellar vesicles (SUVs). <br><br> To form supported lipid bilayers (SLBs), 5 µL of the SUV suspension (0.1 mg mL⁻¹ total lipid concentration) was deposited onto freshly cleaved mica. Following vesicle fusion, excess lipids were removed by rinsing with deionized water and then buffer. Annexin V was introduced into the imaging buffer at varying concentrations (100-200nM). <br><br> All high-speed AFM measurements were performed using the NanoRacer HS-AFM (Bruker) operating in amplitude modulation mode. Imaging was conducted in liquid at ambient temperature within an acoustic isolation enclosure on an active anti-vibration table. Short cantilevers (USC-F1.2-k0.15, NanoWorld) were used, with nominal properties: Spring constant: ~0.15 N·m⁻¹; Resonance frequency: ~0.6 MHz; Quality factor: ~2 <br><br> Data Access and Tools The dataset includes raw HS-AFM image sequences along with associated metadata for each acquisition. Recommended tools for accessing and analysing the data: <br><br> - NanoLocz (https://github.com/George-R-Heath/NanoLocz/releases) <br><br> - PlayNano (https://github.com/derollins/playNano) <br><br> Note! Use the “Height” channel (feedback signal) rather than the “Height Measured” channel (capacitive measurement). Notes <br><br> - The dataset focuses on time-resolved membrane-protein assembly dynamics. <br><br> - Metadata fields include scan size, pixel resolution, scan speed, line rate, and imaging channel. <br><br> - Image files are organised in 1 zip per image stack, with corresponding entries in the metadata table: <br><br> Folder Name Frames Use channel Speed (FPS) Scan Size (nm) y pixels x pixels Pixel Per nm Line Speed (Hz) Notes <br><br> imaging-13.08.28.653 7 Height-ReTrace 0.78 600 256 256 0.43 200 diffusing annexin  <br><br> imaging-13.26.46.569 81 Height -Bi-Directional 1.56 100 256 256 2.56 200 diffusing annexin <br><br> imaging-13.30.11.268 8 Height -Bi-Directional 1.56 200 256 256 1.28 200 diffusing annexin  <br><br> imaging-13.37.48.575 7 Height -Bi-Directional 0.78 400 512 512 1.28 200 diffusing annexin  <br><br> imaging-13.46.35.510 59 Height -Bi-Directional 0.78 350 512 512 1.46 200 lattice appears <br><br> imaging-13.47.52.797 9 Height -Bi-Directional 0.78 200 512 512 2.56 200 lattice assembly  <br><br> imaging-13.48.05.546 41 Height -Bi-Directional 1.56 200 256 256 1.28 200 lattice assembly  <br><br> imaging-13.48.42.653 36 Height-ReTrace 0.78 200 256 256 1.28 200 lattice assembly  <br><br> imaging-13.49.30.677 17 Height -Bi-Directional 1.56 200 256 256 1.28 200 lattice assembly  <br><br> imaging-13.49.42.515 100 Height -Bi-Directional 2.73 200 256 256 1.28 350 lattice assembly  <br><br> imaging-13.51.38.236 75 Height -Bi-Directional 12.50 200 128 128 0.64 800 lattice assembly  <br><br> imaging-13.51.54.501 56 Height -Bi-Directional 15.63 200 128 128 0.64 1000 lattice assembly  <br><br> imaging-13.52.13.441 81 Height -Bi-Directional 11.72 200 128 128 0.64 750 lattice assembly  <br><br> imaging-13.52.33.276 73 Height -Bi-Directional 12.50 200 128 128 0.64 800 lattice assembly  <br><br> imaging-13.53.38.041 437 Height -Bi-Directional 23.44 100 64 128 1.28 750 lattice assembly  <br><br> imaging-13.54.14.288 436 Height -Bi-Directional 31.25 100 64 128 1.28 1000 lattice assembly  <br><br> imaging-13.55.22.617 490 Height -Bi-Directional 31.25 85 64 128 1.51 1000 lattice assembly  <br><br> imaging-13.55.40.346 762 Height -Bi-Directional 31.25 85 64 128 1.51 1000 lattice assembly  <br><br> imaging-14.01.11.254 15 Height -Bi-Directional 0.78 170 256 256 1.51 100 lattice assembly  <br><br> imaging-14.04.11.121 276 Height -Bi-Directional 23.44 120 64 128 1.07 750 lattice assembly  <br><br> imaging-14.14.05.504 14 Height-ReTrace 0.75 70 400 400 5.71 300 lattice  <br><br> imaging-14.14.26.048 5 Height-ReTrace 1.17 70 256 256 3.66 300 lattice  <br><br> imaging-14.14.31.069 145 Height -Bi-Directional 2.34 70 256 256 3.66 300 lattice  <br><br> imaging-14.15.34.569 184 Height -Bi-Directional 3.91 70 256 256 3.66 500 lattice  <br><br> imaging-14.16.23.572 57 Height -Bi-Directional 3.91 50 256 256 5.12 500 lattice  <br><br> imaging-14.16.54.040 141 Height -Bi-Directional 7.81 50 128 256 5.12 500 lattice  <br><br> imaging-14.20.38.415 350 Height -Bi-Directional 11.72 40 128 256 6.40 750 lattice  <br><br> imaging-14.21.25.854 723 Height -Bi-Directional 31.25 30 64 128 4.27 1000 lattice  <br><br> imaging-14.23.39.213 201 Height -Bi-Directional 54.69 20 64 128 6.40 1750 lattice  <br><br> imaging-14.23.44.983 2437 Height -Bi-Directional 54.69 20 64 128 6.40 1750 lattice  <br><br> imaging-14.25.58.071 232 Height -Bi-Directional 1.17 85 256 256 3.01 150 lattice  <br><br> imaging-14.29.34.756 96 Height -Bi-Directional 0.59 200 512 512 2.56 150 lattice  <br><br> imaging-14.37.19.845 3 Height-ReTrace 0.38 70 400 400 5.71 150 lattice  <br><br> imaging-14.37.28.689 5 Height-ReTrace 1.00 70 400 400 5.71 400 lattice  <br><br> imaging-14.37.34.764 17 Height-ReTrace 0.50 70 400 400 5.71 200 lattice  <br><br> imaging-14.39.16.156 6 Height-ReTrace 1.56 60 256 256 4.27 400 lattice  <br><br> imaging-14.39.20.305 96 Height -Bi-Directional 3.13 60 256 256 4.27 400 lattice |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: High-Speed Atomic Force Microscopy (HS-AFM)
- **Instrument**: Bruker NanoRacer HS-AFM (amplitude modulation mode, liquid)
- **Probe**: USC-F1.2-k0.15 (NanoWorld), spring constant ~0.15 N·m⁻¹, resonance ~0.6 MHz
- **Sample**: Annexin V (33 kDa) on DOPC:DOPS = 8:2 supported lipid bilayer on mica

## Dataset Contents

37 HS-AFM image sequences (multi-frame video stacks) capturing Annexin V assembly dynamics.
Each sequence is one zip archive with multiple `.jpk` frame files.
Scan sizes range from 20–600 nm; pixel resolutions 64×128 to 512×512; frame rates 0.38–54.69 fps.

## File Format

- **Format**: `.jpk` (JPK/Bruker proprietary binary, used by NanoRacer HS-AFM)
- **NOT supported** by the current pynxtools-spm parser
- An exploratory parser `jpk_parser.py` exists in this directory (from prior investigation)
- Recommended channel: "Height" (feedback signal), NOT "Height Measured" (capacitive)

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/19254504/`  
**Upload date**: 2026-06-25  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 7815 files

**S3 key pattern**: `zenodo/19254504/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `*.jpk` | AFM | 7815 | `zenodo/19254504/For Zenodo/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Parsability Assessment

- **Current parser compatibility**: Not supported (`.jpk` is not in the dispatch table)
- **Path to support**: Would require a new `jpk` parser subclassing `SPMBase`, a new config JSON,
  a new formatter (likely under `nxformatters/bruker/` since NanoRacer is Bruker), and dispatch
  entry in `reader.py` for `(AFM, jpk)`.
- **Complexity**: Medium — `.jpk` is a zip-based format (can open with `zipfile`); metadata is in
  XML/properties files inside the zip; image data is in binary files.
- **Recommendation**: Register as `Unknown Format` until a JPK parser is implemented.

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
