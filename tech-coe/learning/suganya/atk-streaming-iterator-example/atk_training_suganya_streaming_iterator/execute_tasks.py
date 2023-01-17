# Loads the functions from a path and makes them available in a list.

from typing import List, Callable, Iterator
from inspect import isfunction, getmembers
import os
import pathlib
from importlib.machinery import SourceFileLoader
import logging
import sys
import yaml

from atk_training_suganya_streaming_iterator.python_file_loader import FunctionLoader
logger = logging.getLogger()
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
import fileinput

class ExecuteTasks():
    def __init__(self, functions_path: str, class_names: List[str]):

        ''' Get the input, output file, function path and class_names
            Call FunctionLoader to load the python module and functions dynamically and call get_function() to get the function names '''
        python_function_loader = FunctionLoader(functions_path)
        self.tasks_pipeline = []
        
        for class_name in class_names:
            function_name = python_function_loader.get_function(class_name)
            print(f"Function_name:{function_name}")
            self.tasks_pipeline.append(function_name)


    def get_file_input_and_execute(self, input_file, output_file):
            ''' Convert the input file to an iterator and get the input lines as a list '''
            lines: Iterator[str] = fileinput.input(input_file)

            ''' Calls the __call__ method to process the lines '''
            for function_name in self.tasks_pipeline:
                lines: Iterator[str] = function_name.__call__(lines)
            
            ''' Write output to a file'''
            for r in lines:
                with open(output_file, "a+") as outp:
                    outp.write(r)

