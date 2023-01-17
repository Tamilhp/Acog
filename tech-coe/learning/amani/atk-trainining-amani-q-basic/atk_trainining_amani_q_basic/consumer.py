import sqlite3
from atk_training_pq.persistentQ import PQ
import time
import logging
import typer
from atk_training_pq.parse_yaml import ParseYml

logging.basicConfig(level='INFO')
app = typer.Typer()


@app.command()
def fetch_item() -> None:
    parse = ParseYml()
    dbname = parse.dbname
    pq = PQ({'dbname': dbname, 'dbtype': sqlite3})
    delay = parse.consumer_delay
    retry_time = parse.retry_time
    while True:
        logging.info("Fetching item from Q")
        item_info = pq.get_item()
        item_id = item_info['item_id']
        item = item_info['item']
        if item is None:
            time.sleep(retry_time)
            logging.info("No items in Q")
        else:
            # perform some processing
            process_item(item)
            status = "Processed"
            pq.update_status(item_id, status, 1)
            time.sleep(delay)


def process_item(item: str) -> str:
    return item.upper()


if __name__ == '__main__':
    app()
