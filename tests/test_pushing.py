# "pushing" is the action of zipping up a service directory along with all the discovered recordings directories
from test_context_creator import initialize_test_context, get_test_name
from utils import pushd

from ship import stage_files, ShipContext

import os
import pdb
import pytest


STAGED_FILES_INCLUDING_NON_NON_JSON = [
        "azure-data-tables/tests/recordings/test_retry_async.pyTestStorageRetrytest_no_retry.json",
        "azure-data-tables/src/recordings/recording_like_named_project.py",
        "azure-data-tables/src/recordings/recording_like_named_project_content.yml",
        "azure-data-tables/tests/async/recordings/test_retry_async.pyTestStorageRetryAsynctest_no_retry_async.json"
]

STAGED_FILES_SINGLE_DIRECTORY = [
    "tests/recordings/test_retry.pyTestStorageRetrytest_no_retry.json",
    "tests/recordings/test_retry.pyTestStorageBlobClienttest_upload_blob.json"
]

STAGED_FILES_JSON_ONLY = [
    "azure-data-tables/tests/recordings/test_retry_async.pyTestStorageRetrytest_no_retry.json",
    "azure-data-tables/tests/async/recordings/test_retry_async.pyTestStorageRetryAsynctest_no_retry_async.json"
]

def test_push_files_in_single_directory(is_live):
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/", 
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [ "**/tests/recordings/*.json", "**/test/recordings/*.json" ],
            "storage_account": "{}",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": "abc123"
        }
    }""".replace(
        "{}", (is_live[2])
    )

    # fmt: off
    target_directory = initialize_test_context(STAGED_FILES_SINGLE_DIRECTORY, recording_json)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on
    
    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    files = context.get_recordings_files()
    staged_path = stage_files(context, files)
    initial_contents = os.listdir(staged_path)
    
    assert(len(initial_contents) > 0)

def test_push_stage_files_in_multiple_directories(is_live):
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/", 
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [ "**/tests/recordings/*.json", "**/test/recordings/*.json" ],
            "storage_account": "{}",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": "abc123"
        }
    }""".replace(
        "{}", (is_live[2])
    )

    # fmt: off
    target_directory = initialize_test_context(STAGED_FILES_JSON_ONLY, recording_json)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on
    
    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    files = context.get_recordings_files()
    staged_path = stage_files(context, files)
    initial_contents = os.listdir(staged_path)

    assert(len(initial_contents) > 0)

# @pytest.mark.live_only
def test_push_stage_files_in_multiple_directories_with_non_json_present(is_live):
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/", 
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [ "**/tests/recordings/*.json", "**/test/recordings/*.json" ],
            "storage_account": "{}",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": "abc123"
        }
    }""".replace(
        "{}", (is_live[2])
    )
    
    # fmt: off
    target_directory = initialize_test_context(STAGED_FILES_INCLUDING_NON_NON_JSON, recording_json)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on
    
    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )
    
    files = context.get_recordings_files()
    staged_path = stage_files(context, files)
    initial_contents = os.listdir(staged_path)

    assert(len(initial_contents) > 0)


# @pytest.mark.live_only
def test_push_stage_files_empty_directory(is_live):
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/", 
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [ "**/tests/recordings/*.json", "**/test/recordings/*.json" ],
            "storage_account": "{}",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": "abc123"
        }
    }""".replace(
        "{}", (is_live[2])
    )

    # fmt: off
    target_directory = initialize_test_context([], recording_json)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on
    
    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    files = context.get_recordings_files()
    staged_path = stage_files(context, files)
    initial_contents = os.listdir(staged_path)

    assert(len(initial_contents) == 0)
