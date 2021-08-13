from menu import menu, pausa
from db import getData, insertDB, searchDB
from datetime import datetime

def main():
    title = "Menu"
    items = ["1 Insert", 
             "2 GetData", 
             "3 Search",
             "Exit"]

    repeat = True
    while repeat:
        opc = menu(title, items)

        if (opc == 1):
            task = input('Enter a task: ')
            date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            insertDB(task, date)
            pausa(0)

        elif (opc == 2):
            getData()
            pausa(0)

        elif (opc == 3):
            id = input('Enter an id to search: ')
            if searchDB(id) == 1:
                print('Id found')
                pausa(0)
            else:
                print('Id not found')
                pausa()
            
        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
