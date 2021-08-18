from menu import menu, pausa, receivedData, menuShortcuts
from db import getAll, insertDB, updateDB, removeDB

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
            id = receivedData('Select', idL, nameL)
            id = id if id is not None else 'Exit'
            op = menuShortcuts(['[Update]', '[Remove]'], 'Select an option', 'green') if id != 'Exit' else id
            updateDB(id) if op == 0 else removeDB(id)
            pausa(0.5)

        elif (opc == 3):
            pausa()

        elif (opc == 4):
            pausa()

        elif (opc == 5):
            pausa()

        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
