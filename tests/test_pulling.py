# "pulling" is the action of pulling a blob from a storage location decompressing it into temporary folder structure, and then populating in the target directories
from test_context_creator import initialize_test_context
from utils import pushd
from ship import pull
import pytest

# example expected pytest exception
# with pytest.raises(RuntimeError) as excinfo:

#     def f():
#         f()

#     f()
# assert "maximum recursion" in str(excinfo.value)


@pytest.mark.live_only
def test_pull_entirely_empty_directory_structure(is_live):
    recording_json = """

    """

    # fmt: off
    test_context = initialize_test_context([], recording_json)
    # fmt: on
    pass


@pytest.mark.live_only
def test_pull_partially_present_directory_structure(is_live):
    recording_json = """

    """

    # fmt: off
    test_context = initialize_test_context([
        "directory1/",
        "directory2/",
        "directory3/directory4/"
    ], recording_json)
    # fmt: on
    pass


@pytest.mark.live_only
def test_pull_partially_filled_directory_structure(is_live):
    recording_json = """

    """

    # fmt: off
    test_context = initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ], recording_json)
    # fmt: on

    pass


@pytest.mark.live_only
def test_pull_entirely_filled_directory_structure(is_live):
    recording_json = """

    """

    # fmt: off
    initialize_test_context([
        "directory1/test2.json",
        "directory2/test39.json",
        "directory2/test40.json",
        "directory3/directory4/test1.json"
        "directory3/directory4/test45.json"
        "directory3/directory4/test47.json"
    ], recording_json)
    # fmt: on
    pass
