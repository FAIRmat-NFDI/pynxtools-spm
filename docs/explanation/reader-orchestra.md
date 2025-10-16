# Scanning Probe Microscopy (SPM)

Scanning Probe Microscopy (SPM) is a high resolution imaging technique used to study material surface at nano scale. The technique can take on a wide range form of experiments categorized by operating environment (e.g., ambient, vacuum) and setup, type of interaction between prob and specimen, number of probe and actuation modes, etc. Therefore, there are many sub-techniques, like STM (Scanning Tunneling Microscopy), AFM (Atomic Force Microscopy), STS (Scanning Probe Spectroscopy). These complex experiments require complex setup of instruments provided by different technology companies which turns out diverse data model (mostly unstructured) and data format. How can we compare the diverged data model and data format? Can we interpret the data in a common data model and format accessible to all SPM community? Does the proposed data model follow FAIR data principle?

We have developed community driven standard application definition, using [NeXus](https://www.nexusformat.org/) data format, for [SPM](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html) subdomains e.g., [STM](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), [STS](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html), [AFM](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html) and a few base classes to describe instrument components (e.g. [Lock-in](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXlockin.html#nxlockin), [Cantilever](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm_cantilever.html#nxspm-cantilever)). Based on our data model, we build the data workflow that connects the data from experiment generated raw files to the standard application definition inscribed in a HDF5 file (as we are using NeXus data format in HDF5 file, later on we also call it NeXus file with '.nxs' extension).
TODO: mention one can use `NXspm` for any sub technique do not warranty the validation of the parsed data.

## __SPM Readers__
The SPM reader is plugin of material science reader framework [pynxtools](https://github.com/FAIRmat-NFDI/pynxtools) and anchors a bundle of readers from STM, STS and AFM. The readers follow a [common structure](../reader_structure.md) that shall allow to extend reader orchestra by including new readers of different SPM sub-technique (e.g. SPSTM). For each type of techniques (e.g., STM, STS, and AFM), there might be multiple instruments vendors (e.g., Nanonis, Omicron) and each vendor favors different data format and data model. Therefore, each reader is designed to be modular and configurable to adapt different data format and data model. These allows to integrate more and more data format and data model from different vendors without changing the reader structure.

The prime purpose of the readers is to transform data from measurement files into NeXus file according to the SPM community supported schema (NeXus applications and base classes) which allows experimentalists to store, organize, search, analyze, and share experimental data in NOMAD (if plugin `pynxtools-spm` is integrated with [NOMAD](https://nomad-lab.eu/nomad-lab/)) research data management (RDM) platform. 

To understand the reader structure, one might start understanding the design pattern of the application definitions [NXspm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html), [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), [NXsts]https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), and [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html) on the [FAIRmat NeXus Proposal](https://fairmat-nfdi.github.io/nexus_definitions/) page or in the [GitHub repository].

### __Reader Members of `pynxtools-spm` reader orchestra__
`pynxtools-spm` includes three readers:

- STS reader
- STM reader
- AFM reader

The `section`, `sub_sections`, and `quantities` refer to the root level entity (behaves like a `group`), `group`, and `field` of the NeXus definition, respectively. The given schema ELN can be read as follows, `stm` ELN has direct fields `attribute`, `definition` and direct groups `Instrument`, `Sample`, with each group optionally containing nested `group`s and `field`s.

This type of ELN needs to be used if the reader is run from the command line. To know which fields and groups refer to which type of data, one needs to read the NeXus definition on the [FAIRmat NeXus Proposal](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html#nxsts) page or in the [GitHub repository](https://github.com/FAIRmat-NFDI/nexus_definitions/blob/fairmat/contributed_definitions/NXsts.nxdl.xml).


#### __STS reader__

The `STS` reader builds on the [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html) application definition and needs an experimental file, a config file and a eln (eln stands for electronic lab notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html) according to the application concepts.

#### __STM Reader__
The STM reader is a part of `pynxtools-spm` package and builds on the [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html) application definition and needs an experimental file, a config file and a eln (eln stands for electronic lab notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file according to the [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html) application concepts.

#### __AFM Reader__
The AFM reader is a part of `pynxtools-spm` package and builds on the [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html) application definition and needs an experimental file, a config file and a eln (eln stands for electronic lab notebook) file to transform the experiment generated data (from raw files) and user provided data (from ELN) into NeXus file according to the [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html) application concepts.

!!! Warning 
  The config file is a map from the data model of raw file to the data model inscribed in corresponding application definition, which infers raw files from different software version or different vendor require different config files. Most likely, the path is path to the raw data file needs to be updated in the config file. 

### __Supported Vendor files and Formats__
Readers support the following vendor files and formats.

- __STS__
    - Nanonis `STS` files
        - Extension: `.dat`
- __STM__
    - Nanonis `STM` files
        - Extension: `.sxm`
    - Omicron `STM` files
        - Extension: `.sm4`
- __AFM__
    - Nanonis `AFM` files
        - Extension: `.sxm`

### __Input files__
The readers mainly need three input files to transform the data into the `NXsts`, `NXstm`, and `NXafm` application definitions for `STS`, `STM`, and `AFM` techniques, respectively. The three input files are - 

#### __Experimental file__ 
The experimental file is the raw data file generated by the instrument software e.g., (`.dat` for Nanonis `STS` files).

#### __Config file__ 
The config file is a `json` file which maps between the data model (unstructured data) of the raw data file and the data model inscribed in the (e.g., `NXsts`) application definition. Note that, as a intermediate step the corresponding parser generates a data object (e.g., Python dictionary) developing slash separated string key mapping to the value. In the config file, the key string path is used as a path referring the data in raw file. To know how to read this config file and modify it, please follow `Config File` in  [Work with Reader](../how-to-guides/how-to-use-the-reader.md) guide.


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

#### __ELN Schema file__ 
The ELN schema file is a `yaml` file which describes the metadata of the experiment. To know how to read this ELN schema file and modify it, please follow section `ELN Schema File` [Work with Reader](../how-to-guides/how-to-use-the-reader.md) guide. This file only usable in [NOMAD](https://nomad-lab.eu/nomad-lab/) RDM system.

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
The ELN YAML file is a human created ELN and can be used to run reader in Jupyter notebook or local Python environment. For more details please follow the section `ELN YAML File` in [Work with Reader](../how-to-guides/how-to-use-the-reader.md) guide.

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
=== "Eln YAML File (AFM)"
    <div class="scrollable">
    ```yaml
    --8<-- "included_file_content/afm/eln_data.yaml"
    ```
    </div>