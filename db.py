from tinydb import TinyDB, Query
from uuid import uuid4
from datetime import datetime
from menu import menuShortcuts
from colored import fg, attr

colorRed = fg('red')
colorGreen = fg('green')
colorBlue = fg('blue')
res = attr('reset')

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

def getAll():
    idL, nameL = [], []
    for item in db:
        idL.append(item['id'])
        nameL.append(item['name'])
    idL.append('Exit')
    nameL.append('Exit')
    return idL, nameL

def searchDB(id): return len(db.search(Element.id == id))

def getById(id, message):
    name = db.search(Element.id == id)[0]['name']
    inProgress = db.search(Element.id == id)[0]['state']['inProgress']  
    complete = db.search(Element.id == id)[0]['state']['complete']
    date = db.search(Element.id == id)[0]['date']
    info = f"\n{message}\n\n{colorBlue}Name{res} :: {name}\nIn progress :: {inProgress}\nComplete :: {complete}\nDate :: {date}\n"
    return info, name, inProgress, complete, date

def updateDB(id):
    if searchDB(id) == 1:
        info, name, inProgress, complete, date = getById(id, 'Current data')
        print(info)

        changeName = menuShortcuts(['[Yes]', '[NO]'], 'Modify name', 'green')
        changeName = True if changeName == 0 else False
        name = input('Please enter a new name: ') if changeName else name
        name = valitadateText(name, 'Please enter a valid name: ')

        changeState = menuShortcuts(['[Pending]', '[In progress]', '[Finished]'], 'Modify state', 'green')
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
        sure = menuShortcuts(['Yes', 'No'], 'Are you sure to delete?', 'red')
        remove = True if sure == 0 else False
        if remove: db.remove(Element.id == id)

def getPending():
    idL, nameL = [], []
    for item in db:
        if item['state']['complete'] == False and item['state']['inProgress'] == False: 
            idL.append(item['id'])
            nameL.append(item['name'])
    idL.append('Exit')
    nameL.append('Exit')
    return idL, nameL

def getComplete():
    idL, nameL = [], []
    for item in db:
        if item['state']['complete']: 
            idL.append(item['id'])
            nameL.append(item['name'])
    idL.append('Exit')
    nameL.append('Exit')
    return idL, nameL

def getInProgress():
    idL, nameL = [], []
    for item in db:
        if item['state']['inProgress']: 
            idL.append(item['id'])
            nameL.append(item['name'])
    idL.append('Exit')
    nameL.append('Exit')
    return idL, nameL
