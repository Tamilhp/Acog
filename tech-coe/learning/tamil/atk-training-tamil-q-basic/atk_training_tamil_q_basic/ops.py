import time
from atk_training_tamil_q_basic.sqlite3queue import PersistentQueue
from atk_training_tamil_q_basic.yamlparser import YamlParser
import typer
import logging

app = typer.Typer()
logging.basicConfig(level='INFO')


@app.command()
def operational_console() -> None:
    yaml_data: YamlParser = YamlParser()
    yaml_data.parse_yaml()
    q: PersistentQueue = PersistentQueue()
    while True:
        time.sleep(yaml_data.ops_time)
        data: 'records' = q.current_status_check()
        logging.info(f"The total number of records are {data[0][0][0]}")
        logging.info(f"The total number of records are not processed {data[0][0][0]-data[1][0][0]-data[2][0][0]}")
        logging.info(f"The total number of records that are in_process {data[1][0][0]}")
        logging.info(f"The total number of records are processed {data[2][0][0]}")
        logging.info(f"The average processing time is {data[3][0][0]}")
        logging.info(f"The total number of files that are crashed more than thrice and unprocessed {data[4][0][0]}")


def main() -> None:
    app()
