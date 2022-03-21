from azure.storage.blob import BlobServiceClient
from .context import ShipContext
from azure.storage.blob import BlobClient

import pdb


def upload_blob_from_client(context: ShipContext, client: BlobClient, file_location: str):
    with open(file_location, "rb") as data:
        result = client.upload_blob(data)
        pdb.set_trace()


def upload_blob(context: ShipContext, blob_name: str, file_location: str):
    bc = context.get_blob_client(blob_name)

    with open(file_location, "rb") as data:
        result = bc.upload_blob(data)
        pdb.set_trace()
