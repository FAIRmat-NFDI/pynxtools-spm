# Dataset Report: Zenodo Record 14196316

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for "An Alternative Chlorine-Assisted Optimization of CdS/Sb2Se3 Solar Cells: Towards Understanding of Chlorine Incorporation Mechanism" |
| **DOI**    | [10.5281/zenodo.14196316](https://doi.org/10.5281/zenodo.14196316) |
| **Url**    | [https://zenodo.org/records/14196316](https://zenodo.org/records/14196316) |
| **Date**   | 2024-11-21 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Kuliček, Jaroslav; Bouzek, Karel; Paušová, Šárka |
| **Tags**   | VZ3, CVUT, 214 021, 214 023, Kelvin probe, CdS/Sb2Se3, solar cells, SEM, chlorine doping |
| **Description** | The current strategies in the development of Sb2Se3 thin film solar cells involve fabrication and optimization of superstrate and substrate device architectures, with the preferable choice for TiO2 and CdS heterojunction layers. For CdS-based superstrate cells, several studies reported the necessity to apply CdCl2 or other metal halide-based post-deposition treatment (PDT), highlighting improvement of CdS/Sb2Se3 device efficiency. However, the need, effect, and mechanism of such PDT are very often not described. Additionally, the fact that many groups have not succeeded in demonstrating its benefits suggests that this strategy is not straightforward, requiring a deeper understanding towards a more unified concept. The present study proposes an alternative approach to the challenging CdCl2 PDT of CdS in CdS/Sb2Se3 device, involving controllable Cl incorporation in CdS films by systematically varying the concentration of NH4Cl in the CBD precursor solution from 1 to 8 mM. Structural and electrical characterizations are correlated with advanced measurements of Scanning Kelvin Probe, surface photovoltage, and atomic force microscopy to understand the impact of Cl incorporation on the properties of CdS films and CdS/Sb2Se3 devices. The validity of Cl incorporation in the CdS lattice and interdiffusion processes at the CdS-Sb2Se3 interface is confirmed by secondary ion mass spectrometry analysis. It is demonstrated that incorporation of 1 mM of NH4Cl, as a Cl source in CBD CdS, can boost the PCE of CdS/Sb2Se3 by ~20 %. With this approach, we offer new perspectives on the optimization methodology for Cl-based CdS/Sb2Se3 device processing and complementary understanding of the physiochemistry behind these processes. |
| **Experiment information related files** | `ReadMe_v2.txt` |

## Technique

- **Primary SPM technique**: AFM + Scanning Kelvin Probe + Surface Photovoltage
- **Instrument**: Unknown AFM vendor (`.Dat` files — Scanning Kelvin Probe data format)

## Dataset Contents

40 files (`.Dat`, `.txt`, `.jpg`) related to CdS/Sb₂Se₃ solar cell characterisation. Dat files contain Scanning Kelvin Probe and AFM measurements at different Cl⁻ concentrations.

## File Format

- **Format**: `.Dat` (Scanning Kelvin Probe format — unknown vendor), `.txt`, `.jpg`
- **Parsability**: Not directly supported. `.Dat` files may contain Kelvin probe or AFM data but the vendor format is unrecognised by the current parser.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14196316/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 40 files

**S3 key pattern**: `zenodo/14196316/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `VZ3_010_021_CVUT_D_0002_v1.Dat` | AFM | 1 | `zenodo/14196316/VZ3_010_021_CVUT_D_0002_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0003_v1.Dat` | AFM | 2 | `zenodo/14196316/VZ3_010_021_CVUT_D_0003_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0004_v1.Dat` | AFM | 3 | `zenodo/14196316/VZ3_010_021_CVUT_D_0004_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0005_v1.Dat` | AFM | 4 | `zenodo/14196316/VZ3_010_021_CVUT_D_0005_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0006_v1.Dat` | AFM | 5 | `zenodo/14196316/VZ3_010_021_CVUT_D_0006_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0007_v1.Dat` | AFM | 6 | `zenodo/14196316/VZ3_010_021_CVUT_D_0007_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0008_v1.Dat` | AFM | 7 | `zenodo/14196316/VZ3_010_021_CVUT_D_0008_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0009_v1.Dat` | AFM | 8 | `zenodo/14196316/VZ3_010_021_CVUT_D_0009_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0010_v1.Dat` | AFM | 9 | `zenodo/14196316/VZ3_010_021_CVUT_D_0010_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0011_v1.Dat` | AFM | 10 | `zenodo/14196316/VZ3_010_021_CVUT_D_0011_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0014_v1.Dat` | AFM | 11 | `zenodo/14196316/VZ3_010_021_CVUT_D_0014_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0015_v1.Dat` | AFM | 12 | `zenodo/14196316/VZ3_010_021_CVUT_D_0015_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0016_v1.Dat` | AFM | 13 | `zenodo/14196316/VZ3_010_021_CVUT_D_0016_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0017_v1.Dat` | AFM | 14 | `zenodo/14196316/VZ3_010_021_CVUT_D_0017_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0018_v1.Dat` | AFM | 15 | `zenodo/14196316/VZ3_010_021_CVUT_D_0018_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0020_v1.Dat` | AFM | 16 | `zenodo/14196316/VZ3_010_021_CVUT_D_0020_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0021_v1.Dat` | AFM | 17 | `zenodo/14196316/VZ3_010_021_CVUT_D_0021_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0022_v1.Dat` | AFM | 18 | `zenodo/14196316/VZ3_010_021_CVUT_D_0022_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0023_v1.Dat` | AFM | 19 | `zenodo/14196316/VZ3_010_021_CVUT_D_0023_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0024_v1.Dat` | AFM | 20 | `zenodo/14196316/VZ3_010_021_CVUT_D_0024_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0025_v1.Dat` | AFM | 21 | `zenodo/14196316/VZ3_010_021_CVUT_D_0025_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0026_v1.Dat` | AFM | 22 | `zenodo/14196316/VZ3_010_021_CVUT_D_0026_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0027_v1.Dat` | AFM | 23 | `zenodo/14196316/VZ3_010_021_CVUT_D_0027_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0028_v1.Dat` | AFM | 24 | `zenodo/14196316/VZ3_010_021_CVUT_D_0028_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0029_v1.Dat` | AFM | 25 | `zenodo/14196316/VZ3_010_021_CVUT_D_0029_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0030_v1.Dat` | AFM | 26 | `zenodo/14196316/VZ3_010_021_CVUT_D_0030_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0031_v1.Dat` | AFM | 27 | `zenodo/14196316/VZ3_010_021_CVUT_D_0031_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0032_v1.Dat` | AFM | 28 | `zenodo/14196316/VZ3_010_021_CVUT_D_0032_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0033_v1.Dat` | AFM | 29 | `zenodo/14196316/VZ3_010_021_CVUT_D_0033_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0034_v1.Dat` | AFM | 30 | `zenodo/14196316/VZ3_010_021_CVUT_D_0034_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0035_v1.Dat` | AFM | 31 | `zenodo/14196316/VZ3_010_021_CVUT_D_0035_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0036_v1.Dat` | AFM | 32 | `zenodo/14196316/VZ3_010_021_CVUT_D_0036_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0037_v1.Dat` | AFM | 33 | `zenodo/14196316/VZ3_010_021_CVUT_D_0037_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0038_v1.Dat` | AFM | 34 | `zenodo/14196316/VZ3_010_021_CVUT_D_0038_v1.Dat/` | — | — |
| `VZ3_010_021_CVUT_D_0039_v1.Dat` | AFM | 35 | `zenodo/14196316/VZ3_010_021_CVUT_D_0039_v1.Dat/` | — | — |
| `*.jpg` | AFM | 1 | `zenodo/14196316/VZ3_010_021_CVUT_D_0001_v1.jpg/` | — | — |
| `*.jpg` | AFM | 1 | `zenodo/14196316/VZ3_010_021_CVUT_D_0012_v1.jpg/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/14196316/VZ3_010_021_CVUT_D_0013_v1.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/14196316/VZ3_010_021_CVUT_D_0019_v1.txt/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `ReadMe_v2.txt` | AFM | 1 | `zenodo/14196316/ReadMe_v2.txt/` |

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
