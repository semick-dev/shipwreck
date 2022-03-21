from test_context_creator import initialize_test_context
from ship import RecordingConfig
from utils import pushd
import os
import pdb


def validate_recording_config(
    recording_config: RecordingConfig, expected_targeting_guid: str, expected_patterns_length: int
) -> None:
    assert recording_config.blob_prefix is not None
    assert len(recording_config.recordings_patterns) == expected_patterns_length
    assert recording_config.account is not None
    assert recording_config.container is not None
    assert recording_config.guid == expected_targeting_guid


def test_file_parse():
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

    test_context = initialize_test_context([], None)
    temporary_file = os.path.join(test_context, "recording.json")
    with open(temporary_file, "w") as f:
        f.write(recording_json)

    recording_config = RecordingConfig.load_from_file(temporary_file)

    validate_recording_config(recording_config, "abc321", 0)


def test_json_content_parse():
    recording_json = (
        "{"
        '"configuration": {'
        '"assets-prefix-path": "recordings/",'
        '"blob_prefix": "sdk/tables/",'
        '"recordings_directory_patterns": [ "**/tests/recordings/*.json", "**/test/recordings/*.json" ],'
        '"storage_account": "https://testaccount.blob.core.windows.net/",'
        '"storage_account_container": "test0"'
        "},"
        '"targeting": {'
        '    "guid": "abc123"'
        "}"
        "}"
    )

    recording_config = RecordingConfig.load_from_json_string(recording_json)

    validate_recording_config(recording_config, "abc123", 2)
    pass
