import os
import sys
import shutil
import uuid
import pdb

from typing import List
from .context import ShipContext
from .operations import upload_blob


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
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        shutil.copyfile(file, new_path)

    # todo: something with symlinks here for optimization
    return staging_directory


def create_artifact(context: ShipContext, staging_directory: str, new_guid: str) -> None:
    basename = os.path.join(context.work_directory, new_guid)
    result = shutil.make_archive(basename, "gztar", staging_directory)

    return result


def write_to_storage(context: ShipContext, staged_path: str) -> str:
    new_guid = str(uuid.uuid4())
    compressed_path = create_artifact(context, staged_path, new_guid)
    result = upload_blob(context, new_guid, compressed_path)

    # return new guid
    return new_guid


def push(context: ShipContext) -> None:
    all_files = context.get_recordings_files()
   
    staged_files = stage_files(context, all_files)

    new_guid = write_to_storage(context, staged_files)

    # update the local reference
    context.update_guid(new_guid)
