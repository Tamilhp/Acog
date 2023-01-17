"""This code illustrates progressively better ways of extending the code"""
import typer
import atk_learning_rama_p1.record_process_functions as atk
from typing import Dict, Callable, Any, List
import yaml
from atk_learning_rama_p1.record_process_functions import upper_case, lower_case, capitalize, get_ip_city
from atk_function_loader_from_path import FunctionLoader

app = typer.Typer()

StringFunction = Callable[[str], str]


@app.command()
def method1(filename: str) -> None:
    """All the processing is hardcoded"""
    with open(filename) as fp:
        for line in fp:
            result = atk.upper_case(atk.get_ip_city(line.strip()))
            print(result)


def yaml_reader(config_file: str) -> Dict[str, Any]:
    with open(config_file, "r") as fp:
        config_data = yaml.safe_load(fp)
    return config_data


# Anti pattern: We really should be keeping it a module

def get_function_statically(func_name: str) -> StringFunction:
    """BAD CODE: At least keep them in an array and do a lookup."""
    if func_name == "upper_case": return upper_case
    if func_name == "lower_case": return lower_case
    if func_name == "get_ip_city": return get_ip_city
    if func_name == "capitalize": return capitalize


# Here is an alternative:

class FunctionGetter:
    """This function gets the function given the name. It intializes using hardcoding. Does not scale well.
    When we introduce a new function, we have to edit in two places. In the functions and here, in import as well
    as here in this code.

    Better than doing if then else.
    Worse than dynamically figuring out
    """

    def __init__(self):
        self.function_dict: Dict[str, StringFunction] = {
            "upper_case": upper_case,
            "lower_case": lower_case,
            "get_ip_city": get_ip_city,
            "capitalize": capitalize
        }

    def __call__(self, func_name: str) -> StringFunction:
        """We can directly call object as a function. We made the object a callable!"""
        return self.function_dict.get(func_name, None)


@app.command()
def method_yaml(filename: str, config_file: str) -> None:
    """Here the pipeline is not hardcoded. we get it from yaml file"""
    config_data = yaml_reader(config_file)
    pipeline = config_data.get('pipeline')
    # function_list: List[StringFunction] = [get_function_statically(func_name) for func_name in pipeline ]
    # Better version using calsses:
    string_to_function = FunctionGetter()
    function_list: List[StringFunction] = [string_to_function(func_name) for func_name in pipeline]
    exec_list_on_file(filename, function_list)


def exec_list_on_file(filename, function_list):
    with open(filename) as fp:
        for record in fp:
            for f in function_list:
                record = f(record)
            print(record)

class DynamicGetter:
    """This function """
    def __init__(self, files_path: str):
        self.function_loader = FunctionLoader([files_path])

    def __call__(self, func_name:str) -> StringFunction:
        return self.function_loader.get_function(func_name)

@app.command()
def method_yaml(filename: str, config_file: str) -> None:
    """Here the pipeline is not hardcoded. we get it from yaml file"""
    config_data = yaml_reader(config_file)
    pipeline = config_data.get('pipeline')
    # function_list: List[StringFunction] = [get_function_statically(func_name) for func_name in pipeline ]
    # Better version using calsses:
    string_to_function = FunctionGetter()
    function_list: List[StringFunction] = [string_to_function(func_name) for func_name in pipeline]

    exec_list_on_file(filename, function_list)