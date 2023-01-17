def main(name: str = "rama", times: int = 2):
    """
     name: The name we greet you with
     times: Number of times we greet you

     I can write any help text I want to.
    """
    for i in range(times):
        print(f'{i}: welcome {name}')


if __name__ == '__main__':
    import typer
    typer.run(main)
