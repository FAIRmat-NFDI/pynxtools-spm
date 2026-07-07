# CONTEXT 1 — Dataset Report Curation

Instructions for updating every `ZenodoDataCollection/<record_id>_*/dataset_report.md`.
Follow this file top-to-bottom for each dataset subfolder. This workflow touches **all**
datasets (SPM and non-SPM). It never converts data — conversion is
[CONTEXT_2_spm_conversion_upload.md](CONTEXT_2_spm_conversion_upload.md).

## Ground rules

- **Never download dataset files from Zenodo.** All raw data is already in S3.
- **Metadata-only fetch is allowed**: `curl https://zenodo.org/api/records/<record_id>`
  (JSON record — title, html url, description, creators, license, file list).
- **S3 access**: bucket `s3://spm-zenodo-data-897035677417` (eu-central-1), profile `RubDev`.
  List objects with `aws s3 ls --recursive` or `aws s3api list-objects-v2 --profile RubDev`.
- **S3 key pattern**: `zenodo/<record_id>/<zip_root_or_folder>/<subfolders...>/<filename>/<filename>`
  — every raw file sits in its own folder named after the file, so ELN/config/NeXus can be
  added next to it later.
- **Idempotent**: re-running must update tables in place, never duplicate rows or sections.
- The reference example for the target report format is
  [19087372_STM_STS_Moresco_ACSNano/dataset_report.md](19087372_STM_STS_Moresco_ACSNano/dataset_report.md).

## Per-dataset steps

### Step 1 — Collect context

1. Extract `<record_id>` from the folder name (`<record_id>_<technique>_<label>`).
2. Fetch the Zenodo record JSON: `curl -s https://zenodo.org/api/records/<record_id>`.
3. List the S3 objects: `aws s3 ls s3://spm-zenodo-data-897035677417/zenodo/<record_id>/ --recursive --profile RubDev`.
4. Cross-check against `InvestigationOnZenodoData.md` for the earlier categorisation notes.

### Step 2 — Fill the Metadata table placeholders

The Metadata table contains rows whose value starts with `PlaceHolder:`. Replace them:

| Row | Fill with |
|-----|-----------|
| **Url** | The record's canonical URL, e.g. `https://zenodo.org/records/<record_id>` (from `links.self_html`) |
| **Description** | The full dataset description from the Zenodo record (condense HTML to readable markdown; keep sample/experiment details verbatim — they feed the ELN in CONTEXT 2) |
| **Experiment information related files** | Comma-separated list of files in the record/bucket that carry experiment context: readme(.md/.rtf/.txt), CSVs with parameters, PDFs, docx — anything human-readable describing samples, chemical formulas, temperatures, instrument settings |

If a report predates these rows, add them (same order as the reference example).

### Step 3 — Upgrade the raw-file table (hybrid granularity)

Target header:

```markdown
| file | experiment | count | S3 key | PS | Uploaded |
|------|------------|-------|--------|----|----------|
```

Column semantics:

- **file** — full file name (with extension).
- **experiment** — experiment name/technique (STM, STS, AFM, XPS, Raman, OM, …).
- **count** — for per-file rows: running index of the file (1…N). For grouped rows: number of files in the group.
- **S3 key** — full key of the **folder that contains the file** (per-file rows), e.g.
  `zenodo/19087372/A240329.111649.dat/`; for grouped rows the shared key prefix.
- **PS** — `True` if the pynxtools-spm parse succeeded, `False` if attempted and failed,
  `—` if not yet attempted. **Initialize to `—`** — CONTEXT 2 sets the real value.
- **Uploaded** — `True` once ELN + config + generated `.nxs` are uploaded into the same
  S3 folder as the raw file; otherwise `—`/`False`. **Initialize to `—`.**

Granularity rules (hybrid):

- **SPM-parsable raw files** (`.sxm`, `.dat`, `.sm4`, `.spm`, Bruker `.spm.txt`): **one row per file**.
- **Everything else** (CSVs, images, optical files, unsupported formats like `.jpk`):
  **one grouped row per folder/file-type**, `count` = number of files, `PS`/`Uploaded` = `—` (n/a).
  This keeps reports readable for datasets with thousands of ancillary objects (e.g. 20439519).

If the existing report uses the old header `| file | experiment | count | S3 key prefix |`,
rewrite it to the new header and re-derive the rows from the S3 listing.

### Step 4 — Fill the Information Files table

Under `**Information Files**:`, list every human-readable metadata file found in the bucket
(the same files named in the *Experiment information related files* metadata row):

```markdown
| file | experiment | count | S3 key |
|------|------------|-------|--------|
```

Same column semantics as Step 3 (per-file rows; these files are never parsed/converted, so
no PS/Uploaded columns). Leave the table header in place with no rows if the record has none.

### Step 5 — Status checklist

Keep/normalise the trailing checklist:

```markdown
## Status

- [x] Files uploaded to S3
- [ ] Parser test not yet attempted        ← CONTEXT 2 flips this
- [ ] Reference .nxs file not yet generated ← CONTEXT 2 flips this
```

## Order of work

Process datasets in the order they appear in `upload_pipeline_overview.md` (Interest records
first), but any subset is fine — each report is independent. After each report, verify the
markdown renders (tables well-formed) before moving on.
