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
