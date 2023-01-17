import yaml
from singleton_decorator import singleton


@singleton
class ParseYml:
    def __init__(self):
        self.manager_delay = None
        self.max_crashes = None
        self.processing_time = None
        self.producer_delay = None
        self.consumer_delay = None
        self.ops_console_delay = None
        self.retry_time = None
        self.dbname = None
        self.parse_yaml()

    def parse_yaml(self):
        with open('./config.yml') as file:
            yaml_configuration = yaml.safe_load(file)
        config = yaml_configuration['config']
        self.manager_delay = config['manager_delay']
        self.max_crashes = config['max_crashes']
        self.processing_time = config['processing_time']
        self.producer_delay = config['producer_delay']
        self.consumer_delay = config['consumer_delay']
        self.ops_console_delay = config['ops_console_delay']
        self.retry_time = config['retry_time']
        self.dbname = config['dbname']
