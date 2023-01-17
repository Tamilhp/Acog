import sqlite3
import sys
from prompt_toolkit import prompt

db_name = "my.db"


def main():
    while True:
        result = prompt("Please enter:\n"
                        "'create' for creating the database\n"
                        "'load' for ingesting into the database\n"
                        "'exit' to Quit\n"
                        "'find' for Finding the employees\n"
                        "'clean' for Cleaning the database: ")

        if result == 'create':
            create_db()
        elif result == 'load':
            emp_count = prompt("Please enter the number of employees:")
            dept_count = prompt("Please enter the number of depts:")
            
            load_db(int(emp_count), int(dept_count))
        elif result == 'exit':
            sys.exit()
        elif result == 'clean':
            clean_db()
        elif result == 'find':
            no_of_depts = prompt("Please type number of Depts:")
            find_employees(int(no_of_depts))
        else:
            print("Wrong Input")


def options(conn, cursor):
        options = prompt("Do you want to continue: Yes/No:")
        if options == 'No' or options == 'no' or options == 'n':
            cursor.close()
            conn.close()
            sys.exit()
        

def create_db():
    conn, cursor = fetch_connection_cursor()
    print(f"Connected to the database: {db_name}")
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS employees (emp_id INTEGER PRIMARY KEY,emp_name TEXT NOT NULL,"
                       "dept_id INTEGER NOT NULL)")
        conn.commit()
        print(f"Created the table: {db_name}")
        options(conn, cursor)
    except sqlite3.Error as er:
        print("SQLite error: %s'" % (' '.join(er.args)))
        options(conn, cursor)


def load_db(num_employees: int = 1000, num_depts: int = 100):
    # Create the employees
    values = []
    for i in range(num_employees):
        values.append((i, "employee-" + str(i), i % num_depts))
    conn, cursor = fetch_connection_cursor()
    try:
        cursor.executemany('INSERT INTO employees  VALUES (?,?,?)', values)
        conn.commit()
        print("Loaded the table: Employees")
        options(conn, cursor)
    except sqlite3.Error as er:
        print("SQLite error: %s'" % (' '.join(er.args)))
        options(conn, cursor)


def clean_db():
    conn, cursor = fetch_connection_cursor()
    print(f"Connected to the database {db_name}")
    try:
        cursor.execute(f"DROP TABLE employees")
        conn.commit()
        print("Dropped the table:  Employees")
        options(conn, cursor)
    except sqlite3.Error as er:
        print("SQLite error: %s'" % (' '.join(er.args)))
        options(conn, cursor)


def find_employees(dept_id: int):
    conn, cursor = fetch_connection_cursor()
    try:
        cursor.execute(f"SELECT * FROM employees WHERE dept_id = {dept_id}")
        records = cursor.fetchall()
        for r in records:
            print(r)
            options(conn, cursor)
    except sqlite3.Error as er:
        print("SQLite error: %s'" % (' '.join(er.args)))
        options(conn, cursor)


def find_dept(emp_id: int):
    pass


def find_ids(emp_name: str):
    pass


def validate_password(emp_id: int, password: str):
    pass


def fetch_connection_cursor():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


if __name__ == "__main__":
    main()