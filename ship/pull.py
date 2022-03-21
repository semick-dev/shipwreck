from .context import ShipContext
from typing import List

import os
import uuid


def stage_files(context: ShipContext) -> str:
    staging_directory = os.path.join(context.work_directory, ".staging")

    # create the directory
    os.mkdir(staging_directory)

    # todo: something with symlinks here
    return staging_directory


def create_context_file(context: ShipContext, file_list: List[str]) -> None:
    # copy files in list to new context

    # todo: something with symlinks here
    pass


def get_from_storage(context: ShipContext) -> str:
    newfile = os.path.join(context.work_directory, "content.tar.gz")

    # download the targeted file from storage.

    # return new guid
    return newfile


def pull(context: ShipContext) -> None:
    print("pull")
