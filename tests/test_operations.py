from test_context_creator import initialize_test_context, get_test_name
from utils import pushd

from ship import ShipContext, get_shipwreck_dir
from test_config import validate_recording_config

import os
import pdb
import pytest
import json

RECORDING_JSON_GUID: str = "abc321"
RECORDING_JSON_PATTERNS_LENGTH: int = 2
RECORDING_JSON: str = """{
    "configuration": {
        "assets-prefix-path": "recordings/", 
        "blob_prefix": "sdk/tables/",
        "recordings_directory_patterns": [ "**/tests/recordings/*.json", "**/test/recordings/*.json" ],
        "storage_account": "{}",
        "storage_account_container": "test0"
    },
    "targeting": {
        "guid": "abc321"
    }
}"""

@pytest.mark.live_only
def test_operations_upload_blob_from_name(is_live):
    # fmt: off
    target_directory = initialize_test_context([], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

@pytest.mark.live_only
def test_operations_upload_blob_from_client(is_live):
    # fmt: off
    target_directory = initialize_test_context([], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on
    
    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    