from azure.storage.blob import BlobServiceClient
from ship.context import ShipContext

CONNECTION_STRING = (
    "DefaultEndpointsProtocol=https;AccountName=",
    "{hostname};AccountKey={key};EndpointSuffix=core.windows.net",
)


def get_service_content(context: ShipContext) -> BlobServiceClient:
    pass
