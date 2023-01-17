from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
import typer

app = FastAPI()

@app.get("/message")
async def info():
    return {"msg": """
    This message is coming from the backend.
    I can put whatever text here I want. In reality, you want to establish a
    standard json format to be sent back so that you can extract whatever value you want out of it.
    This is just an illustration using minimal JS.
    """}


app.mount("/", StaticFiles(directory="static", html=True), name="static")

def run_app(port:int = 8000, debug:bool = True):
    uvicorn.run(app, host="0.0.0.0", port=port, debug=debug)

def main():
    typer.run(run_app)