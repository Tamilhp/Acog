# This producer randomly generate strings
import time
import random
import string
import logging
import sqlite3
from atk_training_pq.persistentQ import PQ
import typer
from atk_training_pq.parse_yaml import ParseYml


logging.basicConfig(level='INFO')
app = typer.Typer()


@app.command()
def create_item() -> None:
    parse = ParseYml()
    delay = parse.producer_delay
    dbname = parse.dbname
    pq = PQ({'dbname': dbname, 'dbtype': sqlite3})
    print("In producer")
    while True:
        item = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        logging.info(f"passing generated item {item} to persistent Q")
        pq.put_item(item)
        time.sleep(delay)


if __name__ == '__main__':
    app()
