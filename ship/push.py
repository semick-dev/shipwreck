from .context import ShipContext


def push(context: ShipContext) -> None:
    all_files = context.get_recordings_files()

    # find
    print("push")
