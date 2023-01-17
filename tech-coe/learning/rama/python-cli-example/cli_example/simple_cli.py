
def main(name: str = "rama", times:int = 2):
    for i in range(times):
        print(f'{i}: welcome {name}')


if __name__ == '__main__':
    import typer
    typer.run(main)
