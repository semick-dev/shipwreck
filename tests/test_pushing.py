# "pushing" is the action of zipping up a service directory along with all the discovered recordings directories
from test_context_creator import initialize_test_context
from ship import RecordingConfig
from utils import pushd
import os
import pdb


def test_push_entirely_empty_directory():
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/",
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [],
            "storage_account": "https://testaccount.blob.core.windows.net/",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": "abc321"
        }
    }"""
    # fmt: off
    test_context = initialize_test_context([], recording_json or None)
    # fmt: on

    pass


def test_push_files_in_single_directory():
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/",
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [],
            "storage_account": "https://testaccount.blob.core.windows.net/",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": "abc321"
        }
    }"""
    # fmt: off
    test_context = initialize_test_context([], recording_json or None)
    # fmt: on

    pass


def test_push_files_in_multiple_directories():
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/", 
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [],
            "storage_account": "https://testaccount.blob.core.windows.net/",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": "abc321"
        }
    }"""
    # fmt: off
    test_context = initialize_test_context([], recording_json or None)
    # fmt: on

    pass


def test_push_files_in_multiple_directories_with_non_json_present():
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/", 
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [],
            "storage_account": "https://testaccount.blob.core.windows.net/",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": "abc321"
        }
    }"""
    # fmt: off
    test_context = initialize_test_context([], recording_json or None)
    # fmt: on

    pass
