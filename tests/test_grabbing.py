# "grabbing" is the action of pulling a blob from a storage location decompressing it into temporary folder structure, and then populating in the target directories
from context_creator import initialize_test_context

def test_grab_entirely_empty_directory_structure():
    pass


def test_grab_partially_present_directory_structure():
    pass


def test_grab_partially_filled_directory_structure():
    # fmt: off
    initialize_test_context([
        "directory1/",
        "directory1/test1.json",
        "directory2/",
        "directory3/directory4/test1.json"
    ])
    # fmt: on
    
    pass


def test_grab_entirely_filled_directory_structure():
    pass
