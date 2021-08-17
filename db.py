from tinydb import TinyDB, Query
from uuid import uuid4
from datetime import datetime
from menu import menuShortcuts

db = TinyDB('db/db.json', indent=2, separators=(',', ': '))
db.default_table_name = 'list'
Element = Query()

def valitadateText(text, message, valName = True, count = 0):
    while valName:
        for _ in text: count += 1
        text = input(f'{message}') if count == 0 else text
        valName = (count == 0)
    return text

def insertDB():
    name = input('Enter a name: ')
    name = valitadateText(name, 'Please enter a valid name: ')
    
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

def getById(id, message):
    name = db.search(Element.id == id)[0]['name']
    inProgress = db.search(Element.id == id)[0]['state']['inProgress']  
    complete = db.search(Element.id == id)[0]['state']['complete']
    date = db.search(Element.id == id)[0]['date']
    info = f"\n{message}\n\nName :: {name}\nIn progress :: {inProgress}\nComplete :: {complete}\nDate :: {date}\n"
    return info, name, inProgress, complete, date

def updateDB(id):
    if searchDB(id) == 1:
        info, name, inProgress, complete, date = getById(id, 'Current data')
        print(info)

        changeName = menuShortcuts(['[Si]', '[NO]'], 'Modify name')
        changeName = True if changeName == 0 else False
        name = input('Please enter a new name: ') if changeName else name
        name = valitadateText(name, 'Please enter a valid name: ')

        changeState = menuShortcuts(['[Pending]', '[In progress]', '[Finished]'], 'Modify state')
        inProgress = True if changeState == 1 else False
        inProgress = False if changeState == 0 else inProgress
        complete = True if changeState == 2 else False
        complete = False if changeState == 0 else complete

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
        info = getById(id, 'Data to remove')
        print(info[0])
        sure = input('Are you sure to delete, 1 yes, 0 no: ')
        remove = True if sure == '1' else False
        if remove: db.remove(Element.id == id)

def getComplete():
    # com = db.search(Element.state.complete == True)
    return ''
