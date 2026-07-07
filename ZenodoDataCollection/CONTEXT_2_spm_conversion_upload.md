# CONTEXT 2 — SPM Conversion and S3 Upload

Instructions for converting the S3-archived SPM raw files (STM, STS, AFM only) to NeXus
with `pynxtools-spm`, and uploading ELN + config + `.nxs` next to each raw file in S3.
Run [CONTEXT_1_dataset_report_curation.md](CONTEXT_1_dataset_report_curation.md) for a
dataset first — this workflow fills the `PS` / `Uploaded` columns that CONTEXT 1 creates.

## Ground rules

- **Never download from Zenodo** — pull data from S3 only
  (bucket `s3://spm-zenodo-data-897035677417`, profile `RubDev`, eu-central-1).
- **Temporary storage**: use the dataset's existing subfolder
  `ZenodoDataCollection/<record_id>_*/` (e.g. pull into `<record folder>/s3_data/`).
- **Logs**: append everything (commands, converter stdout/stderr, decisions, failures) to
  `<record folder>/conversion.log` with one clearly delimited section per raw file.
- `experiment_technique` is mandatory in every ELN — the reader raises `ValueError` without it.

## Supported variants → ELN/config templates

Templates live in [ElnExamples/](ElnExamples/). Choose by vendor + extension + technique:

| Vendor  | Ext        | Technique | Template folder            | NXDL   |
|---------|-----------|-----------|----------------------------|--------|
| Nanonis | `.sxm`    | STM       | `ElnExamples/nanonis_sxm_stm/` | NXstm |
| Nanonis | `.sxm`    | AFM       | `ElnExamples/nanonis_sxm_afm/` | NXafm |
| Nanonis | `.dat`    | STS       | `ElnExamples/nanonis_dat_sts/` | NXsts |
| Bruker  | `.spm`    | AFM       | `ElnExamples/bruker_spm_afm/`  | NXafm |
| Bruker  | `.txt` (NanoScope export) | AFM | `ElnExamples/bruker_txt_afm/` | NXafm |
| Omicron | `.sm4`    | STM       | `ElnExamples/omicron_sm4_stm/` | NXstm |

Known caveats:

- Nanonis `.dat` is supported **only as STS**. STM-image `.dat` files (common in the Moresco
  records) are expected to fail → record `PS = False`; that is a correct outcome, not an error.
- Bruker `.spm` parser is registered for software version `9.64`; other versions fall through
  to a brute-force attempt — log the version found in the file header.
- `.jpk`, `.ibw`, and other unsupported extensions are out of scope — leave their rows grouped.
- Bruker `.spm` files may lack an extension (record 20439519, e.g. `..._area_168.002`) —
  identify them by content/report, not extension alone.

## Per-dataset steps

### Step 1 — Pull the bucket locally

```bash
aws s3 sync s3://spm-zenodo-data-897035677417/zenodo/<record_id>/ \
    ZenodoDataCollection/<record folder>/s3_data/ --profile RubDev
```

Pulling the entire record is allowed — the metadata/readme files are needed for the ELN.

### Step 2 — Build the metadata context

Read, in this priority order (later fills gaps, earlier wins on conflict):
1. Human-readable files in the bucket (readme.md/.rtf/.txt, parameter CSVs, …).
2. The dataset's `dataset_report.md` (Description, Tags, Authors, Url rows).
3. The Zenodo record JSON (`curl -s https://zenodo.org/api/records/<record_id>`, metadata only).

Collect: sample name / chemical formula / history, experiment description, scan mode,
instrument software + version, authors, DOI, record URL.

### Step 3 — Per raw file: prepare ELN + config

For each SPM-parsable raw file (per-file rows in the report table):

1. Create `ZenodoDataCollection/<record folder>/conversion/<filename>/`.
2. Copy `eln_data.yaml` and the config JSON from the matching `ElnExamples/` variant into it.
3. Fill every `PlaceHolder` in the ELN from the Step 2 context:
   - `Sample.*` — sample name/formula/description/history (leave the placeholder text only if
     genuinely not findable; note that in the log).
   - `experiment_description` — from the dataset description.
   - `identifier_collection` — the dataset URL (`https://zenodo.org/records/<record_id>`).
   - `identifier_experiment` — the raw file name.
   - `scan_mode` — from the raw file header or dataset description.
   - `Instrument.*.model` / `model/@version` — from raw file header if determinable.
   - `citeID` — authors / url / doi / description of the Zenodo record.
4. Keep the config JSON unmodified unless the conversion in Step 4 shows a mapping problem.

### Step 4 — Convert

```bash
dataconverter --reader spm --nxdl <NXDL> <raw_file> eln_data.yaml <config.json> \
    --output <raw_file_stem>.nxs >> <record folder>/conversion.log 2>&1
```

- Success → `PS = True`. Failure → `PS = False`; copy the traceback into the log and move on.

### Step 5 — Validate the default plot chain

Open the `.nxs` with `h5py` and verify `/@default` → entry, entry `@default` → an **existing
NXdata group**. If the referenced NXdata does not exist:

1. List the NXdata groups actually present in the file.
2. Set the ELN `default:` to one of those instance names (prefer a topography/current forward
   channel).
3. Re-run Step 4 and re-check.

### Step 6 — Upload on success

Only when `PS = True` and the default chain validates, upload all three artefacts into the
raw file's own S3 folder (the folder that already contains the raw file):

```bash
aws s3 cp eln_data.yaml  s3://…/zenodo/<record_id>/…/<filename>/eln_data.yaml  --profile RubDev
aws s3 cp <config.json>  s3://…/zenodo/<record_id>/…/<filename>/<config.json>  --profile RubDev
aws s3 cp <stem>.nxs     s3://…/zenodo/<record_id>/…/<filename>/<stem>.nxs     --profile RubDev
```

Verify with `aws s3 ls` that all three landed → `Uploaded = True`.

### Step 7 — Update the dataset report

In `dataset_report.md`:
- Set the file's `PS` and `Uploaded` cells (`True`/`False`).
- When all parsable files are processed, update the Status checklist
  (parser test attempted / `.nxs` generated).

### Step 8 — Cleanup (per raw file)

- **Parse succeeded and uploaded** → delete that file's local raw copy and its
  `conversion/<filename>/` folder (ELN, config, `.nxs` are all in S3 now).
- **Parse failed** → **keep** the raw file, ELN, and config locally for debugging.
- In all cases keep: `dataset_report.md` and `conversion.log`.
- After the whole record: remove `s3_data/` except raw files kept for failed parses.

## Failure policy

- A single file failing never aborts the record — log it, mark `PS = False`, continue.
- If **every** file of a variant fails, stop that record and summarise the common error in
  the log — likely a parser/config issue worth fixing in `pynxtools-spm` itself before retrying.
