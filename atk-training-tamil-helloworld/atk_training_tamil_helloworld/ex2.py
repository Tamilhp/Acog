
import typer

app = typer.Typer()


@app.command()
def ex2(name: str):
    print("Hello buddy..I cracked you")
    print("Hello from Hyderabad!!")


def main():
    app()


if __name__ == "__main__":
    main()
