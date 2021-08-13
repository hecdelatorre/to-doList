from tinydb import TinyDB, Query
from uuid import uuid4

db = TinyDB('db/db.json', sort_keys=True, indent=2, separators=(',', ': '))
db.default_table_name = 'tasks'
Task = Query()

def insertDB(task, date):
    complete = False
    data = {
        'id': str(uuid4()),
        'task': task,
        'complete': complete,
        'date': date
    }
    db.insert(data)  

def getData(): 
    for item in db: print(f"id :: {item['id']}\nTask :: {item['task']}\nComplete :: {item['complete']}\nDate :: {item['date']}\n")
