import typer


app = typer.Typer()

@app.command()
def hello_world(name: str = None) -> None:

    if name == None:
        print("Its Hello World Project, Nice to meet you!!!")

    else:
        print(f"Its Hello World Project, Nice to meet you {name}!!!")