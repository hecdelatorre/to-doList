from menu import menu, pausa
from db import getData, insertDB
from datetime import datetime

def main():
    title = "Menu"
    items = ["1 Insert", 
             "2 GetData", 
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
            
        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
