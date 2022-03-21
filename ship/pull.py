from .context import ShipContext
from typing import List
from .operations import download_blob
import zipfile
import shutil
import os
import uuid


def get_real_path(context: ShipContext, staging_directory: str, staging_file_name: str) -> str:
    relative_path = staging_file_name.replace(staging_directory, "").lstrip(os.sep)
    new_target_path = os.path.join(context.target_directory, relative_path)

    return new_target_path


def create_staging_directory(context: ShipContext, staged_targz_file: str) -> str:
    staging_directory = os.path.join(context.work_directory, ".staging")

    # create the directory
    os.mkdir(staging_directory)

    # unzip into it
    shutil.unpack_archive(filename=staged_targz_file, extract_dir=staging_directory, format="gztar")

    # todo: something with symlinks here
    return staging_directory


def get_from_storage(context: ShipContext) -> str:
    name = context.config.guid

    staging_file = os.path.join(context.work_directory, "{}.tar.gz".format(name))

    # download the targeted file from storage.
    download_blob(context, name, staging_file)

    # return new guid
    return staging_file


def apply_staged_files(context: ShipContext, staging_directory: str) -> str:
    staged_files = context.get_recordings_files(staging_directory)

    for file in staged_files:
        new_path = get_real_path(context, staging_directory, file)
        os.makedirs(os.path.dirname(new_path), exist_ok=True)
        shutil.copyfile(file, new_path)

    return context.target_directory


def pull(context: ShipContext) -> None:
    staging_file = get_from_storage(context)

    staging_directory = create_staging_directory(context, staging_file)

    root_of_applied_files = apply_staged_files(context, staging_directory)
