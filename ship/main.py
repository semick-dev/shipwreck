import argparse
import pdb
import os
import sys
import tempfile
import shutil

from typing import Tuple, List

from .context import ShipContext
from .config import RecordingConfig
from .push import push
from .pull import pull
from .clear import clear


def main():
    parser = argparse.ArgumentParser(
        description="This CLI app is used to push and pull service directory recordings back and forth to "
        + 'blob storage. A "reset" operation is merely clearing all discovered recordings directories. '
        + 'Same as before a "pull" operation.'
    )

    parser.add_argument(
        "command",
        type=str,
        nargs="?",
        choices=["push", "pull", "clear"],
        help="Uploading, downloading, or resetting, which do you need?",
    )

    parser.add_argument(
        "-d",
        "--directory",
        dest="directory",
        help="The directory context in which to begin the search for a recording.json. "
        + "Crawls upwards until it finds either a .git folder or recording.json. "
        + "Not providing this argument will start the search from os.getcwd().",
    )
    args = parser.parse_args()

    try:
        # find recording file, resolve target directory
        # get a recording context from resolved directory
        context = ShipContext.load_from_directory(args.directory)

        if args.command[0] == "push":
            push(context)
        elif args.command[0] == "pull":
            pull(context)
        elif args.command[0] == "clear":
            clear(context)
    finally:
        pass
