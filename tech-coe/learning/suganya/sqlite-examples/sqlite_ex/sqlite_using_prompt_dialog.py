from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog, message_dialog, button_dialog
import sqlite3
import sys
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

db_name = "my.db"

db_style = Style.from_dict(
    {
        'dialog': 'bg:#cdbbb3',
        'button': 'bg:#bf99a4',
        'checkbox': '#e8612c',
        'dialog.body': 'bg:#a9cfd0',
        'dialog shadow': 'bg:#c98982',
        'frame.label': '#fcaca3',
        'dialog.body label': '#fd8bb6',
    }
)


def main():
    while True:
        result = radiolist_dialog(
            values=[
                ("create", "Create"),
                ("load", "Load"),
                ("exit", "Exit"),
                ("clean", "Drop"),
                ("find", "Find")
            ],
            title="DB transactions",
            text="Please select an option: ",
            style=db_style
        ).run()
        
        if result == 'create':
            create_db()
        if result == 'load':
            # emp_count = prompt("Please type number of employees:")
            # dept_count = prompt("Please type number of depts:")
            emp_count = input_dialog(
                title="Load the Database", text="Please type number of employees:",
                style=db_style,
            ).run()
            dept_count = input_dialog(
                title="Load the Database", text="Please type number of Depts:",
                style=db_style,
            ).run()
            load_db(int(emp_count), int(dept_count))
        if result == 'exit':
            sys.exit()
        if result == 'clean':
            clean_db()
        if result == 'find':
            no_of_depts = input_dialog(
                title="Load the Database", text="Please type number of Depts:",
                style=db_style,
            ).run()
            find_employees(int(no_of_depts))


def message_box(text):
    message_dialog(
        title="",
        text=text,
        style=db_style,
    ).run()


def create_db():
    conn, cursor = fetch_connection_cursor()
    print(f"Connected to the database: {db_name}")
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS employees (emp_id INTEGER PRIMARY KEY,emp_name TEXT NOT NULL,"
                       "dept_id INTEGER NOT NULL)")
        conn.commit()
        message_box("Created the table: Employees. Press OK to continue.")
    except sqlite3.Error as er:
        message_box("SQLite error: %s'" % (' '.join(er.args)))
        button_box()
    cursor.close()
    conn.close()
    
    
def load_db(num_employees: int = 1000, num_depts: int = 100):
    # Create the employees
    values = []
    for i in range(num_employees):
        values.append((i, "employee-" + str(i), i % num_depts))
    conn, cursor = fetch_connection_cursor()
    try:
        cursor.executemany('INSERT INTO employees  VALUES (?,?,?)', values)
        conn.commit()
        message_box("Loaded the table: Employees. Press OK to continue.")
    except sqlite3.Error as er:
        message_box("SQLite error: %s'" % (' '.join(er.args)))
    cursor.close()
    conn.close()


def clean_db():
    conn, cursor = fetch_connection_cursor()
    print(f"connected to the database {db_name}")
    try:
        cursor.execute(f"DROP TABLE employees")
        conn.commit()
        message_box("Dropped the table:  Employees. Press OK to continue.")
    except sqlite3.Error as er:
        message_box("SQLite error: %s'" % (' '.join(er.args)))
    cursor.close()
    conn.close()


def find_employees(dept_id: int):
    conn, cursor = fetch_connection_cursor()
    try:
        cursor.execute(f"SELECT * FROM employees WHERE dept_id = {dept_id}")
        records = cursor.fetchall()
        message_box(f"Records: {records} ")
    except sqlite3.Error as er:
        message_box("SQLite error: %s'" % (' '.join(er.args)))
    cursor.close()
    conn.close()


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