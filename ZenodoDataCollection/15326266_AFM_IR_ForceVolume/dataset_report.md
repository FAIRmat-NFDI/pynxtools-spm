# Dataset Report: Zenodo Record 15326266

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Force Volume Atomic Force Microscopy-Infrared for Simultaneous Nanoscale Chemical and Mechanical Spectromicroscopy |
| **DOI**    | [10.5281/zenodo.15326266](https://doi.org/10.5281/zenodo.15326266) |
| **Url**    | [https://zenodo.org/records/15326266](https://zenodo.org/records/15326266) |
| **Date**   | 2025-05-05 |
| **Access** | Open |
| **License**| cc-by-nc-nd-4.0 |
| **Authors**| Wagner, Martin; Hu, Qichi; Hu, Shuiqing et al. |
| **Tags**   | AFM-IR, photothermal, infrared nanospectroscopy, force volume, nanomechanical, contact resonance, Q-factor, damping, infrared spectroscopy, atomic force microscopy |
| **Description** | The uploaded data is used in the following publication and its Supporting Information: <br><br> Force Volume Atomic Force Microscopy-Infrared for Simultaneous Nanoscale Chemical and Mechanical Spectromicroscopy <br><br> ACS Nano 2025, 19, 19, 18791–18803 <br><br> https://doi.org/10.1021/acsnano.5c04015 (https://doi.org/10.1021/acsnano.5c04015) <br><br>   <br><br> ABSTRACT OF THE PUBLICATION: <br><br> Photothermal atomic force microscopy-infrared (AFM-IR) combines the nanoscale spatial resolution of AFM with the chemical identification capability of infrared spectroscopy and has thrived in various applications. Currently executed in three major AFM modes (contact, tapping and peak force tapping) we introduce a fourth variant built upon force volume mode comprising a defined engage, hold and retract segment in each pixel. IR laser pulsing at a probe resonance frequency during the constant-force hold segment duplicates the resonance enhanced AFM-IR detection principle of contact mode. However, force volume AFM-IR removes the lateral forces that cause tip wear and sample damage while adding the spatial resolution of tapping AFM-IR. As demonstrated on different materials this imaging and spectroscopy technique integrates monolayer sensitivity, sub-10 nm spatial chemical resolution, simultaneous nanomechanical property sensing and precise force control. The ability to sweep the infrared laser repetition rate in each pixel provides additional, rich information in the form of contact resonance curves, while compensating for mechanically induced probe resonance shifts in an alternative to conventional phase-locked loop based frequency tracking. Such sweeps inherently consider the Q-factor (i.e. mechanical damping) in the AFM-IR response, a little investigated aspect. Furthermore, the probing depth can be varied by selecting different resonances recorded within a single broad frequency sweep. Switching to the surface sensitive AFM-IR detection scheme during the hold segment additionally limits the probing depth. These qualities should position force volume AFM-IR as a valuable addition to established AFM-IR modes. <br><br>   <br><br> DESCRIPTION OF UPLOADED DATA: <br><br> File names start with ‘Fig…’ followed by a short description and refer to the specific figure in the publication and its Supporting Information where the data is discussed. The following SI figures are based on the same data sets as other figures: <br><br> Fig. S6: see spectra of Fig. 3 <br><br> Fig. S7: same data as Fig. 4 <br><br> Fig. S8: same data as Fig. 5 <br><br> Fig. S10: same data as Fig. 5 <br><br> Fig. S11: same data as Fig. 6. <br><br> Data sets comprise atomic force microscopy (AFM) imaging files (*.spm, mostly containing force volume data), spectra (*.txt) or curves (*.txt) discussed in the publication. Txt-files contain ASCII data in tab delimited format. <br><br> The atomic force microscopy (AFM) imaging files (*.spm) can be opened and processed in Bruker NanoScope Analysis V3.00R1sr7. Earlier Nanoscope Analysis versions as well as other AFM imaging software may be used as well but full compatibility is not guaranteed. |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: AFM-IR (Force Volume mode) — combined AFM and infrared spectroscopy
- **Instrument**: Bruker NanoScope (`.spm` force volume files)

## Dataset Contents

44 files for an AFM-IR force-volume study on polymer thin films (PS-b-PMMA, PS-LDPE, purple membrane). Includes Bruker `.spm` force volume files (up to 1.6 GB each) and `.txt` spectral data, organised by figure.

## File Format

- **Format**: Bruker `.spm` (force volume AFM-IR), `.txt` (spectra), `.PNG`
- **Parsability**: Parsable by `BrukerSpmAFM` for standard channels. Force-volume specific channels may require extended support.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/15326266/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 44 files

**S3 key pattern**: `zenodo/15326266/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `Fig1 dPS-b-PMMA 98Hz 140nm 1730cm 5ms sweep 1660-1720kHz PMMA zeroscan.0_00024.spm` | AFM | 1 | `zenodo/15326266/Fig1 dPS-b-PMMA 98Hz 140nm 1730cm 5ms sweep 1660-1720kHz PMMA zeroscan.0_00024.spm/` | — | — |
| `Fig1 dPS-b-PMMA 98Hz 140nm 1730cm.0_00030.spm` | AFM | 2 | `zenodo/15326266/Fig1 dPS-b-PMMA 98Hz 140nm 1730cm.0_00030.spm/` | — | — |
| `Fig2 PS-b-PMMA 80nm 156Hz 5ms 1492cm - flipped horizontally.0_00097.spm` | AFM | 3 | `zenodo/15326266/Fig2 PS-b-PMMA 80nm 156Hz 5ms 1492cm - flipped horizontally.0_00097.spm/` | — | — |
| `Fig2 PS-b-PMMA 80nm 156Hz 5ms 1730cm - flipped horizontally.0_00096.spm` | AFM | 4 | `zenodo/15326266/Fig2 PS-b-PMMA 80nm 156Hz 5ms 1730cm - flipped horizontally.0_00096.spm/` | — | — |
| `Fig3 purple mem 1660cm 195Hz 100nm - flipped horizontally.0_00026.spm` | AFM | 5 | `zenodo/15326266/Fig3 purple mem 1660cm 195Hz 100nm - flipped horizontally.0_00026.spm/` | — | — |
| `Fig4 PS-LDPE 98Hz 40nm 1472cm - flipped horizontally.0_00015.spm` | AFM | 6 | `zenodo/15326266/Fig4 PS-LDPE 98Hz 40nm 1472cm - flipped horizontally.0_00015.spm/` | — | — |
| `Fig4 PS-LDPE 98Hz 40nm 1493cm - flipped horizontally.0_00014.spm` | AFM | 7 | `zenodo/15326266/Fig4 PS-LDPE 98Hz 40nm 1493cm - flipped horizontally.0_00014.spm/` | — | — |
| `Fig4 PS-LDPE 98Hz 40nm 1493cm Quantitative mod, radius=3.1nm k=25Nm poisson=0.34 angle=18deg 50nmV - flipped horizontally.0_00014.spm` | AFM | 8 | `zenodo/15326266/Fig4 PS-LDPE 98Hz 40nm 1493cm Quantitative mod, radius=3.1nm k=25Nm poisson=0.34 angle=18deg 50nmV - flipped horizontally.0_00014.spm/` | — | — |
| `Fig5 dPS-b-PMMA 98Hz 120nm 1730cm-1 25ms sweep 1720-1780kHz.0_00029.spm` | AFM | 9 | `zenodo/15326266/Fig5 dPS-b-PMMA 98Hz 120nm 1730cm-1 25ms sweep 1720-1780kHz.0_00029.spm/` | — | — |
| `Fig6 1066kHz 1720cm.0_00022.spm` | AFM | 10 | `zenodo/15326266/Fig6 1066kHz 1720cm.0_00022.spm/` | — | — |
| `Fig6 1483kHz 1720cm.0_00023.spm` | AFM | 11 | `zenodo/15326266/Fig6 1483kHz 1720cm.0_00023.spm/` | — | — |
| `Fig6 1965kHz 1720cm.0_00022.spm` | AFM | 12 | `zenodo/15326266/Fig6 1965kHz 1720cm.0_00022.spm/` | — | — |
| `Fig6 470kHz 1720cm.0_00022.spm` | AFM | 13 | `zenodo/15326266/Fig6 470kHz 1720cm.0_00022.spm/` | — | — |
| `Fig6 729kHz 1720cm.0_00022.spm` | AFM | 14 | `zenodo/15326266/Fig6 729kHz 1720cm.0_00022.spm/` | — | — |
| `Fig6 sweep 1s 100-2100kHz 1720cm.0_00019.spm` | AFM | 15 | `zenodo/15326266/Fig6 sweep 1s 100-2100kHz 1720cm.0_00019.spm/` | — | — |
| `FigS1 CM - 1x1um.0_00004.spm` | AFM | 16 | `zenodo/15326266/FigS1 CM - 1x1um.0_00004.spm/` | — | — |
| `FigS1 FV - 1x1um.0_00000.spm` | AFM | 17 | `zenodo/15326266/FigS1 FV - 1x1um.0_00000.spm/` | — | — |
| `FigS1 FV - 1x1um.0_00029.spm` | AFM | 18 | `zenodo/15326266/FigS1 FV - 1x1um.0_00029.spm/` | — | — |
| `FigS2 CM dPS-b-PMMA 0.5Hz.0_00026.spm` | AFM | 19 | `zenodo/15326266/FigS2 CM dPS-b-PMMA 0.5Hz.0_00026.spm/` | — | — |
| `FigS2 CM dPS-b-PMMA 0.5Hz.0_00027.spm` | AFM | 20 | `zenodo/15326266/FigS2 CM dPS-b-PMMA 0.5Hz.0_00027.spm/` | — | — |
| `FigS2 REFV dPS-b-PMMA 140nm 98Hz 5ms.0_00009.spm` | AFM | 21 | `zenodo/15326266/FigS2 REFV dPS-b-PMMA 140nm 98Hz 5ms.0_00009.spm/` | — | — |
| `FigS2 REFV dPS-b-PMMA 140nm 98Hz 5ms.0_00020.spm` | AFM | 22 | `zenodo/15326266/FigS2 REFV dPS-b-PMMA 140nm 98Hz 5ms.0_00020.spm/` | — | — |
| `FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 100ms sweep 1650-1710kHz.0_00047.spm` | AFM | 23 | `zenodo/15326266/FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 100ms sweep 1650-1710kHz.0_00047.spm/` | — | — |
| `FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 10ms sweep 1650-1710kHz.0_00045.spm` | AFM | 24 | `zenodo/15326266/FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 10ms sweep 1650-1710kHz.0_00045.spm/` | — | — |
| `FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 25ms sweep 1650-1710kHz.0_00046.spm` | AFM | 25 | `zenodo/15326266/FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 25ms sweep 1650-1710kHz.0_00046.spm/` | — | — |
| `FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 2ms sweep 1650-1710kHz.0_00043.spm` | AFM | 26 | `zenodo/15326266/FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 2ms sweep 1650-1710kHz.0_00043.spm/` | — | — |
| `FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 5ms sweep 1650-1710kHz.0_00044.spm` | AFM | 27 | `zenodo/15326266/FigS3 itPMMA 98Hz 140nm 1730cm zeroscan 5ms sweep 1650-1710kHz.0_00044.spm/` | — | — |
| `FigS4 1550-1950kHz 5 segments, uncalibrated force scale.0_00100.spm` | AFM | 28 | `zenodo/15326266/FigS4 1550-1950kHz 5 segments, uncalibrated force scale.0_00100.spm/` | — | — |
| `FigS5 PS-LDPE 50nm 49Hz setpt=+0.1nm.0_00032.spm` | AFM | 29 | `zenodo/15326266/FigS5 PS-LDPE 50nm 49Hz setpt=+0.1nm.0_00032.spm/` | — | — |
| `FigS5 PS-LDPE 50nm 49Hz setpt=-0.1nm.0_00031.spm` | AFM | 30 | `zenodo/15326266/FigS5 PS-LDPE 50nm 49Hz setpt=-0.1nm.0_00031.spm/` | — | — |
| `FigS9 dPS-b-PMMA 98Hz 120nm 1730cm-1 25ms 1748kHz.0_00028.spm` | AFM | 31 | `zenodo/15326266/FigS9 dPS-b-PMMA 98Hz 120nm 1730cm-1 25ms 1748kHz.0_00028.spm/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/Fig3 spectrum Au.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/Fig3 spectrum PM.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/Fig4 LDPE.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/Fig4 PS.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/Fig6 curves panel A.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/Fig6 curves panel B.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/Fig7 spectra REFV and SSFV.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/FigS2 CM dPS-b-PMMA 0.5Hz.0_00026.spm - 10nm wide profile.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/FigS2 CM dPS-b-PMMA 0.5Hz.0_00027.spm - 10nm wide profile.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/FigS2 REFV dPS-b-PMMA 140nm 98Hz 5ms.0_00009.spm - 10nm wide profile.txt/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/FigS2 REFV dPS-b-PMMA 140nm 98Hz 5ms.0_00020.spm - 10nm wide profile.txt/` | — | — |
| `*.png` | AFM | 1 | `zenodo/15326266/FigS3 evaluated area is at image center over 10 pixels.PNG/` | — | — |
| `*.txt` | AFM | 1 | `zenodo/15326266/FigS3 graph data.txt/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
