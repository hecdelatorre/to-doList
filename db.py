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
    idL, taskL = [], []
    data = ''
    for item in db:
        idL.append(item['id'])
        taskL.append(item['task'])
        data = data + f"\nid :: {item['id']}\nTask :: {item['task']}\nComplete :: {item['complete']}\nDate :: {item['date']}\n"

    return idL, taskL, data

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

def removeDB(id):
    if searchDB(id) == 1: 
        sure = input('Are you sure to delete, 1 yes, 0 no: ')
        remove = True if sure == '1' else False
        if remove: db.remove(Task.id == id)
