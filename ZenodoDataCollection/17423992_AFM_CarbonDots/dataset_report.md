# Dataset Report: Zenodo Record 17423992

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for  Blue Laser for Production of Carbon Dots |
| **DOI**    | [10.5281/zenodo.17423992](https://doi.org/10.5281/zenodo.17423992) |
| **Url**    | [https://zenodo.org/records/17423992](https://zenodo.org/records/17423992) |
| **Date**   | 2024-10-03 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Cutroneo, Mariapompea |
| **Tags**   | AFM, carbon dots, Bruker Dimension ICON, ScanAsyst, thin film |
| **Description** | The PCL + CDs composites were studied using attenuated total reflectance coupled with Fourier transform infrared spectroscopy (ATR-FTIR) and were monitored using a JASCO Model 4600 spectrophotometer working in the (400–4000) cm−1 wavenumber range. The luminescence of the produced CDs was observed using the Avantes AvaSpec-2048-USB2 optical spectrometer. The luminescence was monitored in the transmission mode in the region 200–800 nm. The exciting UV light source operating at 365 nm and at a fluence of about 100 mJ/cm2 illuminated the front of the cuvette containing the CD suspension at a 10 cm distance and at 0°, while the fiber connected to the spectrometer was located on the back of the cuvette at a 1 mm distance and at 180°. The silicon cuts 1 cm × 1 cm in size were covered with drops of CD suspension and dried in air overnight. The formed films were studied by AFM. A dimension ICON AFM system (Bruker Corp., Bremen, Germany) operating in the ScanAsyst imaging mode in air has been employed. A commercial silicon Tip and SCANASYST, in air mode, with a spring constant of 0.4 N/m, supported 3 μm2 scanning. The identification of the CDs was carried out using AFM images recorded and processed using NanoScope Analysis 1.80 with 32-bit software. |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — ScanAsyst imaging mode
- **Instrument**: Bruker Dimension ICON (ScanAsyst mode in air)

## Dataset Contents

2 `.dat` files (Fig4 and Fig6) from Bruker Dimension ICON AFM measurements of carbon dot films on silicon. Data processed with NanoScope Analysis 1.80 (32-bit). Note: these are Bruker `.dat` export files, not Nanonis `.dat` files.

## File Format

- **Format**: `.dat` (Bruker NanoScope ASCII/binary export — not Nanonis format)
- **Parsability**: Not supported by current parsers. These `.dat` files are Bruker NanoScope exports, not Nanonis spectroscopy files. Format investigation needed.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/17423992/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 2 files

**S3 key pattern**: `zenodo/17423992/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `Fig4.dat` | AFM | 1 | `zenodo/17423992/Fig4.dat/` | — | — |
| `Fig6.dat` | AFM | 2 | `zenodo/17423992/Fig6.dat/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Unknown/Unsupported Format**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
