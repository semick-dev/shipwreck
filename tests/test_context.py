from test_context_creator import initialize_test_context, get_test_name
from utils import pushd

from ship import ShipContext, get_shipwreck_dir
from test_config import validate_recording_config

import os
import pdb

RECORDING_JSON_GUID: str = "abc321"
RECORDING_JSON_PATTERNS_LENGTH: int = 2
RECORDING_JSON: str = """{
    "configuration": {
        "assets-prefix-path": "recordings/", 
        "blob_prefix": "sdk/tables/",
        "recordings_directory_patterns": [ "**/tests/recordings/*.json", "**/test/recordings/*.json" ],
        "storage_account": "https://testaccount.blob.core.windows.net/",
        "storage_account_container": "test0"
    },
    "targeting": {
        "guid": "abc321"
    }
}"""


def test_load_from_directory_cwd():
    start_directory_name = "directory1/"

    # fmt: off
    target_directory = initialize_test_context([
        start_directory_name,
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    start_directory = os.path.join(target_directory, "directory1/")

    with pushd(start_directory):
        context = ShipContext.load_from_directory(optional_work_directory=ship_working_directory)
        validate_recording_config(context.config, RECORDING_JSON_GUID, RECORDING_JSON_PATTERNS_LENGTH)


def test_load_from_directory_passed():
    start_directory_name = "directory1/"

    # fmt: off
    target_directory = initialize_test_context([
        start_directory_name,
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    start_directory = os.path.join(target_directory, "directory1/")

    context = ShipContext.load_from_directory(
        start_directory=start_directory, optional_work_directory=ship_working_directory
    )
    validate_recording_config(context.config, RECORDING_JSON_GUID, RECORDING_JSON_PATTERNS_LENGTH)


def test_load_internal_temp_dir():
    start_directory_name = "directory1/"

    # fmt: off
    target_directory = initialize_test_context([
        start_directory_name,
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(start_directory=target_directory)

    validate_recording_config(context.config, RECORDING_JSON_GUID, RECORDING_JSON_PATTERNS_LENGTH)


def test_context_creation_empty_directory():
    # fmt: off
    target_directory = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on


def test_context_creation_filled_directory():
    # fmt: off
    target_directory = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on
    pass


def test_context_create_start_below_recording_json():
    # fmt: off
    target_directory = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on


def test_context_create_fails_without_recording_json_present():
    # fmt: off
    target_directory = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on


def test_context_creation_filled_directory():
    # fmt: off
    target_directory = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on
    pass
