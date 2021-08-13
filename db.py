from tinydb import TinyDB, Query

db = TinyDB('db/db.json', sort_keys=True, indent=2, separators=(',', ': '))
db.default_table_name = 'tasks'
Task = Query()

def insertDB(task, date):
    complete = False
    data = {
        'task': task,
        'complete': complete,
        'date': date
    }
    dat = db.insert(data)
    print(dat)
    

def getData():
    for item in db: print(item)
