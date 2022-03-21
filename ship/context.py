import os
from typing import List, Tuple
import sys
import shutil
import glob
import pdb

from azure.storage.blob import ContainerClient, BlobClient, BlobServiceClient

from .config import RecordingConfig

CONNECTION_STRING = (
    "DefaultEndpointsProtocol=https;AccountName={only_hostname};AccountKey={key};EndpointSuffix=core.windows.net"
)

# https://scottydoes.dfs.core.windows.net/test0/.docsettings.yml.7z
UPLOAD_PATTERN = "{full_hostname}/{container}/{blob_prefix}/{guid}"


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
        self.work_directory = os.path.normpath(temp_context_directory)
        self.target_directory = os.path.normpath(target_directory)
        self.recording_json = os.path.normpath(os.path.join(target_directory, "recording.json"))

    def clear(self):
        files = self.get_recordings_files()
        for file in files:
            os.remove(file)

    def get_recordings_files(self):
        results = []
        for pattern in self.config.recordings_patterns:
            target_glob = os.path.join(self.target_directory, pattern)
            results.extend(glob.glob(target_glob, recursive=True))

        return results

    def update_guid(self, new_guid: str):
        self.config.update_recording_json_guid(self.recording_json, new_guid)

    def get_connection_string(self) -> str:
        host_name = self.config.account.replace("https://", "")
        host_name = host_name[0 : host_name.index(".")]

        key = os.getenv("STORAGE_KEY")

        return CONNECTION_STRING.format(only_hostname=host_name, key=key)

    def get_container_client(self) -> ContainerClient:
        # Instantiate a BlobServiceClient using a connection string
        blob_service_client = BlobServiceClient.from_connection_string(self.get_connection_string())

        # Instantiate a ContainerClient
        container_client = blob_service_client.get_container_client(self.config.container)
        return container_client

    def get_blob_url(self, name: str) -> str:
        return os.path.normpath(os.path.join(self.config.blob_prefix, name)).replace(os.sep, "/")

    def get_blob_client(self, name: str) -> BlobClient:
        container_client = self.get_container_client()

        blob_path = self.get_blob_url(name)

        blob_client = container_client.get_blob_client(blob_path)

        return blob_client

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
