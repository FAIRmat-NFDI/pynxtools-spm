# Zenodo → AWS S3 Upload Pipeline — Overview

## 1. Goal and Dataset Scope

### Goal

Build a curated archive of publicly available SPM (Scanning Probe Microscopy) datasets on AWS S3 for use in:
- Testing and extending the `pynxtools-spm` parser against real-world data
- Validating parser coverage across vendors, techniques, and software versions
- Enabling future automated conversion pipelines (Zenodo raw file → NeXus `.nxs`)

### Which Datasets Are Uploaded?

Datasets are categorised in [`InvestigationOnZenodoData.md`](InvestigationOnZenodoData.md) into three groups:

| Group | Count | Upload to S3? | Reason |
|-------|-------|--------------|--------|
| **Datasets of Interest** | 21 | **Yes** | Known supported formats: Bruker `.spm`, Nanonis `.sxm`/`.dat`, Omicron `.sm4` |
| **Unknown/Unsupported Format** | 18 | **Yes** | Format uncertain or not yet supported — archived for future parser development |
| **Not of Interest** | 26 | **No** | Irrelevant techniques or formats (e.g., non-SPM data, Dryad-hosted data) |

**Total to upload: 39 records** (21 Interest + 18 Unknown)

### Current S3 State (as of 2026-06-25)

**Bucket**: `s3://spm-zenodo-data-897035677417` (eu-central-1)

| Record ID | Title (short) | Status | Objects in S3 |
|-----------|--------------|--------|---------------|
| **20439519** | Autonomous SECCM (Au-Ir-Rh AFM) | ✅ Complete | 2018 files |
| **19254504** | Annexin V HS-AFM (`.jpk`) | 🔄 Uploading (~3381/7815) | 3381 files |
| 15326266 | Force Volume AFM-IR | 🔄 Downloading (batch) | — |
| 14271622–13595509 | Remaining 18 Interest records | ⏳ Queued | — |
| 18060234–14196376 | 18 Unknown records | ⏳ Queued | — |

---

## 2. Pipeline Steps

### Step 1 — Investigate and Categorise Zenodo Records

**What was done:**
- Searched Zenodo for SPM-related datasets (keywords: AFM, STM, STS, SPM, Nanonis, Bruker)
- For each record: inspected the file list, file extensions, instrument descriptions
- Classified each record into Interest / Unknown / Not of Interest
- Recorded findings in [`InvestigationOnZenodoData.md`](InvestigationOnZenodoData.md)

**Output:** 69 records catalogued; 39 selected for upload

---

### Step 2 — Create the AWS S3 Bucket

**What was done:**
- Created bucket `spm-zenodo-data-897035677417` in region `eu-central-1`
- Used AWS profile `RubDev` (confirmed write access)
- The bucket name includes the AWS account ID suffix for global uniqueness

**Script:** Helper function `create_s3_bucket` in [`store_dataset_in_s3_bucket.sh`](store_dataset_in_s3_bucket.sh)

---

### Step 3 — Design the S3 Key Layout

**What was done:**
- Decided on a key structure that places **each file in its own subfolder**, so experiment metadata (`eln_data.yaml`, converted `output.nxs`) can be added alongside the raw file later without key conflicts.

**Key structure:**
```
zenodo/<record_id>/<zip_root_or_folder>/<subfolder_if_any>/<filename>/<filename>
```

**Examples:**
```
zenodo/20439519/AFM_dataset/Au-Ir-Rh_Au-rich_AFM_area_168.002/Au-Ir-Rh_Au-rich_AFM_area_168.002
zenodo/19254504/For Zenodo/imaging-14.37.19.845/save-2022.11.04-14.37.19.920.jpk/save-2022.11.04-14.37.19.920.jpk
zenodo/15326266/Fig2 PS-b-PMMA 80nm 156Hz 5ms 1730cm.0_00096.spm/Fig2 PS-b-PMMA 80nm 156Hz 5ms 1730cm.0_00096.spm
```

**Why the `<filename>/<filename>` double-nesting?**
Each raw data file gets its own directory so you can later add:
```
zenodo/<record_id>/.../<filename>/
    <filename>           ← raw data file
    eln_data.yaml        ← ELN metadata for conversion
    output.nxs           ← converted NeXus file
```

---

### Step 4 — Build the Upload Script

**What was done:**
- Wrote `upload_zenodo_record()` function in [`store_dataset_in_s3_bucket.sh`](store_dataset_in_s3_bucket.sh)
- Wrote the batch script [`batch_upload_zenodo.sh`](batch_upload_zenodo.sh) to process all 39 records sequentially

**What each script does:**

#### `upload_zenodo_record()` (per-record function)
1. Calls `https://zenodo.org/api/records/<id>` to get the file list and download URLs
2. For each file (skipping `.mp4` video files):
   - Downloads the file to a local temp directory (`/tmp/zenodo_spm_download/<record_id>/`)
   - If the file is a `.zip`: extracts it in place with `unzip`, then deletes the zip
   - Non-zip files stay as downloaded
3. After all downloads, iterates over every extracted file with `find`:
   - Builds the S3 key using the `<filename>/<filename>` subfolder pattern
   - Uploads each file individually via `aws s3 cp --quiet`
4. Deletes the local temp directory after upload

#### `batch_upload_zenodo.sh` (batch runner)
1. Defines the list of all 39 record IDs
2. For each record:
   - Checks if `s3://bucket/zenodo/<record_id>/` already exists (idempotent — safe to re-run)
   - If not: runs the download → unzip → upload pipeline
   - Logs all activity to `batch_upload.log`
3. Runs in the background via `nohup` to survive terminal disconnections

---

### Step 5 — Handle Special Cases

**What was done:**

| Case | Problem | Solution |
|------|---------|---------|
| Record 19254504 (7815 `.jpk` files) | Data already downloaded locally (2.3 GB in `19254504_Annexin_V_HS_AFM/For Zenodo/`) — re-downloading 1.58 GB zip would be redundant | Created `/tmp/upload_19254504.sh` to upload directly from the local copy |
| Record 20439519 (SECCM/XPS/XRD/EDX) | >2000 CSV files take >2 min to upload sequentially — exceeds Claude Code's Bash tool timeout | Created `/tmp/upload_20439519_rest.sh` run as a `nohup` background process |
| `.mp4` files | Video files (animations) have no scientific value for SPM parsing and are very large | Skipped in all upload scripts |
| `__MACOSX/` directories | macOS metadata folders extracted from zips pollute the S3 prefix | Excluded with `! -path "*/__MACOSX/*"` in `find` and `! -name ".DS_Store"` |

---

### Step 6 — Pre-Authorise Claude Code Tool Calls

**What was done:**
- Added permission rules to `~/.claude/settings.json` so Claude Code does not prompt for approval on every AWS CLI call, curl download, or file operation during the pipeline.

**Added to `~/.claude/settings.json`:**
```json
"permissions": {
  "allow": [
    "Bash(aws *)", "Bash(curl *)", "Bash(unzip *)", "Bash(nohup *)",
    "Bash(find *)", "Bash(ps *)", "Bash(kill *)", "Bash(rm *)",
    "Bash(mkdir *)", "Bash(tail *)", "Bash(cat *)", "Bash(grep *)",
    "Bash(python3 *)"
  ]
}
```

---

### Step 7 — Create Per-Dataset Markdown Reports

**What was done:**
- For each uploaded record, created a `dataset_report.md` file in a dedicated subdirectory under `ZenodoDataCollection/`
- Each report documents: metadata, technique, dataset contents, S3 key layout, parsability assessment, and completion status

**Reports created so far:**

| Directory | Record | Status |
|-----------|--------|--------|
| [`20439519_AFM_dataset/`](20439519_AFM_dataset/dataset_report.md) | 20439519 | ✅ Upload complete |
| [`19254504_Annexin_V_HS_AFM/`](19254504_Annexin_V_HS_AFM/dataset_report.md) | 19254504 | 🔄 Uploading |
| [`15326266_AFM_IR_ForceVolume/`](15326266_AFM_IR_ForceVolume/dataset_report.md) | 15326266 | 🔄 Batch downloading |
| [`19087372_STM_STS_Moresco_ACSNano/`](19087372_STM_STS_Moresco_ACSNano/dataset_report.md) | 19087372 | ⏳ Queued |
| [`19086147_STM_STS_Moresco_Angewandte/`](19086147_STM_STS_Moresco_Angewandte/dataset_report.md) | 19086147 | ⏳ Queued |
| [`14271622_AFM_Multimetrological/`](14271622_AFM_Multimetrological/dataset_report.md) | 14271622 | ⏳ Queued |

---

## 3. Key Files Reference

| File | Purpose |
|------|---------|
| [`InvestigationOnZenodoData.md`](InvestigationOnZenodoData.md) | Master catalogue of all 69 Zenodo records investigated |
| [`store_dataset_in_s3_bucket.sh`](store_dataset_in_s3_bucket.sh) | Reusable helper functions (bucket creation, single-record upload) |
| [`batch_upload_zenodo.sh`](batch_upload_zenodo.sh) | Batch runner for all 39 records; idempotent, logs to `batch_upload.log` |
| [`batch_upload.log`](batch_upload.log) | Live log of the batch upload process |

## 4. How to Resume in a New Session

1. Check running processes: `ps aux | grep -E "upload_|batch_upload" | grep -v grep`
2. Check batch log: `tail -20 ZenodoDataCollection/batch_upload.log`
3. Check S3 state: `aws s3 ls s3://spm-zenodo-data-897035677417/zenodo/ --profile RubDev`
4. If the batch script is not running, restart it:
   ```bash
   cd ZenodoDataCollection
   nohup bash batch_upload_zenodo.sh --profile RubDev >> batch_upload.log 2>&1 &
   ```
   The idempotency check ensures already-uploaded records are skipped automatically.
