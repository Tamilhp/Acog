# Loads the functions from a path and makes them available in a list.

from typing import List, Callable
from inspect import isfunction, getmembers, isclass
import os
import pathlib
from importlib.machinery import SourceFileLoader
import logging
import sys
from atk_training_tamil_p1.yaml_parser import YamlParser

logger = logging.getLogger()
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
parser = YamlParser()


class FunctionLoader(object):
    """This class loads all the functions in a given file and returns a dictionary with function names and functions"""
    def __init__(self, path_list: List[str] = None):
        if path_list is None:
            path_list: list[str] = parser.parse_yaml('./config.yml', "path")
        self.function_list = {}
        self.class_list = {}
        for path in path_list:
            self.load_files_from_path(path)

    def load_files_from_path(self, path: str):
        """Loads files from a path -- uses glob to list all files and uses SourceFileLoader to load the file."""
        tasks: list[str] = parser.parse_yaml('./config.yml', "task")
        for task in tasks:
            for file in pathlib.Path(path).glob('*.py'):
                module_name = os.path.basename(os.path.splitext(file)[0])
                loader = SourceFileLoader(module_name, file.as_posix())  # .load_module()
                module = loader.load_module()
                classes = getmembers(module, isclass)

                # Print attributes that are classes
                for (cls_name, cls) in classes:
                    if cls_name == task:
                        logger.debug(f"{cls_name} adding. ")
                        self.class_list[cls_name] = cls

    def get_function(self, class_name: str) -> List[Callable[[str], str]]:
        return self.class_list.get(class_name)

    def get_function_dict(self) -> List[Callable[[str], str]]:
        return self.class_list

    def give_function(self, class_name) -> List[Callable[[str], str]]:
        exec_function = self.get_function(class_name)
        if exec_function is not None:
            return self.class_list.get(class_name)


