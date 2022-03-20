import json
from typing import List, Tuple

class RecordingConfig:
    def __init__(
        self, blob_prefix: str, recordings_patterns: List[str], account: str, container: str, guid: str
    ) -> None:
        self.blob_prefix = name  # instance attribute
        self.recordings_patterns = age  # instance attribute
        self.account = account
        self.container = container
        self.guid = guid

    def parse_init_tuple(self, json_content: str) -> Tuple[str, List[str], str, str, str]:
        prefix = json_config["configuration"]["blob_prefix"]
        patterns = json_config["configuration"]["recordings_directory_patterns"]
        account = json_config["configuration"]["storage_account"]
        container = json_config["configuration"]["storage_account_container"]
        guid = json_config["targeting"]["guid"]

        return Tuple[refix, patterns, account, container, guid]

    @classmethod
    def load_from_file(cls, json_path: str):
        with open(json_path, "r") as f:
            json_config = json.loads(f.read())

        return cls(*self.parse_init_tuple(json_config))

    @classmethod
    def load_from_json(cls, json_path: str):
        return cls(*self.parse_init_tuple(json_config))
