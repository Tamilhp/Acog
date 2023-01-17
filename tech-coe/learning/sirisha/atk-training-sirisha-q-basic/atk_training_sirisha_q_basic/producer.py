import string
from atk_training_sirisha_q_basic.persitent_queue import PersistentQueueDb
from atk_training_sirisha_q_basic.parse_yaml import parse_yaml
import random
import logging
import sqlite3
import typer
import time

logging.basicConfig(level='INFO')
app = typer.Typer()


@app.command()
def producer() -> None:
    pq = PersistentQueueDb({'db_name': 'persist_q.db', 'db_type': sqlite3})
    py = parse_yaml()
    config_data = py.get_instance()
    sleeping_interval = config_data['checking_interval']
    while True:
        item = ''.join([random.choice(string.ascii_letters) for _ in range(5)])
        logging.info(f"Adding {item} to to the queue")
        pq.add_item(item)
        time.sleep(sleeping_interval)


if __name__ == '__main__':
    app()

