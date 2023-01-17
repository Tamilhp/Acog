import yaml


class ConfigLoader:
    def __init__(self):
        pass

    def load_config(self, config_path):
        with open(config_path, 'r') as stream:
            configuration = yaml.safe_load(stream)
            print(configuration)
            return configuration
