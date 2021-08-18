from tinydb import TinyDB, Query
from uuid import uuid4
from datetime import datetime
from menu import menuShortcuts
from colored import fg, attr

colorRed = fg('#CC0000')
colorGreen = fg('#73D216')
colorBlue = fg('#338CFF')
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
    description = input('Enter a description: ')
    description = valitadateText(description, 'Please enter a valid description: ')
    date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    data = {
        'id': str(uuid4()),
        'name': name,
        'description': description,
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

def getById(id, message = 'Current data'):
    name = db.search(Element.id == id)[0]['name']
    description = db.search(Element.id == id)[0]['description']
    inProgress = db.search(Element.id == id)[0]['state']['inProgress']  
    complete = db.search(Element.id == id)[0]['state']['complete']
    date = db.search(Element.id == id)[0]['date']
    info = f"\n{message}\n\n{colorBlue}Name{res} :: {name}\n{colorBlue}Description{res} :: {description}\n{colorBlue}In progress{res} :: {colorGreen if inProgress else colorRed}{inProgress}{res}\n{colorBlue}Complete{res} :: {colorGreen if complete else colorRed}{complete}{res}\n{colorBlue}Date{res} :: {date}\n"
    return info, name, description, inProgress, complete, date

def updateDB(id):
    if searchDB(id) == 1:
        _, name, description, inProgress, complete, date = getById(id)

        changeName = menuShortcuts(['[Yes]', '[NO]'], 'Modify name', 'green')
        changeName = True if changeName == 0 else False
        name = input('Please enter a new name: ') if changeName else name
        name = valitadateText(name, 'Please enter a valid name: ')

        changeDescription = menuShortcuts(['[Yes]', '[NO]'], 'Modify description', 'green')
        changeDescription = True if changeDescription == 0 else False
        description = input('Please enter a new description: ') if changeDescription else description
        description = valitadateText(description, 'Please enter a valid description: ')

        changeState = menuShortcuts(['[Pending]', '[In progress]', '[Finished]'], 'Modify state', 'green')
        inProgress = True if changeState == 1 else False
        inProgress = False if changeState == 0 else inProgress
        complete = True if changeState == 2 else False
        complete = False if changeState == 0 else complete

        date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        data = {
            'name': name,
            'description': description,
            'state': {
                'inProgress': inProgress,
                'complete': complete
            },
            'date': date
        }
        db.update(data, Element.id == id)

def removeDB(id):
    if searchDB(id) == 1: 
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
