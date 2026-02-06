# NOMAD Uploader

A comprehensive Python tool for automated conversion and upload of SPM (Scanning Probe Microscopy) experimental data to the NOMAD (FAIR data management platform). This module converts raw SPM data files (STS, STM, AFM) to NeXus format and uploads them to NOMAD with metadata management.

## Features

- **Automated SPM Data Conversion**: Converts raw SPM files (`.dat`, `.sxm`) to NeXus format (`NXsts`, `NXstm`, `NXafm`)
- **Batch Processing**: Process multiple files in parallel using multiprocessing
- **NOMAD Integration**: Direct upload to NOMAD with OAuth2 authentication
- **Metadata Management**: Modify and manage upload metadata before publishing
- **Status Tracking**: Real-time monitoring of upload and processing status
- **Automatic Decompression**: Handles compressed files automatically
- **Logging**: Comprehensive logging for debugging and tracking progress
- **Error Handling**: Robust error handling with retry mechanisms

## Directory Structure

```
nomad_uploader/
├── README.md                      # This file
├── uploader.py                    # Main uploader orchestration
├── nomad_upload_api.py           # NOMAD API client
├── reader_config_setup.py        # SPM conversion configuration
├── example_upload_script.py      # Example usage script
├── helper.py                      # Utility functions
└── files_movers.py               # File management utilities
```

## Module Overview

### `uploader.py`
Main orchestration module containing:
- `NOMADSettings`: Configuration for NOMAD connection and authentication
- `DataProcessingSettings`: Configuration for SPM data processing
- `run_uploader_with()`: Main entry point for uploading data

### `nomad_upload_api.py`
NOMAD REST API client with functions:
- `get_authentication_token()`: OAuth2 authentication
- `upload_to_NOMAD()`: Upload files to NOMAD
- `check_upload_status()`: Monitor upload/processing status
- `publish_upload()`: Publish uploads to NOMAD
- `edit_upload_metadata()`: Modify upload metadata
- `delete_upload()`: Delete failed uploads
- `create_dataset()`: Group uploads into datasets
- `trigger_reprocess_upload()`: Trigger NOMAD reprocessing

### `reader_config_setup.py`
SPM data conversion module:
- `SPMConvertInputParameters`: Configuration for SPM conversion
- `convert_spm_experiments()`: Convert raw SPM data to NeXus format

## Quick Start

### Basic Usage

```python
from pynxtools_spm.nomad_uploader.uploader import (
    run_uploader_with,
    NOMADSettings,
    DataProcessingSettings,
)
from pathlib import Path

# Configure NOMAD connection
nomad_settings = NOMADSettings(
    url_protocol="https",
    url_domain="nomad-lab.eu",
    url_version="prod/v1/develop/api/v1/",
    username="your_username",
    password="your_password",
    token="",  # Will be auto-generated
    modify_upload_metadata=True,
    publish_to_nomad=False,
)

# Configure data processing
data_proc_settings = DataProcessingSettings(
    raw_file_exts=(".dat", ".sxm"),
    single_batch_processing_time=90,  # seconds
    logger_dir=Path("./logs"),
    src_dir=Path("/path/to/spm/data"),
    sts_eln=Path("/path/to/sts_eln.yaml"),
    stm_eln=Path("/path/to/stm_eln.yaml"),
    afm_eln=Path("/path/to/afm_eln.yaml"),
    number_of_uploads=10,
    create_pseudo_file=True,
    pseudo_exts=".done",
)

# Run uploader
if __name__ == "__main__":
    run_uploader_with(
        nomad_settings=nomad_settings,
        data_proc_settings=data_proc_settings,
    )
```

## Configuration

### NOMADSettings

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `url_protocol` | str | Yes | - | Protocol (`https` or `http`) |
| `url_domain` | str | Yes | - | NOMAD domain (e.g., `nomad-lab.eu`) |
| `url_version` | str | Yes | - | API version path (e.g., `prod/v1/develop/api/v1/`) |
| `username` | str | Yes | - | NOMAD username |
| `password` | str | Yes | - | NOMAD password |
| `token` | str | Yes | - | OAuth2 token (auto-generated on first run) |
| `url` | str | No | Auto | Full API URL (auto-constructed if not provided) |
| `modify_upload_metadata` | bool | No | False | Whether to modify metadata before publish |
| `publish_to_nomad` | bool | No | False | Automatically publish uploads to NOMAD |
| `max_upload_attempt` | int | No | 20 | Max retry attempts for upload status check |
| `nomad_processing_time` | int | No | 3 | Wait time (seconds) between status checks |

### DataProcessingSettings

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `raw_file_exts` | tuple | Yes | - | Supported file extensions (e.g., `.dat`, `.sxm`) |
| `single_batch_processing_time` | int | Yes | - | Processing timeout per batch (seconds) |
| `logger_dir` | Path | Yes | - | Directory for log files |
| `src_dir` | Path | Yes | - | Source directory with raw SPM files |
| `sts_eln` | Path | Yes | - | Path to STS ELN (Electronic Lab Notebook) file |
| `stm_eln` | Path | Yes | - | Path to STM ELN file |
| `afm_eln` | Path | Yes | - | Path to AFM ELN file |
| `spm_params_obj_l` | List | No | [] | List of conversion parameters (auto-populated) |
| `dst_dir` | Path | No | None | Destination for processed files |
| `create_pseudo_file` | bool | No | True | Create marker file after successful upload |
| `pseudo_exts` | str | No | `.done` | Extension for marker file |
| `sts_config` | Path | No | None | Optional STS-specific config |
| `stm_config` | Path | No | None | Optional STM-specific config |
| `afm_config` | Path | No | None | Optional AFM-specific config |
| `number_of_uploads` | int | No | 10 | Max files to process per batch |
| `delete_failed_uploads` | bool | No | False | Delete uploads on timeout |
| `upload_metadata` | dict | No | None | Metadata to apply to all uploads |
| `file_specific_eln` | dict | No | None | Map filenames to specific ELN files |

## Metadata Management

### Modifying Upload Metadata

```python
# Example metadata structure
metadata = {
    "metadata": {
        "upload_name": "My SPM Experiment",
        "coauthors": ["colleague@institution.edu"],
        "references": ["https://doi.org/10.xxxx/xxxxx"],
        "datasets": "dataset_id",
        "embargo_length": 0,  # 0 = public, >0 = days of embargo
        "comment": "Description of the experiment"
    }
}

# Apply to settings
data_proc_settings.upload_metadata = metadata
```

## Logging

The uploader generates detailed logs in the specified `logger_dir`:

- **`upload.log`**: Upload operations, status checks, API interactions
- **`converter.log`**: SPM data conversion progress and NeXus generation

### Log Levels

- `INFO`: Standard operation messages
- `ERROR`: Failed operations and errors
- `DEBUG`: Detailed debugging information

### Example Log Entry

```
2024-02-06 10:45:23,456 - uploader - INFO - Upload request with Upload ID (7BWDvsn7TmeNyOBHTcgpwA) corresponding to (...) 
2024-02-06 10:45:25,789 - uploader - INFO - Upload status for 7BWDvsn7TmeNyOBHTcgpwA: Process process_upload completed successfully
```

## File Processing Workflow

```
Raw SPM File (.dat/.sxm)
    ↓
[Automatic Detection] (STS/STM/AFM)
    ↓
[NeXus Conversion] (pynxtools reader)
    ↓
Intermediate Files
    ├── NeXus file (.nxs)
    └── Metadata file
    ↓
[Zip Creation]
    ↓
ZIP Archive
    ↓
[NOMAD Upload] (OAuth2)
    ↓
Upload ID assigned
    ↓
[Status Monitoring] (polling)
    ↓
[Processing Complete]
    ↓
[Optional Metadata Edit]
    ↓
[Optional Publishing]
    ↓
Marker File Created (.done)
```

## API Workflow

### Authentication Flow

```
NOMADSettings
  ↓
[OAuth2 Password Grant]
  ↓
Access Token
  ↓
API Requests
```

### Upload Status States

1. **Adding files**: Files being uploaded to NOMAD
2. **Process process_upload completed successfully**: Data converted to standardized format
3. **Process process_publish_upload completed successfully**: Published to NOMAD

## Error Handling

### Common Issues and Solutions

#### Authentication Failed
```
Error: Authentication token not found in response
Solution: Verify username, password, and NOMAD API endpoint
```

#### Upload Status Message Not Found
```
Error: Upload status message not found in response
Solution: Check response structure from NOMAD API
```

#### Timeout During Processing
```
Error: Upload is time out for upload ID: XXX
Solution: Increase `max_upload_attempt` or `nomad_processing_time` in NOMADSettings
```

## Advanced Usage

### Processing Only Unprocessed Files

The uploader automatically creates `.done` marker files for successful uploads. On subsequent runs, it only processes files without corresponding `.done` markers.

```python
# First run - processes all files
# Creates: file.dat.done for each successful upload

# Second run - skips already processed files
# Only processes new files without .done markers
```

### Batch Processing with Custom ELN Mapping

```python
data_proc_settings.file_specific_eln = {
    "sample1.dat": Path("/path/to/sample1_eln.yaml"),
    "sample2.sxm": Path("/path/to/sample2_eln.yaml"),
}
# Default ELN will be used for files not in this mapping
```

### Publishing to NOMAD

```python
nomad_settings.publish_to_nomad = True
nomad_settings.modify_upload_metadata = True

# Configure metadata for publishing
data_proc_settings.upload_metadata = {
    "metadata": {
        "embargo_length": 0,  # Make public immediately
        "upload_name": "Published Dataset",
    }
}
```

## Performance Tuning

### For Large Batches

```python
data_proc_settings.number_of_uploads = 50  # Process more files per batch
data_proc_settings.single_batch_processing_time = 300  # Longer timeout
nomad_settings.max_upload_attempt = 30  # number of NOMAD API retries
```

### For Large Files

```python
data_proc_settings.single_batch_processing_time = 600  # 10 minutes
nomad_settings.nomad_processing_time = 5  # Longer wait between checks
```

## NOMAD REST API Reference

### Key Endpoints Used

- **Authentication**: `POST /auth/token`
- **Upload Creation**: `POST /uploads?file_name=...&upload_name=...`
- **Upload Status**: `GET /uploads/{upload_id}`
- **Metadata Edit**: `POST /uploads/{upload_id}/edit`
- **Publishing**: `POST /uploads/{upload_id}/action/publish`
- **Dataset Creation**: `POST /datasets/`

For complete NOMAD API documentation, visit: https://nomad-lab.eu/docs

## Examples

See `example_upload_script.py` for a complete working example with real configuration.

## Contributing

When modifying the uploader:
1. Update type hints (`Optional[Literal[...]]` for restricted values)
2. Maintain consistent logger usage (pass `upload_logger` to all functions)
3. Add comprehensive docstrings
4. Update this README with new features


## Support

For issues or questions:
- Check the logs in `logger_dir` for detailed error messages
- Review the NOMAD documentation at https://nomad-lab.eu
- Open an issue on the project repository
