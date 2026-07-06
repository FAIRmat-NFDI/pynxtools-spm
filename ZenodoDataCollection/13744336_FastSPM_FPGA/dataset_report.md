# Dataset Report: Zenodo Record 13744336

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Dataset supplementing "Design of an FPGA-Based Controller for Fast Scanning Probe Microscopy" in Sensors 2024 |
| **DOI**    | [10.5281/zenodo.13744336](https://doi.org/10.5281/zenodo.13744336) |
| **Date**   | 2024-09-11 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Gregorat, Leonardo; Cautero, Marco; Carrato, Sergio; Giuressi, Dario et al. |
| **Tags**   | fast SPM, FPGA, STM, AFM, scanning probe microscopy |

## Technique

- **Primary SPM technique**: STM + AFM (fast imaging)
- **Instrument**: Omicron VT-AFM (fast STM), Beetle-type EC-STM, MFP-3D (fast AFM)

## Dataset Contents

Fast imaging datasets: (9a) fast STM of Pt5 cluster on Fe₃O₄(001) at 4 fps; (9b) fast EC-STM of Pd-porphyrin on Au(111) at 12 fps; (9c) fast AFM of TGX1 grating at 4 fps. 24 objects extracted from data.zip.

## File Format

- **Format**: `.h5` / `.h5_meta` (Omicron fast SPM proprietary HDF5 variant)
- **Parsability**: Not supported. Format is `.h56` / `.h5_meta` from Omicron VT-AFM fast controller. No parser implemented.

## S3 Upload

**Bucket**: `s3://spm-zenodo-data-897035677417`  
**Prefix**: `zenodo/13744336/`  
**Upload date**: 2026-06-26  
**Profile used**: RubDev (eu-central-1)  
**Total objects**: 24 files

**S3 key pattern**: `zenodo/13744336/data/<figure>/<filename>/<filename>`

Source zip: `data.zip` → 3 subfolders: `Fig9a` (fast STM, Pt/Fe₃O₄), `Fig9b` (fast EC-STM, Pd-porphyrin/Au), `Fig9c` (fast AFM, TGX1 grating) — each with 8 files ([S3 folder](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/13744336/data/))

| file | experiment | S3 key |
|------|------------|--------|
| `Fig9a/FS_231026_009.h5`          | STM | `zenodo/13744336/data/Fig9a/FS_231026_009.h5/FS_231026_009.h5` |
| `Fig9a/FS_231026_009.h5_meta.txt` | STM | `zenodo/13744336/data/Fig9a/FS_231026_009.h5_meta.txt/FS_231026_009.h5_meta.txt` |
| `Fig9a/FS_231026_009.log`         | STM | `zenodo/13744336/data/Fig9a/FS_231026_009.log/FS_231026_009.log` |
| `Fig9a/FS_231026_009_0-72_udi.mp4` | STM | `zenodo/13744336/data/Fig9a/FS_231026_009_0-72_udi.mp4/FS_231026_009_0-72_udi.mp4` |
| `Fig9a/FS_231026_009_51di.png`    | STM | `zenodo/13744336/data/Fig9a/FS_231026_009_51di.png/FS_231026_009_51di.png` |
| `Fig9a/FS_231026_009_51ui.png`    | STM | `zenodo/13744336/data/Fig9a/FS_231026_009_51ui.png/FS_231026_009_51ui.png` |
| `Fig9a/FS_231026_009_61ui.png`    | STM | `zenodo/13744336/data/Fig9a/FS_231026_009_61ui.png/FS_231026_009_61ui.png` |
| `Fig9a/FS_231026_009_62di.png`    | STM | `zenodo/13744336/data/Fig9a/FS_231026_009_62di.png/FS_231026_009_62di.png` |
| `Fig9b/FS_240705_009.h5`          | STM | `zenodo/13744336/data/Fig9b/FS_240705_009.h5/FS_240705_009.h5` |
| `Fig9b/FS_240705_009.h5_meta.txt` | STM | `zenodo/13744336/data/Fig9b/FS_240705_009.h5_meta.txt/FS_240705_009.h5_meta.txt` |
| `Fig9b/FS_240705_009.log`         | STM | `zenodo/13744336/data/Fig9b/FS_240705_009.log/FS_240705_009.log` |
| `Fig9b/FS_240705_009_0-497_udi.mp4` | STM | `zenodo/13744336/data/Fig9b/FS_240705_009_0-497_udi.mp4/FS_240705_009_0-497_udi.mp4` |
| `Fig9b/FS_240705_009_212di.png`   | STM | `zenodo/13744336/data/Fig9b/FS_240705_009_212di.png/FS_240705_009_212di.png` |
| `Fig9b/FS_240705_009_212ui.png`   | STM | `zenodo/13744336/data/Fig9b/FS_240705_009_212ui.png/FS_240705_009_212ui.png` |
| `Fig9b/FS_240705_009_310di.png`   | STM | `zenodo/13744336/data/Fig9b/FS_240705_009_310di.png/FS_240705_009_310di.png` |
| `Fig9b/FS_240705_009_310ui.png`   | STM | `zenodo/13744336/data/Fig9b/FS_240705_009_310ui.png/FS_240705_009_310ui.png` |
| `Fig9c/FS_231116_002.h5`          | AFM | `zenodo/13744336/data/Fig9c/FS_231116_002.h5/FS_231116_002.h5` |
| `Fig9c/FS_231116_002.h5_meta.txt` | AFM | `zenodo/13744336/data/Fig9c/FS_231116_002.h5_meta.txt/FS_231116_002.h5_meta.txt` |
| `Fig9c/FS_231116_002.log`         | AFM | `zenodo/13744336/data/Fig9c/FS_231116_002.log/FS_231116_002.log` |
| `Fig9c/FS_231116_002_0-24_uf.mp4` | AFM | `zenodo/13744336/data/Fig9c/FS_231116_002_0-24_uf.mp4/FS_231116_002_0-24_uf.mp4` |
| `Fig9c/FS_231116_002_1uf.png`     | AFM | `zenodo/13744336/data/Fig9c/FS_231116_002_1uf.png/FS_231116_002_1uf.png` |
| `Fig9c/FS_231116_002_19uf.png`    | AFM | `zenodo/13744336/data/Fig9c/FS_231116_002_19uf.png/FS_231116_002_19uf.png` |
| `Fig9c/FS_231116_002_20uf.png`    | AFM | `zenodo/13744336/data/Fig9c/FS_231116_002_20uf.png/FS_231116_002_20uf.png` |
| `Fig9c/FS_231116_002_2uf.png`     | AFM | `zenodo/13744336/data/Fig9c/FS_231116_002_2uf.png/FS_231116_002_2uf.png` |

## Category

**Unknown/Unsupported Format**

## Status

- [x] Files uploaded to S3
- [ ] Parser not implemented
- [ ] Reference .nxs file not generated
