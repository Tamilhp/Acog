import yaml


class parse_yaml:
    @staticmethod
    def yaml_parsing():
        with open('./config.yml') as file:
            yaml_configuration = yaml.safe_load(file)
            return yaml_configuration['config']


if __name__ == '__main__':
    parse_yaml()
