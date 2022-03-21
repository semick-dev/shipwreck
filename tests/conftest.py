import sys
import os
import pytest
import shutil

from typing import Tuple
from dotenv import load_dotenv

# load up all the environment variables from .env files in the test directory
load_dotenv()

# this import makes each file directly under `helpers` available as a namespace in a test file. EG: "import context_creator.<function>"
sys.path.append(os.path.join(os.path.dirname(__file__), "helpers"))

# clean up before every session starts
def pytest_sessionstart(session):
    run_dir = os.path.join(os.path.dirname(__file__), ".run")

    if os.path.exists(run_dir):
        shutil.rmtree(run_dir)


def get_storage_key():
    return os.getenv("STORAGE_KEY")


def pytest_runtest_setup(item):
    if "live_only" in item.keywords and not get_storage_key():
        pytest.skip("LiveTest Only")


# used to determine if a test is live
@pytest.fixture(scope="session")
def is_live() -> Tuple[bool, str, str]:
    storage_key = get_storage_key()
    storage_uri = os.getenv("TEST_STORAGE_URI", "https://testaccount.blob.core.windows.net/")

    if storage_key:
        return (True, storage_key, storage_uri)

    return (False, None, storage_uri)
