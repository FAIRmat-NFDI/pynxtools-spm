---
hide: toc
---

<!-- A single sentence that says what the product is, succinctly and memorably -->
<!-- A paragraph of one to three short sentences, that describe what the product does. -->
<!-- A third paragraph of similar length, this time explaining what need the product meets -->
<!-- Finally, a paragraph that describes whom the product is useful for. -->

# Documentation for pynxtools-spm

!!! danger "Work in progress"
`pynxtools-spm`-serving standard converter STM, STS and AFM techniques according the NeXus datamodel-is a plugin of `pynxtools` dataconverter framework.

## **Motivation for pynxtools-spm**

Data from Scanning Probe Microscopy (SPM) techinques such as Scanning Tunneling Microscopy (STM), Scanning Tunneling Spectroscopy (STS), and Atomic Force Microscopy (AFM) are widely used in condensed matter physics and surface science. However, the data formats used by different SPM instruments are often proprietary and incompatible with each other, making it difficult to share and analyze data across different platforms. To address this issue, the NeXus-FAIRmat community has developed NeXus application definition for [NXspm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXspm.html), [NXstm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXstm.html), [NXsts](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXsts.html) and [NXafm](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXafm.html) and based on the application defintions `pynxtools-spm` reader provides a standardized way to store and share SPM data. The `pynxtools-spm` is designed to convert raw data from various SPM instruments into the NeXus format accoding to the application definitions, making the data accessible for everyone disregarding the instrument and software used to acquire the data.

`pynxtools-spm` is a Python package that provides a unified interface for working with SPM data in the NeXus format. It is built on top of the `pynxtools` dataconverter framework and leverages its capabilities to read and write NeXus files. The package includes modules for reading data from various SPM instruments, including Nanonis and Omicron, and converting it into the NeXus format according to the NeXus application definitions for SPM techniques.

<div markdown="block" class="home-grid">
  <div markdown="block">

### Tutorial

<!-- 1. [Installation](tutorial/installation.md)
         1. With Command Line Interface (CLI) to convert data into NeXus format
     2. Discover the Reader functionality in Nomad
         1. Upload data in Nomad using drag and drop
         2. Upload data in Nomad using yaml ELN file
 -->

- [Installation](tutorials/installation.md)
- [Reader Use in Nomad](tutorials/reader-use-in-nomad.md)

</div>
<div markdown="block">

### How-To-Guide

<!--3. Extend the reader functionality or Add new reader for other file formats
      1. Add new file format
      2. Extend existing file format
      3. Test your changes
      4. Contribute your changes
    4. Extend the application definition

-->

- [How to Use Reader](how-to-guides/how-to-interact-with-reader.md)

</div>
<div markdown="block">

### Learn

<!-- 1. Reader architecture
     2. Reader interface and its components
          1. ELN file
          2. Config file of Reader
     2. Code principle
     3. Explanation of important concepts
         1. Explanation
         2. Supported File Formats and File Versions
         3. NeXus Application Definition
         4. Introduction to Reader Input Files
         5. Useful Functions
     4. Application definition design
-->

- [Explanation](explanation/reader-explanation.md)
- [Supported File Formats and File Versions](explanation/reader-explanation.md#supported-file-formats-and-file-versions)
- [NeXus Application Definition](explanation/reader-explanation.md#nexus-application-definition)
- [Introduction to Reader Input Files](explanation/reader-explanation.md#introduction-to-reader-input-files)
- [Useful Functions](explanation/reader-explanation.md#useful-functions)
</div>
<div markdown="block">

### Reference

<!-- 1. List of files supported by the Reader follow XPS -->

- [Reader in Nomad](reference/reference.md#nomad)
- [NeXus application definition in Reader](reference/reference.md#nexus)

</div>
</div>

## Project and Community

The reader is the part of project [FAIRmat](https://www.fairmat-nfdi.eu/fairmat) a FAIR data infrastructure for condensed-matter physics and the chemical physics of solids.

- [FAIRmat project](https://gepris.dfg.de/gepris/projekt/460197019?language=en) which is funded by [NFDI](https://www.nfdi.de/)
- Reach NOMAD via [MATSCI community discourse](https://matsci.org/c/nomad/32)
- Reach reader developers via [GitHub issue tracker](https://github.com/FAIRmat-NFDI/pynxtools-spm/issues)
- Reach pynxtools developers via [GitHub issue tracker](https://github.com/FAIRmat-NFDI/pynxtools/issues)

- Reach the NeXus-FAIRmat community via the [webpage](https://fairmat-nfdi.github.io/nexus_definitions/) or the [GitHub issue tracker](https://fairmat-nfdi.github.io/nexus_definitions/) -->
