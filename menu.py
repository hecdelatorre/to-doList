# pip install simple-term-menu

from simple_term_menu import TerminalMenu
import time

def pausa(t = 1): 
    if(t == 0): input('Press a key to continue ')
    else: time.sleep(t)

def menu(title, items):
    cursor = "❯ "
    cursor_style = ("fg_cyan", "bold")
    menu_style = ("fg_gray", "fg_cyan")

    main_menu = TerminalMenu(
        menu_entries = items,
        title = f'  {title}',
        menu_cursor = cursor,
        menu_cursor_style = cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )
    
    num = main_menu.show()
    num = num + 1 if num is not None else exit()
    return num

def receivedData(title, idL, nameL, color):
    cursor = "❯ "
    cursor_style = (f"fg_{color}", "bold")
    menu_style = ("fg_gray", f"fg_{color}")
    main_menu = TerminalMenu(
        menu_entries = nameL,
        title = f'  {title}',
        menu_cursor = cursor,
        menu_cursor_style = cursor_style,
        menu_highlight_style = menu_style,
        cycle_cursor = True,
        clear_screen = True
    )
    
    num = main_menu.show()
    return idL[num]

def menuShortcuts(items, title):
    menu = TerminalMenu (
        items, 
        title = f"  {title}",
        menu_cursor = "❯ ",
        menu_cursor_style = ("fg_cyan", "bold"),
        menu_highlight_style = ("fg_gray", "fg_cyan"),
        shortcut_key_highlight_style = ("fg_green",),
        shortcut_brackets_highlight_style = ("fg_green",)
    )

    index = menu.show()
    return index
