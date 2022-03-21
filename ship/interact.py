from ship.context import ShipContext
from .config import RecordingConfig


def pull(context: ShipContext) -> None:
    print("pull")


def push(context: ShipContext) -> None:
    # find
    print("push")
