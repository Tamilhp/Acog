
import typer

app = typer.Typer()


@app.command()
def ex1(name: str):
    print("Hello from Hyderabad!!")


def main():
    app()


if __name__ == "__main__":
    ex1('Tamil')
