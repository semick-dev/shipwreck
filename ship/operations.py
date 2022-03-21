from azure.storage.blob import BlobProperties, BlobClient

from .context import ShipContext

import pdb
import os


def upload_blob_from_client(context: ShipContext, client: BlobClient, file_location: str):
    with open(file_location, "rb") as data:
        result = client.upload_blob(data)
        return client.get_blob_properties()


def upload_blob(context: ShipContext, blob_name: str, file_location: str) -> BlobProperties:
    bc = context.get_blob_client(blob_name)

    with open(file_location, "rb") as data:
        result = bc.upload_blob(data)

    return bc.get_blob_properties()


def download_blob(context: ShipContext, blob_name: str, file_location: str) -> BlobProperties:
    bc = context.get_blob_client(blob_name)

    with open(file_location, "wb") as zip:
        download_stream = bc.download_blob()
        zip.write(download_stream.readall())

    return bc.get_blob_properties()
