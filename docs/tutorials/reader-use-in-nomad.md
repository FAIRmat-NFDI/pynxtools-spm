# __Use Reader in NOMAD__

The reader functionality of the `pynxtools-spm` package can be used in [NOMAD](https://nomad-lab.eu/nomad-lab/) if the package is installed as a plugin of the `pynxtools` package where NOMAD is installed. For instructions on installing `pynxtools-spm` with NOMAD, please follow the [installation guide](../tutorials/installation.md#install-pynxtools-spm-with-nomad).

## __Use Example Available in NOMAD__

If the `pynxtools-spm` package is installed with NOMAD as a plugin, there are three demo examples for __STS__, __STM__, and __AFM__ available in NOMAD. Using these examples may help you understand how to use the reader functionality in NOMAD.

<video controls>
  <source src="../assets/DemoFromExampleUpload.webm" type="video/mp4">
</video>

These examples in NOMAD can be utilized to extend or modify the reader input files, such as the `ELN schema file` or `config file`, to customize the reader functionality according to user requirements. For details, see the [How to Interact with Reader](../how-to-guides/how-to-act-with-reader.md) guide.

## __Drag and Drop Example in NOMAD__

The provided examples in NOMAD may not be sufficient to store all data and metadata from an experiment. You can modify the ELN schema file to structure and store metadata according to the application definitions. Below are a few steps to upload data in NOMAD using the drag and drop method:

__1.__ Create a NOMAD upload by clicking the `CREATE A NEW UPLOAD` button on the NOMAD upload page.

<div class="scrollable-img">
    <img src="../assets/create_upload.png"
          alt="create_upload">
</div>

__2.__ Rename `unnamed upload` as desired, and drop the schema file (e.g., `sts.schema.archive.yaml`). NOMAD will create an entry.

<div class="scrollable-img">
    <img src="../assets/upload_schema_eln.png"
          alt="Sample Image">
</div>

__3.__ Create a NOMAD [archive](https://nomad-lab.eu/prod/v1/docs/reference/glossary.html#archive) entry. Based on the newly uploaded schema file, you need to create the archive from the `custom schema` option as the uploaded schema file is not a built-in schema in NOMAD.

<video controls>
  <source src="../assets/CreateArchiveFromCustomSchema.webm" type="video/mp4">
</video>

__4.__ After creating an archive entry, the data section will immediately expand, and you can add input data along with raw data files. By filling in the required metadata (e.g., name of `nxdl`, software and hardware specifications), the data can be saved in a NeXus file.

<video controls>
  <source src="../assets/FinishupCustomizeUpload.webm" type="video/mp4">
</video>