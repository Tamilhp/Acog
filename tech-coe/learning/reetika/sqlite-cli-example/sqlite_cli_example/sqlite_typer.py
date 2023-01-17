# This is an example program that implements the homework

from typer import Typer
import sqlite3

app=Typer()

db_name = "my.db"

EMP_TABLE_CREATE = """
CREATE TABLE IF NOT EXISTS employees (
emp_id INTEGER PRIMARY KEY,
emp_name TEXT NOT NULL,
dept_id INTEGER NOT NULL
)
"""
EMP_TABLE_DROP = """
DROP TABLE employees
"""


@app.command()
def create_db():
    con = sqlite3.connect(db_name)
    print(f"connected to the database {db_name}")
    cursor = con.cursor()
    cursor.execute(EMP_TABLE_CREATE)
    con.commit()
    con.close()

@app.command()
def info():
    print(f"Library version: {sqlite3.version}")
    print(f"SQLite3 version: {sqlite3.sqlite_version}")


@app.command()
def load_db(num_employees:int = 1000, num_depts:int=100):
    # First create the names
    values = []
    for i in range(num_employees):
        values.append( (i, "employee-"+str(i), i % num_depts))
    con = sqlite3.connect(db_name)
    con.execute(EMP_TABLE_CREATE)
    cursor = con.cursor()
    cursor.executemany('INSERT INTO employees  VALUES (?,?,?)', values)
    print(f"Inserted {cursor.rowcount} records into the table")
    con.commit()
    con.close()


@app.command()
def clean_db():
    con = sqlite3.connect(db_name)
    print(f"connected to the database {db_name}")
    cursor = con.cursor()
    cursor.execute(EMP_TABLE_DROP)
    con.close()


@app.command()
def find_employees(dept_id:int):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM employees WHERE dept_id = {dept_id}")
    records = cursor.fetchall()
    for r in records:
        print(r)
    con.commit()
    con.close()


@app.command()
def find_dept(emp_id:int):
    pass


@app.command()
def find_ids(emp_name:str):
    pass


@app.command()
def validate_password(emp_id: int, password: str):
    pass

if __name__ == "__main__":
    app()
