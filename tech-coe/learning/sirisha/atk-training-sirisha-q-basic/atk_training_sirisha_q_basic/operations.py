import time

from atk_training_sirisha_q_basic.persitent_queue import PersistentQueueDb
from atk_training_sirisha_q_basic.parse_yaml import parse_yaml
import typer
import logging
import sqlite3

logging.basicConfig(level='INFO')
app = typer.Typer()


@app.command()
def ops_console():
    pq = PersistentQueueDb({'db_name': 'persist_q.db', 'db_type': sqlite3})
    py=parse_yaml()
    config_data = py.get_instance()
    sleeping_interval = config_data['checking_interval']
    while True:
        rows = pq.manual_checking_items()
        for row in rows:
            print(f"{row['item_value']} requires manual intervention because it crashed more than allowed")
        time.sleep(sleeping_interval)


if __name__ == '__main__':
    app()
