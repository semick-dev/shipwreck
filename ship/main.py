import argparse
from decimal import InvalidOperation


def main():
    parser = argparse.ArgumentParser(
        description="This CLI app is used to push and pull service directory recordings back and forth to blob storage."
    )

    parser.add_argument(
        "command",
        metavar="cmd",
        type=str,
        nargs="+",
        choices=["push", "pull"],
        help="Uploading or downloading, which do you need?",
    )

    parser.parse_args()

    if not parser.command:
        raise InvalidOperation("That is not a valid command. ")
