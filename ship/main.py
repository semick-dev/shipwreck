import argparse
import pdb
import os
from .config import RecordingConfig
from typing import Tuple, List


def resolve_target_directory(dir_from_cmd: str = None) -> Tuple[str, RecordingConfig]:
    cwd = os.getcwd()

    pass


def main():
    parser = argparse.ArgumentParser(
        description="This CLI app is used to push and pull service directory recordings back and forth to blob storage."
    )

    parser.add_argument(
        "command",
        type=str,
        nargs="?",
        choices=["push", "pull"],
        help="Uploading or downloading, which do you need?",
    )

    parser.add_argument(
        "-d",
        "--directory",
        help=(
            "The directory context in which to begin the search for a recording.json. "
            "Crawls upwards until it finds either a .git folder or recording.json. "
            "Not providing this argument will start the search from os.getcwd()."
        ),
    )
    args = parser.parse_args()

    if args.command[0] == "push":
        print("push")
    elif args.command[0] == "pull":
        print("pull")
