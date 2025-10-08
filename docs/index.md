---
hide: toc
---

<!-- A single sentence that says what the product is, succinct and memorable -->
<!-- A paragraph of one to three short sentences, that describe what the product does. -->
<!-- A third paragraph of similar length, this time explaining what need the product meets -->
<!-- Finally, a paragraph that describes whom the product is useful for. -->

# Documentation for pynxtools-spm

## **Motivation for pynxtools-spm**

Data from __Scanning Probe Microscopy (SPM)__ techniques such as __Scanning Tunneling Microscopy (STM)__, __Scanning Tunneling Spectroscopy (STS)__, and __Atomic Force Microscopy (AFM)__ are widely produced and analyzed in condensed matter physics and surface science. However, the data formats rendered by different SPM vendor instruments often follow proprietary data models and are incompatible with each other, making it difficult to share and analyze data across different labs using different vendor instrument setups. To address this issue, the NeXus-FAIRmat community has developed NeXus application definitions for [NXspm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html), [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html), and [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html). Based on these application definitions, the `pynxtools-spm` reader provides a standardized way to convert raw data from various STM/STS/AFM experiments into the NeXus format according to the application definitions, making the data accessible for everyone regardless of the providing instruments and softwares used to acquire the data from experiments. The data can be stored and shared in research data management platforms, e.g., [NOMAD](https://nomad-lab.eu/nomad-lab/).

`pynxtools-spm`, a Python package, provides a unified interface for storing the SPM data in the NeXus format. The package is built on top of the [`pynxtools`](https://github.com/FAIRmat-NFDI/pynxtools) (see [documentation](https://fairmat-nfdi.github.io/pynxtools/index.html)) [dataconverter](https://github.com/FAIRmat-NFDI/pynxtools/tree/master/src/pynxtools/dataconverter) framework that provides template to store curated data from reader, validator to data according to the application definition and writer to write the data in a NeXus file. In this package, `pynxtools-spm` has taken full benifit from the `pynxtools` converter. `pynxtools-spm` package includes modules of parsers for reading data from diverse SPM experiment raw files, e.g., Nanonis and Omicron instruments, and converting the data into the NeXus format satisfying the NeXus application definitions for SPM techniques.

<div markdown="block" class="home-grid">
<div markdown="block">

### Tutorial
- [Installation](tutorials/installation.md)
- [Use Reader in NOMAD](tutorials/reader-use-in-nomad.md)
- [Use Reader from Command Line](reference/transfer-raw-data.md)

</div>
<!--
     1. Run Reader in north tools
 -->
<div markdown="block">

### How-To Guide

- [Work with Reader](how-to-guides/how-to-interact-with-reader.md)
- [Extend Readers Orchestra](how-to-guides/how-to-extend-readers.md)

</div>
<div markdown="block">

### Learn
<!-- 
    1. Useful Functions
-->

- [Scanning Probe Microscopy (SPM) Application Definitions](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/spm-structure.html#spm-structure)
- [NeXus-FAIRmat](https://fairmat-nfdi.github.io/nexus_definitions/index.html)

</div>
<div markdown="block">

### Reference

<!-- 1. List of files supported by the Reader follow XPS -->

- Define [NOMAD](https://nomad-lab.eu/nomad-lab/) [ELN schema](https://nomad-lab.eu/prod/v1/staging/docs/howto/customization/elns.html#schemas-for-elns)
- [NOMAD Glossary](https://nomad-lab.eu/prod/v1/staging/docs/reference/glossary.html)
- [NeXus Format](https://www.nexusformat.org/)
- [Reader in NOMAD](reference/reference.md#nomad)
- [NeXus application definition in Reader](reference/reference.md#nexus)
- [NeXus-FAIRmat](https://fairmat-nfdi.github.io/nexus_definitions/index.html)
- [nanonispy for reading Nanonis files](https://github.com/underchemist/nanonispy)
- [spym for reading Omicron files (e.g., `.sm4`)](https://github.com/underchemist/spym)

</div>
</div>

## Project and Community

The reader is part of the project [FAIRmat](https://www.fairmat-nfdi.eu/fairmat), a FAIR data infrastructure for condensed-matter physics and the chemical physics of solids.

- [FAIRmat project](https://gepris.dfg.de/gepris/projekt/460197019?language=en), which is funded by [NFDI](https://www.nfdi.de/)
- Reach reader developers via [GitHub issue tracker](https://github.com/FAIRmat-NFDI/pynxtools-spm/issues)
- Reach pynxtools developers via [GitHub issue tracker](https://github.com/FAIRmat-NFDI/pynxtools/issues)

- Reach the NeXus-FAIRmat community via the [webpage](https://fairmat-nfdi.github.io/nexus_definitions/) or the [GitHub issue tracker](https://fairmat-nfdi.github.io/nexus_definitions/)
