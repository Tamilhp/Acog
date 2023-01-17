import typer
from atk_training_avnish_wf_basic import processing_functions as functions

app = typer.Typer()


@app.command()
def basic(input_file_name: str, output_file_name: str = None) -> str:
    with open(input_file_name, 'r') as f1:
        lines = f1.readline().split('.')

        if output_file_name is None:
            with open(input_file_name.split('.')[0] + '.processed.txt', 'a') as f2:
                for line in lines:
                    f2.write(functions.upper_case(line))
                    f2.write('\n')

        else:

            with open(output_file_name, 'a') as f2:
                for line in lines:
                    f2.write(functions.upper_case(line))
                    f2.write('\n')


