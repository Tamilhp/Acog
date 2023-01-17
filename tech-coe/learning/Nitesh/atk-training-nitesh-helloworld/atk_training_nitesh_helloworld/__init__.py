import typer

app = typer.Typer()


@app.command()
def hello(string: str) -> None:
    print('hello'+ " " + string)


def main():
    app()
