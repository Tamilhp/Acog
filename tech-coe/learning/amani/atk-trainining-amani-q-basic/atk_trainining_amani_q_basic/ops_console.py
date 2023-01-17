import sqlite3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template
import uvicorn
from atk_training_pq.parse_yaml import ParseYml
from atk_training_pq.persistentQ import PQ
import os
import pathlib


app = FastAPI()
parse = ParseYml()
dbname = parse.dbname
pq = PQ({'dbname': dbname, 'dbtype': sqlite3})
# app.mount("/static", StaticFiles(directory="static"), name="static")
main_dir = pathlib.Path(__file__).parent.resolve()


@app.get("/")
def show_records():
    records = pq.get_items()
    # Render the template with the records
    template = Template(open(os.path.join(main_dir, 'template.html')).read())
    html = template.render(records=records)
    # Serve the rendered HTML
    return HTMLResponse(html, status_code=200)


@app.get("/delete-records")
def delete_item(item_id):
    pq.delete_item(item_id)
    return {"message": "Item deleted successfully"}


@app.get("/update-status")
def update_status(item_id):
    pq.update_status(item_id, 'unprocessed', 0)
    return {"message": "Updated item status successfully"}


@app.get("/unprocessed")
def get_status():
    records = pq.get_status('unprocessed')
    template = Template(open(os.path.join(main_dir, 'template.html')).read())
    html = template.render(records=records)
    # Serve the rendered HTML
    return HTMLResponse(html, media_type="text/html", status_code=200)


@app.get("/under-process")
def get_status():
    records = pq.get_status('under_process')
    template = Template(open(os.path.join(main_dir, 'template.html')).read())
    html = template.render(records=records)
    # Serve the rendered HTML
    return HTMLResponse(html, media_type="text/html", status_code=200)


@app.get("/processed")
def get_status():
    records = pq.get_status('processed')
    template = Template(open(os.path.join(main_dir, 'template.html')).read())
    html = template.render(records=records)
    # Serve the rendered HTML
    return HTMLResponse(html, media_type="text/html", status_code=200)


@app.get("/manual-check")
def get_status():
    records = pq.get_status('manual_check')
    template = Template(open(os.path.join(main_dir, 'template.html')).read())
    html = template.render(records=records)
    # Serve the rendered HTML
    return HTMLResponse(html, media_type="text/html", status_code=200)


def main():
    uvicorn.run(app, port=8000, host='0.0.0.0')
