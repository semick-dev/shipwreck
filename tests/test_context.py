from test_context_creator import initialize_test_context, get_test_name
from utils import pushd

from ship import ShipContext, get_shipwreck_dir
from test_config import validate_recording_config

import os
import pdb
import pytest

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


def validate_context(
    context: ShipContext,
    expected_target_dir: str,
    expected_work_dir: str,
    json_guid: str = RECORDING_JSON_GUID,
    json_patterns_length: int = RECORDING_JSON_PATTERNS_LENGTH,
):
    validate_recording_config(context.config, json_guid, json_patterns_length)
    assert context.work_directory == expected_work_dir
    assert context.target_directory == expected_target_dir


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
        validate_context(context, target_directory, ship_working_directory)


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
    validate_context(context, target_directory, ship_working_directory)


def test_load_internal_temp_dir():
    start_directory_name = "directory1/"

    # fmt: off
    target_directory = initialize_test_context([
        start_directory_name,
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(start_directory=target_directory)
    validate_context(context, target_directory, get_shipwreck_dir())


def test_context_creation_filled_work_directory():
    # fmt: off
    target_directory = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], RECORDING_JSON)
    ship_working_directory = initialize_test_context([
        "test1.json"
        "directory1/test30.json",
        "directory1/test1.json",
        "directory2/test30.json",
        "directory3/directory4/test1.json"
    ], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )
    validate_context(context, target_directory, ship_working_directory)

    # this should always be emptied when we start!
    assert len(os.listdir(ship_working_directory)) == 0


def test_context_create_finds_recording_json_at_root():
    # fmt: off
    target_directory = initialize_test_context([], RECORDING_JSON)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )
    validate_context(context, target_directory, ship_working_directory)


def test_context_create_fails_without_recording_json_present():
    # fmt: off
    target_directory = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], None)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on
    start_directory = os.path.join(target_directory, "directory1/")
    with pytest.raises(Exception) as exception:
        context = ShipContext.load_from_directory(
            start_directory=start_directory, optional_work_directory=ship_working_directory
        )
    assert "Unable to locate a recording json." in str(exception)
