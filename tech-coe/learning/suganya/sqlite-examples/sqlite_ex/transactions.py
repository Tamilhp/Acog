import sqlite3
# from cli_commands import options


class DBTransactions:
    def __init__(self):
        self.db_name = "my.db"

    def create_db(self):
        conn, cursor = self.fetch_connection_cursor()
        print(f"Connected to the database: {self.db_name}")
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS employees (emp_id INTEGER PRIMARY KEY,emp_name TEXT NOT NULL,"
                           "dept_id INTEGER NOT NULL)")
            conn.commit()
            print(f"Created the table: {self.db_name}")
        except sqlite3.Error as er:
            print("SQLite error: %s'" % (' '.join(er.args)))

    def load_db(self, num_employees: int = 1000, num_depts: int = 100):
        # Create the employees
        values = []
        for i in range(num_employees):
            values.append((i, "employee-" + str(i), i % num_depts))
        conn, cursor = self.fetch_connection_cursor()
        try:
            cursor.executemany('INSERT INTO employees  VALUES (?,?,?)', values)
            conn.commit()
            print("Loaded the table: Employees")
        except sqlite3.Error as er:
            print("SQLite error: %s'" % (' '.join(er.args)))

    def clean_db(self):
        conn, cursor = self.fetch_connection_cursor()
        print(f"Connected to the database {self.db_name}")
        try:
            cursor.execute(f"DROP TABLE employees")
            conn.commit()
            print("Dropped the table:  Employees")
        except sqlite3.Error as er:
            print("SQLite error: %s'" % (' '.join(er.args)))

    def find_employees(self, dept_id: int):
        conn, cursor = self.fetch_connection_cursor()
        try:
            cursor.execute(f"SELECT * FROM employees WHERE dept_id = {dept_id}")
            records = cursor.fetchall()
            for r in records:
                print(r)
        except sqlite3.Error as er:
            print("SQLite error: %s'" % (' '.join(er.args)))

    def find_dept(self, emp_id: int):
        pass

    def find_ids(emp_name: str):
        pass

    def validate_password(emp_id: int, password: str):
        pass

    def fetch_connection_cursor(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        return connection, cursor

