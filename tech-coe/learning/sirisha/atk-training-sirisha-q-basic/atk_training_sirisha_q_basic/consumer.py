import time
from atk_training_sirisha_q_basic.persitent_queue import PersistentQueueDb
from atk_training_sirisha_q_basic.parse_yaml import parse_yaml
import logging
import sqlite3
import typer

logging.basicConfig(level='INFO')
app = typer.Typer()


@app.command()
def consumer() -> None:
    pq = PersistentQueueDb({'db_name': 'persist_q.db', 'db_type': sqlite3})
    py = parse_yaml()
    config_data = py.get_instance()
    sleeping_interval = config_data['checking_interval']
    while True:
        row = pq.get_item()
        if row:
            '''Process the item'''
            logging.info(f"I am processing the {row['item_value']}!!!")
            #
            pq.update_item_status(row['item_id'], 'Processed')
        time.sleep(sleeping_interval)


if __name__ == '__main__':
    app()

