from atk_training_pq.persistentQ import PQ
import time
import sqlite3
import logging
import typer
from atk_training_pq.parse_yaml import ParseYml


logging.basicConfig(level='INFO')
app = typer.Typer()


@app.command()
def monitor_q():
    parse = ParseYml()
    dbname = parse.dbname
    pq = PQ({'dbname': dbname, 'dbtype': sqlite3})
    delay = parse.manager_delay
    check_time = parse.processing_time
    while True:
        pq.manage_q(check_time)
        time.sleep(delay)


if __name__ == '__main__':
    app()

