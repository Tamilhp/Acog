"""This is to show how to separate library and the executable so that we can use the library in multiple programs """
import modulefinder

from simple_chalk import chalk, green

def hello_world(name:str):
    print(f"Hello {green.bold(name)}")
    print(f"This comes from { __name__}")
