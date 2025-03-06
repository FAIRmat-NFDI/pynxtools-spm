from pynxtools_spm.nomad_uploader.reader_config_setup import (
    SPMConvertInputParameters,
    convert_spm_experiments,
)
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from dataclasses import asdict, dataclass
import time

from pynxtools_spm.nomad_uploader.nomad_upload_api import (
    get_authentication_token,
    create_dataset,
    upload_to_NOMAD,
    edit_upload_metadata,
    publish_upload,
    check_upload_status,
)
from pynxtools_spm.nomad_uploader.files_movers import copy_directory_structure

from multiprocessing import Process, Lock, Queue


debug = True
current_dir = Path(__file__).parent

@dataclass
class NOMADSettings:
    url_protocol: str = "https"
    url_domain: str = "nomad-lab.eu"
    url_version: str = "prod/v1/api/v1/"
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
        current_dir.parent.parent.parent / "tests" / "data" / "cronJobTest"
    )
    copy_file_elsewhere: bool = False
    # Destination directory for the experiment files, if files are moved
    # to another location after processing is done, needs `copy_file_elsewhere`
    # to be True
    dst_dir: Optional[Path] = "/tmp"
    # create and empty file if upload is sucessfull
    create_pseudo_file: bool = True
    # Extension to the empty file if upload is sucessfull
    pseudo_exts: str = ".done"
    # List of SPMConvertInputParameters objects to run reader on each object
    spm_params_obj_l = []
    sts_eln = (
        src_dir
        / ".."
        / "nanonis"
        / "sts"
        / "version_gen_5e_with_described_nxdata"
        / "eln_data.yaml"
    )
    sts_config = ""
    stm_eln = (
        src_dir
        / ".."
        / "nanonis"
        / "stm"
        / "version_gen_4_5_with_described_nxdata"
        / "eln_data.yaml"
    )
    stm_config = ""
    afm_eln = (
        src_dir
        / ".."
        / "nanonis"
        / "afm"
        / "version_gen_4_with_described_nxdata"
        / "eln_data.yaml"
    )
    afm_config = ""


def get_unprocessed_files(src_dir: Path) -> list:
    """Filter out the files that are not processed yet.

    E.g. an input file `file.dat` will be denoted as `file.dat.done` after
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
        file, is_processed = arg[0], arg[1]
        if not is_processed:
            return file

    return list(map(filter_non_processed_file, process_status_map.items()))


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
        if (
            not DataProcessingSettings.dst_dir
            or not DataProcessingSettings.dst_dir.is_dir()
        ):
            print(
                "Porcess Exits: Destination directory is required to store the files."
            )
            exit(1)

        copy_directory_structure(
            DataProcessingSettings.src_dir,
            DataProcessingSettings.dst_dir,
            run_action_on_files=set_and_store_prepared_parameters,
        )
    else:
        file_list = get_unprocessed_files(DataProcessingSettings.src_dir)
        # Prepare the input parameters for the SPM reader for each file
        _ = [
            set_and_store_prepared_parameters(file)
            for file in file_list
            if (file and file.is_file())
        ]
        print("Process Info: Files to process", file_list)

    if debug:
        print(
            "Debug: Files copied over to the destination directory.",
            DataProcessingSettings.spm_params_obj_l,
        )
    # TODO: We Need scrutiny observation for parallel processing

    if not DataProcessingSettings.parallel_processing:
        pass

    lock = Lock()
    results_q = Queue()
    time_out = int(DataProcessingSettings.single_batch_processing_time / 3)  # seconds

    def queue_results(input_params, lock, results_q):
        lock.acquire()
        try:
            result = convert_spm_experiments(input_params)
            results_q.put(result)
        except Exception as e:
            print(f"Oops! Error in processing {input_params.input_file}: {e}")
            raise e
        finally:
            lock.release()

    processes_list = []

    for input_params in DataProcessingSettings.spm_params_obj_l:
        p = Process(
            target=queue_results,
            args=(input_params, lock, results_q),
        )
        p.start()
        processes_list.append(p)
    if debug:
        print("Debug: Processes started...", processes_list)
        print("DEbug: Processes started...", DataProcessingSettings.spm_params_obj_l)
    for _, (p, input_params) in enumerate(
        zip(processes_list, DataProcessingSettings.spm_params_obj_l)
    ):
        p.join(time_out)
        if p.is_alive():
            print(
                f"Process is still running, terminating it. Process handles input data {asdict(input_params)}",
            )
            p.terminate()
            p.join()

    indices = []
    completed_param_objs = []
    while not results_q.empty():
        # Get back input_params obj with output files
        completed_param_objs.append(results_q.get())
    upload_time_limit = datetime.now() + timedelta(seconds=time_out)

    while (
        len(completed_param_objs) > len(indices) and datetime.now() < upload_time_limit
    ):
        sucess_ind = []
        failed_ind = []
        for ind, complete_param_obj in enumerate(completed_param_objs):
            zip_to_upload = complete_param_obj.zip_file_path
            if ind in indices:  # already processed or failed
                continue
            if not zip_to_upload:
                indices.append(ind)
                continue
            indices.append(ind)
            massage = "Adding files"
            max_attempt = 20
            attempt = 0
            try:
                upload_id = upload_to_NOMAD(
                    NOMADSettings.url, NOMADSettings.token, zip_to_upload
                )
                massage = check_upload_status(
                    NOMADSettings.url, NOMADSettings.token, upload_id
                )
                print(f"Process Info: Upload ID: {upload_id}")
                sucess_ind.append(ind)
            except Exception as e:
                print(f"Error in uploading {zip_to_upload}: {e}")
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

            while (
                not massage.startswith("Process process_upload completed successfully")
                and attempt < max_attempt
            ):
                attempt += 1
                massage = check_upload_status(
                    NOMADSettings.url, NOMADSettings.token, upload_id
                )
                time.sleep(4 / 60)  # 4 second

            print(f"Process Info: Upload status: {massage}")
        for ind, input_params in enumerate(completed_param_objs):
            raw_file = list(
                filter(
                    lambda x: x.suffix in DataProcessingSettings.raw_file_exts,
                    input_params.input_file,
                )
            )[0]
            # Clean up the files generated during the process
            if input_params.zip_file_path and input_params.zip_file_path.is_file():
                input_params.zip_file_path.unlink()
            if input_params.output and input_params.output.is_file():
                input_params.output.unlink()
            if (
                DataProcessingSettings.create_pseudo_file
                or not DataProcessingSettings.copy_file_elsewhere
            ):
                # Track if upload is successfully done
                pseudo_file = raw_file.with_suffix(
                    f"{raw_file.suffix}{DataProcessingSettings.pseudo_exts}"
                )
                pseudo_file.touch()
                # remove the mimicked file if upload is failed
                if pseudo_file and ind in failed_ind:
                    pseudo_file.unlink()
            elif DataProcessingSettings.copy_file_elsewhere:
                # As raw file stored in other location, remove it
                raw_file.unlink()

    print("Process Info: All done!")
