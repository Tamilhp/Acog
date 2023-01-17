import string
import random
from atk_training_tamil_q_basic.sqlite3queue import PersistentQueue
from atk_training_tamil_q_basic.yamlparser import YamlParser
import logging
import time
import typer

app = typer.Typer()
logging.basicConfig(level='INFO')


@app.command()
def producer() -> None:
    yaml_data: YamlParser = YamlParser()
    yaml_data.parse_yaml()
    q: PersistentQueue = PersistentQueue()
    with q:
        for i in range(30):
            time.sleep(yaml_data.producer_delay)
            item: str = ''.join(random.choices(string.ascii_lowercase, k=3))
            logging.info(f"Adding the item {item} in the queue")
            q.put(item)


def main() -> None:
    app()


if __name__ == "__main__":
    producer()
