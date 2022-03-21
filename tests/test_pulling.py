# "pulling" is the action of pulling a blob from a storage location decompressing it into temporary folder structure, and then populating in the target directories
from test_context_creator import initialize_test_context, get_test_name
from tests.test_operations import RECORDING_JSON
from utils import pushd
from ship.pull import pull, create_staging_directory, get_from_storage, apply_staged_files
import pytest
import os

from ship import ShipContext
from test_pushing import STAGED_FILES_SINGLE_DIRECTORY
from common import PLACEHOLDER_KNOWN_PRESENT_BLOB

PULL_RECORDING_JSON = """{
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
}"""


@pytest.mark.live_only
def test_pull_get_from_storage_filled_directory_structure(is_live):
    recording_json = PULL_RECORDING_JSON.replace("{}", (is_live[2])).replace("abc123", PLACEHOLDER_KNOWN_PRESENT_BLOB)

    # fmt: off
    target_directory = initialize_test_context(STAGED_FILES_SINGLE_DIRECTORY, recording_json)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    staged_zip = get_from_storage(context)

    assert staged_zip is not None


@pytest.mark.live_only
def test_pull_create_staging_directory_entirely_empty_directory_structure(is_live):
    recording_json = PULL_RECORDING_JSON.replace("{}", (is_live[2])).replace("abc123", PLACEHOLDER_KNOWN_PRESENT_BLOB)

    # fmt: off
    target_directory = initialize_test_context([], recording_json)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    staged_zip = get_from_storage(context)
    staging_directory = create_staging_directory(context, staged_zip)

    assert len(os.listdir(staging_directory)) > 0


@pytest.mark.live_only
def test_pull_apply_staged_files_entirely_filled_directory_structure(is_live):
    recording_json = PULL_RECORDING_JSON.replace("{}", (is_live[2])).replace("abc123", PLACEHOLDER_KNOWN_PRESENT_BLOB)

    # fmt: off
    target_directory = initialize_test_context(STAGED_FILES_SINGLE_DIRECTORY, recording_json)
    ship_working_directory = initialize_test_context([], None, get_test_name() + "_working")
    # fmt: on

    context = ShipContext.load_from_directory(
        start_directory=target_directory, optional_work_directory=ship_working_directory
    )

    staged_zip = get_from_storage(context)
    staging_directory = create_staging_directory(context, staged_zip)
    apply_staged_files(context, staging_directory)
