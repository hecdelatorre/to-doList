from menu import menu, pausa, receivedData, menuShortcuts
from db import getAll, insertDB, updateDB, removeDB, getById, getPending, getInProgress, getComplete

def main():
    title = "Menu"
    items = ["1 Insert", 
             "2 List all", 
             "3 List pending",
             "4 List in progress",
             "5 List completed",
             "Exit"]

    repeat = True
    while repeat:
        opc = menu(title, items)

        if (opc == 1):
            insertDB()
            pausa(0)

        elif (opc == 2):
            idL, nameL = getAll()
            id = receivedData('Select', idL, nameL, 'purple')
            id = id if id is not None else 'Exit'
            if id != 'Exit':
                info = getById(id, 'Current data')
                print(info[0])
                op = menuShortcuts(['[Update]', '[Remove]', '[Exit]'], 'Select an option', 'green') if id != 'Exit' else id
                if op == 0: updateDB(id)
                elif op == 1: removeDB(id)
            pausa(0.5)

        elif (opc == 3):
            idL, nameL = getPending()
            id = receivedData('Select', idL, nameL, 'red')
            id = id if id is not None else 'Exit'
            if id != 'Exit':
                info = getById(id, 'Current data')
                print(info[0])
                op = menuShortcuts(['[Update]', '[Remove]', '[Exit]'], 'Select an option', 'green') if id != 'Exit' else id
                if op == 0: updateDB(id)
                elif op == 1: removeDB(id)
            pausa(0.5)


        elif (opc == 4):
            idL, nameL = getInProgress()
            id = receivedData('Select', idL, nameL, 'blue')
            id = id if id is not None else 'Exit'
            if id != 'Exit':
                info = getById(id, 'Current data')
                print(info[0])
                op = menuShortcuts(['[Update]', '[Remove]', '[Exit]'], 'Select an option', 'green') if id != 'Exit' else id
                if op == 0: updateDB(id)
                elif op == 1: removeDB(id)
            pausa(0.5)

        elif (opc == 5):
            idL, nameL = getComplete()
            id = receivedData('Select', idL, nameL, 'green')
            id = id if id is not None else 'Exit'
            if id != 'Exit':
                info = getById(id, 'Current data')
                print(info[0])
                op = menuShortcuts(['[Update]', '[Remove]', '[Exit]'], 'Select an option', 'green') if id != 'Exit' else id
                if op == 0: updateDB(id)
                elif op == 1: removeDB(id)
            pausa(0.5)

        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
