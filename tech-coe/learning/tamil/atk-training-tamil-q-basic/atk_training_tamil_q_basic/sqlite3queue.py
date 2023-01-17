import sqlite3
from abc import ABC, abstractmethod
from atk_training_tamil_q_basic.yamlparser import YamlParser


class AbstractPersistQueue(ABC):

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def update_status(self):
        pass

    @abstractmethod
    def check_and_change_status(self):
        pass

    @abstractmethod
    def crash_count_check(self):
        pass

    @abstractmethod
    def current_status_check(self):
        pass


class PersistentQueue(AbstractPersistQueue):
    def __init__(self):
        self.yaml_data: YamlParser = YamlParser()
        self.yaml_data.parse_yaml()
        self.conn = sqlite3.connect(self.yaml_data.db_name, isolation_level='DEFERRED')
        self.conn_normal = sqlite3.connect(self.yaml_data.db_name, isolation_level='DEFERRED')
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        self.cur_normal = self.conn_normal.cursor()
        self.current_item = None
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {self.yaml_data.table_name} (Id INTEGER PRIMARY KEY AUTOINCREMENT, data Text, status TEXT DEFAULT None, arrived_time INTEGER DEFAULT None, process_start_time INTEGER DEFAULT None,process_end_time INTEGER DEFAULT None, crash_counts INTEGER DEFAULT 0);")

    def __enter__(self):
        print("__enter__ called")
        return self

    def __exit__(self, exc_type: str, exc_value: str, traceback: str):
        print("__exit__ called")
        self.conn.close()

    def put(self, *data: str) -> None:
        self.cur.execute(f"INSERT INTO {self.yaml_data.table_name} (data, status, arrived_time) VALUES (?, 'unprocessed', CURRENT_TIMESTAMP)", data)
        self.conn.commit()

    def get(self) -> 'record':
        self.cur.execute("BEGIN TRANSACTION;")
        self.cur.execute(f"SELECT * FROM {self.yaml_data.table_name} WHERE status = 'unprocessed' ORDER BY Id ASC LIMIT 1;")
        self.current_item: 'record' = self.cur.fetchone()
        if self.current_item:
            self.current_item: 'record' = dict(self.current_item)
            if self.current_item.get('status') != 'in_process':
                self.cur.execute(f"UPDATE {self.yaml_data.table_name} SET status = 'in_process',process_start_time = CURRENT_TIMESTAMP WHERE Id = {self.current_item.get('Id')};")
                self.cur.execute("COMMIT;")
                return self.current_item
        else:
            self.cur.execute("COMMIT;")
            return None

    def update_status(self, id_no: str) -> None:
        self.cur.execute(f"UPDATE {self.yaml_data.table_name} SET status = 'processed', process_end_time = CURRENT_TIMESTAMP WHERE id = ?", (self.current_item.get('Id'),))
        self.conn.commit()

    def check_and_change_status(self) -> None:
        self.cur.execute(f"UPDATE {self.yaml_data.table_name} SET status = 'unprocessed', crash_counts = crash_counts + 1 WHERE status = 'in_process' AND (JULIANDAY(CURRENT_TIMESTAMP)-JULIANDAY(process_start_time))*86400 > {self.yaml_data.crash_time};")
        self.conn.commit()

    def crash_count_check(self) -> 'records':
        self.cur.execute(f"SELECT * FROM {self.yaml_data.table_name} WHERE crash_counts > 3 AND status IN ('unprocessed', 'in_process')")
        crashed_files: 'records' = dict(self.cur.fetchall())
        return crashed_files

    def current_status_check(self) -> 'records':
        self.cur.execute(f"SELECT COUNT(*) FROM {self.yaml_data.table_name};")
        data0: 'record' = self.cur.fetchall()
        self.cur.execute(f"SELECT COUNT(*) FROM {self.yaml_data.table_name} WHERE status = 'in_process';")
        data1: 'record' = self.cur.fetchall()
        self.cur.execute(f"SELECT COUNT(*) FROM {self.yaml_data.table_name} WHERE status = 'processed';")
        data2: 'record' = self.cur.fetchall()
        self.cur.execute(f"SELECT AVG((JULIANDAY(process_end_time)-JULIANDAY(process_start_time))*86400) FROM {self.yaml_data.table_name} WHERE status = 'processed';")
        data3: 'record' = self.cur.fetchall()
        self.cur.execute(f"SELECT COUNT(*) FROM {self.yaml_data.table_name} WHERE crash_counts > 3 AND status IN ('unprocessed','in_process');")
        data4: 'record' = self.cur.fetchall()
        return data0, data1, data2, data3, data4

    def get_all(self) -> 'records':
        self.cur_normal.execute(f"SELECT * FROM {self.yaml_data.table_name};")
        data: 'records' = self.cur_normal.fetchall()
        return data
