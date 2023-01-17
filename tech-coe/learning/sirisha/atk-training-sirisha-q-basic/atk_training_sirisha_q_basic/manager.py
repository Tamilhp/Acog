import datetime
import time
from atk_training_sirisha_q_basic.persitent_queue import PersistentQueueDb
from atk_training_sirisha_q_basic.parse_yaml import parse_yaml
import logging
import sqlite3
import typer

logging.basicConfig(level='INFO')

app = typer.Typer()


@app.command()
def manager() -> None:
    pq = PersistentQueueDb({'db_name': 'persist_q.db', 'db_type': sqlite3})
    py = parse_yaml()
    config_data = py.get_instance()
    sleeping_interval = config_data['checking_interval']
    max_crashes = config_data['max_crashes']
    while True:
        row = pq.get_item_state()
        if row:
            if row['timestamp'] < datetime.datetime.now() - datetime.timedelta(hours=1) and row['resubmit_count'] < max_crashes:
                pq.update_item_status(row['item_id'], 'unprocessed')
                logging.info("changing the status of the item back to unprocessed")
            elif row['timestamp'] < datetime.datetime.now() - datetime.timedelta(hours=1) and row['resubmit_count'] == max_crashes:
                logging.info("""Code has crashed for more than 3 times.
                changed the status of the item to manual check""")
                pq.update_item_status(row['item_id'], 'Manual_check')
            time.sleep(sleeping_interval)


if __name__ == '__main__':
    app()




