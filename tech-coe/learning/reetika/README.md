**Examples of the sqlite**

Here are the tasks to do:

Start with SQLite
Write a simple program that opens up SQLite on the local machine in a file. Make sure that you use typer so that you get the command line. That is, it takes a db file name and creates a SQLite db in that file. And, prints out the version of SQLite and the library. We will use https://docs.python.org/3/library/sqlite3.html for that.
Next create a database with the following structure
employee id, name, dept id
dept id, dept name, parent dept (NULL means there is none)
employee id, password Assume id's are unique. So, they can be used as keys.
Create the tables in the db, if they do not exist
Generate names and ids and depts randomly (Use python module names for that) and insert them into the db. Departments may not be random -- you can hard code names using the dept id.
Write a function that gets top n employees or all, from the given dept.
Given an employee, find the dept.
Given an empoyee id and password, return true/false
Given a name, return all the possible ids
For now, command line program that takes these options will be great. Like the following commands:

createdb
loaddb -n [number of employees] -d [number of depts]
cleandb
findemployees [deptid]
finddept [empid]
findids [empname]
validpassword id password
No ORM for now. Feel free to use SQL.

Future directions:

Convert it to web services
Using ORM
Supporting Postgres with the same code
-----------------------------------------
Tasks: 
0. Modularize the existing program and add exception Handling
1. Use prompt_toolkit instead of typer 
2. Added 2 files: sqlite_using_prompt.py & sqlite_using_promp_dialog.py
    sqlite_using_prompt.py: 
    0. Get the input from the user to call the respective methods. along with its required inputs to call the
       respective functions.
    1. Once the user enters the correct option[say for e.g. , if user enters `create`, call create_db()],
       the respective methods will be called. 
    2. If the user enters a wrong option, then, the user will be provided with a prompt stating `Wrong Input`
    3. User is again prompted for database inputs. 
    4. Several prompts being added for the user to understand. Say for e.g., once the db is created,the user
       will be prompted with a message stating `DB is created along with the <db_name>`. Likewise, for other 
       db operations and exceptions.
    5. After each and every db operation, user is being prompted with a `Yes/No` message to continue 
       the flow/not. Once the user enters `exit` option, the current flow exits.
       
    sqlite_using_prompt_dialog.py: 
    0. Get the input from the user by using the prompt's built-in radiolist_dialog() to do the respective db operations.
    1. Once the user clicks the correct option, the respective methods will be called.[say for e.g. , if user chooses 
       `Create`, then create_db()  method will be called].
    2. Several messages are being added for the user to understand. Say for e.g., once the db is created,the user
       will be prompted with a message using prompt's built-in message dialog box(message_dialog()) stating 
       `DB is created along with the <db_name>`. 
       Likewise, for other db operations and exceptions.
    3. For getting the input for the db related operations, prompt's built-in input dialog box (input_dialog()) is being used. 
    4. Once the user select `Exit` option from the prompt's built-in radiolist_dialog(), the current flow exits.
    5. To style the application, prompt's built-in Style is being used.
    