---
project_name: atk-training-sirisha-q-basic
short_description: A project to implement Persistent Queue mechanism that guarantees no loss of data and can be used by producer, consumer and manager programes to handle restarting the process if it crashes with Sqlite3 as backend
tags: [persist queue]
category: tech
long_description: >
  Pipeline to make sure the jobs crashed while being processed by consumer are readded to the queue. A persitent_queue to implement the mechanism using sqlite3 as backend and a manager program that constantly watches over consumer to check if a process is crashed to add it to queue again.
  Built with poetry
---

TODO: Fix the following
# Problem description
Consider a system with producers producing jobs and consumers accepting the jobs for processing 
# Installation
Import the atk-training-sirisha-q-basic.SQLitePersistentQueue() to use it.

# How to use it

Producer: If a producer uses a Pq library then it uses `put_item` to write the generated file to write it in the sqlite3 table along with the timestamp

``` python
# Here is the psuedo code
pq = persistentQ({name: "db_name", type: "sqlite"})

# To submit the job
id = pq.put_item(item:str)

```

Consumer: If a consumer uses a Pq library and requests for the queued file using get_file() so it fetches the 1st record of the table. The consumer program should be idempotent process. 

``` python

# Here is the psuedo code
pq = persistentQ({name: "db_name", type: "sqlite"})

# To get an item from the queue: Questions to answer:
# How do we know if there are items in the Q?
# what happens if Q is empty?
while terminate_producer is False:
  row = pq.get_item()
  if row:
    #process the item
    def process_item():
      pass
    #update the status of the item as processed.
    pq.update_job_status(item_id,status='DONE') 
  else:
    sleep(100)

#So the consumer waits for a while if there is no item in the file to check again. Otherwise if there is an item to be processed it takes and process it and call get_item() again to get another item. 

```

Manager's job is to make sure that it clears the lingering records that are not processed over "n" minutes (customized via configuration):

``` python
pq = persistentQ({name: "db_name", type: "sqlite"})
# We need to get all the items that are older than a specific duration -- that means that item is orphaned.
# We also want to specify the status of the item -- like under_process or whatever. For each such item,
# take the item and do:
# - change the status so that it will be picked up again.
#
    def monitor(self) -> None:
        pQ.database_connect()
        while self.terminate_manager is False:
            row = pQ.get_item_state()
            if row[1] < datetime.datetime.now() - datetime.timedelta(hours=1) and row[2] < 3:
                pQ.update_item_status(row[0], 'unprocessed')
            elif row[1] < datetime.datetime.now() - datetime.timedelta(hours=1) and row[2] == 3:
                pQ.remove_item(row[0])

            time.sleep(300)
```

The Ops console:

``` python
pq = persistentQ({name: "db_name", type: "sqlite"})

# To print the items
array_of_items_dict = q.get_all_items()

# To manually remove the items from the q
pq.purge(duration, status='processed')

```
