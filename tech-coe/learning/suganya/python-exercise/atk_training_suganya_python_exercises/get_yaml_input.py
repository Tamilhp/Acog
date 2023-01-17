import yaml
from typing import Callable
from typer import Typer
from atk_training_suganya_python_exercises.task_manager import TaskManager

app = Typer()

@app.command()
def process_text(input_file:str, output_file:str):
      transformed_line = apply_process_pipeline(input_file, output_file)

def apply_process_pipeline(input_file: str, output_file: str = None) -> None:
   transformed_line: str =''
   task_manager = TaskManager('./config.yml')
   with open(input_file, 'r') as fp, open(output_file, 'w') as op:
        lines = [line.rstrip() for line in fp]
        for line in lines:
            transformed_line = task_manager.execute_pipeline(line)
            print(transformed_line, file=op)
      

def main():
 app()