from pynxtools_spm.nomad_uploader.reader_config_setup import (
    SPMConvertInputParameters,
    convert_spm_experiments,
)
from datetime import datetime, timedelta
from pathlib import Path
from dataclasses import asdict
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

current_dir = Path(__file__).parent
# File extensions
available_file_extensions = (".dat", ".sxm")
# Peseudo extension if upload is sucessfull
done_extensions = (".done",)
nomad_url = "https://nomad-lab.eu/prod/v1/test/api/v1/"
username = "Mozumder"
password = ""
parallel_processing = True
time_for_cron_job = 10 * 60  # seconds
copy_file_elsewhere = False  # Copy files to another location
# Mimic sucessfully uploaded raw file with `done` extension
mimic = True
exp_src_path = (
    current_dir.parent.parent.parent
    / "tests"
    / "nomad_upload"
    / "data"
    / "src_dir_tree"
)  # Where experiment files are stored after expriment by default
exp_dst_path = Path("/tmp")
modify_upload_metadata = False  # Modify metadata of the upload
publish_to_nomad = False  # Publish the upload to the central NOMAD repository

# List of SPMConvertInputParameters objects to run reader on each object
SPM_PARAMS_OBJ_L = []

def get_unprocessed_files(src_dir: Path) -> list:
    """Filter out the files that are not processed yet.

    An input file `file.dat` will be denoted as `file.dat.done` after
    successful upload to NOMAD.
    """
    process_status_map = {}
    for file in src_dir.iterdir():
        if file.is_file() and file.suffix in available_file_extensions:
            process_status_map[file] = False
    for file in src_dir.iterdir():
        if file.is_file() and file.suffix in done_extensions:
            # Remove the pseudo extension
            process_status_map[file.with_suffix("")] = True

    def get_non_processed_file(file, is_processed):
        if not is_processed:
            return file

    return list(filter(get_non_processed_file, process_status_map.items()))


def set_and_store_prepare_parameters(file):
    # sts exeriment
    sts_eln_file = exp_src_path / "sts" / "eln_data.yaml"
    sts_config_file = ""

    # stm exeriment
    stm_eln_file = exp_src_path / "stm" / "eln_data.yaml"
    stm_config_file = ""

    # afm exeriment
    afm_eln_file = ""
    afm_config_file = ""

    file_str = str(file)
    params_obj = None
    if file_str.endswith(".dat"):
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=sts_eln_file,
            expriement_type="sts",
            config=sts_config_file,
            nxdl="NXsts",
            raw_extension="dat",
            create_zip=True,
        )
    elif file_str.endswith(".sxm"):
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=stm_eln_file,
            expriement_type="stm",
            config=stm_config_file,
            nxdl="NXstm",
            raw_extension="sxm",
            create_zip=True,
        )
    elif file_str.endswith(".sxm"):
        params_obj = SPMConvertInputParameters(
            input_file=(file,),
            eln=afm_eln_file,
            expriement_type="afm",
            config=afm_config_file,
            nxdl="NXafm",
            raw_extension="sxm",
            create_zip=True,
        )
    if not params_obj:
        return
    # global SPM_PARAMS_OBJ_L
    SPM_PARAMS_OBJ_L.append(params_obj)


if __name__ == "__main__":
    token = get_authentication_token(nomad_url, username, password)
    if not token:
        print("Authentication failed!")
        exit(1)
    # In case user wants to store the files elsewhere
    if copy_file_elsewhere:
        copy_directory_structure(
            exp_src_path,
            exp_dst_path,
            run_action_on_files=set_and_store_prepare_parameters,
        )
    else:
        file_list = get_unprocessed_files(exp_src_path)

        _ = [set_and_store_prepare_parameters(file) for file in file_list]

    print("Files copied over to the destination directory.", SPM_PARAMS_OBJ_L)
    # TODO: We can use parallel processing here

    if not parallel_processing:
        pass

    lock = Lock()
    results_q = Queue()
    time_out = int(time_for_cron_job / 3)  # seconds

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

    for input_params in SPM_PARAMS_OBJ_L:
        p = Process(
            target=queue_results,
            args=(input_params, lock, results_q),
        )
        p.start()
        processes_list.append(p)
    print("Processes started...", processes_list)
    print("Processes started...", SPM_PARAMS_OBJ_L)
    for _, (p, input_params) in enumerate(zip(processes_list, SPM_PARAMS_OBJ_L)):
        p.join(time_out)
        if p.is_alive():
            print(
                f"Process is still running, terminating it. Process handles input data {asdict(input_params)}",
            )
            p.terminate()
            p.join()

    indices = []
    completed_param_objs = []
    # TODO: Get the input parameters rom the queue, on which we can delete the raw files.
    while not results_q.empty():
        completed_param_objs.append(results_q.get())
    upload_time_limit = datetime.now() + timedelta(seconds=time_out)

    while (
        len(completed_param_objs) > len(indices) and datetime.now() < upload_time_limit
    ):
        for ind, complete_param_obj in enumerate(completed_param_objs):
            zip_to_upload = complete_param_obj.zip_file_path
            if ind in indices:  # already processed or failed
                continue
            if not zip_to_upload:
                indices.append(ind)
                continue
            indices.append(ind)
            upload_id = upload_to_NOMAD(nomad_url, token, zip_to_upload)
            print(f"Upload ID: {upload_id}")
            # To modify metadata
            if modify_upload_metadata:
                dataset_id = create_dataset(nomad_url, token, "Test_Dataset")
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
                edit_upload_metadata(nomad_url, token, upload_id, metadata)

            if publish_to_nomad:
                publish_upload(nomad_url, token, upload_id)
            massage = "Adding files"
            max_attempt = 20
            attempt = 0
            while (
                not massage.startswith("Process process_upload completed successfully")
                and attempt < max_attempt
            ):
                # TODO: If upload is sucessfull, remove the zip and raw files
                attempt += 1
                massage = check_upload_status(nomad_url, token, upload_id)
                time.sleep(4 / 60)  # 4 second

            print(f"Info: Upload status: {massage}")

            if (mimic or not copy_file_elsewhere) and massage.startswith(
                "Process process_upload completed successfully"
            ):
                raw_file = list(
                    filter(
                        lambda x: x.suffix in available_file_extensions,
                        input_params.input_file,
                    )
                )[0]
                # Track if upload is sucessully done
                mimicked_file = raw_file.with_suffix(f"{raw_file.suffix}.done").touch()

    print("All done!", indices)
