# CLAUDE.md — pynxtools-spm Developer Guide

## Instructions

- Never upgrade `pySPM` from `==0.6.3` without running all Bruker tests first — its API changed between versions.
- Always run `pytest -sv tests/` before committing any formatter or parser changes.
- When adding a new formatter, follow the checklist in the "Adding a New Formatter" section exactly.
- Do not edit reference `.nxs` files in `tests/data/` manually — regenerate them by running the reader and copying the output.
- `experiment_technique` in the ELN YAML is mandatory — `SPMReader.read()` raises `ValueError` if it is absent; do not add a fallback.
- `_construct_nxscan_controllers` must fully populate `self.scan_control` before returning — NXdata axis generation depends on it.
- `pynxtools` is installed from `master` in CI — keep the plugin compatible with the upstream development version, not just the latest release.
- Do not add `now()`-based timestamps to any fields other than `start_time`/`end_time` without also updating `ignore_sections` in `test_reader.py`.

---

## Project Overview

**pynxtools-spm** is a [pynxtools](https://github.com/FAIRmat-NFDI/pynxtools) plugin that converts vendor-specific Scanning Probe Microscopy (SPM) data files into standardized [NeXus](https://www.nexusformat.org/) HDF5 files (`.nxs`). It integrates with the [NOMAD](https://nomad-lab.eu) research data management platform via a plugin entry-point system.

**Supported techniques:** STM (Scanning Tunneling Microscopy), STS (Scanning Tunneling Spectroscopy), AFM (Atomic Force Microscopy)

**Supported vendors and formats:**

| Vendor  | File Extension | Techniques     |
|---------|---------------|----------------|
| Nanonis | `.sxm`        | STM, AFM       |
| Nanonis | `.dat`        | STS            |
| Omicron | `.sm4`        | STM            |
| Bruker  | `.spm`        | AFM            |
| Bruker  | `.txt`        | AFM (metadata) |

**NeXus definitions repository:** `/home/rubel/NOMAD-FAIRmat/GH/nexus_definitions/`
or check for the git repo `nexus_definitions` recursively under `~/NOMAD-FAIRmat/` and update here.

**Application definitions** (`applications/`):

| Definition | File | Technique |
|---|---|---|
| `NXspm` | `applications/NXspm.nxdl.xml` | Parent SPM definition (all techniques inherit from this) |
| `NXstm` | `applications/NXstm.nxdl.xml` | Scanning Tunneling Microscopy |
| `NXsts` | `applications/NXsts.nxdl.xml` | Scanning Tunneling Spectroscopy |
| `NXafm` | `applications/NXafm.nxdl.xml` | Atomic Force Microscopy |

**SPM base classes** (`base_classes/`):

| Class | File | Purpose |
|---|---|---|
| `NXspm_scan_control` | `base_classes/NXspm_scan_control.nxdl.xml` | Scan geometry: axes, range, offset, step size |
| `NXspm_scan_region` | `base_classes/NXspm_scan_region.nxdl.xml` | Physical scan area definition |
| `NXspm_scan_pattern` | `base_classes/NXspm_scan_pattern.nxdl.xml` | Raster or other scan trajectory |
| `NXspm_bias_spectroscopy` | `base_classes/NXspm_bias_spectroscopy.nxdl.xml` | Bias voltage sweep parameters |
| `NXspm_cantilever` | `base_classes/NXspm_cantilever.nxdl.xml` | AFM cantilever mechanical properties |
| `NXspm_cantilever_config` | `base_classes/NXspm_cantilever_config.nxdl.xml` | AFM cantilever configuration |
| `NXspm_cantilever_oscillator` | `base_classes/NXspm_cantilever_oscillator.nxdl.xml` | Cantilever oscillation parameters (dynamic AFM) |
| `NXspm_piezo_config` | `base_classes/NXspm_piezo_config.nxdl.xml` | Piezo scanner configuration |
| `NXspm_piezoelectric_material` | `base_classes/NXspm_piezoelectric_material.nxdl.xml` | Piezoelectric material properties |
| `NXspm_piezo_sensor` | `base_classes/NXspm_piezo_sensor.nxdl.xml` | Piezo sensor readout |
| `NXspm_positioner` | `base_classes/NXspm_positioner.nxdl.xml` | Coarse positioner (e.g., stepper motor) |
| `NXspm_temperature_sensor` | `base_classes/NXspm_temperature_sensor.nxdl.xml` | Temperature measurement |

---

## Repository Layout

```text
pynxtools-spm/
├── src/pynxtools_spm/
│   ├── reader.py                   # Main entry point: SPMReader
│   ├── parsers/                    # Layer 1 — raw file → Python dict
│   │   ├── __init__.py             # SPMParser orchestrator
│   │   ├── base_parser.py          # SPMBase abstract class
│   │   ├── helpers.py              # Parsing utilities
│   │   ├── nanonis_sxm.py          # Nanonis .sxm parser
│   │   ├── nanonis_dat.py          # Nanonis .dat parser
│   │   ├── omicron_sm4.py          # Omicron .sm4 parser
│   │   ├── bruker_spm.py           # Bruker .spm parser
│   │   ├── bruker_txt.py           # Bruker .txt parser
│   │   ├── bruker/                 # Low-level Bruker helpers
│   │   └── nanonispy/              # Vendored Nanonis file reading library
│   ├── nxformatters/               # Layer 2 — dict → NeXus template
│   │   ├── base_formatter.py       # SPMformatter base class
│   │   ├── helpers.py              # Unit conversion, variadic names, etc.
│   │   ├── nanonis/                # Nanonis formatters (STM, AFM, STS)
│   │   ├── omicron/                # Omicron formatters (STM)
│   │   └── bruker/                 # Bruker formatters (AFM)
│   ├── configs/                    # JSON mapping files (raw path → NeXus path)
│   │   ├── nanonis/
│   │   ├── omicron/
│   │   └── bruker/
│   └── nomad/                      # NOMAD platform integration
│       ├── entrypoints.py          # NOMAD plugin entry points
│       ├── apps/                   # NOMAD SPM app definition
│       └── example_uploads/        # Example data for STM, STS, AFM
├── tests/
│   ├── test_reader.py              # Parametrized integration tests
│   ├── functionality_test.py       # Unit tests for helper functions
│   ├── nomad/                      # NOMAD-specific tests
│   └── data/                       # Test data (raw files + expected .nxs output)
│       ├── nanonis/{stm,sts,afm}/
│       ├── omicron/stm/
│       └── bruker/afm/
├── docs/                           # MkDocs documentation source
├── .github/workflows/              # CI/CD pipelines
├── pyproject.toml                  # Project metadata, dependencies, entry points
├── mkdocs.yml                      # Documentation configuration
└── .pre-commit-config.yaml         # Pre-commit hooks
```

---

## Architecture: Three-Layer Pipeline

```text
Raw File (.sxm / .dat / .sm4 / .spm / .txt)
        │
        ▼
  ┌─────────────┐
  │   Parser    │  src/pynxtools_spm/parsers/
  │  (Layer 1)  │  Reads vendor format → flat {"/key": value} dict
  └─────────────┘
        │
        ▼ raw_data_dict + ELN YAML + Config JSON
  ┌─────────────┐
  │  Formatter  │  src/pynxtools_spm/nxformatters/
  │  (Layer 2)  │  Maps raw dict → pynxtools Template (NeXus paths)
  └─────────────┘
        │
        ▼
  ┌─────────────┐
  │   Reader    │  src/pynxtools_spm/reader.py
  │  (Layer 3)  │  SPMReader.read() → validated Template → .nxs HDF5
  └─────────────┘
```

### Layer 1 — Parsers

All parsers inherit from `SPMBase` ([src/pynxtools_spm/parsers/base_parser.py](src/pynxtools_spm/parsers/base_parser.py)) and implement a single `parse()` method that returns a flat `dict[str, Any]` where keys are slash-separated paths (e.g., `"/SCANIT_TYPE"`) and values are Python scalars, strings, or `numpy.ndarray`.

The `SPMParser` class ([src/pynxtools_spm/parsers/__init__.py](src/pynxtools_spm/parsers/__init__.py)) selects the correct parser using a nested navigation dict keyed on `(file_ext → vendor → software_version)`. If the ELN file does not specify vendor/version, all parsers for that file extension are tried in sequence until one succeeds.

**Adding a new parser:**
1. Create `src/pynxtools_spm/parsers/<vendor>_<ext>.py` extending `SPMBase`.
2. Implement `parse() -> dict`.
3. Register the class in `SPMParser.__parser_navigation` in `parsers/__init__.py`.

### Layer 2 — Formatters

All formatters inherit from `SPMformatter` ([src/pynxtools_spm/nxformatters/base_formatter.py](src/pynxtools_spm/nxformatters/base_formatter.py)) and implement `get_nxformatted_template()` which fills the pynxtools `Template` object.

The class hierarchy is:
```text
SPMformatter
├── NanonisBase
│   ├── NanonisSxmSTM
│   ├── NanonisSxmAFM
│   └── NanonisDatSTS
├── OmicronBase
│   └── OmicronSM4STM
└── BrukerBase
    └── BrukerSpmAFM
```

Formatters are driven by **JSON config files** in `src/pynxtools_spm/configs/` that map raw slash-separated parser keys to NeXus field paths. The JSON structure of each config file directly mirrors the hierarchical group/field nesting defined in the NeXus application definitions (`NXstm`, `NXsts`, `NXafm`) and their constituent base classes — each nested JSON key corresponds to a NeXus group or field at the same level in the definition tree. Users can supply their own config file to override or extend the default mapping.

**Key formatter concepts:**
- `replace_variadic_name_part`: handles `N[n]`-style repeated NeXus groups (e.g., `CHANNEL[channel_1]`).
- `CONVERT_DICT`: maps ELN YAML keys to NeXus group name conventions.
- `PINT_QUANTITY_MAPPING`: maps physical dimension signatures to unit categories for automatic unit validation/conversion via `pint`.
- `add_local_timezone`: attaches local timezone info to all timestamp fields.

### Layer 3 — Reader

`SPMReader.read()` ([src/pynxtools_spm/reader.py](src/pynxtools_spm/reader.py)) is the pynxtools entry point. It:
1. Classifies input files by extension (`.sxm/.dat/.sm4/.spm/.txt` = data, `.json` = config, `.yaml/.yml` = ELN).
2. Reads `experiment_technique` from the ELN YAML (`STM`, `STS`, or `AFM`).
3. Selects the appropriate formatter based on `(experiment_technique, file_ext)`.
4. Calls `formatter_obj.get_nxformatted_template()`.
5. Filters out `None`/empty values and applies `manually_filter_data_type` for known type-coercion edge cases.
6. Returns the filled `Template`.

**Technique × format dispatch table:**

| `experiment_technique` | `raw_file_ext` | Formatter class |
|------------------------|----------------|-----------------|
| `STM`                  | `sxm`          | `NanonisSxmSTM` |
| `STM`                  | `sm4`          | `OmicronSM4STM` |
| `AFM`                  | `sxm`          | `NanonisSxmAFM` |
| `AFM`                  | `spm`          | `BrukerSpmAFM`  |
| `STS`                  | `dat`          | `NanonisDatSTS` |

---

## NXFormatters — Detailed Internals

### Inheritance Tree

```text
ABC  (Python abstract base class)
└── SPMformatter                   base_formatter.py
    │   Abstract methods: _get_conf_dict, get_nxformatted_template,
    │                     _construct_nxscan_controllers
    │   Shared state:     self.scan_control (NXScanControl)
    │                     self.bias_sweep   (BiasSweep)
    │                     self.raw_data     (flat dict from parser)
    │                     self.config_dict  (JSON config)
    │                     self.eln          (flattened ELN dict)
    │
    ├── NanonisBase                nanonis/nanonis_base.py
    │   │   Adds: rearrange_data_according_to_axes()
    │   │         _arange_axes() — sets fast/slow axis on scan_control
    │   │
    │   ├── NanonisSxmSTM          nanonis/nanonis_sxm_stm.py
    │   ├── NanonisSxmAFM          nanonis/nanonis_sxm_afm.py
    │   └── NanonisDatSTS          nanonis/nanonis_dat_sts.py
    │
    ├── OmicronBase                omicron/omicron_base.py   (empty shell)
    │   └── OmicronSM4STM          omicron/omicron_sm4_stm.py
    │
    └── BrukerBase                 bruker/bruker_base.py     (empty _grp_to_func)
        └── BrukerSpmAFM           bruker/bruker_spm_afm.py
```

`OmicronBase` and `BrukerBase` are intentionally thin today — they exist as extension points so vendor-specific shared logic can be added without touching `SPMformatter`.

---

### Shared Dataclasses

Two dataclass instances are created in `SPMformatter.__init__` and **shared across the entire conversion run**. Hooks write into them; NXdata construction reads from them.

**`NXScanControl`** — stores the physical scan geometry:

| Field | Description |
|---|---|
| `x_points`, `y_points` | Number of scan pixels per axis |
| `x_start`, `y_start` | Start coordinate (physical units) |
| `x_end`, `y_end` | End coordinate (physical units) |
| `x_range`, `y_range` | Scan size |
| `x_offset`, `y_offset` | Scan offset from centre |
| `x_*_unit`, `y_*_unit` | Corresponding unit strings |
| `fast_axis`, `slow_axis` | Direction strings, e.g. `"-y"`, `"x"` |

**`BiasSweep`** — stores bias spectroscopy parameters:

| Field | Description |
|---|---|
| `scan_start_bias`, `scan_end_bias` | Voltage sweep limits |
| `scan_range_bias`, `scan_offset_bias` | Sweep range and offset |
| `scan_points_bias` | Number of bias points |
| `scan_size_bias` | Step size |

**Critical ordering contract:** `scan_control` must be fully populated by `_construct_nxscan_controllers` **before** any NXdata group is built, because NXdata construction calls `np.linspace(scan_control.x_start, scan_control.x_end, x_points)` to generate axis arrays. The `_grp_to_func` hook mechanism guarantees this ordering.

---

### `__init__` Execution Order

```text
Leaf.__init__(template, raw_file, eln_file, config_file)
    └── super().__init__(...)   [SPMformatter]
            ├── self.scan_control = NXScanControl()
            ├── self.bias_sweep   = BiasSweep()
            ├── self.template     = template          (pynxtools Template)
            ├── self.raw_file     = raw_file
            ├── self.eln          = _get_eln_dict(eln_file)
            │       ├── yaml.safe_load
            │       ├── write_multiple_concepts_instance   (expands list concepts)
            │       └── flatten_and_replace(CONVERT_DICT)  (normalises key names)
            ├── self.raw_data     = get_raw_data_dict()
            │       └── SPMParser().get_raw_data_dict(raw_file, eln=self.eln)
            └── self.config_dict  = _get_conf_dict(config_file)   [abstract]
                    ├── user file  → fhs.read_config_file(config_file)
                    └── default    → load_default_config("<name>")
```

`_get_conf_dict` is called **last** so each leaf can decide whether to load its bundled default or the user-supplied override. The raw data is parsed **once** and cached in `self.raw_data` for the entire conversion.

---

### `get_nxformatted_template` — Three-Phase Pattern

Every leaf formatter follows the same three calls:

```python
def get_nxformatted_template(self):
    self.walk_though_config_nested_dict(self.config_dict, "")  # Phase 1
    self._format_template_from_eln()                            # Phase 2
    self._handle_special_fields()                               # Phase 3
```

**Phase 1 — Config-driven walk** fills the template from raw data using the JSON config.
**Phase 2 — ELN override** iterates over all flattened ELN entries and writes them directly into `self.template`. ELN values win over raw-data values for the same NeXus key.
**Phase 3 — Post-processing** fixes timestamps, attaches timezone offsets, and coerces types for known edge cases.

---

### Phase 1: `walk_though_config_nested_dict`

This recursive method is the core engine. It walks the nested JSON config dict and dispatches on the shape of each value:

```text
config value type                              action
────────────────────────────────────────────────────────────────────────────
str starting with "@default_link:"             resolve internal HDF5 link
key matches _grp_to_func                       call registered hook method
dict with "raw_path"                           LEAF — fetch value, write template + /@units + /@attrs
dict with ("title" or "grp_name") + "data"     build full NXdata group
list of dicts (each has one key + end_dict)    VARIADIC FIELDS — embed suffix into N[n] pattern
plain dict                                     recurse, appending key to parent_path
```

#### The `_grp_to_func` Hook Registry

Each leaf formatter declares a class-level dict that maps a config key prefix to a method name:

```python
# NanonisSxmSTM
_grp_to_func = {
    "SPM_SCAN_CONTROL[spm_scan_control]": "_construct_nxscan_controllers",
    "start_time":                          "_set_start_end_time",
    "end_time":                            "_set_start_end_time",
    "BIAS_SWEEP[bias_sweep]":              "_construct_bias_sweep_grp",
}
# NanonisDatSTS
_grp_to_func = {"BIAS_SWEEP[bias_sweep]": "_construct_bias_sweep_grp"}
# BrukerSpmAFM
_grp_to_func = {"SPM_SCAN_CONTROL[spm_scan_control]": "_construct_nxscan_controllers"}
```

When the walker encounters a config key matching a registered entry, it calls `getattr(self, method_name)(val, parent_path, key)` instead of generic recursion. This lets complex groups use hand-written logic while everything else remains config-driven.

#### `_get_data_unit_and_others` — Leaf Value Extraction

Every leaf node resolves to a call to this helper ([helpers.py:135](src/pynxtools_spm/nxformatters/helpers.py#L135)):

```python
data, unit, other_attrs = _get_data_unit_and_others(
    data_dict=self.raw_data,
    end_dict={"raw_path": "/SCAN/RANGE", "@units": "@default:m"}
)
```

Resolution rules for `raw_path`:
- **Single string** → `self.raw_data[path]`
- **List of strings** → tried in order; first non-empty value wins (fallback paths for different software versions)
- **`@default:value`** → the literal string after the prefix is used directly, not looked up in raw data

Resolution rules for `@units`: same three rules as `raw_path`; result is validated through `pint` (`ureg`) before being stored; invalid unit strings are logged and stored as `None`.

Return value: `(data, unit_str, extra_attrs_dict)` where `extra_attrs_dict` holds any additional `@key` entries from the end dict (e.g., `@calibration`, `@offset`).

After this call, the walker writes:
```python
self.template[f"{parent_path}/{key}"]         = to_intended_t(data)
self.template[f"{parent_path}/{key}/@units"]  = unit
self.template[f"{parent_path}/{key}/@<attr>"] = v   # for each extra attr
```

#### `to_intended_t` — Automatic Type Coercion

All raw values pass through `to_intended_t` ([helpers.py:284](src/pynxtools_spm/nxformatters/helpers.py#L284)) before entering the template. It tries conversions in this order:

```text
None        → None
list        → np.ndarray (float64)
np.ndarray  → returned as-is
str         → "off"/"on"          → "false"/"true"
            → infinity strings    → None
            → int() if possible
            → float() if possible
            → JSON array if starts with "["
            → split on ";"        → list → ndarray if all numeric
            → returned as str if nothing else matches
```

Raw strings like `"512"`, `"9.000E-9"`, and `"3.14"` automatically become Python `int` or `float` without any explicit casting in the formatter code.

---

### `_construct_nxscan_controllers` — Scan Geometry Assembly

This hook is the most important method in the formatter layer. It is called when the walker reaches the `SPM_SCAN_CONTROL[spm_scan_control]` group in the config.

**Nanonis (`NanonisSxmSTM`):**
1. Reads `independent_scan_axes` from raw data (scan direction string e.g. `"down"`).
2. Calls `_arange_axes(direction)` → sets `scan_control.fast_axis` and `scan_control.slow_axis` (e.g., `fast_axis="-y"`, `slow_axis="x"` for a downward scan).
3. Calls `construct_scan_region_grp`: extracts scan offsets → `x_offset`/`y_offset`/`x_start`/`y_start`; extracts scan angles → writes `scan_angleN[scan_angle_x/y]`; extracts scan ranges → `x_range`/`y_range`, computes `x_end`/`y_end`; calls `put_scan_2d_region_field_in_template`.
4. Calls `construct_scan_pattern_grp`: splits scan points string → `x_points`/`y_points`; computes step sizes; calls `construct_scan_data_grps` which parses the channel metadata header and creates one NXdata group per channel per direction (forward/backward).

**Bruker (`BrukerSpmAFM`):**
1. Calls `construct_region_region_grp`: reads `X_Offset`/`Y_Offset` → `x_offset`/`y_offset`; reads `X_Position`/`Y_Position` → `x_start = position + offset`; reads `Scan_Size` and applies `Aspect_Ratio` (e.g. `"1:1"`) to compute `x_range` and `y_range` separately; uses `pint` unit conversion (`ureg.Quantity(data, unit).to(x_start_unit)`) before computing `x_end`/`y_end`.
2. Calls `construct_scan_pattern_grp`: reads x/y scan points from separate variadic config entries; computes `step_size_x = x_range / (x_points - 1)` and same for y.

---

### `_nxdata_grp_from_conf_description` — NXdata Group Builder

This method builds a complete NeXus NXdata group from a config sub-dict. It is called for every config node that contains both a `"data"` key and either `"grp_name"` or `"title"`.

**Input config shape:**
```json
{
    "grp_name": "topography_forward",
    "data": {"name": "Topography", "raw_path": "/Z/forward", "@units": "@default:m"},
    "0": {"name": "X", "raw_path": "@default:linspace", "axis_ind": 0},
    "title": {"raw_path": "@default:Topography Forward"}
}
```

**Execution steps (base class):**
1. Builds the variadic group name: `replace_variadic_name_part(group_name, grp_name_to_embed)`.
2. Fetches the signal array via `_get_data_unit_and_others`.
3. If 2D and `rearrange_2d_data=True`, calls `rearrange_data_according_to_axes`.
4. Writes `template["…/DATA[field_nm]"]`, `/@units`, `/@long_name`, `/@signal`.
5. For each integer-keyed entry (`"0"`, `"1"`, …), fetches axis data and writes `AXISNAME[name]`, `/@units`, `/@long_name`, `/@AXISNAME_indices[name_indices]`, `/@axes`.
6. Writes any `@attr`-prefixed group attributes directly to the NXdata group path.

**Leaf overrides:**

`NanonisSxmSTM._nxdata_grp_from_conf_description`: determines `is_forward` from whether `"forward"` appears in `raw_path`; calls `super()` then, if no axis keys (`"0"`, `"1"`) were in the config, auto-generates x and y axes using `np.linspace` from `scan_control` coordinates.

`BrukerSpmAFM._nxdata_grp_from_conf_description`: calls `super()` with `rearrange_2d_data=False` (Bruker arrays are already correctly oriented); writes the `title` field from raw data if available; auto-generates x/y axes from `scan_control` with a shape validation step — if signal array shape does not match expected point counts, regenerates axis arrays to match actual data shape and logs a warning.

---

### Variadic NeXus Names — `replace_variadic_name_part`

NeXus application definitions use uppercase letters to mark variable parts of group/field names. For example, `scan_pointsN[scan_points_n]` means the `N` part should be replaced with an actual suffix at write time.

`replace_variadic_name_part(name, part_to_embed)` ([helpers.py:435](src/pynxtools_spm/nxformatters/helpers.py#L435)) finds the first uppercase run in the name prefix (before `[`) and replaces it with `part_to_embed` in both the class name and the instance name inside the brackets.

Examples:
```text
("scan_pointsN[scan_points_n]",  "x")            → "scan_pointsN[scan_points_x]"
("scan_offset_valueN[scan_offset_value_n]", "y")  → "scan_offset_valueN[scan_offset_value_y]"
("DATA[data]",  "topography_forward")             → "DATA[topography_forward]"
("AXISNAME[axisname]", "bias_voltage")            → "AXISNAME[bias_voltage]"
```

In the config file, variadic fields are a **list of single-key dicts** where the key is the suffix to embed:

```json
"scan_pointsN[scan_points_n]": [
    {"x": {"raw_path": "/SCAN/PIXELS/X"}},
    {"y": {"raw_path": "/SCAN/PIXELS/Y"}}
]
```

---

### Phase 3: `_handle_special_fields` — Post-Processing

Runs over the entire template after it is fully populated.

**Timestamp normalisation:**
- Keys ending in `start_time` or `end_time`: re-parses `DD.MM.YYYY HH:MM:SS` → ISO 8601 via `datetime.strptime(...).isoformat()`.
- All keys matching `(date|time)$`: attaches local timezone offset (e.g., `+02:00`) via `tzlocal.get_localzone()`; timestamps that already carry a timezone suffix (`Z` or `±HH:MM`) are left unchanged.

**Type coercions** (applied via regex matching on template key):

| Key pattern | Coercion |
|---|---|
| `active_channel$` | `str(val)` |
| `model/@version$` | `str(val)` |
| `/model$` | `str(val)` |
| `lockin_amplifier/(demodulated\|modulation)_signal$` | `val.lower()` |
| LockIn filter order fields | empty string if not numeric |

---

### NanonisSxmSTM Borrows from NanonisDatSTS (Monkey-Patching)

`NanonisSxmSTM` needs to build the same `BIAS_SWEEP[bias_sweep]` group as `NanonisDatSTS` when a `.sxm` file contains bias spectroscopy data. Rather than using multiple inheritance, the bias sweep method is **borrowed at runtime**:

```python
def _construct_bias_sweep_grp(self, partial_conf_dict, parent_path, group_name):
    sts_bias_sweep = getattr(NanonisDatSTS, "_construct_bias_sweep_grp")
    NanonisSxmSTM._construct_scan_region_grp_in_bias_spec = (
        lambda self, *a: getattr(NanonisDatSTS, "_construct_scan_region_grp_in_bias_spec")(self, *a)
    )
    NanonisSxmSTM._construct_linear_sweep_grp = (
        lambda self, *a: getattr(NanonisDatSTS, "_construct_linear_sweep_grp")(self, *a)
    )
    sts_bias_sweep(self, partial_conf_dict, parent_path, group_name)
```

No permanent class modification occurs. **Be aware:** if `NanonisDatSTS._construct_bias_sweep_grp` is refactored, the `.sxm` STM bias sweep path is affected too.

---

### ELN Dict Processing — `write_multiple_concepts_instance`

Before the ELN YAML is flattened, repeatable NeXus concepts (`Sample_component`, `User`, `Note`) are expanded. A list under one of these keys:

```yaml
User:
  - name: Yan Wang
    affiliation:
      - Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China
  - name: Cojal González, José David
    affiliation:
      - Department of Physics & IRIS Adlershof, Humboldt-Universität zu Berlin, 12489 Berlin, Germany
    email:
      - cojal@physik.hu-berlin.de
  - name: Rubel Mozumder
    affiliation:
      - FAIRmat, Humboldt-Universität zu Berlin, Berlin
    email:
      - rubel.mozumder@physik.hu-berlin.de
  - name: Prof. Carlos-Andres Palma
    affiliation:
      - Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China
      - Department of Physics & IRIS Adlershof, Humboldt-Universität zu Berlin, 12489 Berlin, Germany
    email:
      - palma@iphy.ac.cn
```

becomes `{"user_1": {...}, "user_2": {...}}` and `CONVERT_DICT` is updated with `{"user_1": "USER[user_1]", "user_2": "USER[user_2]"}`. The result is passed to pynxtools `flatten_and_replace` which converts the nested dict into slash-separated NeXus-style keys.

---

### Adding a New Formatter — Full Checklist

Follow all steps in order. Skipping any step produces either broken output or missing test coverage.

**Step 1 — Parser**
1. Create `src/pynxtools_spm/parsers/<vendor>_<ext>.py` subclassing `SPMBase`.
2. Implement `parse() -> dict[str, Any]` returning flat slash-separated keys.
3. Register the class in `SPMParser.__parser_navigation` in `parsers/__init__.py`.

**Step 2 — Config file**
1. Create `src/pynxtools_spm/configs/<vendor>/<vendor>_<ext>_<technique>.json`.
2. Map raw parser keys (from `parse()` output) to NeXus template paths.
3. Register the config name in `src/pynxtools_spm/configs/__init__.py` (the `load_default_config` lookup table).

**Step 3 — Formatter**
1. Create `src/pynxtools_spm/nxformatters/<vendor>/<vendor>_<ext>_<technique>.py`.
2. Inherit from the appropriate vendor base (`NanonisBase`, `OmicronBase`, `BrukerBase`) or directly from `SPMformatter` for a new vendor.
3. Implement `_get_conf_dict` → `load_default_config("<name>")` or `fhs.read_config_file(config_file)`.
4. Implement `get_nxformatted_template` → call the three-phase pattern (walk → eln → special fields).
5. Implement `_construct_nxscan_controllers` → populate `self.scan_control` completely before returning. Use `pass` only for techniques (like STS) that have no 2D scan.
6. Register `_grp_to_func` for any group that requires hand-written logic.

**Step 4 — Reader dispatch**
1. Add a dispatch branch in `SPMReader.read()` in `reader.py` for the new `(experiment_technique, raw_file_ext)` combination.

**Step 5 — Tests**
1. Create `tests/data/<vendor>/<technique>/<scenario>/` containing the raw file, `eln_data.yaml`, optional `config.json`, and reference `<expected>.nxs`.
2. Add a parametrized entry to the appropriate `test_*_reader` function in `test_reader.py`.
3. Run `pytest -sv tests/` and confirm all tests pass before committing.

---

## Input Files

Every conversion requires **three input files** passed together to `dataconverter` or `SPMReader`:

| File | Extension | Purpose |
|------|-----------|---------|
| Raw data | `.sxm`, `.dat`, `.sm4`, `.spm`, `.txt` | Instrument output |
| ELN metadata | `.yaml` / `.yml` | Experiment description; `experiment_technique` is required |
| Config (optional) | `.json` | Override or extend raw_path → NeXus path mapping |

**Minimal ELN file example:**
```yaml
experiment_technique: STM
/ENTRY[entry]/INSTRUMENT[instrument]/software/vendor: Nanonis
/ENTRY[entry]/INSTRUMENT[instrument]/software/model: Generic 5e
```

Any key prefixed with `/ENTRY[entry]/...` is written directly into the template. `experiment_technique` is the only required key.

---

## Configuration Files (JSON Mapping)

Located in `src/pynxtools_spm/configs/<vendor>/`. Each JSON file maps raw parser keys to NeXus template paths:

```json
{
  "/ENTRY[entry]/INSTRUMENT[instrument]/ENVIRONMENT[environment]/current_sensor/current": {
    "raw_path": "/Bias/Current (A)"
  }
}
```

Special notations:
- `N[n]` in NeXus paths denotes a variadic group (e.g., repeated scan channels).
- `@units` keys hold physical unit strings.
- Users can provide a custom config file at runtime to supplement defaults.

---

## Development Setup

```bash
git clone https://github.com/FAIRmat-NFDI/pynxtools-spm
cd pynxtools-spm
pip install -e ".[dev]"
pre-commit install
```

**Python version requirement:** 3.10 or higher.

---

## Running Tests

```bash
pytest -sv tests/
coverage run -m pytest -sv tests/ && coverage report
pytest -sv tests/test_reader.py
pytest -sv tests/functionality_test.py
```

### Test Structure

Integration tests use `pynxtools.testing.nexus_conversion.ReaderTest` which: (1) converts the test data directory's raw files to a temporary `.nxs` file, (2) compares the output against the reference `.nxs` file committed in the test directory, (3) asserts reproducibility using `check_reproducibility_of_nexus`.

**Each test data directory contains:**
```text
tests/data/<vendor>/<technique>/<scenario>/
├── <raw_file>       # e.g., scan.sxm
├── eln_data.yaml    # ELN metadata
├── config.json      # (optional) custom mapping
└── <expected>.nxs   # reference NeXus output
```

`ignore_sections` in `test_reader.py` exempts time-dependent fields (`start_time`, `end_time`, `calibration_date`) from the reproducibility comparison.

---

## Running the Converter (CLI)

```bash
dataconverter --reader spm --nxdl NXstm scan.sxm eln_data.yaml config.json --output output.nxs
```

**Programmatic usage:**
```python
from pynxtools_spm.reader import SPMReader
from pynxtools.dataconverter.template import Template

filled = SPMReader().read(
    template=Template(),
    file_paths=("scan.sxm", "eln_data.yaml", "config.json"),
)
```

**Inspect raw parsed data (debugging):**
```python
from pynxtools_spm.parsers import SPMParser, write_spm_raw_file_data

data = SPMParser().get_raw_data_dict("scan.sxm")
for k, v in data.items():
    print(f"{k}: {v}")

write_spm_raw_file_data("scan.sxm", output_file="scan_raw.txt")
```

**Bruker TXT parser (standalone):**
```python
from pynxtools_spm.parsers.bruker_txt import TxtBruker
data = TxtBruker("measurement.txt").parse()
```

---

## Code Quality

**Linter:** `ruff` (pycodestyle + pylint rules, configured in `pyproject.toml`)
```bash
ruff check src/ tests/
ruff format src/ tests/
```

**Type checker:** `mypy` (non-strict mode, `ignore_missing_imports = true`)
```bash
mypy src/
```

**Spell checker:** `cspell` via pre-commit (config in `cspell.json` and `.cspell/`)

**Pre-commit** enforces ruff, mypy, pyupgrade, nbstripout, and cspell on every commit. Run manually: `pre-commit run --all-files`

**Ruff ignored rules** (do not re-enable without discussion): `E501` (line length), `PLR0912` (too many branches), `PLR0913` (too many arguments), `PLC0415` (import outside top-level — used intentionally in `reader.py` for lazy imports).

---

## CI/CD Pipelines (`.github/workflows/`)

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `pytest.yml` | push/PR to main | Run tests on Python 3.10–3.13 |
| `publish.yml` | GitHub release | Build and publish to PyPI |
| `pylint.yml` | push/PR | Linting checks |
| `spellcheck.yaml` | push/PR | cspell spell checking |
| `mkdocs-deploy.yml` | push to main | Deploy docs to GitHub Pages |
| `compatibility_with_pynxtools_release.yml` | scheduled | Test against pynxtools releases |

Tests install `pynxtools` from the `master` branch (not a pinned release), so the plugin must remain compatible with the upstream development version.

---

## Key Dependencies

| Package | Version | Role |
|---------|---------|------|
| `pynxtools` | ≥0.14.0 | Core NeXus conversion framework + `BaseReader`, `Template` |
| `pySPM` | ==0.6.3 | Low-level Bruker `.spm` file reading (pinned — API is unstable) |
| `spym` | ≥0.9.2 | Omicron `.sm4` file reading |
| `findiff` | ≥0.11.1 | Numerical derivatives for scan data processing |
| `pint` | (transitive) | Physical unit parsing and conversion |
| `nomad-lab` | ≥0.4.1 | NOMAD platform integration for example uploads and apps |
| `tzlocal` | any | Local timezone detection for timestamp fields |

`pySPM` is **pinned to 0.6.3** because its API changed between versions. Do not upgrade without testing all Bruker parsing paths.

---

## NOMAD Integration

Entry points are defined in `pyproject.toml` under `[project.entry-points."nomad.plugin"]`:

| Entry point | Module | Purpose |
|-------------|--------|---------|
| `sts_example` | `nomad/entrypoints.py` | STS example upload for NOMAD |
| `stm_example` | `nomad/entrypoints.py` | STM example upload for NOMAD |
| `afm_example` | `nomad/entrypoints.py` | AFM example upload for NOMAD |
| `spm_app` | `nomad/apps/__init__.py` | SPM application in NOMAD UI |

Example data for NOMAD uploads lives in `src/pynxtools_spm/nomad/example_uploads/`.

---

## Documentation

Built with **MkDocs + Material theme**.

```bash
pip install -e ".[docs]"
mkdocs serve    # local preview at http://127.0.0.1:8000
mkdocs build    # build static site into site/
```

Key documentation pages (under `docs/`):
- `explanation/reader-orchestra.md` — overview of all supported techniques and vendors
- `explanation/reader-structure.md` — modular parser/formatter/config design
- `how-to-guides/work-with-reader.md` — ELN and config file usage
- `how-to-guides/how-to-extend-readers.md` — guide for adding new readers
- `reference/` — standalone usage examples and NeXus definition references

---

## Common Pitfalls

- **Missing `experiment_technique` in ELN:** `SPMReader.read()` raises `ValueError` immediately — this field is mandatory.
- **Bruker `.spm` version mismatch:** `SPMParser.__parser_navigation` only registers version `"9.64"` for Bruker. Files from other versions fall through to a brute-force attempt; add new versions to the navigation dict as needed.
- **`pySPM` version:** Locked at `==0.6.3`. A version change will break Bruker parsing silently if the API changes.
- **Variadic NeXus groups:** Config keys with `N[n]` require `replace_variadic_name_part`. Omitting it causes template key mismatches.
- **Type coercion:** If a new field has persistent type issues, add it to `nexus_key_to_dt` in `manually_filter_data_type` (`reader.py`) rather than patching the parser or formatter.
- **Time fields excluded from tests:** `start_time`, `end_time`, and `calibration_date` are excluded from reproducibility checks because they embed the current timestamp. Do not add `now()`-based values to other fields without also updating `ignore_sections` in `test_reader.py`.
