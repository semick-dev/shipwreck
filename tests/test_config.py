from context_creator import initialize_test_context
from ship.config import RecordingConfig
from utils import pushd
import os
import pdb


def test_file_parse():
    recording_json = """{
        "configuration": {
            "assets-prefix-path": "recordings/", 
            "blob_prefix": "sdk/tables/",
            "recordings_directory_patterns": [ "**/tests/recordings/*.json"],
            "storage_account": "https://testaccount.blob.core.windows.net/",
            "storage_account_container": "test0"
        },
        "targeting": {
            "guid": ""
        }
    }"""

    # fmt: off
    test_context = initialize_test_context([], None)

    temporary_file = os.path.join(test_context, "recording.json")
    
    with open(temporary_file, "w") as f:
        f.write(recording_json)

    recording_config = RecordingConfig.load_from_file(temporary_file)
    pdb.set_trace()

    # fmt: on
    pass

def test_json_content_parse():
    recording_json = ("{"
        '"configuration": {'
            '"assets-prefix-path": "recordings/",'
            '"blob_prefix": "sdk/tables/",'
            '"recordings_directory_patterns": [ "**/tests/recordings/*.json"],'
            '"storage_account": "https://testaccount.blob.core.windows.net/",'
            '"storage_account_container": "test0"'
        '},'
        '"targeting": {'
        '    "guid": ""'
        '}'
    '}')

    # fmt: off
    recording_config = RecordingConfig.load_from_json_string(recording_json)

    pdb.set_trace()

    # fmt: on
    pass