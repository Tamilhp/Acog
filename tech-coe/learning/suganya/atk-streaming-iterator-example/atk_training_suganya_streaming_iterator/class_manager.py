from typing import List, Callable
import yaml
import pathlib


class ClassManager():
    """ This class loads the config.yaml file dynamically from the path given and return the class names and function_path """
    def __init__(self):
        pass
    
    def get_class_and_function_names_from_yaml(self, path_list: str):
        
        """Loads files from a path -- uses glob to list the yaml file"""
        class_names=[]
        for path in path_list:
            for file in pathlib.Path(path).glob('*.yaml'):
                with open(file) as fp:
                    yaml_data = yaml.safe_load(fp)
                function_path = yaml_data["function_path"]
                class_names = yaml_data["pipeline"]

        return function_path, class_names
