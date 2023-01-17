0. Created a new poetry project - python-exercise
1. The package name is atk_training_suganya_python_exercises
2. In atktraining_sugan_py1.py 
    - Wrote a basic program to cover step 1 and step 2 of problem 1
```Problem 1: Record processing
Here is the problem, which we will build step-by-step. One of the standard problems in computers is processing of files. The files can be CSV to be processed and put in the databases. Or, it can be tweets to be processed to be put in the database. We are going to build up to a system that does it with the following:

It should be reusable: People should be able to use it as a command, as a library, and as a framework.
It should be extendible: People should be able add new kinds of processing to the system, without having to learn all about it.
It should be customizable: People should be able to customize the processing.
It should be maintainable: People should be able to update the system. And, understand the system from documentation.
Step 1: Basic record processing
Your task is to write a program that processes a line at a time in a file. Each line is changed to upper case and written to another file. It should take the input filename as an argument, and optionally the output filename as well. If the output filename is not given, it adds filename.upper and produces it. Write that function, with the following guidelines:

Name your package atk-trainng-yourname-p1.
Name your command atk-yourname-upcase
Keep the main program and your function separately.
Use pytproject.toml to define your script. Use typer to parse command line args.

Step 2: Extending functionality of the processing
The problem with this code is what transformation you can do is fixed. Let us fix this problem by writing a new transformation function called transform_remove_stopwords. It can be more involved, but in this case, just remove the words "a", "an", "the", "and" "or". To make the problem simpler, let us assume that the text does not contain any punctuation – and the words are separated by just simple space. Simply put, you can do split to get words and remove the stop words and join them to get the result.

Add a function transform_remove_stopwords that takes a record and removes the stop words.
Extend the program by taking a command line option to use one of two transforms. (uppercase by default or )
Name this command atktraining-yourname-py1-extended1 and publish your package.```

For #2, add the command in pyproject.toml - 
#[tool.poetry.scripts]
#atktraining-sugan-py1-basic ="atk_training_suganya_python_exercises.atktraining_sugan_py1:main"
nltk = "^3.7"

#[tool.poetry.scripts]
#atktraining-sugan-py1-extended1 ="atk_training_suganya_python_exercises.atktraining_sugan_py1:main"
Call atktraining-sugan-py1-extended1 in terminal to get the input from the user for both transform_uppercase and transform_remove_stopwords functions.

3. However, whenever we add a new function, we have to change the library. Let's separate the library and command 
Instead of writing the main() in the same file - atktraining-sugan_py1.py, let's call these functions - transform_uppercase() and transform_remove_stopwords() in commands.py and add a main() over there.
For this, add this command in pyproject.toml

#[tool.poetry.scripts]
#atktraining-sugan-py1-extended2 ="atk_training_suganya_python_exercises.commands:main"
IN the terminal , we've to give the command(atktraining-sugan-py1-extended2), input file name, output file name and function to be called
e.g. atktraining-sugan-py1-extended2 /home/acog/tech-coe/projects/learning/suganya/sample_file.txt /home/acog/tech-coe/projects/learning/suganya/processed_file.txt upper_case

4. Now in commands.py, these lines 
function_list:dict={"upper_case": transform_uppercase, "stop_words": transform_remove_stopwords}
from atk_training_suganya_python_exercises.atktraining_sugan_py1 import transform_uppercase, transform_remove_stopwords

will be changed often, because, whenever we add a function , we import that in commands.py and we add that new function in the function_list 
Instead of changing commands.py often, we create a function_lookup.py library, where we can add these 2 lines

5. Now in function_lookup.py, add these lines
function_list:dict={"upper_case": transform_uppercase, "stop_words": transform_remove_stopwords}
from atk_training_suganya_python_exercises.atktraining_sugan_py1 import transform_uppercase, transform_remove_stopwords
def lookup(opt:str) -> Callable[[str], str]:
    return function_list[opt]

Call this lookup in commands.py

```Now let's do step 3
Step 3: Extending it better
The problem with earlier code is that each time we introduce new function into the library, we have to edit the main program to extend. How can we decouple the dependency? (To understand what code dependencies are and the law of demeter is, read the Pragmatic programmer)

Here, we will dynamically load the code.

Modify the function that reads the file and applies the function to each record in the following way:
Take the name of the module
Take the name of the function to apply
Dynamically load the module and the function
Modify the CLI to supply these options. Make sure it works with previous two transformations
If you have come till now, you may find the code Loading modules useful. That codes does not load from standard library, but from a folder```


6. Now, instead of having a function_list dictionary, let's read these functions from a yaml file
```Step 3: Customizing the application
To this task, let us add one more function to our library. Let us call it transform-uk-to-us. In this function, change the “sation” to “zation”. This is not perfect or accurate, but does most UK words to US words. And, add another function called transform_to_lower_case that takes the line and makes it all lower case.

Suppose you want to do the following:

transform_to_lowercase
remove_stop_words
tranform_upper_case
How do you write it? You could, of course, use three python programs. Or, better yet, do all of it in python. Do the following:

Use a yaml file (an alternative to json) that specifies the following
Read this yaml file and use it to execute the pipeline on each record.
Here is the pseudocode

for each record:
   for each function f in the pipeline:
      record=f(record)
write the record
Do not do if-then-else. Use lookups to map function name to function.
```

For the above problem, used get_yaml_input.py and command in pyproject.toml is `atktraining-sugan-py1-extended3`
the command in the terminal is atktraining-sugan-py1-extended3 /home/acog/tech-coe/projects/learning/suganya/sample_file.txt /home/acog/tech-coe/projects/learning/suganya/processed_file.txt
