"""This file is for interacting with the users, leveraging the library. We create the commands in
pyproject.toml.

Try the following: make install
atk-rama-p1-hello --help
That tells what commands are there for use here.

Topics to learn:

1. How to separate libraries and command line [For instance, here the library does not need typer. It is needed only
for command line. We could create one more commandline program using argparse, if we like. And, the library does not
change.
2. How to use typer: Here, we are using typer in multicommand mode. Had we had @app.command for only one function,
it would be single command. Go ahead and test it out.
3. How to tie it up in pyproject.toml: See the section scripts. We are tying the "main" function to cmdline here. You
can use app directly, if you wish too. Of course, we can have multiple app's (app1 = typer.Typer() and app2 = typer.Typer())
and get two single mode commands too.

For coding, I am following google guidelines: https://www.youtube.com/watch?v=woIkysZytSs

Or, the original from: https://google.github.io/styleguide/pyguide.html We disagree with a few (for instance
on typing), but use your judgement.

"""

import typer
from atk_learning_rama_p1 import hello_world

app = typer.Typer()

@app.command()
def say_hello(name:str = "World"):
    hello_world.hello_world(name)

@app.command()
def say_hello_again(name1: str, name2: str):
    hello_world.hello_world(name1)
    hello_world.hello_world(name2)

def main():
    app()
