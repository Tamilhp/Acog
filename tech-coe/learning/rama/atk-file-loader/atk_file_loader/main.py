import typer
from atk_file_loader.file_loader import FunctionLoader

app = typer.Typer()


@app.command()
def exec_function(file_folder: str, function_name:str, input_file:str, output_file:str = None):
    function_loader:FunctionLoader = FunctionLoader()
    if output_file is None:
        output_file = input_file + ".processed"
    with open(input_file) as fp, open(output_file, "w") as outp:
        for line in fp.readlines():
            print(function_loader.apply_function(function_name, line), file=outp)
