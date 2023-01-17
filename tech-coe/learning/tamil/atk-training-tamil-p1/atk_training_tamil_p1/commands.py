"""
This application takes an input file and applies all the transformation functions that are mentioned
in the Yaml file and returns a processed file.
"""
import typer
from typing import Type, Iterator
from atk_training_tamil_p1.task_manager import TaskManager
from atk_training_tamil_p1.stream_converter import PreProcessor
app = typer.Typer()


def apply_process_pipeline(input_file: str, output_file: str = None) -> None:
    """This function transforms the input file using the pipeline found in yaml file."""
    my_task_manager: Type[TaskManager] = TaskManager("./config.yml")
    stream_processor: Type[PreProcessor] = PreProcessor()
    input_streams: Iterator[str] = stream_processor.process(input_file)
    print(type(input_streams))
    with open(output_file, 'w') as op:
        for line in input_streams:
            transformed_line = my_task_manager.execute_pipeline(line)
            for lin in transformed_line:
                if lin == '\n' or lin == '':
                    pass
                else:
                    print(lin, file=op)


@app.command()
def process_text(input_file: str, output_file: str = None) -> None:
    """This is where the execution starts."""
    if output_file is None:
        output_file = input_file + ".processed"

    apply_process_pipeline(input_file, output_file)


def main():
    app()


if __name__ == "__main__":
    app()
