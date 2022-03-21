import os
from typing import List, Tuple
import sys
import shutil
import glob
import pdb

from .config import RecordingConfig


def evaluate_target_dir(target_dir: str) -> Tuple[bool, bool]:
    if os.path.isdir(target_dir):
        folder_contents = os.listdir(target_dir)
        return (
            "recording.json" in folder_contents,
            (".git" in folder_contents or os.path.dirname(target_dir) == target_dir),
        )
    else:
        raise Exception('Requested contents of folder for a file: "{}".'.format(target_dir))


def get_shipwreck_dir() -> str:
    home = "HOME"  # default for all *nix variants
    if sys.platform == "win32":
        home = "APPDATA"
    return os.path.join(os.environ[home], ".shipwreck")


class ShipContext:
    def __init__(self, temp_context_directory: str, target_directory: str, recording_config: RecordingConfig):
        """
        Parameters:
        temp_context_directory (str): The directory with which we can safely do private file operations within.
            Must be cleaned up externally.
        target_directory (str): The resolved directory of the recording.json. The directory from which push
            and pull operations will begin
        recording_config (RecordingConfig): The parsed recording.json.
        """
        self.config = recording_config
        self.work_directory = temp_context_directory
        self.target_directory = target_directory

    def clear(self):
        files = self.get_recordings_files()
        for file in files:
            os.remove(file)

    def get_recordings_files(self):
        results = []
        for pattern in self.config.recordings_patterns:
            target_glob = os.path.join(self.target_directory, pattern)
            results.extend(glob.glob(pattern, recursive=True))

        return results

    @classmethod
    def load_from_directory(cls, start_directory: str = None, optional_work_directory: str = None):
        """
        Parameters:
        start_directory (str): if a target directory was passed from command line, it should be passed in this param.
        optional_work_directory (str): If we want to keep a specific work directory rather than our APPDATA one.
        """

        # where will we work
        if optional_work_directory:
            work_dir = optional_work_directory
        else:
            work_dir = get_shipwreck_dir()

        # clean up said work directory if necessary
        if os.path.exists(work_dir):
            for item in os.listdir(work_dir):
                item_path = os.path.join(work_dir, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
        else:
            os.mkdir(work_dir)

        # resolve where we discover our recording.json
        target_dir = start_directory
        if not target_dir:
            target_dir = os.getcwd()

        found_config, reached_root = evaluate_target_dir(target_dir)

        while not reached_root and not found_config:
            target_dir, _ = os.path.split(target_dir)
            found_config, reached_root = evaluate_target_dir(target_dir)

        # we've searched for a recording json, if we have found one, target_dir will
        # contain which directory that is
        if found_config:
            config = RecordingConfig.load_from_file(os.path.join(target_dir, "recording.json"))
            return cls(work_dir, target_dir, config)
        else:
            raise Exception(
                'Unable to locate a recording json. Ascended to "/" or ".git" from directory "{}".'.format(target_dir)
            )
