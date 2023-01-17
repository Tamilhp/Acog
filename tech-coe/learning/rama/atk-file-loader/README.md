---
project_name: atk-file-loader
short_description: It is subproject created for the class, to illustrate dynamic file loading 
tags: ["learning"]
category: tech
long_description: >
  This class illustrates how to load a file in a given path and extracts functions from it
  for execution purposes. Uses importlib.SourceFileLoader. It also uses inspect to check if
  is a file. It is not robust. 
---

# Purpose
Suppose we want to extend the program at run time by loading a python file and execute functions in it.
These files need not be in a module -- that means usual importlib does not work. This program illustrates
how to load a python file or a group of files in a folder and provide the list of functions. 

# Installation
```
pip install atk_file_loader 
# From https://dev-pypi.aganitha.ai
```

# How to use it
Here is how to use it:

Create a file `functions.py` in some folder say "./test_folder" as follows:
```python 
def upcase_record(in_record:str) -> str:
    return in_record.upper()

def capitalize_record(in_record:str) -> str:
    return in_record.capitalize()
```

Now, you can test it as:
```
atk_rama_exec_function test_folder upcase_record yourinput_file
```
Now, look at `yourinput_file.processed` to see the processed records. 
# Limitations
This is only for illustrative purposes only. Consider the problems:
1. The functions loaded need not match the signature.
2. The typing is not all there.
3. There is no way to initialize before executing the functions. 

How to fix it?

1. Instead of the functions use a class. Use ABC to ensure the functions follow the signature we need.
2. Use the class to invoke the function. 
3. Allow initalization of the class to take parameters.

```python
class ExecFunction(ABC):
    @abstractmethod
    def __init__(self, options: Dict[str, Any]):
      pass
    @abstractmethod
    def exec(self, in_record:str) -> str:
      """This function """
      pass
```
Now, we can only the classes of this type. We can initialize from a yaml file and execute the methods as we need. 
