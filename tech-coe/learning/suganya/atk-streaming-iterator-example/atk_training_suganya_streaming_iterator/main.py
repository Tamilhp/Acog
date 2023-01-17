import typer
from atk_training_suganya_streaming_iterator.execute_tasks import ExecuteTasks
from atk_training_suganya_streaming_iterator.class_manager import ClassManager

app = typer.Typer()


@app.command()
def process_text(input_file:str, output_file: str = None):
    ''' This is the main function - It calls process_pipeline() method by passing both input and output file '''
    if output_file is None:
        output_file = input_file + ".processed"
    process_pipeline(input_file, output_file)

def process_pipeline(input_file: str, output_file) -> None:
    ''' Initialize Class Manager which loads yaml file from path. Returns function path and class_names '''
    class_manager = ClassManager()
    functions_path, class_names = class_manager.get_class_and_function_names_from_yaml("../config.yaml")

    ''' Initialize Execute Tasks and pass function_path, class_names, input and output file to execute the file line by line '''
    execute_tasks:ExecuteTasks = ExecuteTasks(functions_path, class_names)
    execute_tasks.get_file_input_and_execute(input_file, output_file)

def main():
    app()