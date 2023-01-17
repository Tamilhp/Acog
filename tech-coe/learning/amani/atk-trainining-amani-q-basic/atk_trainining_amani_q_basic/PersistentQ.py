# This module consists of PersistentQ abstract class and its implementation
import sqlite3
from abc import ABC
from typing import Any
import logging

logging.basicConfig(level='INFO')


class PersistentQ(ABC):
    def __init__(self, db_info):
        self.dbname = db_info['dbname']
        self.dbtype = db_info['dbtype']
        self.conn = None
        self.cur = None
        self.db_connect()

    def db_connect(self):
        pass

    def put_item(self, item: str) -> None:
        pass

    def get_item(self) -> Any | None:
        pass

    def update_status(self, job_id: int, status: str) -> None:
        pass


class PQ(PersistentQ):
    def db_connect(self):
        # Establishes database connection with given dbtype and dbname
        if self.dbtype == sqlite3:
            logging.info("Connected Database")
            self.conn = sqlite3.connect(self.dbname, isolation_level='DEFERRED', check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
            self.cur = self.conn.cursor()
            create_table = """CREATE TABLE IF NOT EXISTS q_table
                           (item_id integer PRIMARY KEY AUTOINCREMENT, item TEXT,
                           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
                           status TEXT DEFAULT "unprocessed", submission_count integer DEFAULT 0)"""
            self.cur.execute(create_table)
            logging.info("Created Table")
        elif self.dbtype == 'postgres':
            pass
            # Implement postgres connection

    def put_item(self, item: str) -> None:
        # Inserting item into db
        logging.info(f"Inserting the {item} to table")
        self.cur.execute("INSERT INTO q_table (item) VALUES (:item)", (item,))
        self.conn.commit()

    def get_item(self) -> Any | None:
        # Fetches item whose state is in unprocessed
        # cur = self.conn.cursor()
        count = self.cur.execute("SELECT COUNT(*) FROM q_table WHERE status = 'unprocessed'")
        if count:
            cursor = self.cur.execute(f"SELECT item_id,item FROM q_table WHERE status = 'unprocessed' LIMIT 1")
            row = dict(cursor.fetchone())
            status = "under_process"
            self.update_status(row['item_id'], status, 0)
            self.conn.commit()
            return row
        else:
            return None

    def update_status(self, item_id: int, status: str, submission_count: int):
        if submission_count:
            update_status = '''UPDATE q_table SET
                                        status = ?,
                                        timestamp = CURRENT_TIMESTAMP,
                                        submission_count = ?
                                        WHERE item_id = ?'''
            self.cur.execute(update_status, (status, submission_count, item_id))
        else:
            update_status = '''UPDATE q_table SET 
                                status = ?,
                                timestamp = CURRENT_TIMESTAMP,
                                submission_count = submission_count+1
                                WHERE item_id = ?'''

            self.cur.execute(update_status, (status, item_id))
            logging.info(f"Updating status of {item_id} to {status}")
        self.conn.commit()

    def manage_q(self, check_time):
        self.cur.execute('''UPDATE q_table SET "status" = 'manual_check' WHERE submission_count is 3 
                                                  AND status is 'under_process' 
                                                  AND timestamp < DATETIME('now', ?)''', (check_time,))

        self.cur.execute(f"""UPDATE q_table SET status = 'unprocessed' WHERE submission_count < 3 
                                    AND status = 'under_process' AND timestamp < DATETIME('now', ?)""", (check_time,))
        self.conn.commit()

    def get_status(self, status: str = None):
        if status:
            cursor = self.conn.execute('''SELECT * FROM q_table WHERE status = ?''', (status,))
        else:
            cursor = self.conn.execute('''SELECT * FROM q_table''')
        data = cursor.fetchall()
        return data

    def delete_item(self, item_id: int):
        self.cur.execute('''DELETE FROM q_table WHERE item_id = ? ''', (item_id,))
        self.conn.commit()

    def get_items(self):
        cursor = self.conn.execute('''SELECT * FROM q_table''')
        data = cursor.fetchall()
        return data
