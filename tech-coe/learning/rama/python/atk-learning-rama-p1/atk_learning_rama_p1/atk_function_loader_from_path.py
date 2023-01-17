# Loads the functions from a path and makes them available in a list.

from typing import List, Callable
from inspect import isfunction, getmembers
import os
import pathlib
from importlib.machinery import SourceFileLoader
import logging
import sys


logger = logging.getLogger()
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class FunctionLoader(object):
    """This class loads all the functions in a given file and returns a dictionary with function names and functions"""
    def __init__(self, path_list:List[str] = None):
        if path_list is None:
            path_list = ["."]
        self.function_list={}
        for path in path_list:
            self.load_files_from_path(path)

    def load_files_from_path(self, path: str):
        """Loads files from a path -- uses glob to list all files and uses SourceFileLoader to load the file."""
        for file in pathlib.Path(path).glob('*.py'):
            module_name = os.path.basename(os.path.splitext(file)[0])
            loader = SourceFileLoader(module_name, file.as_posix())  # .load_module()
            module = loader.load_module()
            functions = getmembers(module, isfunction)

            # Print only the attributes that are functions
            for (func_name, func) in functions:
                logger.debug(f"{func_name} adding. ")
                self.function_list[func_name] = func

    def get_function(self, function_name: str):
        return self.function_list.get(function_name, None)

    def get_function_dict(self):
        return self.function_list
