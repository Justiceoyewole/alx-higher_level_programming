#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    # Load the compiled module hidden_4.pyc
    module_name = "hidden_4"
    module_path = "./hidden_4.pyc"  # Adjust the path if needed
    
    # Load the module from the .pyc file
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Retrieve all names defined in the module and filter them
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
