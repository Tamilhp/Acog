from prompt_toolkit import prompt
import sys
from transactions import DBTransactions


def prompt_commands():
    while True:
        result = prompt("Please enter:\n"
                        "'create' for creating the database\n"
                        "'load' for ingesting into the database\n"
                        "'exit' to Quit\n"
                        "'find' for Finding the employees\n"
                        "'clean' for Cleaning the database: ")

        if result == 'create':
            db_transactions.create_db()
            options()

        elif result == 'load':
            emp_count = prompt("Please enter the number of employees:")
            dept_count = prompt("Please enter the number of depts:")

            db_transactions.load_db(int(emp_count), int(dept_count))
            options()
        elif result == 'exit':
            sys.exit()
        elif result == 'clean':
            db_transactions.clean_db()
            options()
        elif result == 'find':
            no_of_depts = prompt("Please type number of Depts:")
            db_transactions.find_employees(int(no_of_depts))
            options()
        else:
            print("Wrong Input")


def options():
    options = prompt("Do you want to continue: Yes/No:")
    if options == 'No' or options == 'no' or options == 'n':
        sys.exit()


if __name__ == "__main__":
    db_transactions = DBTransactions()
    prompt_commands()