import os.path

import yaml
import pathlib


main_dir = pathlib.Path(__file__).parent.resolve()


class YamlParser:

    def __init__(self):
        self.yaml_data: any = None
        self.db_name: str = None
        self.table_name: str = None
        self.manager_time: float = 0
        self.crash_time: float = 0
        self.ops_time: float = 0
        self.producer_delay: float = 0
        self.consumer_delay: float = 0

    def parse_yaml(self) -> None:
        with open(os.path.join(main_dir, "config.yaml")) as fp:
            self.yaml_data: dict[str] = yaml.safe_load(fp)
        self.db_name: str = self.yaml_data['config']['db_name']
        self.table_name: str = self.yaml_data['config']['table_name']
        self.manager_time: float = self.yaml_data['config']['manager_time']
        self.crash_time: float = self.yaml_data['config']['crash_time']
        self.ops_time: float = self.yaml_data['config']['ops_console_time']
        self.producer_delay: float = self.yaml_data['user']['producer_delay']
        self.consumer_delay: float = self.yaml_data['user']['consumer_delay']


