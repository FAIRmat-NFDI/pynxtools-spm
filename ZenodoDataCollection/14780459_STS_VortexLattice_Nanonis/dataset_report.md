# Dataset Report: Zenodo Record 14780459

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Data related to "Inverse melting and re-entrant transformations of the vortex lattice in amorphous Re6Zr thin film" |
| **DOI**    | [10.5281/zenodo.14780459](https://doi.org/10.5281/zenodo.14780459) |
| **Url**    | [https://zenodo.org/records/14780459](https://zenodo.org/records/14780459) |
| **Date**   | 2025-01-31 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Duhan, Rishabh; Sengupta, Subhamita; Jesudasan, John et al. |
| **Tags**   | STM, STS, scanning tunneling spectroscopy, superconductor, vortex lattice, Re6Zr |
| **Description** | This work reports the Inverse Melting of the vortex lattice in a 20 nm thick superconducting Re6Zr thin film, through direct imaging of the vortex lattice using low-temperature scanning tunneling spectroscopy and complementary transport measurements. The central result is that in a superconducting thin film with moderate vortex pinning, vortices form an inhomogeneous liquid at low temperatures and magnetic field and gradually transform to a nearly perfect crystalline solid as the magnetic field or temperature is increased, before melting into a liquid again at higher magnetic fields or temperature. This is qualitatively summarised in "raw_image_addition.png (https://zenodo.org/api/records/14780459/draft/files/raw_image_addition.png/content)". Here, in each panel, we have added a sequence of 20 successive conductance maps acquired in the same area. In each conductance map the more probable locations for vortices appear as local conductance minima. When the vortices are moving, these minima appear at different locations in each image and the contrast becomes poor in the added image. At 460 mK, we observe a gradual evolution from an inhomogeneous vortex liquid to a vortex solid from 3 kOe to 20 kOe, and a gradual melting of this vortex solid again at higher fields. Similarly, at 3 kOe the inhomogeneous vortex liquid gradually crystallises between 460 mK to 3 K and then melts again at 4K.  <br><br>   raw_image_addition.png (https://zenodo.org/api/records/14780459/draft/files/raw_image_addition.png/content) is created by adding the intensities of 20 conductance maps acquired in the same area. A constant background conductance has been subtracted from each image. All images are plotted with the same relative conductance scale. <br><br> The STS raw data used in  creating "raw_image_addition.png (https://zenodo.org/api/records/14780459/draft/files/raw_image_addition.png/content)" and in Figures 1, 2, and 3 of the paper are given in *.sxm format. The files numbered 001 to 020 in each subfolder denote the sequence of conductance maps acquired successively over the same area at a given magnetic field and temperature. The data in subfolder "Fig 1 and 2" are at 460 mK. <br><br> The transport data (processed and unprocessed) are given as *.opju file and classified into subfolders named as per the corresponding figures in the paper. |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: STS (Scanning Tunneling Spectroscopy) — conductance maps at low temperature
- **Instrument**: Nanonis (`.sxm` format) low-temperature STM/STS

## Dataset Contents

318 Nanonis `.sxm` conductance maps organised by figure (Fig 1 & 2, Fig 3) showing vortex lattice states at varying magnetic field and temperature in Re₆Zr thin film. Transport data in `.opju` (Origin). PNG summary image included.

## File Format

- **Format**: Nanonis `.sxm` (STS conductance maps), `.opju` (Origin transport data), `.png`
- **Parsability**: Nanonis `.sxm` files are parsable. Technique is STS (conductance maps), so `NanonisSxmSTM` would apply. Transport `.opju` files are not in scope.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/14780459/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 318 files

**S3 key pattern**: `zenodo/14780459/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
| `001.sxm` | STM | 1 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 2 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 3 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 4 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 5 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 6 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 7 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 8 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 9 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 10 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 11 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 12 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 13 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 14 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 15 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 16 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 17 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 18 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 19 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 20 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 21 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 22 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 23 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 24 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 25 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 26 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 27 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 28 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 29 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 30 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 31 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 32 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 33 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 34 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 35 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 36 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 37 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 38 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 39 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 40 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 41 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 42 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 43 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 44 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 45 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 46 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 47 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 48 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 49 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 50 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 51 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 52 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 53 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 54 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 55 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 56 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 57 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 58 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 59 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 60 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 61 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 62 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 63 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 64 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 65 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 66 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 67 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 68 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 69 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 70 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 71 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 72 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 73 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 74 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 75 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 76 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 77 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 78 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 79 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 80 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 81 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 82 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 83 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 84 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 85 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 86 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 87 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 88 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 89 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 90 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 91 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 92 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 93 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 94 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 95 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 96 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 97 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 98 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 99 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 100 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 101 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 102 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 103 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 104 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 105 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 106 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 107 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 108 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 109 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 110 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 111 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 112 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 113 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 114 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 115 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 116 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 117 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 118 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 119 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 120 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 121 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 122 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 123 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 124 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 125 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 126 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 127 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 128 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 129 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 130 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 131 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 132 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 133 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 134 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 135 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 136 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 137 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 138 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 139 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 140 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 141 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 142 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 143 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 144 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 145 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 146 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 147 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 148 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 149 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 150 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 151 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 152 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 153 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 154 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 155 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 156 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 157 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 158 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 159 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 160 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 161 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 162 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 163 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 164 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 165 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 166 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 167 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 168 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 169 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 170 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 171 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 172 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 173 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 174 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 175 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 176 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 177 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 178 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 179 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 180 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 181 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 182 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 183 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 184 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 185 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 186 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 187 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 188 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 189 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 190 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 191 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 192 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 193 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 194 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 195 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 196 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 197 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 198 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 199 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 200 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 201 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/001.sxm/` | — | — |
| `002.sxm` | STM | 202 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/002.sxm/` | — | — |
| `003.sxm` | STM | 203 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/003.sxm/` | — | — |
| `004.sxm` | STM | 204 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/004.sxm/` | — | — |
| `005.sxm` | STM | 205 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/005.sxm/` | — | — |
| `006.sxm` | STM | 206 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/006.sxm/` | — | — |
| `007.sxm` | STM | 207 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/007.sxm/` | — | — |
| `008.sxm` | STM | 208 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/008.sxm/` | — | — |
| `009.sxm` | STM | 209 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/009.sxm/` | — | — |
| `010.sxm` | STM | 210 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/010.sxm/` | — | — |
| `011.sxm` | STM | 211 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/011.sxm/` | — | — |
| `012.sxm` | STM | 212 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/012.sxm/` | — | — |
| `013.sxm` | STM | 213 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/013.sxm/` | — | — |
| `014.sxm` | STM | 214 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/014.sxm/` | — | — |
| `015.sxm` | STM | 215 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/015.sxm/` | — | — |
| `016.sxm` | STM | 216 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/016.sxm/` | — | — |
| `017.sxm` | STM | 217 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/017.sxm/` | — | — |
| `018.sxm` | STM | 218 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/018.sxm/` | — | — |
| `019.sxm` | STM | 219 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/019.sxm/` | — | — |
| `020.sxm` | STM | 220 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/020.sxm/` | — | — |
| `001.sxm` | STM | 221 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/001.sxm/` | — | — |
| `002.sxm` | STM | 222 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/002.sxm/` | — | — |
| `003.sxm` | STM | 223 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/003.sxm/` | — | — |
| `004.sxm` | STM | 224 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/004.sxm/` | — | — |
| `005.sxm` | STM | 225 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/005.sxm/` | — | — |
| `006.sxm` | STM | 226 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/006.sxm/` | — | — |
| `007.sxm` | STM | 227 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/007.sxm/` | — | — |
| `008.sxm` | STM | 228 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/008.sxm/` | — | — |
| `009.sxm` | STM | 229 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/009.sxm/` | — | — |
| `010.sxm` | STM | 230 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/010.sxm/` | — | — |
| `011.sxm` | STM | 231 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/011.sxm/` | — | — |
| `012.sxm` | STM | 232 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/012.sxm/` | — | — |
| `013.sxm` | STM | 233 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/013.sxm/` | — | — |
| `014.sxm` | STM | 234 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/014.sxm/` | — | — |
| `015.sxm` | STM | 235 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/015.sxm/` | — | — |
| `016.sxm` | STM | 236 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/016.sxm/` | — | — |
| `017.sxm` | STM | 237 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/017.sxm/` | — | — |
| `018.sxm` | STM | 238 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/018.sxm/` | — | — |
| `019.sxm` | STM | 239 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/019.sxm/` | — | — |
| `020.sxm` | STM | 240 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/020.sxm/` | — | — |
| `001.sxm` | STM | 241 | `zenodo/14780459/STM data/Fig3/20kOe_3K/001.sxm/` | — | — |
| `002.sxm` | STM | 242 | `zenodo/14780459/STM data/Fig3/20kOe_3K/002.sxm/` | — | — |
| `003.sxm` | STM | 243 | `zenodo/14780459/STM data/Fig3/20kOe_3K/003.sxm/` | — | — |
| `004.sxm` | STM | 244 | `zenodo/14780459/STM data/Fig3/20kOe_3K/004.sxm/` | — | — |
| `005.sxm` | STM | 245 | `zenodo/14780459/STM data/Fig3/20kOe_3K/005.sxm/` | — | — |
| `006.sxm` | STM | 246 | `zenodo/14780459/STM data/Fig3/20kOe_3K/006.sxm/` | — | — |
| `007.sxm` | STM | 247 | `zenodo/14780459/STM data/Fig3/20kOe_3K/007.sxm/` | — | — |
| `008.sxm` | STM | 248 | `zenodo/14780459/STM data/Fig3/20kOe_3K/008.sxm/` | — | — |
| `009.sxm` | STM | 249 | `zenodo/14780459/STM data/Fig3/20kOe_3K/009.sxm/` | — | — |
| `010.sxm` | STM | 250 | `zenodo/14780459/STM data/Fig3/20kOe_3K/010.sxm/` | — | — |
| `011.sxm` | STM | 251 | `zenodo/14780459/STM data/Fig3/20kOe_3K/011.sxm/` | — | — |
| `012.sxm` | STM | 252 | `zenodo/14780459/STM data/Fig3/20kOe_3K/012.sxm/` | — | — |
| `013.sxm` | STM | 253 | `zenodo/14780459/STM data/Fig3/20kOe_3K/013.sxm/` | — | — |
| `014.sxm` | STM | 254 | `zenodo/14780459/STM data/Fig3/20kOe_3K/014.sxm/` | — | — |
| `015.sxm` | STM | 255 | `zenodo/14780459/STM data/Fig3/20kOe_3K/015.sxm/` | — | — |
| `001.sxm` | STM | 256 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/001.sxm/` | — | — |
| `002.sxm` | STM | 257 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/002.sxm/` | — | — |
| `003.sxm` | STM | 258 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/003.sxm/` | — | — |
| `004.sxm` | STM | 259 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/004.sxm/` | — | — |
| `005.sxm` | STM | 260 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/005.sxm/` | — | — |
| `006.sxm` | STM | 261 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/006.sxm/` | — | — |
| `007.sxm` | STM | 262 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/007.sxm/` | — | — |
| `008.sxm` | STM | 263 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/008.sxm/` | — | — |
| `009.sxm` | STM | 264 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/009.sxm/` | — | — |
| `010.sxm` | STM | 265 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/010.sxm/` | — | — |
| `011.sxm` | STM | 266 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/011.sxm/` | — | — |
| `012.sxm` | STM | 267 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/012.sxm/` | — | — |
| `013.sxm` | STM | 268 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/013.sxm/` | — | — |
| `014.sxm` | STM | 269 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/014.sxm/` | — | — |
| `015.sxm` | STM | 270 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/015.sxm/` | — | — |
| `016.sxm` | STM | 271 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/016.sxm/` | — | — |
| `017.sxm` | STM | 272 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/017.sxm/` | — | — |
| `018.sxm` | STM | 273 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/018.sxm/` | — | — |
| `019.sxm` | STM | 274 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/019.sxm/` | — | — |
| `020.sxm` | STM | 275 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/020.sxm/` | — | — |
| `01.sxm` | STM | 276 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/01.sxm/` | — | — |
| `010.sxm` | STM | 277 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/010.sxm/` | — | — |
| `011.sxm` | STM | 278 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/011.sxm/` | — | — |
| `012.sxm` | STM | 279 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/012.sxm/` | — | — |
| `013.sxm` | STM | 280 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/013.sxm/` | — | — |
| `014.sxm` | STM | 281 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/014.sxm/` | — | — |
| `015.sxm` | STM | 282 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/015.sxm/` | — | — |
| `016.sxm` | STM | 283 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/016.sxm/` | — | — |
| `017.sxm` | STM | 284 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/017.sxm/` | — | — |
| `018.sxm` | STM | 285 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/018.sxm/` | — | — |
| `019.sxm` | STM | 286 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/019.sxm/` | — | — |
| `02.sxm` | STM | 287 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/02.sxm/` | — | — |
| `020.sxm` | STM | 288 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/020.sxm/` | — | — |
| `03.sxm` | STM | 289 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/03.sxm/` | — | — |
| `04.sxm` | STM | 290 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/04.sxm/` | — | — |
| `05.sxm` | STM | 291 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/05.sxm/` | — | — |
| `06.sxm` | STM | 292 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/06.sxm/` | — | — |
| `07.sxm` | STM | 293 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/07.sxm/` | — | — |
| `08.sxm` | STM | 294 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/08.sxm/` | — | — |
| `09.sxm` | STM | 295 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/09.sxm/` | — | — |
| `001.sxm` | STM | 296 | `zenodo/14780459/STM data/Fig3/3 kOe_4K/001.sxm/` | — | — |
| `001.sxm` | STM | 297 | `zenodo/14780459/STM data/Fig3/30kOe_2K/001.sxm/` | — | — |
| `002.sxm` | STM | 298 | `zenodo/14780459/STM data/Fig3/30kOe_2K/002.sxm/` | — | — |
| `003.sxm` | STM | 299 | `zenodo/14780459/STM data/Fig3/30kOe_2K/003.sxm/` | — | — |
| `004.sxm` | STM | 300 | `zenodo/14780459/STM data/Fig3/30kOe_2K/004.sxm/` | — | — |
| `005.sxm` | STM | 301 | `zenodo/14780459/STM data/Fig3/30kOe_2K/005.sxm/` | — | — |
| `006.sxm` | STM | 302 | `zenodo/14780459/STM data/Fig3/30kOe_2K/006.sxm/` | — | — |
| `007.sxm` | STM | 303 | `zenodo/14780459/STM data/Fig3/30kOe_2K/007.sxm/` | — | — |
| `008.sxm` | STM | 304 | `zenodo/14780459/STM data/Fig3/30kOe_2K/008.sxm/` | — | — |
| `009.sxm` | STM | 305 | `zenodo/14780459/STM data/Fig3/30kOe_2K/009.sxm/` | — | — |
| `010.sxm` | STM | 306 | `zenodo/14780459/STM data/Fig3/30kOe_2K/010.sxm/` | — | — |
| `011.sxm` | STM | 307 | `zenodo/14780459/STM data/Fig3/30kOe_2K/011.sxm/` | — | — |
| `012.sxm` | STM | 308 | `zenodo/14780459/STM data/Fig3/30kOe_2K/012.sxm/` | — | — |
| `013.sxm` | STM | 309 | `zenodo/14780459/STM data/Fig3/30kOe_2K/013.sxm/` | — | — |
| `014.sxm` | STM | 310 | `zenodo/14780459/STM data/Fig3/30kOe_2K/014.sxm/` | — | — |
| `015.sxm` | STM | 311 | `zenodo/14780459/STM data/Fig3/30kOe_2K/015.sxm/` | — | — |
| `016.sxm` | STM | 312 | `zenodo/14780459/STM data/Fig3/30kOe_2K/016.sxm/` | — | — |
| `017.sxm` | STM | 313 | `zenodo/14780459/STM data/Fig3/30kOe_2K/017.sxm/` | — | — |
| `018.sxm` | STM | 314 | `zenodo/14780459/STM data/Fig3/30kOe_2K/018.sxm/` | — | — |
| `019.sxm` | STM | 315 | `zenodo/14780459/STM data/Fig3/30kOe_2K/019.sxm/` | — | — |
| `020.sxm` | STM | 316 | `zenodo/14780459/STM data/Fig3/30kOe_2K/020.sxm/` | — | — |
| `*.opju` | STS | 1 | `zenodo/14780459/Transport Data.opju/` | — | — |
| `*.png` | STS | 1 | `zenodo/14780459/raw_image_addition.png/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
