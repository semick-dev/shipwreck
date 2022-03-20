import json
from typing import List, Tuple
import pdb
import os


def parse_init_tuple(json_content: str) -> Tuple[str, List[str], str, str, str]:
    content = json_content.replace("\n", "")
    json_config = json.loads(content)

    prefix = json_config["configuration"]["blob_prefix"]
    patterns = json_config["configuration"]["recordings_directory_patterns"]
    account = json_config["configuration"]["storage_account"]
    container = json_config["configuration"]["storage_account_container"]
    guid = json_config["targeting"]["guid"]

    return (prefix, patterns, account, container, guid)


class RecordingConfig:
    def __init__(
        self, blob_prefix: str, recordings_patterns: List[str], account: str, container: str, guid: str
    ) -> None:
        self.blob_prefix = blob_prefix
        self.recordings_patterns = recordings_patterns
        self.account = account
        self.container = container
        self.guid = guid

    @classmethod
    def load_from_file(cls, json_path: str):
        with open(json_path, "r") as f:
            json_content = f.read()

        arg = parse_init_tuple(json_content)
        return cls(*arg)

    @classmethod
    def load_from_json_string(cls, json_content: str):
        return cls(*parse_init_tuple(json_content))
