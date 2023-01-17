from atk_suganya_helloworld.helloworld import say_hello
import typer


app=typer.Typer()

@app.command()
def hello_world(name:str):
    say_hello(name)

def main():
    app()