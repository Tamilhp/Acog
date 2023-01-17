import logging
from atk_training_tamil_q_basic.yamlparser import YamlParser
from atk_training_tamil_q_basic.sqlite3queue import PersistentQueue
import time
import typer

app = typer.Typer()
logging.basicConfig(level='INFO')


@app.command()
def manager() -> None:
    yaml_data: YamlParser = YamlParser()
    yaml_data.parse_yaml()
    q: PersistentQueue = PersistentQueue()
    while True:
        time.sleep(yaml_data.manager_time)
        q.check_and_change_status()
        crashed_files: 'records' = q.crash_count_check()
        for i in crashed_files:
            logging.info(f"The file {i.get('data')} needs your intervention because it crashed more than 3 times")


def main() -> None:
    app()
