import os.path
import time
import logging
from atk_training_tamil_q_basic.sqlite3queue import PersistentQueue
from atk_training_tamil_q_basic.yamlparser import YamlParser
import typer


logging.basicConfig(level='INFO')
app = typer.Typer()


@app.command()
def consumer() -> None:
    if not os.path.isdir('./processed_files'):
        os.mkdir('./processed_files')
    yaml_data: YamlParser = YamlParser()
    yaml_data.parse_yaml()
    q: PersistentQueue = PersistentQueue()
    with q:
        os.chdir('./processed_files')
        while True:
            item: 'record' = q.get()
            if not item:
                logging.info("There are no items to be processed So waiting for 5 seconds")
                time.sleep(yaml_data.consumer_delay)
                continue
            else:
                logging.info(f"I am going to process {item.get('data')}")
                with open(item.get('data'), 'w') as fp:
                    print("You are processed", file=fp)
                    time.sleep(yaml_data.consumer_delay)
            q.update_status(item.get('id'))


def main() -> None:
    app()
