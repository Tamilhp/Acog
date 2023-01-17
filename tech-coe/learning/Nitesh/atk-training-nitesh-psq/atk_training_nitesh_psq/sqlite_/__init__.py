import sqlite3
import typer


app=typer.Typer()



class SQLITE:
    def __init__(self,db_name:str='queue.db'):
        self.db=db_name
         #Connect to the database
        with sqlite3.connect(db_name) as conn:


# Create a cursor
            cursor = conn.cursor()

# Create the queue table
            cursor.execute('''
                CREATE TABLE if not exists queue (
                id INTEGER PRIMARY KEY,
                    item TEXT,
                    status TEXT
                            )
                        ''')
            conn.commit()
    def put(self,*items):
         with sqlite3.connect(self.db) as conn:

    # Create a cursor
            cursor = conn.cursor()

    # Insert the item into the queue
            for item in items:
                cursor.execute('''
                INSERT INTO queue (item, status)
                VALUES (?, ?)
                ''', (item, 'pending'))

    # Commit the changes
            conn.commit()
    def process(self,db_name:str='queue.db'):
        with sqlite3.connect(self.db) as conn:

    # Create a cursor
            cursor = conn.cursor()

    # Select the first pending item from the queue
            cursor.execute('''
            SELECT id, item FROM queue
                    WHERE status = 'pending'
                    ''')

    # Fetch the item
            item = cursor.fetchall()
    

            if item is not None:
        # Process the item
                for item_ in item:
            
                    print("Processing Item: ---->  " + item_[1].upper())

        # Update the item's status to "completed"
                    cursor.execute('''
                        UPDATE queue
                        SET status = 'completed'
                        WHERE id = ?
                        ''', (item_[0],))
        

        

        # Commit the changes
                    conn.commit()

    # Close the connection


# Commit the changes
@app.command()
def init(db_name:str='queue.db'):
    slq=SQLITE(db_name)
    print

def init_():
    app()
