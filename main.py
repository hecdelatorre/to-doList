from menu import menu, pausa

def main():
    title = "Menu"
    items = ["1 Option", 
             "2 Option", 
             "3 Option", 
             "Exit"]

    repeat = True
    while repeat:
        opc = menu(title, items)

        if (opc == 1):
            print('Option 1')
            pausa()
        elif (opc == 2):
            print('Option 2')
            pausa()
        elif (opc == 3):
            print('Option 3')
            pausa()
    
        repeat = (opc < len(items))

if __name__ == "__main__":
    main()
