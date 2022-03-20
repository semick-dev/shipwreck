
from pathlib import Path
from typing import List
import shutil
import os

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))

def get_test_name() -> str:
    name = os.environ.get('PYTEST_CURRENT_TEST')
    test_name = name.split("::")[1]
    return test_name.split(" ")[0]

def create_target_directory() -> str:
    test_name = get_test_name()
    target_directory = os.path.abspath(os.path.join(root_dir, "tests", '.run', test_name))
    
    if os.path.exists(target_directory):
        shutil.rmtree(target_directory)

    Path(target_directory).mkdir(parents=True, exist_ok=False)

    return target_directory

def initialize_test_context(folder_structure_list: List[str]) -> str:
    target_directory = create_target_directory()

    for path in folder_structure_list:
        ext = os.path.splitext(os.path.normpath(path))[1]

        if ext:
            resolved_path = os.path.join(target_directory, path)
            target_directory = os.path.dirname(resolved_path)

            if not os.path.exists(target_directory):
                Path(target_directory).mkdir(parents=True, exist_ok=True)

            if ext == ".json":
                with open(resolved_path, "w") as f:
                    f.write("{ \"a\", \"b\" }")
            
        else:
            resolved_path = os.path.join(target_directory, path)
            Path(resolved_path).mkdir(parents=True, exist_ok=True)
        
    return target_directory
