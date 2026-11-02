# CONTEXT 2 — SPM Conversion and S3 Upload

Instructions for converting the S3-archived SPM raw files (STM, STS, AFM only) to NeXus
with `pynxtools-spm`, and uploading ELN + config + `.nxs` next to each raw file in S3.
Run [CONTEXT_1_dataset_report_curation.md](CONTEXT_1_dataset_report_curation.md) for a
dataset first — this workflow fills the `PS` / `Uploaded` columns that CONTEXT 1 creates.

## Ground rules

- **License gate — process only open licenses.** Convert/upload a dataset **only if its Zenodo
  license is `CC BY 4.0` (`cc-by-4.0`) or `CC0` (`cc-zero`/`cc0-1.0`)**. For any other license,
  **skip the whole record** — do not convert or upload; note the skip (license id) in the
  dataset's `conversion.log` and `dataset_report.md`. Check the license via the record JSON
  (`metadata.license.id`) before Step 1.
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

- Nanonis `.dat` is a **spectroscopy (STS)** format — a genuine Nanonis `.dat` begins with the
  header line `Experiment<TAB>bias spectroscopy` and is supported by `NanonisDatSTS`. **There is
  no such thing as a Nanonis STM-image `.dat`** (STM/AFM images are `.sxm`).
- **Not every `.dat` is Nanonis.** Some records use the `.dat` extension for a *different,
  unsupported* format. In particular the **Moresco records (19087372, 19086147)** store 2D STM
  images in the **`Paramco32`** format (German control software; header `[Paramco32]`,
  `Num.X`/`Num.Y=256`) — this is **not Nanonis and not STS**; treat it as an unsupported format
  (out of scope, like `.jpk`), not as a "Nanonis STS that failed". (19086147's actual spectra are
  in `.VERT`, another non-Nanonis format.) **Detect by header before assuming Nanonis STS:**
  `[Paramco32]` → unsupported STM image; `Experiment<TAB>bias spectroscopy` → convert as STS.
- Nanonis **multi-pass `.sxm`** files name their channels `[P1]_Current`, `[P1]_Z`,
  `[P2]_Current`, … (two passes). The `ElnExamples/nanonis_sxm_*` template configs map only
  single-pass `/Current`, `/Z`, so multi-pass files yield no NXdata (`PS = False`) until the
  config is extended with `[Pn]_`-prefixed channel entries.
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
4. **Online search of the linked publication** when the dataset itself is thin on sample
   details. Search the paper title/DOI; prefer an **open-access mirror** (PMC / europepmc /
   arXiv / ResearchGate) if the publisher page is paywalled (`403`). Pull: sample material +
   **chemical formula**, substrate, layer count/thickness, preparation, instrument, and mode.

Collect: sample name / chemical formula / history, experiment description, scan mode,
instrument software + version, authors, DOI, record URL.

**Chemical formula.** Always fill `Sample.Sample_component.chemical_formula` with the closest
correct formula, even if the paper does not state one literally — derive it from the material
(e.g. graphene → `C`; MoS₂ → `MoS2`; HOPG/graphite → `C`; SiO₂ substrate → `SiO2`). If the
sample is chemically modified (e.g. graphene oxide from local anodic oxidation), give the
pristine material's formula and note the modification in the description. Only leave it blank
if the material is genuinely unidentifiable; note that in the log.

### Step 3 — Per raw file: prepare ELN + config

For each SPM-parsable raw file (per-file rows in the report table):

1. Create `ZenodoDataCollection/<record folder>/conversion/<filename>/`.
2. Copy `eln_data.yaml` and the config JSON (but always use `config.json` name for the config file) from the matching `ElnExamples/` variant into it.
3. Fill every `PlaceHolder` in the ELN from the Step 2 context:
   - `Sample.*` — sample name/formula/description/history (leave the placeholder text only if
     genuinely not findable; note that in the log).
   - `experiment_description` — from the dataset description.
   - `identifier_collection` — the dataset URL (`https://zenodo.org/records/<record_id>`).
   - `identifier_experiment` — the raw file name.
   - `scan_mode` — from the raw file header or dataset description.
   - `Instrument.*.model` / `model/@version` — from raw file header if determinable.
   - `citeID` — authors / url / doi / description of the Zenodo record. The `citeID.description`
     must hold the **full Zenodo dataset description** (verbatim, HTML condensed to text), then a
     blank line, then a provenance note naming the original raw file — because many raw file
     names are cryptic. Use a YAML literal block, e.g.:

     ```yaml
     citeID:
       description:
         - |
           <full Zenodo description text…>

           Note - original raw file name is `Fig2_SPG.spm`
     ```
4. Keep the config JSON unmodified unless the conversion in Step 4 shows a mapping problem
   (e.g. no NXdata groups written because the file's channels are not mapped — see
   "Config conventions" below).

> **NEVER use or modify the default config that ships in the `pynxtools-spm` source code**
> (`src/pynxtools_spm/configs/**`). For a dataset, always start from the matching template in
> [`ElnExamples/`](ElnExamples/) (per the vendor + extension + technique table above), copy it
> into the file's `conversion/<file>/` folder as `config.json`, and **only there** may you edit
> it. When editing, change the **raw-data keys** — the `raw_path` values that point at channels
> in the raw file (e.g. `/Current/forward` → `/[P1]_Current/forward` for a multi-pass Nanonis
> file) — to match that dataset's actual raw channel names. Do not touch the src-tree configs.

**Config conventions** (apply when you must edit/extend a config for a dataset):

- **NXdata `title` naming — use concise scientific labels**, not verbose sentences. Pattern:
  `"<Quantity> (<Forward|Backward>)"`. Height/height-sensor topography is titled
  **`Topography`**. Examples:
  - `Height Plot of AFM Experiment (Forward Direction)` → `Topography (Forward)`
  - `Adhesion Plot of AFM Experiment (Forward Direction)` → `Adhesion (Forward)`
  - Other Bruker quantities: `DMT Modulus`, `Adhesion`, `Deformation`, `Dissipation`,
    `Peak Force Error`, `Amplitude`, `Amplitude Error`, `Phase`, `TM Deflection`.
  Set each entry's `title.raw_path` to `"@default:<the scientific title>"`.
- **Bruker channel coverage.** The default `bruker_spm_afm.json` maps only TappingMode channels
  (`/Height_Sensor`, `/Amplitude`, `/Amplitude_Error`, `/Phase`, `/TM_Deflection`). **PeakForce
  QNM** files instead carry `/Height`, `/DMTModulus`, `/LogDMTModulus`, `/Adhesion`,
  `/Deformation`, `/Dissipation`, `/Peak_Force_Error`. If a converted `.nxs` has **no NXdata
  groups**, the channels are unmapped: add per-channel `DATA[data]` entries (distinct
  `grp_name`s such as `height_forward`, `dmt_modulus_forward`, … so they never collide with the
  TappingMode groups) in the **dataset's** `config.json`. Suggested units: Height/Deformation
  `nm`, DMT Modulus `Pa`, Adhesion/Peak Force Error `nN`, Dissipation `eV`. Set the ELN
  `default:` to an existing group (prefer `height_forward`).

### Step 4 — Convert

**Name the output `.nxs` meaningfully.** Many raw file names are cryptic (e.g. `image_051.sxm`,
`016.sxm`, `T190613_004.sxm`). Give the generated `.nxs` a **sample/result-based** name by
prepending a short slug of the sample/result to the original stem:
`<sample_slug>_<raw_file_stem>.nxs` (e.g. `Re6Zr_vortex_image_051.nxs`, `WSe2_016.nxs`,
`TwistedBLG_SiCCAO#C012_300mV.nxs`). The original raw file keeps its name (and is recorded in
`citeID.description`), so provenance is preserved.

```bash
slug="Re6Zr_vortex"                 # short sample/result slug for this dataset
stem="$(basename "<raw_file>")"; stem="${stem%.*}"
dataconverter --reader spm --nxdl <NXDL> <raw_file> eln_data.yaml config.json \
    --output "${slug}_${stem}.nxs" >> <record folder>/conversion.log 2>&1
```

- Success → `PS = True`. Failure → `PS = False`; copy the traceback into the log and move on.
- **If re-processing a record that was already uploaded with the old (raw-stem) name**, delete
  the stale `.nxs` from the file's S3 folder before uploading the newly-named one so the folder
  holds exactly one `.nxs`:

  ```bash
  # remove any previously-uploaded .nxs in the folder, then upload the new one
  aws s3 ls "s3://<bucket>/<key>/" --profile RubDev | awk '{print $NF}' | grep '\.nxs$' \
    | while read old; do aws s3 rm "s3://<bucket>/<key>/$old" --profile RubDev; done
  aws s3 cp "${slug}_${stem}.nxs" "s3://<bucket>/<key>/${slug}_${stem}.nxs" --profile RubDev
  ```

### Step 5 — Validate the `.nxs` (default chain + NXdata shapes)

**Always open the generated `.nxs` with `h5py` and validate it before uploading.**

**5a. Default plot chain.** Verify `/@default` → entry, entry `@default` → an **existing
NXdata group**. If the referenced NXdata does not exist:

1. List the NXdata groups actually present in the file.
2. Set the ELN `default:` to one of those instance names (prefer a topography/height forward
   channel, e.g. `height_forward`).
3. Re-run Step 4 and re-check.

**5b. NXdata shape check (every NXdata group).** For each NXdata group, the axis dataset
lengths must match the signal array shape **according to `@axes` order**. NeXus lists `@axes`
slow-to-fast, i.e. `['y', 'x']` for a 2D image: `y` is signal dimension 0, `x` is dimension 1.
So an axis named in position *i* of `@axes` must have length `signal.shape[i]`:

```python
import h5py
with h5py.File(nxs, "r") as f:
    e = f["entry"]
    for k in e:
        g = e[k]
        if not isinstance(g, h5py.Group) or g.attrs.get("NX_class") != "NXdata":
            continue
        sig = g.attrs["signal"]; axes = list(g.attrs.get("axes", []))
        shape = g[sig].shape
        for dim, ax in enumerate(axes):
            assert ax in g and g[ax].shape[0] == shape[dim], (
                f"{k}: axis '{ax}' len {g[ax].shape[0]} != signal dim{dim} {shape[dim]}")
```

Why this matters: **partial/interrupted or non-square scans** (e.g. 114 lines × 512 samples)
expose axis/signal mismatches. A crossed x/y (x sized to `shape[0]` instead of `shape[1]`)
makes plots swap axes, and downstream tools raise errors like
`Expected array to have length 512 at least`. The Bruker AFM formatter now sizes each axis
from its own signal dimension (`y = shape[0]`, `x = shape[1]`), so square **and** non-square
scans stay aligned; still run the assertion above on every file as a guard.

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
- **Extend the raw-file table with two columns — `sample` and `chemical_formula`** — filled per
  file from the ELN `Sample.name` and `Sample.Sample_component.chemical_formula` used for that
  file. This makes a later cross-dataset roll-up (which sample / formula each raw file holds)
  straightforward. The per-file table header becomes:

  ```markdown
  | file | experiment | sample | chemical_formula | count | S3 key | PS | Uploaded |
  ```

  Use the same value on every row when a dataset has a single sample; put `—` for
  grouped/non-parsed rows where a formula is not meaningful, and `—` for `chemical_formula`
  when the material has no single molecular formula (e.g. a protein — see the ELN note).
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
