from pathlib import Path
from typing import List
import shutil
import os
import pdb
import uuid

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))


def get_test_name() -> str:
    name = os.environ.get("PYTEST_CURRENT_TEST")
    test_name = name.split("::")[1]
    return test_name.split(" ")[0]


def create_target_directory(optional_test_name: str = None) -> str:
    test_name = optional_test_name or get_test_name()
    target_directory = os.path.abspath(os.path.join(root_dir, "tests", ".run", test_name))

    if os.path.exists(target_directory):
        shutil.rmtree(target_directory)

    Path(target_directory).mkdir(parents=True, exist_ok=False)

    return target_directory


def initialize_test_context(
    folder_structure_list: List[str], recording_json_content: str = None, test_name: str = None
) -> str:
    target_directory = create_target_directory(test_name)
    possible_recording_json_location = [path for path in folder_structure_list if path.endswith("recording.json")]
    if any(possible_recording_json_location):
        if len(possible_recording_json_location) > 1:
            raise Exception("Misconfigured test, you cannot place multiple custom recording.json locations.")
        target_recording_json = possible_recording_json_location[0]
    else:
        target_recording_json = os.path.join(target_directory, "recording.json")

    if recording_json_content:
        with open(target_recording_json, "w") as f:
            f.write(recording_json_content)

    for path in folder_structure_list:
        ext = os.path.splitext(os.path.normpath(path))[1]
        if ext:
            resolved_path = os.path.join(target_directory, os.path.normpath(path))
            resolved_target_directory = os.path.dirname(resolved_path)

            if not os.path.exists(resolved_target_directory):
                Path(resolved_target_directory).mkdir(parents=True, exist_ok=True)

            if ext == ".json" and not path.endswith("recording.json"):
                with open(resolved_path, "w") as f:
                    f.write('{ "a": "' + str(uuid.uuid4()) + '" }')
            elif ext == ".yml":
                with open(resolved_path, "w") as f:
                    f.write("- list item!")
        else:
            resolved_path = os.path.join(target_directory, path)
            Path(resolved_path).mkdir(parents=True, exist_ok=True)

    return target_directory
