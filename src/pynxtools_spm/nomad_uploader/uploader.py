from pynxtools_spm.nomad_uploader.reader_config_setup import (
    SPMConvertInputParameters,
    convert_spm_experiments,
)
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List
from dataclasses import asdict, dataclass
import time
import re
import logging
from datetime import datetime

from pynxtools_spm.nomad_uploader.nomad_upload_api import (
    get_authentication_token,
    upload_to_NOMAD,
    publish_upload,
    check_upload_status,
    delete_upload,
    create_dataset,
    trigger_reprocess_upload,
    edit_upload_metadata,
)

# from pynxtools_spm.nomad_uploader.files_movers import copy_directory_structure
from pynxtools_spm.nomad_uploader.helper import (
    setup_logger,
)
from multiprocessing import Process, Lock, Queue


@dataclass
class NOMADSettings:
    url_protocol: str
    url_domain: str
    url_version: str
    url: str
    username: str
    password: str
    token: str
    # If metadata of the upload file will be modified
    modify_upload_metadata: bool = False
    # If the upload will be published to the central NOMAD database
    publish_to_nomad: bool = False


@dataclass
class DataProcessingSettings:
    raw_file_exts: tuple[str, ...]
    single_batch_processing_time: int  # seconds
    # Where the log files will be stored
    logger_dir: Path
    sts_eln: Path
    stm_eln: Path
    afm_eln: Path
    # Considered as a root directory for the experiment files
    src_dir: Path
    # List of SPMConvertInputParameters objects to run reader on each object
    spm_params_obj_l: Optional[List[Path]] = list
    # Destination directory for the experiment files, if files are moved
    # to another location after processing is done, needs `copy_file_elsewhere`
    # to be True
    dst_dir: Optional[Path] = None
    # create and empty file if upload is sucessfull
    create_pseudo_file: bool = True
    # Extension to the empty file if upload is sucessfull
    pseudo_exts: str = ".done"
    sts_config: Optional[Path] = None
    stm_config: Optional[Path] = None
    afm_config: Optional[Path] = None
    # Currently copying the file to another location and removing the original
    # file has been disabled
    # copy_file_elsewhere: bool = False
    # Number of files to be uploaded in a single batch
    number_of_uploads: int = 10
    delete_failed_uploads: bool = False


def create_preseudo_file(
    params_obj: SPMConvertInputParameters,
    data_processing_settings: DataProcessingSettings,
) -> None:
    """Create a pseudo file if upload is successful."""
    if (
        not data_processing_settings.create_pseudo_file
        # and not data_processing_settings.copy_file_elsewhere
    ):
        return

    source_fls = list(
        filter(
            lambda x: x.suffix in data_processing_settings.raw_file_exts,
            params_obj.input_file,
        )
    )
    for source_f in source_fls:
        if data_processing_settings.create_pseudo_file:
            pseudo_file_ = source_f.with_suffix(
                f"{source_f.suffix}{data_processing_settings.pseudo_exts}"
            )
            pseudo_file_.touch()
        # elif data_processing_settings.copy_file_elsewhere:
        #     pass
        # As raw file stored in other location, remove it
        # source_f.unlink()


def get_unprocessed_files(src_dir: Path, data_processing_settings) -> list:
    """Filter out the files that are already processed.

    E.g. an input file `file.dat` will be denoted as `file.dat.done` after
    the upload is successful. It is assumed that
    DataProcessingSettings.create_pseudo_file is True
    and DataProcessingSettings.pseudo_exts is set to `.done`.
    This function checks for the raw files where the corresponding `.done`
    file is not present.
    """
    process_status_map = {}
    for file in src_dir.glob("**/*.*"):
        if file.is_file() and file.suffix in data_processing_settings.raw_file_exts:
            process_status_map[file] = False
    for file in src_dir.glob("**/*.*"):
        if file.is_file() and file.suffix == data_processing_settings.pseudo_exts:
            # Remove extra pseudo extension
            process_status_map[file.with_suffix("")] = True
    raw_file_list = [
        file for file, is_processed in process_status_map.items() if not is_processed
    ]
    max_uploads = (
        data_processing_settings.number_of_uploads
        if data_processing_settings.number_of_uploads <= len(raw_file_list)
        else len(raw_file_list)
    )
    return raw_file_list[:max_uploads]


def set_and_store_prepared_parameters(
    file: Path, data_processing_settings: DataProcessingSettings
) -> None:
    params_obj = None
    if file.suffix == ".dat":
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=data_processing_settings.sts_eln,
            expriement_type="sts",
            config=data_processing_settings.sts_config,
            nxdl="NXsts",
            raw_extension="dat",
            create_zip=True,
        )
    elif file.suffix == ".sxm":
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=data_processing_settings.stm_eln,
            expriement_type="stm",
            config=data_processing_settings.stm_config,
            nxdl="NXstm",
            raw_extension="sxm",
            create_zip=True,
        )
    elif file.suffix == ".sxm":
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=data_processing_settings.afm_eln,
            expriement_type="afm",
            config=data_processing_settings.afm_config,
            nxdl="NXafm",
            raw_extension="sxm",
            create_zip=True,
        )
    if not params_obj:
        return
    data_processing_settings.spm_params_obj_l.append(params_obj)


converter_logger = None
converter_handeler = None
upload_handler = None
upload_logger = None


def run_uploader_with(
    data_processing_settings: DataProcessingSettings, data_settings: NOMADSettings
) -> None:
    """Run the uploader with the given settings."""
    global converter_logger, converter_handeler, upload_handler, upload_logger
    if converter_logger is None and upload_logger is None:
        logger_dir = data_processing_settings.logger_dir
        upload_logger, upload_handler = setup_logger(
            name="uploader", log_file=logger_dir / "upload.log"
        )
        pynxtools_logger = logging.getLogger("pynxtools")
        converter_logger, converter_handeler = setup_logger(
            name="data converter",
            log_file=logger_dir / "converter.log",
            existing_logger=pynxtools_logger,
        )

    data_settings.token = get_authentication_token(
        data_settings.url, data_settings.username, data_settings.password
    )
    if not data_settings.token:
        upload_logger.error(
            "Authentication failed: Token is required to upload files."
        )
        return
    if (
        not data_processing_settings.src_dir
        or not data_processing_settings.src_dir.is_dir()
    ):
        upload_logger.error(
            "Process Exits: Source directory is required to process the files."
        )
        return

    # # In case user wants to store the files elsewhere
    # if data_processing_settings.copy_file_elsewhere:

    #     copy_directory_structure(
    #         src=data_processing_settings.src_dir,
    #         dst=data_processing_settings.dst_dir,
    #         run_action_on_files=set_and_store_prepared_parameters,
    #         data_processing_settings=data_processing_settings,
    #     )

    file_list = get_unprocessed_files(
        data_processing_settings.src_dir, data_processing_settings
    )
    upload_logger.info(
        f"Total '{len(file_list)}' files to process in in {data_processing_settings.src_dir}:\n"
        f"{'\n\t\t'.join([str(file) for file in file_list])}"
    )
    # Prepare the input parameters for the SPM reader for each file
    _ = [
        set_and_store_prepared_parameters(file, data_processing_settings)
        for file in file_list
        if (file and file.is_file())
    ]
    # For logging massage
    obj_type_num = {}
    for obj in data_processing_settings.spm_params_obj_l:
        type_ = obj.__class__.__name__
        if type_ not in obj_type_num:
            obj_type_num[type_] = 1
        else:
            obj_type_num[type_] += 1

    log_msg = "\n".join([f"Instance of {t}: {n}" for t, n in obj_type_num.items()])
    upload_logger.info(
        f"Total '{len(data_processing_settings.spm_params_obj_l)}' input parameter object: \n {log_msg}"
    )

    lock = Lock()
    results_q = Queue()
    time_out = int(data_processing_settings.single_batch_processing_time / 3)  # seconds

    def queue_results(input_params, lock, results_q):
        lock.acquire()
        try:
            upload_logger.info(
                f"Start conversion job with inputs {input_params.input_file} via {input_params.__class__.__name__} instance."
            )
            result = convert_spm_experiments(
                input_params, converter_logger, converter_handeler
            )
            results_q.put(result)

        except Exception as e:
            upload_logger.error(f"Error in processing {input_params.input_file}: {e}")
        finally:
            upload_logger.info(
                f"Converter job is completed for {input_params.input_file} via {input_params.__class__.__name__} instance."
            )
            lock.release()

    processes_list = []

    for input_params in data_processing_settings.spm_params_obj_l:
        p = Process(
            target=queue_results,
            args=(input_params, lock, results_q),
        )
        p.start()
        upload_logger.info(
            f"Process job has been submited with input files {input_params.input_file} via process id {p.pid}."
        )
        processes_list.append(p)

    for _, (p, input_params) in enumerate(
        zip(processes_list, data_processing_settings.spm_params_obj_l)
    ):
        p.join(time_out)
        if p.is_alive():
            upload_logger.critical(
                f"Terminating process (PID: {p.pid}) is still "
                f"running and expected to be done in {time_out}s.\n"
                f"Converter job with input prameters {asdict(input_params)}",
            )
            p.terminate()
            p.join()

    indices = []
    completed_param_objs = []
    while not results_q.empty():
        # Get back input_params obj with output files
        completed_param_objs.append(results_q.get())
    upload_time_limit = datetime.now() + timedelta(seconds=time_out)
    # TODO: Use asynchrounous request for api requests
    while (
        len(completed_param_objs) > len(indices) and datetime.now() < upload_time_limit
    ):
        success_ind = []
        failed_ind = []
        # TODO: Try to send multiple async requests to nomad
        for ind, complete_param_obj in enumerate(completed_param_objs):
            zip_to_upload = complete_param_obj.zip_file_path
            if ind in indices:  # already processed or failed
                continue
            if not zip_to_upload:
                failed_ind.append(ind)
                indices.append(ind)
                continue
            indices.append(ind)
            massage = "Adding files"
            max_attempt = 20
            try:
                upload_id = upload_to_NOMAD(
                    data_settings.url, data_settings.token, zip_to_upload
                )
                upload_logger.info(
                    f"Upload request with Upload ID ({upload_id}) corresponding to {complete_param_obj.input_file}."
                )
                # trigger_reprocess_upload(
                #     data_settings.url, data_settings.token, upload_id
                # )
                massage = check_upload_status(
                    data_settings.url, data_settings.token, upload_id
                )
                upload_logger.info(f"Upload status for {upload_id}: \n{massage}")

            except Exception as e:
                upload_logger.error(
                    f"Error in uploading (upload_id:{upload_id}) {zip_to_upload}: {e}"
                )
                failed_ind.append(ind)
                continue
            # To modify metadata
            if data_settings.modify_upload_metadata:
                upload_logger.info(f"Modifying metadata is not implemented yet.")
                raise NotImplementedError("Modifying metadata is not implemented yet.")

                # dataset_id = create_dataset(
                #     data_settings.url, data_settings.token, "Test_Dataset"
                # )
                # # TODO: Metadata dictionary shoudl come from data_processing_settings
                # metadata = {
                #     "metadata": {
                #         "upload_name": "Test_Upload",
                #         "references": ["https://doi.org/xx.xxxx/x.xxxx"],
                #         "datasets": dataset_id,
                #         "embargo_length": 0,
                #         "coauthors": ["coauthor@affiliation.de"],
                #         "comment": "This is a test upload...",
                #     },
                # }
                # edit_upload_metadata(
                #     data_settings.url, data_settings.token, upload_id, metadata
                # )

            if data_settings.publish_to_nomad:
                publish_upload(data_settings.url, data_settings.token, upload_id)

            attempt = 0
            while attempt < max_attempt:
                attempt += 1
                if massage.startswith("Process process_upload completed successfully"):
                    upload_logger.info(
                        f"Upload status: Upload successfully completed with upload ID: {upload_id}"
                    )
                    success_ind.append(ind)
                    create_preseudo_file(complete_param_obj, data_processing_settings)
                    break
                # Check if the upload is failed with any massage that contains error
                elif re.search(r"\berror\b", massage, re.IGNORECASE):
                    failed_ind.append(ind)
                    upload_logger.error(
                        f"Upload status: Upload failed with error: {massage} for upload ID: {upload_id}"
                    )
                    upload_logger.error(
                        f"Upload status: Upload ID: {upload_id} handles by {complete_param_obj.input_file}"
                    )
                    break
                elif (
                    attempt == max_attempt
                    and data_processing_settings.delete_failed_uploads
                ):
                    upload_logger.error(
                        f"Upload status: Upload is time out for upload ID: {upload_id}"
                    )
                    upload_logger.error(
                        f"Upload status: Delete Upload ID: {upload_id} ."
                    )
                    delete_upload(
                        data_settings.url, data_settings.token, upload_id, upload_logger
                    )
                    break

                massage = check_upload_status(
                    data_settings.url, data_settings.token, upload_id
                )
                time.sleep(1)

        for ind, input_params in enumerate(completed_param_objs):
            # Whether successfully uploaded or not, remove the zip file and ouuput file
            if input_params.zip_file_path and input_params.zip_file_path.is_file():
                input_params.zip_file_path.unlink()
            if input_params.output and input_params.output.is_file():
                input_params.output.unlink()
