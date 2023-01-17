import collections
from abc import ABC
import sqlite3
from typing import Any


class PersistentQueue(ABC):
    def __init__(self, db_info):
        # Connect to the database
        self.db_name = db_info['db_name']
        self.db_type = db_info['db_type']
        self.conn=None
        self.cursor=None

    def database_connect(self):
        pass

    def add_item(self, job):
        pass

    def get_item(self):
        pass

    def update_job_status(self, job_id, status):
        pass

    def manual_checking_items(self):
        pass


class PersistentQueueDb(PersistentQueue):

    def database_connect(self) -> None:
        if self.db_type == sqlite3:
            self.conn = self.db_type.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS queue (
                                    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    item_value TEXT,
                                    status TEXT DEFAULT unprocessed,
                                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                                    resubmit_count INTEGER DEFAULT 0
                                );
                            ''')
            self.cursor.execute('SELECT * FROM queue')

        else:
            pass
            # conn = psycopg2.connect(database="db_name",
            #                         host="db_host",
            #                         user="db_user",
            #                         password="db_pass",
            #                         port="db_port")
            # Create the jobs table if it doesn't exist

    def add_item(self, item: str) -> None:
        # Insert a new job into the queue
        self.cursor.execute("INSERT INTO queue (item_value) VALUES (:item)", (item,))
        self.cursor.execute("COMMIT")

    def get_item(self) -> Any | None:
        # Get the next job from the queue
        count = self.conn.execute("SELECT count(*) FROM queue WHERE status = 'unprocessed'")
        print(*count)
        if count:
            cursor = self.conn.execute("SELECT * FROM queue WHERE status = 'unprocessed' LIMIT 1")
            row = cursor.fetchone()
            print(row)
            self.conn.execute(f"""UPDATE queue SET status='under_process', resubmit_count=resubmit_count+1,
            timestamp=CURRENT_TIMESTAMP WHERE item_id={row[0]}""")
            self.conn.commit()
            return row
        else:
            return None

    def update_item_status(self, item_id: int, status: str) -> None:
        # Update the job status
        self.conn.execute("UPDATE queue SET status = ? WHERE item_id = ?", (status, item_id))
        self.conn.commit()

    def get_item_state(self) -> Any:
        cursor = self.conn.execute("""SELECT item_id,timestamp,resubmit_count from 
        queue where status = 'under_process' LIMIT 1""")
        return cursor.fetchone()

    def manual_checking_items(self):
        cursor = self.conn.execute("SELECT * FROM queue WHERE status = 'Manual_check'")
        rows = cursor.fetchall()
        return rows

