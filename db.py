from tinydb import TinyDB, Query
from uuid import uuid4
from datetime import datetime

db = TinyDB('db/db.json', sort_keys=True, indent=2, separators=(',', ': '))
db.default_table_name = 'tasks'
Task = Query()

def insertDB():
    task = input('Enter a task: ')
    date =datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = {
        'id': str(uuid4()),
        'task': task,
        'complete': False,
        'date': date
    }
    db.insert(data)

def getData(): 
    for item in db: print(f"id :: {item['id']}\nTask :: {item['task']}\nComplete :: {item['complete']}\nDate :: {item['date']}\n")

def searchDB(id): return len(db.search(Task.id == id))

def updateDB(id):
    if searchDB(id) == 1:
        task = input('Enter task: ')
        mark = input('Mark as completed 1 and not completed 0: ')
        complete = True if mark == '1' else False
        date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        data = {
            'task': task,
            'complete': complete,
            'date': date
        }
        db.update(data, Task.id == id)
