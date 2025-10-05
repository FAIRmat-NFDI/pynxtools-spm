# Use Reader in NOMAD
## __Use Example available in NOMAD__
If `pynxtools-spm` plugin package is installed with NOMAD, there are a few demo examples for __STS__, __STM__, and __AFM__ available in NOMAD. Use of these examples may help to undertand how to use the reader functionality in NOMAD.

<video controls>
<source src="../assets/DemoFromExampleUpload.webm" type="video/mp4">
</video>

This available example in NOMAD can be utilized to extend or modify the reader input files e.g., `ELN schema file`, `config file` to customize the reader functionality as per the user requirement. For details see [How to Interact with Reader](../how-to-guides/how-to-interact-with-reader.md) guide.

## Drag and Drop Example in NOMAD
Provided the examples in `NOMAD` may not be sufficient to store data and metadata from a experiment. One can modify the ELN schema file to structure and store the metadata according to the application definitions. A few steps to upload data in NOMAD using drag and drop method is shown below.

__1.__ Create a NOMAD upload by clicking on the button `CREATE A NEW UPLOAD` in nomad upload page.
![](../assets/create_upload.png)

__2.__ Rename `unnamed upload` according to the upload name and drop schema file (e.g., `sts.scheme.archive.yaml`) and nomad will create an entry.
![](../assets/upload_schema_eln.png)

__3.__ Let's create an nomad [archive](https://nomad-lab.eu/prod/v1/docs/reference/glossary.html#archive) entry. Base on the schema file, user needs to create an archive entry from schema file. As newly uploaded schema file is not a built-in schema in NOMAD, user needs to create archive from `custom schema` option.

<video controls>
  <source src="../assets/CreateArchiveFromCustomSchema.webm" type="video/mp4">
</video>

__4.__ After creation of an archive entry, the data section will immediately expand, and the user can add input data along with raw data files. Filling the required metadata e.g., name of `nxdl`, software, and hardware specification, data can be saved in a NeXus file.

<video controls>
  <source src="../assets/FinishupCustomizeUpload.webm" type="video/mp4">
</video>