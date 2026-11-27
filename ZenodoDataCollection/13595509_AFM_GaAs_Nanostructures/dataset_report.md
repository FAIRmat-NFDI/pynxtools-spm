# Dataset Report: Zenodo Record 13595509

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Nucleation-Limited Kinetics of GaAs Nanostructures Grown by Selective Area Epitaxy: Implications for Shape Engineering in Optoelectronics Devices |
| **DOI**    | [10.5281/zenodo.13595509](https://doi.org/10.5281/zenodo.13595509) |
| **Url**    | [https://zenodo.org/records/13595509](https://zenodo.org/records/13595509) |
| **Date**   | 2024-08-12 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Zendrini, Michele; Piazza, Valerio; Fontcuberta i Morral, Anna et al. |
| **Tags**   | SAE, MOVPE, GaAs, Nanowires, Growth kinetics |
| **Description** | This dataset corresponds to the following manuscript:  <br><br> Zendrini, M., Dubrovskii, V., Rudra, A., Dede, D., Fontcuberta i Morral, A., Piazza, V. “Nucleation-Limited Kinetics of GaAs Nanostructures Grown by Selective Area Epitaxy: Implications for Shape Engineering in Optoelectronics Devices” ACS Applied Nano Materials 7,16 (2024): 19065–19074 <br><br> DOI: doi.org/10.1021/acsanm.4c02765 (http://doi.org/10.1021/acsanm.4c02765) <br><br> The dataset contains raw SEM images in .tif format for all the arrays of nanowires and nanomembranes discussed in the paper. The dataset also contains the AFM scans in .xyz format for all the arrays of nanowires and nanomembranes. The data for the morphological analysis are extracted from the SEM images and the AFM scans and they are collected in two separate .txt files for NWs and NMs. |
| **Experiment information related files** | `README.txt` |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy, TappingMode) + SEM
- **Instrument**: Bruker AFM (native NanoScope `.spm`)

## Sample (from the linked publication)

Researched 2026-07-08 (the Zenodo record has no sample chemistry). From *Nucleation-Limited
Kinetics of GaAs Nanostructures Grown by Selective Area Epitaxy* (Zendrini et al., ACS Applied
Nano Materials 2024, 7(16), 19065–19074,
[DOI 10.1021/acsanm.4c02765](https://doi.org/10.1021/acsanm.4c02765)):

- **Material / chemical formula**: **GaAs** (gallium arsenide) nanowires and nanomembranes.
- **Substrate**: **GaAs(111)B**, patterned with a dielectric mask (circular holes → vertical
  nanowires; rectangular slits → horizontal nanomembranes).
- **Growth**: selective-area epitaxy by MOVPE; file names encode the growth condition
  (e.g. growth time 45–840 s, or "Annealing").

## Dataset Contents

AFM and SEM datasets of GaAs nanowires (NWs) and nanomembranes (NMs) grown by selective area epitaxy at varying growth times (45–840 s and annealing). 269 objects organised by growth condition and nanostructure type.

## File Format

- **Format**: Bruker `.spm` (AFM) and `.tif` (SEM). **Note:** of the 130 `.spm`-named files,
  only **89 are native Bruker NanoScope**; **37 are Gwyddion files** (`GWYP` header) and **4 are
  ISO/TC 201 exports** — both re-saved with a `.spm` extension and not parseable by pySPM.
- **Parsability**: the 89 native Bruker files are parsed by `BrukerSpmAFM` (TappingMode:
  Height Sensor, Amplitude, Amplitude Error, Phase). SEM `.tif` files not in scope.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/13595509/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 269 files

**S3 key pattern**: `zenodo/13595509/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `AFM_NMs_120s_w140_p1000.0_00010.spm` | AFM | 1 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w140_p1000.0_00010.spm/` | True | True |
| `AFM_NMs_120s_w140_p2000.0_00011.spm` | AFM | 2 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w140_p2000.0_00011.spm/` | False | — |
| `AFM_NMs_120s_w140_p2000_cut_Figure_2.spm` | AFM | 3 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w140_p2000_cut_Figure_2.spm/` | False | — |
| `AFM_NMs_120s_w140_p4000.0_00012.spm` | AFM | 4 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w140_p4000.0_00012.spm/` | True | True |
| `AFM_NMs_120s_w140_p500.0_00009.spm` | AFM | 5 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w140_p500.0_00009.spm/` | True | True |
| `AFM_NMs_120s_w40_p1000.0_00002.spm` | AFM | 6 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w40_p1000.0_00002.spm/` | True | True |
| `AFM_NMs_120s_w40_p2000.0_00003.spm` | AFM | 7 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w40_p2000.0_00003.spm/` | True | True |
| `AFM_NMs_120s_w40_p4000.0_00004.spm` | AFM | 8 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w40_p4000.0_00004.spm/` | True | True |
| `AFM_NMs_120s_w40_p500.0_00001.spm` | AFM | 9 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w40_p500.0_00001.spm/` | True | True |
| `AFM_NMs_120s_w80_p1000.0_00006.spm` | AFM | 10 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w80_p1000.0_00006.spm/` | False | — |
| `AFM_NMs_120s_w80_p2000.0_00007.spm` | AFM | 11 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w80_p2000.0_00007.spm/` | True | True |
| `AFM_NMs_120s_w80_p4000.0_00008.spm` | AFM | 12 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w80_p4000.0_00008.spm/` | True | True |
| `AFM_NMs_120s_w80_p500.0_00005.spm` | AFM | 13 | `zenodo/13595509/AFM_NMs_120s/AFM_NMs_120s_w80_p500.0_00005.spm/` | True | True |
| `AFM_NMs_180s_w140_p1000_L20.0_00012.spm` | AFM | 14 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w140_p1000_L20.0_00012.spm/` | True | True |
| `AFM_NMs_180s_w140_p2000_L20.0_00014.spm` | AFM | 15 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w140_p2000_L20.0_00014.spm/` | True | True |
| `AFM_NMs_180s_w140_p4000_L20.0_00019.spm` | AFM | 16 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w140_p4000_L20.0_00019.spm/` | True | True |
| `AFM_NMs_180s_w140_p500.0_00004_fullArray.spm` | AFM | 17 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w140_p500.0_00004_fullArray.spm/` | True | True |
| `AFM_NMs_180s_w140_p500.0_00005.spm` | AFM | 18 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w140_p500.0_00005.spm/` | True | True |
| `AFM_NMs_180s_w40_p1000_L20.0_00013.spm` | AFM | 19 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w40_p1000_L20.0_00013.spm/` | True | True |
| `AFM_NMs_180s_w40_p2000_L20.0_00015.spm` | AFM | 20 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w40_p2000_L20.0_00015.spm/` | True | True |
| `AFM_NMs_180s_w40_p4000_L20.0_00017.spm` | AFM | 21 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w40_p4000_L20.0_00017.spm/` | True | True |
| `AFM_NMs_180s_w80_p1000.0_00001.spm` | AFM | 22 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w80_p1000.0_00001.spm/` | False | — |
| `AFM_NMs_180s_w80_p2000_L20.0_00016.spm` | AFM | 23 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w80_p2000_L20.0_00016.spm/` | True | True |
| `AFM_NMs_180s_w80_p4000_L20.0_00018.spm` | AFM | 24 | `zenodo/13595509/AFM_NMs_180s/AFM_NMs_180s_w80_p4000_L20.0_00018.spm/` | True | True |
| `AFM_NMs_420s_w140_p1000.0_00010.spm` | AFM | 25 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w140_p1000.0_00010.spm/` | True | True |
| `AFM_NMs_420s_w140_p2000.0_00009.spm` | AFM | 26 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w140_p2000.0_00009.spm/` | True | True |
| `AFM_NMs_420s_w140_p4000.0_00008.spm` | AFM | 27 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w140_p4000.0_00008.spm/` | True | True |
| `AFM_NMs_420s_w140_p500.0_00011.spm` | AFM | 28 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w140_p500.0_00011.spm/` | True | True |
| `AFM_NMs_420s_w40_p1000.0_00002.spm` | AFM | 29 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w40_p1000.0_00002.spm/` | True | True |
| `AFM_NMs_420s_w40_p2000.0_00001.spm` | AFM | 30 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w40_p2000.0_00001.spm/` | True | True |
| `AFM_NMs_420s_w40_p4000.0_00000.spm` | AFM | 31 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w40_p4000.0_00000.spm/` | True | True |
| `AFM_NMs_420s_w40_p500.0_00006.spm` | AFM | 32 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w40_p500.0_00006.spm/` | True | True |
| `AFM_NMs_420s_w80_p1000.0_00005.spm` | AFM | 33 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w80_p1000.0_00005.spm/` | True | True |
| `AFM_NMs_420s_w80_p2000.0_00006.spm` | AFM | 34 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w80_p2000.0_00006.spm/` | True | True |
| `AFM_NMs_420s_w80_p4000.0_00007.spm` | AFM | 35 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w80_p4000.0_00007.spm/` | True | True |
| `AFM_NMs_420s_w80_p500.0_00008.spm` | AFM | 36 | `zenodo/13595509/AFM_NMs_420s/AFM_NMs_420s_w80_p500.0_00008.spm/` | True | True |
| `AFM_NMs_45s_w140_p1000.0_00009.spm` | AFM | 37 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w140_p1000.0_00009.spm/` | True | True |
| `AFM_NMs_45s_w140_p2000.0_00010.spm` | AFM | 38 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w140_p2000.0_00010.spm/` | True | True |
| `AFM_NMs_45s_w140_p4000.0_00011.spm` | AFM | 39 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w140_p4000.0_00011.spm/` | True | True |
| `AFM_NMs_45s_w140_p500.0_00000.spm` | AFM | 40 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w140_p500.0_00000.spm/` | True | True |
| `AFM_NMs_45s_w40_p1000.0_00001.spm` | AFM | 41 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w40_p1000.0_00001.spm/` | True | True |
| `AFM_NMs_45s_w40_p2000.0_00002.spm` | AFM | 42 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w40_p2000.0_00002.spm/` | True | True |
| `AFM_NMs_45s_w40_p4000.0_00003.spm` | AFM | 43 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w40_p4000.0_00003.spm/` | True | True |
| `AFM_NMs_45s_w40_p500.0_00000.spm` | AFM | 44 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w40_p500.0_00000.spm/` | True | True |
| `AFM_NMs_45s_w80_p1000.0_00005.spm` | AFM | 45 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w80_p1000.0_00005.spm/` | True | True |
| `AFM_NMs_45s_w80_p2000.0_00006.spm` | AFM | 46 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w80_p2000.0_00006.spm/` | True | True |
| `AFM_NMs_45s_w80_p4000.0_00007.spm` | AFM | 47 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w80_p4000.0_00007.spm/` | True | True |
| `AFM_NMs_45s_w80_p500.0_00004.spm` | AFM | 48 | `zenodo/13595509/AFM_NMs_45s/AFM_NMs_45s_w80_p500.0_00004.spm/` | True | True |
| `AFM_NMs_60s_w140_p1000.0_00010.spm` | AFM | 49 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w140_p1000.0_00010.spm/` | True | True |
| `AFM_NMs_60s_w140_p2000.0_00011.spm` | AFM | 50 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w140_p2000.0_00011.spm/` | True | True |
| `AFM_NMs_60s_w140_p2000_cut_rotated.spm` | AFM | 51 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w140_p2000_cut_rotated.spm/` | False | — |
| `AFM_NMs_60s_w140_p4000.0_00012.spm` | AFM | 52 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w140_p4000.0_00012.spm/` | True | True |
| `AFM_NMs_60s_w140_p500_new.0_00000.spm` | AFM | 53 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w140_p500_new.0_00000.spm/` | True | True |
| `AFM_NMs_60s_w40_p1000.0_00001.spm` | AFM | 54 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w40_p1000.0_00001.spm/` | True | True |
| `AFM_NMs_60s_w40_p2000.0_00002.spm` | AFM | 55 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w40_p2000.0_00002.spm/` | True | True |
| `AFM_NMs_60s_w40_p4000.0_00003.spm` | AFM | 56 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w40_p4000.0_00003.spm/` | True | True |
| `AFM_NMs_60s_w40_p500.0_00000.spm` | AFM | 57 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w40_p500.0_00000.spm/` | True | True |
| `AFM_NMs_60s_w80_p1000.0_00005.spm` | AFM | 58 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w80_p1000.0_00005.spm/` | True | True |
| `AFM_NMs_60s_w80_p2000.0_00007.spm` | AFM | 59 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w80_p2000.0_00007.spm/` | True | True |
| `AFM_NMs_60s_w80_p4000.0_00008.spm` | AFM | 60 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w80_p4000.0_00008.spm/` | True | True |
| `AFM_NMs_60s_w80_p500.0_00004.spm` | AFM | 61 | `zenodo/13595509/AFM_NMs_60s/AFM_NMs_60s_w80_p500.0_00004.spm/` | True | True |
| `AFM_NMs_840s_w140_p1000.0_00019.spm` | AFM | 62 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w140_p1000.0_00019.spm/` | True | True |
| `AFM_NMs_840s_w140_p2000.0_00020.spm` | AFM | 63 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w140_p2000.0_00020.spm/` | True | True |
| `AFM_NMs_840s_w140_p4000.spm` | AFM | 64 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w140_p4000.spm/` | True | True |
| `AFM_NMs_840s_w140_p500.0_00009.spm` | AFM | 65 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w140_p500.0_00009.spm/` | True | True |
| `AFM_NMs_840s_w40_p1000.0_00002.spm` | AFM | 66 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w40_p1000.0_00002.spm/` | True | True |
| `AFM_NMs_840s_w40_p2000.0_00016.spm` | AFM | 67 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w40_p2000.0_00016.spm/` | True | True |
| `AFM_NMs_840s_w40_p4000.0_00004.spm` | AFM | 68 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w40_p4000.0_00004.spm/` | True | True |
| `AFM_NMs_840s_w40_p500.spm` | AFM | 69 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w40_p500.spm/` | True | True |
| `AFM_NMs_840s_w80_p1000.0_00017.spm` | AFM | 70 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w80_p1000.0_00017.spm/` | True | True |
| `AFM_NMs_840s_w80_p2000.0_00018.spm` | AFM | 71 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w80_p2000.0_00018.spm/` | True | True |
| `AFM_NMs_840s_w80_p4000.spm` | AFM | 72 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w80_p4000.spm/` | True | True |
| `AFM_NMs_840s_w80_p500.spm` | AFM | 73 | `zenodo/13595509/AFM_NMs_840s/AFM_NMs_840s_w80_p500.spm/` | True | True |
| `AFM_NMs_90s_w140_p1000.0_00002.spm` | AFM | 74 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w140_p1000.0_00002.spm/` | True | True |
| `AFM_NMs_90s_w140_p2000.spm` | AFM | 75 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w140_p2000.spm/` | False | — |
| `AFM_NMs_90s_w140_p2000_cut_rotated.spm` | AFM | 76 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w140_p2000_cut_rotated.spm/` | False | — |
| `AFM_NMs_90s_w140_p4000.0_00000.spm` | AFM | 77 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w140_p4000.0_00000.spm/` | True | True |
| `AFM_NMs_90s_w140_p500.0_00003.spm` | AFM | 78 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w140_p500.0_00003.spm/` | True | True |
| `AFM_NMs_90s_w40_p1000.0_00011.spm` | AFM | 79 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w40_p1000.0_00011.spm/` | True | True |
| `AFM_NMs_90s_w40_p2000.0_00010.spm` | AFM | 80 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w40_p2000.0_00010.spm/` | True | True |
| `AFM_NMs_90s_w40_p4000.0_00009.spm` | AFM | 81 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w40_p4000.0_00009.spm/` | True | True |
| `AFM_NMs_90s_w40_p500.spm` | AFM | 82 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w40_p500.spm/` | False | — |
| `AFM_NMs_90s_w80_p1000.0_00006.spm` | AFM | 83 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w80_p1000.0_00006.spm/` | False | — |
| `AFM_NMs_90s_w80_p2000.spm` | AFM | 84 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w80_p2000.spm/` | False | — |
| `AFM_NMs_90s_w80_p4000.spm` | AFM | 85 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w80_p4000.spm/` | False | — |
| `AFM_NMs_90s_w80_p500.0_00007.spm` | AFM | 86 | `zenodo/13595509/AFM_NMs_90s/AFM_NMs_90s_w80_p500.0_00007.spm/` | True | True |
| `AFM_NMs_Annealing_w140_p1000_6um_600mHz_256lines.0_00015.spm` | AFM | 87 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w140_p1000_6um_600mHz_256lines.0_00015.spm/` | True | True |
| `AFM_NMs_Annealing_w140_p2000_L20.0_00008.spm` | AFM | 88 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w140_p2000_L20.0_00008.spm/` | True | True |
| `AFM_NMs_Annealing_w140_p4000_L20.0_00010.spm` | AFM | 89 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w140_p4000_L20.0_00010.spm/` | True | True |
| `AFM_NMs_Annealing_w140_p500.0_00003.spm` | AFM | 90 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w140_p500.0_00003.spm/` | True | True |
| `AFM_NMs_Annealing_w40_p1000_5um.spm` | AFM | 91 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w40_p1000_5um.spm/` | True | True |
| `AFM_NMs_Annealing_w40_p2000_L20.0_00006.spm` | AFM | 92 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w40_p2000_L20.0_00006.spm/` | True | True |
| `AFM_NMs_Annealing_w40_p4000_L20.0_00009.spm` | AFM | 93 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w40_p4000_L20.0_00009.spm/` | True | True |
| `AFM_NMs_Annealing_w40_p500_L20.0_00003.spm` | AFM | 94 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w40_p500_L20.0_00003.spm/` | True | True |
| `AFM_NMs_Annealing_w80_p1000_6um_600mHz_256lines.0_00013.spm` | AFM | 95 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w80_p1000_6um_600mHz_256lines.0_00013.spm/` | True | True |
| `AFM_NMs_Annealing_w80_p2000_L20.0_00007.spm` | AFM | 96 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w80_p2000_L20.0_00007.spm/` | True | True |
| `AFM_NMs_Annealing_w80_p4000.0_00000.spm` | AFM | 97 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w80_p4000.0_00000.spm/` | True | True |
| `AFM_NMs_Annealing_w80_p500_L20.0_00005.spm` | AFM | 98 | `zenodo/13595509/AFM_NMs_Annealing/AFM_NMs_Annealing_w80_p500_L20.0_00005.spm/` | True | True |
| `AFM_NWs_Annealing_d112.0_00008.spm` | AFM | 99 | `zenodo/13595509/AFM_NWs_6913_Annealing/AFM_NWs_Annealing_d112.0_00008.spm/` | False | — |
| `AFM_NWs_Annealing_d138.0_00009.spm` | AFM | 100 | `zenodo/13595509/AFM_NWs_6913_Annealing/AFM_NWs_Annealing_d138.0_00009.spm/` | False | — |
| `AFM_NWs_Annealing_d160.0_00010.spm` | AFM | 101 | `zenodo/13595509/AFM_NWs_6913_Annealing/AFM_NWs_Annealing_d160.0_00010.spm/` | False | — |
| `AFM_NWs_Annealing_d80_or_112.0_00006.spm` | AFM | 102 | `zenodo/13595509/AFM_NWs_6913_Annealing/AFM_NWs_Annealing_d80_or_112.0_00006.spm/` | True | True |
| `AFM_NWs_180s_d112.0_00030.spm` | AFM | 103 | `zenodo/13595509/AFM_NWs_6914_180s/AFM_NWs_180s_d112.0_00030.spm/` | False | — |
| `AFM_NWs_180s_d138.0_00031.spm` | AFM | 104 | `zenodo/13595509/AFM_NWs_6914_180s/AFM_NWs_180s_d138.0_00031.spm/` | False | — |
| `AFM_NWs_180s_d160.0_00032.spm` | AFM | 105 | `zenodo/13595509/AFM_NWs_6914_180s/AFM_NWs_180s_d160.0_00032.spm/` | False | — |
| `AFM_NWs_180s_d80.0_00029.spm` | AFM | 106 | `zenodo/13595509/AFM_NWs_6914_180s/AFM_NWs_180s_d80.0_00029.spm/` | False | — |
| `AFM_NWs_420s_d112.0_00034.spm` | AFM | 107 | `zenodo/13595509/AFM_NWs_6929_420s/AFM_NWs_420s_d112.0_00034.spm/` | False | — |
| `AFM_NWs_420s_d138.0_00035.spm` | AFM | 108 | `zenodo/13595509/AFM_NWs_6929_420s/AFM_NWs_420s_d138.0_00035.spm/` | False | — |
| `AFM_NWs_420s_d160.0_00036.spm` | AFM | 109 | `zenodo/13595509/AFM_NWs_6929_420s/AFM_NWs_420s_d160.0_00036.spm/` | False | — |
| `AFM_NWs_420s_d80.0_00033.spm` | AFM | 110 | `zenodo/13595509/AFM_NWs_6929_420s/AFM_NWs_420s_d80.0_00033.spm/` | False | — |
| `AFM_NWs_45s_d112.0_00013.spm` | AFM | 111 | `zenodo/13595509/AFM_NWs_6930_45s/AFM_NWs_45s_d112.0_00013.spm/` | False | — |
| `AFM_NWs_45s_d138.0_00014.spm` | AFM | 112 | `zenodo/13595509/AFM_NWs_6930_45s/AFM_NWs_45s_d138.0_00014.spm/` | False | — |
| `AFM_NWs_45s_d160.0_00015.spm` | AFM | 113 | `zenodo/13595509/AFM_NWs_6930_45s/AFM_NWs_45s_d160.0_00015.spm/` | False | — |
| `AFM_NWs_45s_d80.0_00012.spm` | AFM | 114 | `zenodo/13595509/AFM_NWs_6930_45s/AFM_NWs_45s_d80.0_00012.spm/` | False | — |
| `AFM_NWs_840s_d112.0_00039.spm` | AFM | 115 | `zenodo/13595509/AFM_NWs_6953_840s/AFM_NWs_840s_d112.0_00039.spm/` | False | — |
| `AFM_NWs_840s_d138.0_00038.spm` | AFM | 116 | `zenodo/13595509/AFM_NWs_6953_840s/AFM_NWs_840s_d138.0_00038.spm/` | False | — |
| `AFM_NWs_840s_d160.0_00040.spm` | AFM | 117 | `zenodo/13595509/AFM_NWs_6953_840s/AFM_NWs_840s_d160.0_00040.spm/` | False | — |
| `AFM_NWs_840s_d80.0_00037.spm` | AFM | 118 | `zenodo/13595509/AFM_NWs_6953_840s/AFM_NWs_840s_d80.0_00037.spm/` | False | — |
| `AFM_NWs_60s_d112.0_00018.spm` | AFM | 119 | `zenodo/13595509/AFM_NWs_6978_60s/AFM_NWs_60s_d112.0_00018.spm/` | True | True |
| `AFM_NWs_60s_d138.0_00019.spm` | AFM | 120 | `zenodo/13595509/AFM_NWs_6978_60s/AFM_NWs_60s_d138.0_00019.spm/` | False | — |
| `AFM_NWs_60s_d160.0_00020.spm` | AFM | 121 | `zenodo/13595509/AFM_NWs_6978_60s/AFM_NWs_60s_d160.0_00020.spm/` | False | — |
| `AFM_NWs_60s_d80.0_00016.spm` | AFM | 122 | `zenodo/13595509/AFM_NWs_6978_60s/AFM_NWs_60s_d80.0_00016.spm/` | False | — |
| `AFM_NWs_90s_d112.0_00022.spm` | AFM | 123 | `zenodo/13595509/AFM_NWs_6979_90s/AFM_NWs_90s_d112.0_00022.spm/` | False | — |
| `AFM_NWs_90s_d138.0_00023.spm` | AFM | 124 | `zenodo/13595509/AFM_NWs_6979_90s/AFM_NWs_90s_d138.0_00023.spm/` | False | — |
| `AFM_NWs_90s_d160.0_00024.spm` | AFM | 125 | `zenodo/13595509/AFM_NWs_6979_90s/AFM_NWs_90s_d160.0_00024.spm/` | False | — |
| `AFM_NWs_90s_d80.0_00021.spm` | AFM | 126 | `zenodo/13595509/AFM_NWs_6979_90s/AFM_NWs_90s_d80.0_00021.spm/` | False | — |
| `AFM_NWs_120s_d112.0_00026.spm` | AFM | 127 | `zenodo/13595509/AFM_NWs_6980_120s/AFM_NWs_120s_d112.0_00026.spm/` | False | — |
| `AFM_NWs_120s_d138.0_00027.spm` | AFM | 128 | `zenodo/13595509/AFM_NWs_6980_120s/AFM_NWs_120s_d138.0_00027.spm/` | False | — |
| `AFM_NWs_120s_d160.0_00028.spm` | AFM | 129 | `zenodo/13595509/AFM_NWs_6980_120s/AFM_NWs_120s_d160.0_00028.spm/` | False | — |
| `AFM_NWs_120s_d80.0_00025.spm` | AFM | 130 | `zenodo/13595509/AFM_NWs_6980_120s/AFM_NWs_120s_d80.0_00025.spm/` | False | — |
| `*.txt` | AFM | 1 | `zenodo/13595509/240812_NMs_data_Final.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/13595509/240812_NWs_data_Final.txt/` | — | — |
| `*.db` | AFM | 1 | `zenodo/13595509/AFM_NMs_120s/` | — | — |
| `*.db` | AFM | 1 | `zenodo/13595509/AFM_NMs_420s/` | — | — |
| `*.db` | AFM | 1 | `zenodo/13595509/AFM_NMs_60s/` | — | — |
| `*.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_120s/` | — | — |
| `*.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_180s/` | — | — |
| `*.db` | SEM | 1 | `zenodo/13595509/SEM_NMs_420s/` | — | — |
| `*.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_420s/` | — | — |
| `*.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_45s/` | — | — |
| `*.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_60s/` | — | — |
| `*.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_840s/` | — | — |
| `*.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_90s/` | — | — |
| `*.tif` | SEM | 12 | `zenodo/13595509/SEM_NMs_Annealing/` | — | — |
| `*.tif` | SEM | 4 | `zenodo/13595509/SEM_NWs_120s/` | — | — |
| `*.tif` | SEM | 4 | `zenodo/13595509/SEM_NWs_180s/` | — | — |
| `*.tif` | SEM | 8 | `zenodo/13595509/SEM_NWs_420s/` | — | — |
| `*.tif` | SEM | 4 | `zenodo/13595509/SEM_NWs_45s/` | — | — |
| `*.tif` | SEM | 4 | `zenodo/13595509/SEM_NWs_60s/` | — | — |
| `*.tif` | SEM | 8 | `zenodo/13595509/SEM_NWs_840s/` | — | — |
| `*.tif` | SEM | 4 | `zenodo/13595509/SEM_NWs_90s/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|
| `README.txt` | AFM | 1 | `zenodo/13595509/README.txt/` |

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08 with `pynxtools-spm` 0.2.5 / `pySPM` 0.6.3. License **`cc-by-4.0`** passes
the open-license gate. **89 of the 130 `.spm` files converted, validated, and uploaded
(`PS = True`, `Uploaded = True`)**; the other **41 are skipped (`PS = False`)** — 37 Gwyddion
(`GWYP`) files and 4 ISO/TC 201 exports, both mislabeled `.spm` and unparseable by pySPM (they
hang its Bruker reader; a per-file convert timeout guards the batch). TappingMode data — the
default config maps the channels, so only scientific NXdata titles were applied. Default plot =
`z_forward` (Topography). Post-audit of all 89 `.nxs`: **0 long units, 0 shape mismatches, 0 bad
defaults**; S3 spot-check confirms short units (`Hz, nm, °`) and the full-description
`citeID.description`. See `conversion.log`.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 89/130 `.spm` converted (`PS = True`); 41 (Gwyddion + ISO/TC 201)
      unsupported (`PS = False`)
- [x] Reference .nxs files generated and uploaded for all 89 converted files
