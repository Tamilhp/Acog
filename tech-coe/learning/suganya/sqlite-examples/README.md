# Examples of the sqlite
Here are the tasks to do:

1. Start with SQLite
2. Write a simple program that opens up SQLite on the local machine in a file. Make sure that you use typer so that you get the command line. That is, it takes a db file name and creates a SQLite db in that file. And, prints out the version of SQLite and the library. We will use https://docs.python.org/3/library/sqlite3.html for that. 
3. Next create a database with the following structure
- employee id, name, dept id
- dept id, dept name, parent dept (NULL means there is none)
- employee id, password
Assume id's are unique. So, they can be used as keys.
4. Create the tables in the db, if they do not exist
5. Generate names and ids and depts randomly (Use python module names for that) and insert them into the db. Departments may not be random -- you can hard code names using the dept id. 
6. Write a function that gets top n employees or all, from the given dept.
7. Given an employee, find the dept.
8. Given an empoyee id and password, return true/false
9. Given a name, return all the possible ids

For now, command line program that takes these options will be great. Like the following commands:

- createdb
- loaddb -n [number of employees] -d [number of depts]
- cleandb
- findemployees [deptid]
- finddept [empid]
- findids [empname]
- validpassword id password

No ORM for now. Feel free to use SQL.

Future directions:
1. Convert it to web services
2. Using ORM
3. Supporting Postgres with the same code

--------------------------------------------------------------------
Tasks:

Modularize the existing program and add exception Handling

Use prompt_toolkit instead of typer

Added 2 files: cli_commands.py & transactions.py:

cli_commands.py:
0. Get the input from the user to call the respective methods. along with its required inputs to call the respective functions.
1. Once the user enters the correct option[say for e.g. , if user enters create, call create_db()], the respective methods will be called.
2. If the user enters a wrong option, then, the user will be provided with a prompt stating Wrong Input . User is again prompted for database inputs.
3. Several prompts being added for the user to understand. Say for e.g., once the db is created,the user will be prompted with a message stating DB is created along with the <db_name>. Likewise, for other db operations and exceptions.
4. After each and every db operation, user is being prompted with a Yes/No message to continue the flow/not. Once the user enters exit option, the current flow exits.

transactions.py:
0. DB transactions happens here
