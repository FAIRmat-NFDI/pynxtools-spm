from pynxtools_spm.nomad_uploader.reader_config_setup import (
    SPMConvertInputParameters,
    convert_spm_experiments,
)
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from dataclasses import asdict, dataclass
import time
import re
import logging

from pynxtools_spm.nomad_uploader.nomad_upload_api import (
    get_authentication_token,
    create_dataset,
    upload_to_NOMAD,
    edit_upload_metadata,
    publish_upload,
    check_upload_status,
    trigger_reprocess_upload,
)
from pynxtools_spm.nomad_uploader.files_movers import copy_directory_structure
from pynxtools_spm.nomad_uploader.helper import (
    setup_logger,
)
from multiprocessing import Process, Lock, Queue
# TODO add the process in single batch of processing and uploading
# set the time out 1 minute for each process 
# Get the directory where the script will be running
current_dir = Path(__file__).parent
upload_logger, upload_handler = setup_logger(name="uploader", log_file=current_dir / "upload.log")
pynxtools_logger = logging.getLogger("pynxtools")
converter_logger, converter_handeler = setup_logger(name="data converter", 
                                                    log_file=current_dir / "converter.log",
                                                    existing_logger=pynxtools_logger)
# TODO: Log file will be running where the script will be launched
debug = True
@dataclass
class NOMADSettings:
    url_protocol: str = "https"
    url_domain: str = "nomad-lab.eu"
    url_version: str = "prod/v1/oasis-b/api/v1/"
    url: str = f"{url_protocol}://{url_domain}/{url_version}"
    username: str = "Mozumder"
    password: str = ""
    token: str = ""
    # If metadata of the upload file will be modified
    modify_upload_metadata: bool = False
    # If the upload will be published to the central NOMAD database
    publish_to_nomad: bool = False


@dataclass
class DataProcessingSettings:
    raw_file_exts: tuple[str, ...] = (".dat", ".sxm")
    single_batch_processing_time: int = 20 * 60  # seconds
    parallel_processing: bool = True
    # Considered as a root directory for the experiment files
    src_dir: Optional[Path] = (
        current_dir.parent.parent.parent / "tests" / "data" / "nanonis"
    )
    copy_file_elsewhere: bool = False
    # Destination directory for the experiment files, if files are moved
    # to another location after processing is done, needs `copy_file_elsewhere`
    # to be True
    dst_dir: Optional[Path] = ""
    # create and empty file if upload is sucessfull
    create_pseudo_file: bool = True
    # Extension to the empty file if upload is sucessfull
    pseudo_exts: str = ".done"
    # List of SPMConvertInputParameters objects to run reader on each object
    spm_params_obj_l = []
    sts_eln = src_dir / "sts" / "version_gen_5e_with_described_nxdata" / "eln_data.yaml"
    sts_config = ""
    stm_eln = (
        src_dir / "stm" / "version_gen_4_5_with_described_nxdata" / "eln_data.yaml"
    )
    stm_config = ""
    afm_eln = src_dir / "afm" / "version_gen_4_with_described_nxdata" / "eln_data.yaml"
    afm_config = ""


def create_preseudo_file(
    params_obj: SPMConvertInputParameters,
    data_processing_settings: DataProcessingSettings,
) -> None:
    """Create a pseudo file if upload is successful."""
    if (
        not data_processing_settings.create_pseudo_file
        and not data_processing_settings.copy_file_elsewhere
    ):
        return

    source_fls = list(
        filter(
            lambda x: x.suffix in DataProcessingSettings.raw_file_exts,
            params_obj.input_file,
        )
    )
    for source_f in source_fls:
        if (
            data_processing_settings.create_pseudo_file
        ):
            pseudo_file_ = source_f.with_suffix(
                f"{source_f.suffix}{DataProcessingSettings.pseudo_exts}"
            )
            pseudo_file_.touch()
        elif data_processing_settings.copy_file_elsewhere:
            # As raw file stored in other location, remove it
            source_f.unlink()


def get_unprocessed_files(src_dir: Path) -> list:
    """Filter out the files that are not processed yet.

    E.g. an input file `file.dat` will be denoted as `file.dat.done` after,
    assume DataProcessingSettings.create_pseudo_file is True
    and DataProcessingSettings.pseudo_exts is set to `.done`,
    successful upload to NOMAD. So, it always checks for the raw files
    and if the corresponding `.done` file is not present, it will be
    considered as unprocessed.
    """
    process_status_map = {}
    for file in src_dir.glob("**/*.*"):
        if file.is_file() and file.suffix in DataProcessingSettings.raw_file_exts:
            process_status_map[file] = False
    for file in src_dir.glob("**/*.*"):
        if file.is_file() and file.suffix == DataProcessingSettings.pseudo_exts:
            # Remove extra pseudo extension
            process_status_map[file.with_suffix("")] = True

    def filter_non_processed_file(arg):
        """Filter out the files that are not processed yet.
        arg[0] is the file and arg[1] is the process status
        e.g. file = file.dat and arg[1] = False
        """
        file, is_processed = arg[0], arg[1]
        if not is_processed:
            return file

    return list(map(filter_non_processed_file, process_status_map.items()))

# TODO: Create log file for each process

def set_and_store_prepared_parameters(file: Path):
    params_obj = None
    if file.suffix == ".dat":
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=DataProcessingSettings.sts_eln,
            expriement_type="sts",
            config=DataProcessingSettings.sts_config,
            nxdl="NXsts",
            raw_extension="dat",
            create_zip=True,
        )
    elif file.suffix == ".sxm":
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=DataProcessingSettings.stm_eln,
            expriement_type="stm",
            config=DataProcessingSettings.stm_config,
            nxdl="NXstm",
            raw_extension="sxm",
            create_zip=True,
        )
    elif file.suffix == ".sxm":
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=DataProcessingSettings.afm_eln,
            expriement_type="afm",
            config=DataProcessingSettings.afm_config,
            nxdl="NXafm",
            raw_extension="sxm",
            create_zip=True,
        )
    if not params_obj:
        return
    DataProcessingSettings.spm_params_obj_l.append(params_obj)


if __name__ == "__main__":
    NOMADSettings.token = get_authentication_token(
        NOMADSettings.url, NOMADSettings.username, NOMADSettings.password
    )
    if not NOMADSettings.token:
        print("AuthenticationFailed: Token is required to upload files.")
        exit(1)
    if (
        not DataProcessingSettings.src_dir
        or not DataProcessingSettings.src_dir.is_dir()
    ):
        print("Process Exits: Source directory is required to process the files.")
        exit(1)

    # In case user wants to store the files elsewhere
    if DataProcessingSettings.copy_file_elsewhere:

        copy_directory_structure(
            DataProcessingSettings.src_dir,
            DataProcessingSettings.dst_dir,
            run_action_on_files=set_and_store_prepared_parameters,
        )
    else:
        file_list = get_unprocessed_files(DataProcessingSettings.src_dir)
        upload_logger.info(
            f"Total '{len(file_list)}' files to process in in {DataProcessingSettings.src_dir}:\n"
            f"{"\n\t\t".join([str(file) for file in file_list])}"
        )
        # Prepare the input parameters for the SPM reader for each file
        _ = [
            set_and_store_prepared_parameters(file)
            for file in file_list
            if (file and file.is_file())
        ]
        # Logging massage
        obj_type_num = {}
        for obj in DataProcessingSettings.spm_params_obj_l:
            type_ = obj.__class__.__name__
            if type_ not in obj_type_num:
                obj_type_num[type_] = 1
            else:
                obj_type_num[type_] += 1
        
        log_msg = "\n".join([f"Instance of {t}: {n}" for t, n in obj_type_num.items()])
        upload_logger.info(
            f"Total '{len(DataProcessingSettings.spm_params_obj_l)}' input parameter object: \n {log_msg}"
        )

    if not DataProcessingSettings.parallel_processing:
        pass

    lock = Lock()
    results_q = Queue()
    time_out = int(DataProcessingSettings.single_batch_processing_time / 3)  # seconds
    from datetime import datetime
    def queue_results(input_params, lock, results_q):
        lock.acquire()
        try:
            upload_logger.info(
                f"Start conversion job with inputs {input_params.input_file} via {input_params.__class__.__name__} instance."
            )
            result = convert_spm_experiments(input_params, converter_logger, converter_handeler)
            results_q.put(result)

        except Exception as e:
            upload_logger.error(
                f"Error in processing {input_params.input_file}: {e}"
            )
            # TODO deactivate the raise statement
            raise e
        finally:
            upload_logger.info(
                f"Converter job is completed for {input_params.input_file} via {input_params.__class__.__name__} instance."
            )
            lock.release()

    processes_list = []

    for input_params in DataProcessingSettings.spm_params_obj_l:
        p = Process(
            target=queue_results,
            args=(input_params, lock, results_q),
        )
        p.start()
        upload_logger.info(
            f"Process job has been submited with input files {input_params.input_file} via process id {p.pid}."
        )
        processes_list.append(p)
    # if debug:
    #     print("Debug: Processes Started : Process list", processes_list)
    #     print(
    #         "Debug: Processes started : SPMConvertInputParameters objects",
    #         DataProcessingSettings.spm_params_obj_l,
    #     )
    for _, (p, input_params) in enumerate(
        zip(processes_list, DataProcessingSettings.spm_params_obj_l)
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
    # TODO: Add option to upload upacked zip files and upload the raw files
    # TODO: Use asynchrounous process for api calls
    while (
        len(completed_param_objs) > len(indices) and datetime.now() < upload_time_limit
    ):
        sucess_ind = []
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
                    NOMADSettings.url, NOMADSettings.token, zip_to_upload
                )
                upload_logger.info(
                    f"Upload request to with Upload ID ({upload_id}) corresponding to {complete_param_obj.input_file}."
                )
                # trigger_reprocess_upload(
                #     NOMADSettings.url, NOMADSettings.token, upload_id
                # )
                massage = check_upload_status(
                    NOMADSettings.url, NOMADSettings.token, upload_id
                )
                upload_logger.info(
                    f"Upload status for {upload_id}: \n{massage}"
                )

            except Exception as e:
                upload_logger.error(
                    f"Error in uploading (upload_id:{upload_id}) {zip_to_upload}: {e}"
                )
                failed_ind.append(ind)
                continue
            # To modify metadata
            if NOMADSettings.modify_upload_metadata:
                dataset_id = create_dataset(
                    NOMADSettings.url, NOMADSettings.token, "Test_Dataset"
                )
                metadata = {
                    "metadata": {
                        "upload_name": "Test_Upload",
                        "references": ["https://doi.org/xx.xxxx/x.xxxx"],
                        "datasets": dataset_id,
                        "embargo_length": 0,
                        "coauthors": ["coauthor@affiliation.de"],
                        "comment": "This is a test upload...",
                    },
                }
                edit_upload_metadata(
                    NOMADSettings.url, NOMADSettings.token, upload_id, metadata
                )

            if NOMADSettings.publish_to_nomad:
                publish_upload(NOMADSettings.url, NOMADSettings.token, upload_id)

            attempt = 0
            while attempt < max_attempt:
                attempt += 1
                if massage.startswith("Process process_upload completed successfully"):
                    upload_logger.info(
                        f"Upload status: Upload completed successfully with upload ID: {upload_id}"
                    )
                    sucess_ind.append(ind)
                    create_preseudo_file(complete_param_obj, DataProcessingSettings)
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
                upload_logger.info(
                    f"Upload status: {massage} for upload ID: {upload_id}"
                )
                massage = check_upload_status(
                    NOMADSettings.url, NOMADSettings.token, upload_id
                )
                time.sleep(4 / 60)  # 4 second
            

        for ind, input_params in enumerate(completed_param_objs):

            # Whether successfully uploaded or not, remove the zip file and ouuput file
            if input_params.zip_file_path and input_params.zip_file_path.is_file():
                input_params.zip_file_path.unlink()
            if input_params.output and input_params.output.is_file():
                input_params.output.unlink()
