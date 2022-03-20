import sys
import os
import pytest

# this import makes each file directly under `helpers` available as a namespace in a test file. EG: "import context_creator.<function>"
sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

from ship import RecordingConfig

@pytest.fixture
def create_test_context(config: RecordingConfig):
    pass

@pytest.fixture(scope="session")
def smtp_connection():
    pass
    # test function should accept an argument with this functions name

@pytest.fixture
def smtp_connection2():
    pass
    # test function should accept an argument with this functions name
