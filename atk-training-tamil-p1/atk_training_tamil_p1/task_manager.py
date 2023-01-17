from typing import List, Callable

from atk_training_tamil_p1.yaml_parser import YamlParser

from atk_training_tamil_p1.file_loader import FunctionLoader

load = FunctionLoader()
parser = YamlParser()


class TaskManager:
    """This is where all the background process are managed. Like Parsing the Yaml, getting the callable, executing
        the steps listed in the yaml file"""
    def __init__(self, yaml_file: str):
        self.yaml_tasks: List[Callable[[str], str]] = parser.parse_yaml(yaml_file, "task")
        self.task_list: List[Callable[[str], str]] = TaskManager.match_function(self.yaml_tasks)

    def execute_pipeline(self, line: str):
        for task in self.task_list:
            line: str = task.exec(self, line)
        yield line

    @classmethod
    def match_function(cls, yaml_tasks: list[str]) -> List[Callable[[str], str]]:
        tasks: List[Callable[[str], str]] = []
        for task_name in yaml_tasks:
            tasks.append(load.give_function(task_name))
        return tasks
