# Dataset Report: Zenodo Record 19707666

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset for 'Layer-dependent oxidation spreading in multilayer graphene during AFM local anodic oxidation' |
| **DOI**    | [10.5281/zenodo.19707666](https://doi.org/10.5281/zenodo.19707666) |
| **Url**    | [https://zenodo.org/records/19707666](https://zenodo.org/records/19707666) |
| **Date**   | 2026-04-23 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Vymazal, Jan; Konečný, Martin; Piastek, Jakub et al. |
| **Tags**   | AFM, atomic force microscopy, graphene, local anodic oxidation, LAO, oxidation, multilayer graphene |
| **Description** | Individual files used for Figures 2-12 are assembled in the folders. The COMSOL Multiphysics files are provided in the folder "COMSOL Simulations". |
| **Experiment information related files** | None |

## Technique

- **Primary SPM technique**: AFM (Atomic Force Microscopy) — local anodic oxidation (LAO) and imaging
- **Instrument**: Bruker AFM (NanoScope `.spm` format, firmware `0x09400202` ≈ v9.4)
- **Modes present**: Tapping + KPFM (surface potential) in the `tecky*.spm` files; PeakForce
  Tapping in `oxid*.spm`.

## Sample (from the linked publication)

Researched 2026-07-07 from the open-access paper *Local Anodic Oxidation of Graphene: The Role
of Number of Layers, Load Force, and Substrate* (ACS Omega 2026;
[PMC12878732](https://pmc.ncbi.nlm.nih.gov/articles/PMC12878732/); the Zenodo title uses the
earlier phrasing "Layer-dependent oxidation spreading …"). The Zenodo record itself carries no
sample detail, so this was recovered by online search.

- **Material / chemical formula**: mechanically exfoliated **graphene**, 1–6 layers (up to
  ~50 nm) → **`C`**. Local anodic oxidation locally converts it toward graphene oxide
  (≈ C:O:H); the pristine sample formula is `C`.
- **Substrate**: 285 nm thermally-grown **SiO₂ on Si** (`SiO2`/Si), partially covering a gold
  electrode; graphene grounded via a copper wire + silver paste.
- **Preparation**: exfoliated from a graphite crystal → PDMS stamp → transferred onto the
  SiO₂/gold-electrode platform.
- **Oxidation parameters**: oxidizing voltage −9 V, load 5–9 nN, tip velocity 1 µm/s.

## Dataset Contents

99 objects extracted from `Data.zip`, organised by figures (Figures 2–12) and COMSOL simulations. Contains Bruker `.spm` AFM files for individual figures in the graphene layer-dependent oxidation spreading study.

## File Format

- **Format**: Bruker `.spm` (native NanoScope, firmware `0x09400202`).
- **Parsability**: **All 7 parse.** `oxid.0_00008.spm` is PeakForce (Height Sensor + Peak Force
  Error). The 6 `tecky*.spm` files also carry KPFM/LockIn2 channels (`Potential`, `Amplitude2`,
  `Phase2`) under `@3:Image Data` that pySPM 0.6.3 cannot scale; the pynxtools-spm Bruker parser
  now skips those and recovers the usable channels (Height Sensor, Amplitude Error, Phase). See
  Conversion.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/19707666/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 99 files

**S3 key pattern**: `zenodo/19707666/<subfolders...>/<filename>/<filename>` — each raw file sits in its own folder so ELN/config/`.nxs` can be added alongside it.

`PS` = pynxtools-spm parse succeeded (`—` = not yet attempted); `Uploaded` = ELN+config+`.nxs` uploaded next to the raw file (`—` = not yet).

| file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
|------|------------|--------|------------------|-------|--------|----|----------|
| `tecky.0_00000.spm` | AFM | Multilayer graphene on SiO2/Si | C | 1 | `zenodo/19707666/Data/Figure 3/tecky.0_00000.spm/` | True | True |
| `tecky.0_00002.spm` | AFM | Multilayer graphene on SiO2/Si | C | 2 | `zenodo/19707666/Data/Figure 3/tecky.0_00002.spm/` | True | True |
| `tecky.0_00000.spm` | AFM | Multilayer graphene on SiO2/Si | C | 3 | `zenodo/19707666/Data/Figure 4/tecky.0_00000.spm/` | True | True |
| `tecky.0_00002.spm` | AFM | Multilayer graphene on SiO2/Si | C | 4 | `zenodo/19707666/Data/Figure 4/tecky.0_00002.spm/` | True | True |
| `tecky.0_00001.spm` | AFM | Multilayer graphene on SiO2/Si | C | 5 | `zenodo/19707666/Data/Figure 7/tecky.0_00001.spm/` | True | True |
| `tecky.0_00002.spm` | AFM | Multilayer graphene on SiO2/Si | C | 6 | `zenodo/19707666/Data/Figure 7/tecky.0_00002.spm/` | True | True |
| `oxid.0_00008.spm` | AFM | Multilayer graphene on SiO2/Si | C | 7 | `zenodo/19707666/Data/Figure 9/oxid.0_00008.spm/` | True | True |
| `*.mdt` | AFM | Multilayer graphene on SiO2/Si | C | 6 | `zenodo/19707666/Data/` | — | — |
| `*.mph` | AFM | Multilayer graphene on SiO2/Si | C | 19 | `zenodo/19707666/Data/` | — | — |
| `*.png` | AFM | Multilayer graphene on SiO2/Si | C | 34 | `zenodo/19707666/Data/` | — | — |
| `*.py` | AFM | Multilayer graphene on SiO2/Si | C | 6 | `zenodo/19707666/Data/` | — | — |
| `*.svg` | AFM | Multilayer graphene on SiO2/Si | C | 6 | `zenodo/19707666/Data/` | — | — |
| `*.svg` | RAMAN | Multilayer graphene on SiO2/Si | C | 1 | `zenodo/19707666/Data/` | — | — |
| `*.txt` | AFM | Multilayer graphene on SiO2/Si | C | 17 | `zenodo/19707666/Data/` | — | — |
| `*.wip` | AFM | Multilayer graphene on SiO2/Si | C | 3 | `zenodo/19707666/Data/` | — | — |

## Information Files

| file | experiment | count | S3 key |
|------|------------|-------|--------|

## Category

**Datasets of Interest**

## Conversion (CONTEXT 2)

Processed 2026-07-08 with `pynxtools-spm` 0.2.5 / `pySPM` 0.6.3. License **`cc-by-4.0`** passes
the open-license gate. **All 7 `.spm` files converted, validated, and uploaded** (`PS = True`,
`Uploaded = True`). The `oxid` file is PeakForce; the 6 `tecky` files are Tapping+KPFM whose KPFM
/LockIn2 channels (`Potential`, `Amplitude2`, `Phase2`, under `@3:Image Data`) pySPM 0.6.3 cannot
scale. The pynxtools-spm Bruker parser was fixed (override `pySPMBruker._get_layer_val` to raise
`KeyError` for missing keys + a per-channel guard) so those channels are skipped and the usable
ones recovered — the `tecky` files yield Topography, Amplitude Error and Phase (default
`z_forward`); the `oxid` file Topography + Peak Force Error. Post-audit: 0 long units, 0 shape
mismatches, 0 bad defaults. `citeID.description` carries the full Zenodo description.

## Status

- [x] Files uploaded to S3
- [x] Parser test attempted — 7/7 `.spm` converted (`PS = True`)
- [x] Reference .nxs files generated and uploaded for all 7 files
