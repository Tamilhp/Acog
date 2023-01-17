from atk_training_sirisha_q_basic.manager import Manager
from atk_training_sirisha_q_basic.producer import Producer
from atk_training_sirisha_q_basic.consumer import Consumer
from atk_training_sirisha_q_basic.persitent_queue import PersistentQueueDb
import random
import string


# Instantiate an object of the class
def producer_creation():
    producer_obj = Producer()
    print(type(producer_obj))
    producer_obj.insert_item()


def consumer_creation():
    consumer_obj = Consumer()
    consumer_obj.process()


def manager_creation():
    manager_obj = Manager()
    manager_obj.monitor()


persistent_obj = PersistentQueueDb({'db_name': 'persistent.db', 'db_type': 'sqlite3'})
producer_creation()
consumer_creation()
manager_creation()

while True:
    jobs_list = [producer_creation(), consumer_creation(), manager_creation()]
    random.choice(jobs_list)
