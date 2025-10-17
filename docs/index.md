---
hide: toc
---

# Documentation for pynxtools-spm

## **Motivation for pynxtools-spm**
Data from __Scanning Probe Microscopy (SPM)__ techniques such as __Scanning Tunneling Microscopy (STM)__, __Scanning Tunneling Spectroscopy (STS)__, and __Atomic Force Microscopy (AFM)__ are widely produced and analyzed in condensed matter physics and surface science. However, the data formats rendered by different SPM lab instruments often follow proprietary data models and are incompatible with each other. To improve this non interoperable situation, FAIRmat has developed NeXus application definitions [NXspm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html), [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html), and [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html). Using these NeXus application definitions, `pynxtools-spm` provides a standardized way to convert raw data from various STM/STS/AFM experiments into the NeXus format according to the application definitions, making the data accessible for everyone regardless of the providing instruments and softwares used to acquire the data from experiments. The data can be stored and shared in research data management platforms, e.g., [NOMAD](https://nomad-lab.eu/nomad-lab/).

`pynxtools-spm` provides a unified data processing workflow for converting SPM data into the NeXus format. As a reader plugin of [`pynxtools`](https://github.com/FAIRmat-NFDI/pynxtools) (see [documentation](https://fairmat-nfdi.github.io/pynxtools/index.html)) `pynxtools-spm` takes advantage of the [dataconverter](https://fairmat-nfdi.github.io/pynxtools/learn/pynxtools/dataconverter-and-readers.html) framework. The framework provides a `Template` (a key-value paired hash map where key is defined according to the NeXus application definitions) to store curated data, a template validator for templated data according to the application definition, and a writer to write the curated data in a NeXus file. `pynxtools-spm` package embraces Python modular structure for parsers that read raw data and formatters that curate the data following corresponding application definition (see [Reader Structure](explanation/reader-structure.md)).

<div markdown="block" class="home-grid">
<div markdown="block">

### Tutorial
- [Installation](tutorials/installation.md)
- [Use Reader in NOMAD](tutorials/use-reader-in-nomad.md)

</div>
<!--
     1. Run Reader in north tools
 -->
<div markdown="block">

### How-To Guides

- [Work with Reader](how-to-guides/work-with-reader.md)
- [Extend Readers' Orchestra](how-to-guides/how-to-extend-readers.md)

</div>
<div markdown="block">

### Explanation
- [Reader Structure](explanation/reader-structure.md)
- [Reader Orchestra](explanation/reader-orchestra.md)

</div>
<div markdown="block">

### Reference

- [Use Reader from Command Line](reference/standalone-usages.md)
- Define [NOMAD](https://nomad-lab.eu/nomad-lab/) [ELN schema](https://nomad-lab.eu/prod/v1/staging/docs/howto/customization/elns.html#schemas-for-elns)
- [NOMAD Glossary](https://nomad-lab.eu/prod/v1/staging/docs/reference/glossary.html)
- [NeXus Format](https://www.nexusformat.org/)
- [NeXus application definition in Reader](reference/reference.md#nexus)
- [NeXus-FAIRmat](https://fairmat-nfdi.github.io/nexus_definitions/index.html)
- [nanonispy for reading Nanonis files (e.g., `.sxm`)](https://github.com/underchemist/nanonispy)
- [spym for reading Omicron files (e.g., `.sm4`)](https://github.com/rescipy-project/spym)
- [Scanning Probe Microscopy (SPM) Application Definitions](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/spm-structure.html#spm-structure)

</div>
</div>

## Project and Community

The `pynxtools-spm` reader is part of the project [FAIRmat](https://www.fairmat-nfdi.eu/fairmat), a FAIR data infrastructure for condensed-matter physics and the chemical physics of solids.

- [FAIRmat project](https://gepris.dfg.de/gepris/projekt/460197019?language=en), which is funded by [NFDI](https://www.nfdi.de/)
- Reach reader developers via [GitHub issue tracker](https://github.com/FAIRmat-NFDI/pynxtools-spm/issues)
- Reach pynxtools developers via [GitHub issue tracker](https://github.com/FAIRmat-NFDI/pynxtools/issues)

- Reach the NeXus-FAIRmat community via the [webpage](https://fairmat-nfdi.github.io/nexus_definitions/).