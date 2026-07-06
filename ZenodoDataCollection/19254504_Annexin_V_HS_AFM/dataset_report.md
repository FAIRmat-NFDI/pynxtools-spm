# Dataset Report: Zenodo Record 19254504

## Metadata

| Field      | Value |
|------------|-------|
| **Title**  | Annexin V assembly dynamics on lipid bilayers by High-Speed AFM |
| **DOI**    | [10.5281/zenodo.19254504](https://doi.org/10.5281/zenodo.19254504) |
| **Date**   | 2026-03-27 |
| **Access** | Open |
| **License**| CC BY 4.0 |
| **Authors**| Heath, George R |
| **Tags**   | AFM, high-speed atomic force microscopy, HS-AFM, annexin V, lipid bilayer, raw data |

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

**S3 key pattern**: `zenodo/19254504/For Zenodo/<imaging-session>/<filename>/<filename>`

Source zip `Annexin V HS AFM.zip` extracted into `For Zenodo/` with 37 imaging sessions ([S3 prefix](https://s3.console.aws.amazon.com/s3/buckets/spm-zenodo-data-897035677417?prefix=zenodo/19254504/For%20Zenodo/))

| file | experiment | count | S3 key prefix |
|------|------------|-------|---------------|
| `For Zenodo/imaging-*/<file>.jpk` | AFM | 7815 | `zenodo/19254504/For Zenodo/` (37 sessions) |

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
- [ ] JPK parser implemented
- [ ] Reference `.nxs` file generated
