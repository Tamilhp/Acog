# Loads the functions from a path and makes them available in a list.

from typing import List, Callable
from inspect import isfunction, getmembers, isclass
import os
import pathlib
from importlib.machinery import SourceFileLoader
import logging
import sys


logger = logging.getLogger()
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class FunctionLoader(object):
    """This class loads all the functions in a given file and returns a dictionary with function names and functions"""
    def __init__(self, path: str):
        # self.function_list = {}
        self.class_list = {}
        self.load_files_from_path(path)

    def load_files_from_path(self, path: str):

        """Loads files from a path -- uses glob to list all files and uses SourceFileLoader to load the file."""
        for file in pathlib.Path(path).glob('*.py'):
            module_name = os.path.basename(os.path.splitext(file)[0])
            loader = SourceFileLoader(module_name, file.as_posix())  # .load_module()
            module = loader.load_module()
            # functions = getmembers(module, isfunction)
            classes = getmembers(module, isclass)

            ''' Print attributes that are classes '''
            for (cls_name, cls) in classes:
                logger.debug(f"{cls_name} adding. ")
                self.class_list[cls_name] = cls

            # ''' Print only the attributes that are functions '''
            # for (func_name, func) in functions:
            #     logger.debug(f"{func_name} adding. ")
            #     self.function_list[func_name] = func

    def get_function(self, class_name: str):
        # if isinstance(class_name, TransformFunctions):
            return self.class_list.get(class_name)
