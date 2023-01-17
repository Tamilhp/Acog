from typing import Callable
import typer
from atk_training_suganya_python_exercises.function_lookup import lookup
from atk_training_suganya_python_exercises.task_manager import TaskManager

app=typer.Typer()

# function_list:dict={"upper_case": transform_uppercase, "stop_words": transform_remove_stopwords}

def apply_process_pipeline(process_func: Callable[[str], str], input_file: str, output_file:str):
    with open(input_file,'r') as inf, open(output_file,'w') as of:
        lines=inf.readlines()
        for line in lines:
            transformed_line = process_func(line)
            of.write(transformed_line +'\n')

# def lookup(opt:str) -> Callable[[str], str]:
#     return function_list[opt]

@app.command()
def process_text(input_file:str, output_file:str, opt:str):
    process_func: Callable[[str], str] = lookup(opt)
    apply_process_function(process_func, input_file, output_file)


def main():
    app()