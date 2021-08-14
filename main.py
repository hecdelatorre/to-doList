from menu import menu, pausa, receivedData
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
            idL, nameL, _ = getData()
            id = receivedData('Select: ', idL, nameL, 'green')
            if id != 'Exit':
                updateDB(id)
                pausa(0)

        elif (opc == 4):
            idL, nameL, _ = getData()
            id = receivedData('Select: ', idL, nameL, 'red')
            if id != 'Exit':
                removeDB(id)
                pausa(0)

        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
