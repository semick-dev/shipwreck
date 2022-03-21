import os
import sys
import shutil
import uuid
import pdb

from typing import List
from .context import ShipContext

def get_staging_path(context: ShipContext, staging_directory: str, file_name: str) -> str:
    relative_path = file_name.replace(context.target_directory, "").lstrip(os.sep)
    new_staging_path = os.path.join(staging_directory, relative_path)

    return new_staging_path


def stage_files(context: ShipContext, file_list: List[str]) -> str:
    # copy files in list to new context
    staging_directory = os.path.join(context.work_directory, ".staging")

    # create the directory
    os.mkdir(staging_directory)

    # todo optimize this. is is slow as hell but works for a demo
    for file in file_list:
        new_path = get_staging_path(context, staging_directory, file)
        os.makedirs(os.path.dirname(new_path),exist_ok=True)
        shutil.copyfile(file, new_path)
    
    # todo: something with symlinks here for optimization
    return staging_directory


def create_context_file(context: ShipContext, file_list: List[str]) -> None:
    # copy files in list to new context

    # todo: something with symlinks here
    pass


def write_to_storage(context: ShipContext, root_dir: str) -> str:
    new_guid = uuid.uuid4()

    # zip the contents of the staging directory

    # return new guid
    return new_guid


def push(context: ShipContext) -> None:
    all_files = context.get_recordings_files()

    # write them to the work directory
    staged_files = stage_files(context, all_files)

    # zip em and write to storage
    new_guid = write_to_storage(context, staged_files)

    # update the local reference
    context.update_guid(new_guid)
