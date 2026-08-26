# Scanning Probe Microscopy (SPM)

Scanning Probe Microscopy (SPM) is a high resolution imaging technique used to study material surface at nano scale. The technique can take on a wide range form of experiments categorized by operating environment (e.g., ambient, vacuum) and setup, type of interaction between prob and specimen, number of probe and actuation modes, etc. Therefore, there are many sub-techniques, like STM (Scanning Tunneling Microscopy), AFM (Atomic Force Microscopy), STS (Scanning Probe Spectroscopy). These complex experiments require complex setup of instruments provided by different technology companies which turns out diverse data model (mostly unstructured) and data format. How can we compare the diverged data model and data format? Can we interpret the data in a common data model and format accessible to all SPM community? Does the proposed data model follow FAIR data principle?

We have developed community driven standard application definition, using [NeXus](https://www.nexusformat.org/) data format, for [SPM](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html) subdomains e.g., [STM](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), [STS](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html), [AFM](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html) and a few base classes to describe instrument components (e.g. [Lock-in](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXlockin.html#nxlockin), [Cantilever](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm_cantilever.html#nxspm-cantilever)). Based on our data model, we build the data workflow that connects the data from experiment generated raw files to the standard application definition inscribed in a HDF5 file (as we are using NeXus data format in HDF5 file, later on we also call it NeXus file with '.nxs' extension).

!!! note
    One can use the supper application definition [NXspm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html) for any sub technique, but do not warranty the validation of the NeXus data file.

## __SPM Readers__
The SPM reader is plugin of material science reader framework [pynxtools](https://github.com/FAIRmat-NFDI/pynxtools) and anchors a bundle of readers from STM, STS and AFM. The readers follow a [common structure](./reader-structure.md) that shall allow to extend the reader orchestra by including new readers for different SPM sub-techniques such as spin-polarized STM. For each type of techniques (e.g., STM, STS, and AFM), there might be multiple instruments providers (e.g., Nanonis, Omicron, Bruker) and each vendor favors different data format and data model. Therefore, each reader is designed to be modular and configurable to work with different data formats and data models.

The prime purpose of the readers is to transform data from measurement files into NeXus file according to the SPM community supported schema (NeXus applications and base classes) which allows experimentalists to store, organize, search, analyze, and share experimental data in NOMAD (if plugin `pynxtools-spm` is integrated with [NOMAD](https://nomad-lab.eu/nomad-lab/)) research data management (RDM) platform. 

To understand the reader structure, one might start understanding the design pattern of the application definitions [NXspm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html), [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), and [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html) on the [FAIRmat NeXus Proposal](https://fairmat-nfdi.github.io/nexus_definitions/) page or in the [GitHub repository](https://github.com/FAIRmat-NFDI/nexus_definitions).

### __Members of `pynxtools-spm` Reader Orchestra__
`pynxtools-spm` includes three readers:

- STS reader
- STM reader
- AFM reader

#### __STS reader__

The `STS` reader builds on the [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html) application definition and needs an experimental file, a config file and a ELN (ELN stands for Electronic Lab Notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file according to the [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html) application concepts.

#### __STM Reader__
The `STM` reader is a part of `pynxtools-spm` package and builds on the [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html) application definition and needs an experimental file, a config file and a ELN (ELN stands for Electronic Lab Notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file according to the [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html) application concepts.

#### __AFM Reader__
The `AFM` reader is also part of `pynxtools-spm` package and builds on the [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html) application definition and needs an experimental file, a config file and a ELN (ELN stands for Electronic Lab Notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file according to the [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html) application concepts.

!!! Warning 
    The configuration file maps the NeXus data model corresponding application definition to the data model from raw file. This implies that raw files from different software versions or vendors require different configuration files. It is most likely that the path referring to the raw data in a input file needs to be updated in the configuration file for different type of instruments.

### __Supported Vendor Files and Formats__
Readers support the following vendor files and formats. The version column refers to the version of the instrument software (or of the file format written by it) that the readers have been tested with; files written by neighboring versions usually work as well, but may need an adapted config file (see the warning above).

| Technique | Vendor | Instrument software (flavor) | Tested version | Extension |
| --- | --- | --- | --- | --- |
| `STS` | [Nanonis](../reference/nanonis.md) | Nanonis SPM control software | Generic 5, Generic 5e | `.dat` |
| `STM` | [Nanonis](../reference/nanonis.md) | Nanonis SPM control software | Generic 5, Generic 5e | `.sxm` |
| `STM` | [Omicron](../reference/omicron.md) | SM4 (read with [spym](https://github.com/rescipy-project/spym)) | not version specific | `.sm4` |
| `AFM` | [Nanonis](../reference/nanonis.md) | Nanonis SPM control software | Generic 4 | `.sxm` |
| `AFM` | [Bruker](../reference/bruker.md) | Bruker `SPMLab` (read with [gwyddionpy](https://pypi.org/project/gwyddionpy/)) | `1.00` | `.flt`, written by the instrument as `.FLT` |
| `AFM` | [Bruker](../reference/bruker.md) | Bruker `NanoScope` (read with [gwyddionpy](https://pypi.org/project/gwyddionpy/)) | `9.x` (Dimension Icon) | `.spm` |
| `AFM (force curve)` | [Bruker](../reference/bruker.md) | Bruker `NanoScope` ASCII export | `9.x` (Dimension Icon) | `.spm.txt` |

Each vendor has its own reference page with the supported formats, the default config file, and a runnable conversion command: [Nanonis](../reference/nanonis.md), [Omicron](../reference/omicron.md), and [Bruker](../reference/bruker.md).

The version of a Bruker FLT file is stated in the `[Data Version]` section at the beginning of the file header (`Program=SPMLab` and `Version=1.00`), while the Nanonis generic version denotes the generation of the Nanonis control software, not the `:NANONIS_VERSION:` entry of the file header. The reader compares file extensions case-insensitively, so both `.flt` and `.FLT` are accepted.

The version of a Bruker `NanoScope` file is stated by the `\Version` key at the top of the ASCII header of both `.spm` and `.spm.txt` (`\Version: 0x09400105` in the reference files, i.e. NanoScope 9.x). Note that the two NanoScope formats are not two spellings of the same content: `.spm` is the native binary file of a raster __image__, whereas `.spm.txt` is the ASCII export of a __force ramp__ (force-distance curve) and therefore describes a point measurement rather than a scanned area.

!!! note "One FLT file holds one channel"
    A Bruker `SPMLab` FLT file stores a __single__ channel of a __single__ scan direction, e.g. `B3320_13_061726074638.SIG_TOPO_FRW.FLT` holds the forward (`FRW`) height (`SIG_TOPO`) image, while the backward scan (`BKW`) and the further channels (e.g. `SIG_USER2`) are written as separate files. Therefore one FLT file is converted into one NeXus file, and the channel name of the file (`DataName` in the header, e.g. `Height`) determines the name of the resulting `NXdata` group.

    The FLT header is INI style text, and the image data that follows it is binary. `pynxtools-spm` reads it via the [gwyddionpy](https://pypi.org/project/gwyddionpy/) package (the `spmlabf` importer of [Gwyddion](http://gwyddion.net/)).

!!! note "One `.spm` file holds many channels"
    A Bruker `NanoScope` `.spm` file behaves the other way around: it stores __every__ recorded channel in __both__ scan directions. The parser exposes them as `/<Channel>/forward` and `/<Channel>/backward` (e.g. `/Height_Sensor/forward`, `/Phase/backward`) and lists the available combinations under `/Scan_list`, so one `.spm` file is converted into one NeXus file that contains several `NXdata` groups.

    The `.spm` header is ASCII (the `\Key: value` lines up to `\*File list end`) and the image block that follows it is binary. `pynxtools-spm` reads it via the [gwyddionpy](https://pypi.org/project/gwyddionpy/) package (the `nanoscope` importer of [Gwyddion](http://gwyddion.net/)), the same package it uses for the `.flt` format.

!!! note "A `.spm.txt` file holds one force curve"
    The NanoScope ASCII export stores the extend (`_Ex`) and retract (`_Rt`) halves of a single force ramp as tab-separated columns behind a quoted `"\Key: value"` header. It needs no external reader, and it is curated into a `point_force_scan` group instead of the `mesh_scan` group used for images.

### __Input files__
The readers mainly need three input files to transform the data into the `NXsts`, `NXstm`, and `NXafm` application definitions for `STS`, `STM`, and `AFM` techniques, respectively. The three input files are - 

#### __Experimental file__ 
The experimental file is the raw data file generated by the instrument software e.g., (file with `.dat` extension for Nanonis `STS` files).

=== "A Nanonis STS Raw Data File (excerpt)"
    <div class="scrollable">
    ```text
    --8<-- "included_file_content/sts/Bias-Spectroscopy00015_20230420.dat"
    ```
    </div>

#### __Config file__ 
The config file is a `json` file which maps between the data model (unstructured data) of the raw data file and the data model inscribed in the application definition (e.g., `NXsts`). Note that, as a intermediate step the corresponding parser (see [Reader Structure](../how-to-guides/work-with-reader.md)) generates key-value pair data object (e.g., Python dictionary) from raw data file. The data object organizes raw data path by a forward slash separated string key mapping to the value (e.g., `'/Experiment/value': 'bias spectroscopy'`). To know how to read this config file and modify it, please follow `Config File` in  [Work with Reader](../how-to-guides/work-with-reader.md) guide.


=== "Config File Nanonis (STS)"
    <div class="scrollable">
    ```json
    --8<-- "included_file_content/sts/config.json"
    ```
    </div>
=== "Config File Nanonis (STM)"
    <div class="scrollable">
    ```json
    --8<-- "included_file_content/stm/config.json"
    ```
    </div>
=== "Config File Nanonis (AFM)"
    <div class="scrollable">
    ```json
    --8<-- "included_file_content/afm/config.json"
    ```
    </div>
=== "Config File Bruker (AFM, SPMLab .flt)"
    <div class="scrollable">
    ```json
    --8<-- "included_file_content/bruker_afm/config.json"
    ```
    </div>
=== "Config File Bruker (AFM, NanoScope .spm)"
    <div class="scrollable">
    ```json
    --8<-- "included_file_content/bruker_spm_afm/config.json"
    ```
    </div>
=== "Config File Bruker (AFM force curve, .spm.txt)"
    <div class="scrollable">
    ```json
    --8<-- "included_file_content/bruker_txt_afm/config.json"
    ```
    </div>

#### __ELN Schema file__ 
The ELN schema file is a `yaml` file which describes the metadata of the experiment. To know how to read this ELN schema file and modify it, please follow the section `ELN Schema File` in the [How to work with readers](../how-to-guides/how-to-use-the-reader.md) guide. This file is only usable within the [NOMAD](https://nomad-lab.eu/nomad-lab/) RDM system.

=== "ELN Schema file (STS)"
    <div class="scrollable">
    ```yaml
    ---8<-- "included_file_content/sts/sts.scheme.archive.yaml"
    ```
    </div>
=== "ELN Schema File (STM)"
    <div class="scrollable">
    ```yaml
    ---8<-- "included_file_content/stm/stm.scheme.archive.yaml"
    ```
    </div>
=== "ELN Schema File (AFM)"
    <div class="scrollable">
    ```yaml
    ---8<-- "included_file_content/afm/afm.scheme.archive.yaml"
    ```
    </div>

#### __ELN YAML File__ 
The ELN YAML file is a human created ELN and can be used to run reader in Jupyter notebook or local Python environment. For more details please follow the section `ELN YAML File` in [Work with Reader](../how-to-guides/work-with-reader.md) guide.

=== "Eln YAML File (STS)"
    <div class="scrollable">
    ```yaml
    --8<-- "included_file_content/sts/eln_data.yaml"
    ```
    </div>
=== "Eln YAML File (STM)"
    <div class="scrollable">
    ```yaml
    --8<-- "included_file_content/stm/eln_data.yaml"
    ```
    </div>
=== "Eln YAML File (AFM, Nanonis)"
    <div class="scrollable">
    ```yaml
    --8<-- "included_file_content/afm/eln_data.yaml"
    ```
    </div>
=== "Eln YAML File (AFM, Bruker SPMLab .flt)"
    <div class="scrollable">
    ```yaml
    --8<-- "included_file_content/bruker_afm/eln_data.yaml"
    ```
    </div>
=== "Eln YAML File (AFM, Bruker NanoScope .spm)"
    <div class="scrollable">
    ```yaml
    --8<-- "included_file_content/bruker_spm_afm/eln_data.yaml"
    ```
    </div>
=== "Eln YAML File (AFM force curve, Bruker .spm.txt)"
    <div class="scrollable">
    ```yaml
    --8<-- "included_file_content/bruker_txt_afm/eln_data.yaml"
    ```
    </div>
