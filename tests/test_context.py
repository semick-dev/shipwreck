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


def test_load_from_directory_cwd(is_live):
    start_directory_name = "directory1/"

    # fmt: off
    target_directory = initialize_test_context([
        start_directory_name,
    ], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    start_directory = os.path.join(target_directory, "directory1/")

    with pushd(start_directory):
        context = ShipContext.load_from_directory(optional_work_directory=ship_working_directory)
        validate_context(context, target_directory, ship_working_directory)


def test_load_from_directory_passed(is_live):
    start_directory_name = "directory1/"

    # fmt: off
    target_directory = initialize_test_context([
        start_directory_name,
    ], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    start_directory = os.path.join(target_directory, "directory1/")
    context = ShipContext.load_from_directory(
        start_directory=start_directory, optional_work_directory=ship_working_directory
    )
    validate_context(context, target_directory, ship_working_directory)


def test_load_internal_temp_dir(is_live):
    start_directory_name = "directory1/"

    # fmt: off
    target_directory = initialize_test_context([
        start_directory_name,
    ], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(start_directory=target_directory)
    validate_context(context, target_directory, get_shipwreck_dir())


def test_context_creation_filled_work_directory(is_live):
    # fmt: off
    target_directory = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], RECORDING_JSON.replace("{}", (is_live[2])))
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


def test_context_create_finds_recording_json_at_root(is_live):
    # fmt: off
    target_directory = initialize_test_context([], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )
    validate_context(context, target_directory, ship_working_directory)


def test_context_create_fails_without_recording_json_present(is_live):
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


def test_context_gets_connection_string(is_live):
    # fmt: off
    target_directory = initialize_test_context([], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    cs = context.get_connection_string()

    assert cs is not None


def test_context_gets_blob_url(is_live):
    # fmt: off
    target_directory = initialize_test_context([], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )
    blobname = "blob1"
    cs = context.get_blob_url(blobname)

    assert cs is not None
    assert blobname in cs


def test_context_updates_target_guid(is_live):
    # fmt: off
    target_directory = initialize_test_context([], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    new_guid = "new_guid"
    context.update_guid(new_guid)

    with open(context.recording_json, "r") as f:
        json_contents = json.loads(f.read())

    result = json_contents["targeting"]["guid"]

    assert result == new_guid


@pytest.mark.live_only
def test_context_gets_container_client(is_live):
    # fmt: off
    target_directory = initialize_test_context([], RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    container_client = context.get_container_client()
    results = container_client.list_blobs()
    assert results is not None
