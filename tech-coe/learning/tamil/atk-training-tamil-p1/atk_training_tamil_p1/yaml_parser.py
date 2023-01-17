import yaml


class YamlParser:
    """This class parses the Yaml configure file and sends the Yaml data"""
    def __init__(self):
        self.task_names: list[str] = []
        self.task_path: list[str] = []

    def parse_yaml(self, yaml_file: str, opt: str) -> list[str]:
        with open(yaml_file) as fp:
            yaml_data: list[str] = yaml.safe_load(fp)
        self.task_names = yaml_data["pipeline"]
        self.task_path = yaml_data['path']
        if opt == "task":
            return self.task_names
        if opt == "path":
            return self.task_path
