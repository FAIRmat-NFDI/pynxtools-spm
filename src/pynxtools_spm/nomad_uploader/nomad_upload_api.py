import requests
import logging

from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)


def get_authentication_token(
    nomad_url: str, username: str, password: str, upload_logger: logging.Logger = None
):
    """Get the token for accessing your NOMAD unpublished uploads remotely"""
    if upload_logger is None:
        upload_logger = logger

    try:
        response = requests.get(
            nomad_url + "auth/token",
            params=dict(username=username, password=password),
            timeout=10,
        )
        token = response.json().get("access_token")
        if token:
            logger.info("Successfully retrieved authentication token")
            return token
        logger.error("Authentication token not found in response")
        logger.error("Response: " + str(response.json()))
        return
    except Exception as e:
        upload_logger.error(f"Something went wrong trying to get authentication token.")
        upload_logger.error(f"Error in dataset creation: {e}")
        return


def create_dataset(
    nomad_url: str, token: str, dataset_name: str, upload_logger: logging.Logger = None
):
    """Create a dataset to group a series of NOMAD entries"""
    if upload_logger is None:
        upload_logger = logger
    try:
        response = requests.post(
            nomad_url + "datasets/",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
            json={"dataset_name": dataset_name},
            timeout=10,
        )
        dataset_id = response.json().get("dataset_id")
        if dataset_id:
            return dataset_id
        upload_logger.error("Dataset ID not found in response")
        upload_logger.error("Response: " + str(response.json()))
        return
    except Exception as e:
        upload_logger.error("Something went wrong trying to create a dataset")
        upload_logger.error(f"Error in dataset creation: {e}")
        return


def upload_to_NOMAD(
    nomad_url: str,
    token: str,
    upload_file: Path,
    file_name: str = None,
    upload_name: str = None,
    upload_logger: logging.Logger = None,
):
    """Upload a single file as a new NOMAD upload. Compressed zip/tar files are
    automatically decompressed.
    """
    upload_name = upload_name if upload_name else upload_file.name
    file_name = file_name if file_name else upload_file.name
    if upload_logger is None:
        upload_logger = logger
    with open(upload_file, "rb") as f:
        try:
            response = requests.post(
                f"{nomad_url}uploads?file_name={file_name}&upload_name={upload_name}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Accept": "application/json",
                },
                data=f,
                timeout=30,
            )
            upload_id = response.json().get("upload_id")
            if upload_id:
                logger.info(
                    f"Successfully uploaded {upload_file} to NOMAD with ID {upload_id}"
                )
                return upload_id

            logger.error("Upload ID not found in response")
            logger.error("Response: " + str(response.json()))
            return
        except Exception:
            upload_logger.error(
                f"Something went wrong uploading {upload_file} to NOMAD"
            )
            upload_logger.error(f"Error in upload: {upload_file}")
            return


def trigger_reprocess_upload(
    nomad_url: str, token: str, upload_id: str, upload_logger: logging.Logger = None
):
    """Trigger reprocessing of an upload"""
    if upload_logger is None:
        upload_logger = logger
    try:
        response = requests.post(
            f"{nomad_url}uploads/{upload_id}/action/process",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
            timeout=30,
        )
        return response
    except Exception as e:
        upload_logger.error(
            "Something went wrong trying to reprocess upload: " + upload_id
        )
        upload_logger.error(f"Error in reprocess: {e}")
        return


def delete_upload(
    nomad_url: str, token: str, upload_id: str, upload_logger: logging.Logger = None
):
    """Delete an upload"""
    if upload_logger is None:
        upload_logger = logger
    try:
        response = requests.delete(
            nomad_url + "uploads/" + upload_id,
            headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
            timeout=30,
        )
        return response
    except Exception as e:
        upload_logger.error(
            "Something went wrong trying to delete upload: " + upload_id
        )
        upload_logger.error(f"Error in delete: {e}")
        return


def check_upload_status(
    nomad_url: str, token: str, upload_id: str, upload_logger: logging.Logger = None
):
    """
    # upload success => returns 'Process publish_upload completed successfully'
    # publish success => 'Process publish_upload completed successfully'
    """
    if upload_logger is None:
        upload_logger = logger
    try:
        response = requests.get(
            nomad_url + "uploads/" + upload_id,
            headers={"Authorization": f"Bearer {token}"},
            timeout=30,
        )
        status_message = response.json().get("data").get("last_status_message")
        if status_message:
            return status_message

        upload_logger.error("Upload status message not found in response")
        upload_logger.error("Response: " + str(response.json()))
        return
    except Exception as e:
        upload_logger.error(
            "Something went wrong trying to check the status of upload: " + upload_id
        )
        return


def edit_upload_metadata(
    nomad_url: str,
    token: str,
    upload_id: str,
    metadata: dict,
    upload_logger: logging.Logger = None,
):
    """
    Example of new metadata:
    upload_name = 'Test_Upload_Name'
    metadata = {
        "metadata": {
        "upload_name": upload_name,
        "references": ["https://doi.org/xx.xxxx/xxxxxx"],
        "datasets": dataset_id,
        "embargo_length": 0,
        "coauthors": ["coauthor@affiliation.de"],
        "comment": 'This is a test upload...'
        },
    }
    """
    if upload_logger is None:
        upload_logger = logger
    try:
        response = requests.post(
            nomad_url + "uploads/" + upload_id + "/edit",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
            json=metadata,
            timeout=30,
        )
        return response
    except Exception:
        upload_logger.error(
            "Something went wrong trying to edit metadata of upload: " + upload_id
        )
        upload_logger.error(f"Error in metadata edit: {upload_id}")
        return


def publish_upload(
    nomad_url: str, token: str, upload_id: str, upload_logger: logging.Logger = None
):
    """Publish an upload"""
    if upload_logger is None:
        upload_logger = logger
    try:
        response = requests.post(
            nomad_url + "uploads/" + upload_id + "/action/publish",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
            timeout=30,
        )
        return response
    except Exception as e:
        upload_logger.error(
            "Something went wrong trying to publish upload: " + upload_id
        )
        upload_logger.error(f"Error in publish: {e}")
        return
