# This is an example program that implements the homework

from typer import Typer
import sqlite3

app=Typer()


db_name = "my.db"


def fetch_connection_cursor():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


@app.command()
def create_db():
    conn, cursor = fetch_connection_cursor()
    print(f"Connected to the database: {db_name}")
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS employees (emp_id INTEGER PRIMARY KEY,emp_name TEXT NOT NULL,"
                       "dept_id INTEGER NOT NULL)")
        conn.commit()
        print(f"Created the table: Employees")
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
    cursor.close()
    conn.close()


@app.command()
def info():
    print(f"Library version: {sqlite3.version}")
    print(f"SQLite3 version: {sqlite3.sqlite_version}")


@app.command()
def load_db(num_employees: int = 1000, num_depts: int = 100):
    # Create the employees
    values = []
    for i in range(num_employees):
        values.append((i, "employee-"+str(i), i % num_depts))
    conn, cursor = fetch_connection_cursor()
    try:
        cursor.executemany('INSERT INTO employees  VALUES (?,?,?)', values)
        conn.commit()
        print(f"Inserted {cursor.rowcount} records into the table")
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
    cursor.close()
    conn.close()


@app.command()
def clean_db():
    conn, cursor = fetch_connection_cursor()
    print(f"connected to the database {db_name}")
    try:
        cursor.execute(f"DROP TABLE employees")
        conn.commit()
        print(f"Dropped the table: Employees")
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
    cursor.close()
    conn.close()


@app.command()
def find_employees(dept_id:int):
    conn, cursor = fetch_connection_cursor()
    try:
        cursor.execute(f"SELECT * FROM employees WHERE dept_id = {dept_id}")
        records = cursor.fetchall()
        for r in records:
            print(r)
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
    cursor.close()
    conn.close()


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
