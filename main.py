from menu import menu, pausa
from db import getData, insertDB, updateDB, removeDB

def main():
    title = "Menu"
    items = ["1 Insert", 
             "2 GetData", 
             "3 Update",
             "4 Remove",
             "Exit"]

    repeat = True
    while repeat:
        opc = menu(title, items)

        if (opc == 1):
            insertDB()
            pausa(0)

        elif (opc == 2):
            _, _, data = getData()
            print(f' Data\n{data}')
            pausa(0)

        elif (opc == 3):
            id = input('Enter an id to update: ')
            updateDB(id)
            pausa(0)

        elif (opc == 4):
            id = input('Enter an id to remove: ')
            removeDB(id)
            pausa(0)

        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
