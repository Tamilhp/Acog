import logging

import requests
from aganitha_base_utils import logconfig
from aganitha_base_utils import Config
import os
import urllib
import typer

app = typer.Typer()

logger = logging.getLogger(__name__)
log_settings = Config().params("logging")
logconfig.setup_logging()


@app.command()
def input_output_val(input_file: str, output_dir: str):
    if os.path.exists(os.getcwd() + '/' + input_file):
        with open(input_file) as files:
            urls: list[str] = [line.rstrip() for line in files]

        output_path: str = os.path.expanduser('~') + '/page-miner/' + str(output_dir) + '/'
        if not os.path.exists(output_path):
            os.makedirs(output_path)  # create folder if it does not exist
        extract_pages(urls, output_path)
    else:
        print("Given file doesnt exists, give proper input file")


def extract_pages(urls: list[str], output_path: str):
    for url in urls:
        ret = requests.head(url)
        print(ret.status_code)
        if ret.status_code < 400:
            file_name: str = str(urls.index(url) + 1) + '.txt'
            file_path: str = os.path.join(output_path, file_name)
            urllib.request.urlretrieve(url, file_path)
            print("Writing to file: ", file_path)
        else:
            print("Website doesn't exists")


if __name__ == '__main__':
    app()
