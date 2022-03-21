import sys
import os
import pytest
import shutil

# this import makes each file directly under `helpers` available as a namespace in a test file. EG: "import context_creator.<function>"
sys.path.append(os.path.join(os.path.dirname(__file__), "helpers"))
from ship import RecordingConfig


def pytest_sessionstart(session):
    run_dir = os.path.join(os.path.dirname(__file__), ".run")
    shutil.rmtree(run_dir)


@pytest.fixture(scope="session")
def smtp_connection():
    pass
    # test function should accept an argument with this functions name


@pytest.fixture
def smtp_connection2():
    pass
    # test function should accept an argument with this functions name
