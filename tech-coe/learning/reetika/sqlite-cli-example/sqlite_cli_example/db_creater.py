from core import DbCore
import typer


def creat_db(config_path):
    s = DbCore()
    s.create_db(config_path)


if __name__ == "__main__":
    typer.run(creat_db)
