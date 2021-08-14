from tinydb import TinyDB, Query
from uuid import uuid4
from datetime import datetime

db = TinyDB('db/db.json', indent=2, separators=(',', ': '))
db.default_table_name = 'list'
Element = Query()

def insertDB():
    name = input('Enter a name: ')
    valName = True
    count = 0
    while valName:
        for _ in name: count += 1
        if count == 0: name = input('Please enter a valid name: ')
        valName = (count == 0)

    date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = {
        'id': str(uuid4()),
        'name': name,
        'state': {
            'inProgress': False,
            'complete': False
        },
        'date': date
    }
    db.insert(data)

def getData():
    idL, nameL = [], []
    data = ''
    for item in db:
        idL.append(item['id'])
        nameL.append(item['name'])
        data = data + f"\nName :: {item['name']}\nIn progress :: {item['state']['inProgress']}\nComplete :: {item['state']['complete']}\nDate :: {item['date']}\n"
    idL.append('Exit')
    nameL.append('Exit')
    return idL, nameL, data

def searchDB(id): return len(db.search(Element.id == id))

def updateDB(id):
    if searchDB(id) == 1:
        name = db.search(Element.id == id)[0]['name']
        inProgress = db.search(Element.id == id)[0]['state']['inProgress']
        complete = db.search(Element.id == id)[0]['state']['complete']
        date = db.search(Element.id == id)[0]['date']

        print(f"\nCurrent data\n\nName :: {name}\nIn progress :: {inProgress}\nComplete :: {complete}\nDate :: {date}\n")
        
        changeName = input('Modify name 1 yes, 0 no: ')
        changeName = True if changeName == '1' else False
        name = input('Please enter a new name: ') if changeName else name
        
        valName = True
        count = 0
        while valName:
            for _ in name: count += 1
            if count == 0: name = input('Please enter a valid name: ')
            valName = (count == 0)

        
        changeState = input('Mark as pending 0, in progress 1 and finished 2: ')
        inProgress = True if changeState == '1' else False
        complete = True if changeState == '2' else False
        date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        data = {
            'name': name,
            'state': {
                'inProgress': inProgress,
                'complete': complete
            },
            'date': date
        }
        db.update(data, Element.id == id)

def removeDB(id):
    if searchDB(id) == 1: 
        sure = input('Are you sure to delete, 1 yes, 0 no: ')
        remove = True if sure == '1' else False
        if remove: db.remove(Element.id == id)

def getComplete():
    # com = db.search(Element.state.complete == True)
    return ''
