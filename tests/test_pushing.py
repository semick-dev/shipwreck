# "pushing" is the action of zipping up a service directory along with all the discovered recordings directories
from test_context_creator import initialize_test_context
from utils import pushd

from ship import RecordingConfig

import os
import pdb
import pytest


@pytest.mark.live_only
def test_push_entirely_empty_directory(is_live):
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
    test_context = initialize_test_context([], recording_json)
    # fmt: on

    pass


@pytest.mark.live_only
def test_push_files_in_single_directory(is_live):
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
    test_context = initialize_test_context([], recording_json)
    # fmt: on

    pass


@pytest.mark.live_only
def test_push_files_in_multiple_directories(is_live):
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
    test_context = initialize_test_context([], recording_json)
    # fmt: on

    pass


@pytest.mark.live_only
def test_push_files_in_multiple_directories_with_non_json_present(is_live):
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
    test_context = initialize_test_context([], recording_json)
    # fmt: on

    pass
