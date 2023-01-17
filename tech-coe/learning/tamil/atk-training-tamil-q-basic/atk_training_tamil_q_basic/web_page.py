import os.path

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import typer
from atk_training_tamil_q_basic.yamlparser import YamlParser
from atk_training_tamil_q_basic.sqlite3queue import PersistentQueue
import pathlib


main_dir = pathlib.Path(__file__).parent.resolve()
static_dir = os.path.join(main_dir, "static")
template_dir = os.path.join(main_dir, "templates")
app = FastAPI()


app.mount(static_dir, StaticFiles(directory=static_dir), name="static")


templates = Jinja2Templates(directory=template_dir)


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/display_data/{query}", response_class=HTMLResponse)
async def read_display(request: Request, query: str):
    yaml_data: YamlParser = YamlParser()
    yaml_data.parse_yaml()
    q: PersistentQueue = PersistentQueue()
    if query == 'data':
        data = q.get_all()
    return templates.TemplateResponse("display_data.html", {"request": request, "data": data})


def server():
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)


def main():
    typer.run(server)


if __name__ == "__main__":
    typer.run(server)







