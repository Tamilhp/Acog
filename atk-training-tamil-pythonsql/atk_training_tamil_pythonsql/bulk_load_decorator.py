import time
from typing import Callable, List
import sqlite3
import pandas as pd
import logging
import functools
import typer

app = typer.Typer()

logging.basicConfig(level=logging.DEBUG)


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        logging.debug(f"Finished {func.__name__} in {run_time:.4f} secs")
        return res
    return wrapper_timer


@app.command()
@timer
def bulk_csv_loader(input_file: str, db_name: str, table_name: str):
    """I am a bulk sqlite3 bulk loader"""

    file = pd.read_csv(input_file)
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute(f"DROP TABLE IF exists {table_name}")
        cur.execute(f"CREATE TABLE dd ({file.columns[0]}, {file.columns[1]}, {file.columns[2]})")
        file.to_sql(table_name, conn, if_exists='append', index=False)
        conn.commit()


def main():
    app()

