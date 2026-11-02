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

- **Primary SPM technique**: STS (Scanning Tunneling Spectroscopy) — dI/dV vortex-lattice maps at low temperature (stored as Nanonis `.sxm`, converted via the STM formatter)
- **Instrument**: Nanonis (`.sxm` format) low-temperature STM/STS

## Sample

- **Material / chemical formula**: 20 nm **amorphous Re₆Zr** superconducting thin film → `Re6Zr`.
- **Study**: the vortex lattice is imaged by low-temperature scanning tunneling spectroscopy
  (dI/dV mapping) vs magnetic field/temperature (inverse melting / re-entrant transformations).

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

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 1 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 2 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 3 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 4 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 5 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 6 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 7 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 8 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 9 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 10 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 11 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 12 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 13 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 14 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 15 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 16 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 17 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 18 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 19 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 20 | `zenodo/14780459/STM data/Fig 1 and 2/10 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 21 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 22 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 23 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 24 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 25 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 26 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 27 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 28 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 29 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 30 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 31 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 32 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 33 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 34 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 35 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 36 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 37 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 38 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 39 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 40 | `zenodo/14780459/STM data/Fig 1 and 2/15 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 41 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 42 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 43 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 44 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 45 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 46 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 47 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 48 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 49 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 50 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 51 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 52 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 53 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 54 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 55 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 56 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 57 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 58 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 59 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 60 | `zenodo/14780459/STM data/Fig 1 and 2/20 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 61 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 62 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 63 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 64 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 65 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 66 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 67 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 68 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 69 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 70 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 71 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 72 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 73 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 74 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 75 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 76 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 77 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 78 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 79 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 80 | `zenodo/14780459/STM data/Fig 1 and 2/25 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 81 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 82 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 83 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 84 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 85 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 86 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 87 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 88 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 89 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 90 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 91 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 92 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 93 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 94 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 95 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 96 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 97 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 98 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 99 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 100 | `zenodo/14780459/STM data/Fig 1 and 2/3 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 101 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 102 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 103 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 104 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 105 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 106 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 107 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 108 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 109 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 110 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 111 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 112 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 113 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 114 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 115 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 116 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 117 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 118 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 119 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 120 | `zenodo/14780459/STM data/Fig 1 and 2/30 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 121 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 122 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 123 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 124 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 125 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 126 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 127 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 128 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 129 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 130 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 131 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 132 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 133 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 134 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 135 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 136 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 137 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 138 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 139 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 140 | `zenodo/14780459/STM data/Fig 1 and 2/4 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 141 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 142 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 143 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 144 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 145 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 146 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 147 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 148 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 149 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 150 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 151 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 152 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 153 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 154 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 155 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 156 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 157 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 158 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 159 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 160 | `zenodo/14780459/STM data/Fig 1 and 2/40 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 161 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 162 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 163 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 164 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 165 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 166 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 167 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 168 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 169 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 170 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 171 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 172 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 173 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 174 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 175 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 176 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 177 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 178 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 179 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 180 | `zenodo/14780459/STM data/Fig 1 and 2/5 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 181 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 182 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 183 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 184 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 185 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 186 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 187 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 188 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 189 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 190 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 191 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 192 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 193 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 194 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 195 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 196 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 197 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 198 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 199 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 200 | `zenodo/14780459/STM data/Fig 1 and 2/50 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 201 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 202 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 203 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 204 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 205 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 206 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 207 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 208 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 209 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 210 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 211 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 212 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 213 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 214 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 215 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 216 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 217 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 218 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 219 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 220 | `zenodo/14780459/STM data/Fig 1 and 2/70 kOe/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 221 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 222 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 223 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 224 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 225 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 226 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 227 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 228 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 229 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 230 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 231 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 232 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 233 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 234 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 235 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 236 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 237 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 238 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 239 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 240 | `zenodo/14780459/STM data/Fig3/20 kOe_2K/020.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 241 | `zenodo/14780459/STM data/Fig3/20kOe_3K/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 242 | `zenodo/14780459/STM data/Fig3/20kOe_3K/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 243 | `zenodo/14780459/STM data/Fig3/20kOe_3K/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 244 | `zenodo/14780459/STM data/Fig3/20kOe_3K/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 245 | `zenodo/14780459/STM data/Fig3/20kOe_3K/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 246 | `zenodo/14780459/STM data/Fig3/20kOe_3K/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 247 | `zenodo/14780459/STM data/Fig3/20kOe_3K/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 248 | `zenodo/14780459/STM data/Fig3/20kOe_3K/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 249 | `zenodo/14780459/STM data/Fig3/20kOe_3K/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 250 | `zenodo/14780459/STM data/Fig3/20kOe_3K/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 251 | `zenodo/14780459/STM data/Fig3/20kOe_3K/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 252 | `zenodo/14780459/STM data/Fig3/20kOe_3K/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 253 | `zenodo/14780459/STM data/Fig3/20kOe_3K/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 254 | `zenodo/14780459/STM data/Fig3/20kOe_3K/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 255 | `zenodo/14780459/STM data/Fig3/20kOe_3K/015.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 256 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 257 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 258 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 259 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 260 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 261 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 262 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 263 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 264 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 265 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 266 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 267 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 268 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 269 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 270 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 271 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 272 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 273 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 274 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 275 | `zenodo/14780459/STM data/Fig3/3 kOe_2K/020.sxm/` | True | True |
| `01.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 276 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/01.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 277 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 278 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 279 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 280 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 281 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 282 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 283 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 284 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 285 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 286 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/019.sxm/` | True | True |
| `02.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 287 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/02.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 288 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/020.sxm/` | True | True |
| `03.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 289 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/03.sxm/` | True | True |
| `04.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 290 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/04.sxm/` | True | True |
| `05.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 291 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/05.sxm/` | True | True |
| `06.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 292 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/06.sxm/` | True | True |
| `07.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 293 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/07.sxm/` | True | True |
| `08.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 294 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/08.sxm/` | True | True |
| `09.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 295 | `zenodo/14780459/STM data/Fig3/3 kOe_3K/09.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 296 | `zenodo/14780459/STM data/Fig3/3 kOe_4K/001.sxm/` | True | True |
| `001.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 297 | `zenodo/14780459/STM data/Fig3/30kOe_2K/001.sxm/` | True | True |
| `002.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 298 | `zenodo/14780459/STM data/Fig3/30kOe_2K/002.sxm/` | True | True |
| `003.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 299 | `zenodo/14780459/STM data/Fig3/30kOe_2K/003.sxm/` | True | True |
| `004.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 300 | `zenodo/14780459/STM data/Fig3/30kOe_2K/004.sxm/` | True | True |
| `005.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 301 | `zenodo/14780459/STM data/Fig3/30kOe_2K/005.sxm/` | True | True |
| `006.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 302 | `zenodo/14780459/STM data/Fig3/30kOe_2K/006.sxm/` | True | True |
| `007.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 303 | `zenodo/14780459/STM data/Fig3/30kOe_2K/007.sxm/` | True | True |
| `008.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 304 | `zenodo/14780459/STM data/Fig3/30kOe_2K/008.sxm/` | True | True |
| `009.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 305 | `zenodo/14780459/STM data/Fig3/30kOe_2K/009.sxm/` | True | True |
| `010.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 306 | `zenodo/14780459/STM data/Fig3/30kOe_2K/010.sxm/` | True | True |
| `011.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 307 | `zenodo/14780459/STM data/Fig3/30kOe_2K/011.sxm/` | True | True |
| `012.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 308 | `zenodo/14780459/STM data/Fig3/30kOe_2K/012.sxm/` | True | True |
| `013.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 309 | `zenodo/14780459/STM data/Fig3/30kOe_2K/013.sxm/` | True | True |
| `014.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 310 | `zenodo/14780459/STM data/Fig3/30kOe_2K/014.sxm/` | True | True |
| `015.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 311 | `zenodo/14780459/STM data/Fig3/30kOe_2K/015.sxm/` | True | True |
| `016.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 312 | `zenodo/14780459/STM data/Fig3/30kOe_2K/016.sxm/` | True | True |
| `017.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 313 | `zenodo/14780459/STM data/Fig3/30kOe_2K/017.sxm/` | True | True |
| `018.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 314 | `zenodo/14780459/STM data/Fig3/30kOe_2K/018.sxm/` | True | True |
| `019.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 315 | `zenodo/14780459/STM data/Fig3/30kOe_2K/019.sxm/` | True | True |
| `020.sxm` | STM | Amorphous Re6Zr superconducting thin film | Re6Zr | 316 | `zenodo/14780459/STM data/Fig3/30kOe_2K/020.sxm/` | True | True |
| `*.opju` | STS | Amorphous Re6Zr superconducting thin film | Re6Zr | 1 | `zenodo/14780459/Transport Data.opju/` | — | — |
| `*.png` | STS | Amorphous Re6Zr superconducting thin film | Re6Zr | 1 | `zenodo/14780459/raw_image_addition.png/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08 with `pynxtools-spm` 0.2.5. License **`cc-by-4.0`** passes the open-license
gate. **All 316 Nanonis `.sxm` files converted, validated, and uploaded** (`PS = True`,
`Uploaded = True`); short units, default `current_forward`, 0 shape mismatches. Output `.nxs`
files are named meaningfully as `Re6Zr_vortex_<raw_stem>.nxs`. `citeID.description` carries the
full Zenodo description + the original raw file name.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 316/316 `.sxm` converted (`PS = True`)
- [x] Reference .nxs files generated and uploaded for all 316 files
