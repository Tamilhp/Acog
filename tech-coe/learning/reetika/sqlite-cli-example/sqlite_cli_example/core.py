import sqlite3
from config_loader import ConfigLoader


class DbCore:
    def __init__(self):
        self.config = ConfigLoader()

    def create_db(self, config_path):
        configuration = self.config.load_config(config_path)
        db_name = configuration['db_name']
        con = sqlite3.connect(db_name)
        print(f"connected to the database {db_name}")
        cursor = con.cursor()
        cursor.execute(configuration['EMP_TABLE_CREATE'])
        con.commit()
        con.close()


if __name__ == "__main__":
    obj = DbCore()
    obj.create_db("/Users/reetika/work/tech-coe/projects/learning/reetika/sqlite-cli-example/sqlite_cli_example/sqlite.yml")
