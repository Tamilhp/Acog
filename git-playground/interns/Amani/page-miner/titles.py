import csv
import requests
from bs4 import BeautifulSoup
import typer
from aganitha_base_utils import logconfig
from aganitha_base_utils import Config
import logging
import urllib
import os

app = typer.Typer()
logger = logging.getLogger(__name__)
log_settings = Config().params("logging")
logconfig.setup_logging()
logging.basicConfig(filename='page-miner.log', level=logging.DEBUG)


@app.command()
def input_val(url_file: str):
    if os.path.exists(os.getcwd() + '/' + url_file):
        with open(url_file) as files:
            urls: list[str] = [line.rstrip() for line in files]
    extract_titles(urls)


def extract_titles(urls: list[str]):
    titles: list[str] = []
    url_list = []
    for url in urls:
        r = requests.get(url)
        if ("text/html" in r.headers["content-type"]) & (r.status_code < 400):
            soup = BeautifulSoup(r.content, 'html.parser')
            titles_h1: str = soup.find('h1').get_text()
            if len(titles_h1) > 1:
                titles.append(titles_h1)
            elif soup.title is not None:
                titles.append(soup.title.text)
            else:
                continue
            url_list.append(url)
        else:
            logging.info('Not a html/txt page or page not found')
            continue
    write_output(url_list, titles)


def write_output(url_list: list[str], titles: list[str]):
    logging.debug("Writing to csv file Titles.csv")
    with open('Titles.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(("urls", "titles"))
        for i in range(len(url_list)):
            writer.writerow((url_list[i], titles[i]))


if __name__ == '__main__':
    app()
