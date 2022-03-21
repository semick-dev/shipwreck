from test_context_creator import initialize_test_context, get_test_name
from utils import pushd

from ship import (
    ShipContext,
    stage_files,
    ShipContext,
    create_artifact,
    upload_blob,
    write_to_storage,
    get_from_storage,
    create_staging_directory,
    pull,
)
from common import PLACEHOLDER_KNOWN_PRESENT_BLOB

import os
import pdb
import pytest
import json
import uuid

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
}""".replace(
    "abc321", PLACEHOLDER_KNOWN_PRESENT_BLOB
)

from test_pushing import STAGED_FILES_JSON_ONLY, STAGED_FILES_INCLUDING_NON_NON_JSON, STAGED_FILES_JSON_ONLY


@pytest.mark.live_only
def test_operations_upload_blob_from_name(is_live):
    # fmt: off
    target_directory = initialize_test_context(STAGED_FILES_JSON_ONLY, RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    files = context.get_recordings_files()
    staged_path = stage_files(context, files)
    new_guid = str(uuid.uuid4())
    compressed_path = create_artifact(context, staged_path, new_guid)

    result = upload_blob(context, new_guid, compressed_path)
    assert result.last_modified is not None


@pytest.mark.live_only
def test_operations_upload_blob_from_client(is_live):
    # fmt: off
    target_directory = initialize_test_context(STAGED_FILES_JSON_ONLY, RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    files = context.get_recordings_files()
    staged_path = stage_files(context, files)
    result = write_to_storage(context, staged_path)

    assert result is not None


@pytest.mark.live_only
def test_operations_download_from_name(is_live):
    # fmt: off
    target_directory = initialize_test_context(STAGED_FILES_JSON_ONLY, RECORDING_JSON.replace("{}", (is_live[2])))
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    result = get_from_storage(context)
