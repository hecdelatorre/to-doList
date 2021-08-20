from simple_term_menu import TerminalMenu
from time import sleep

def pausa(t = 0.5): input('Press a key to continue') if(t == 0) else sleep(t)

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
    return num + 1 if num is not None else exit()

def receivedData(title, idL, nameL, color = 'cyan'):
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
    return idL[num] if num is not None else 'Exit'

def menuShortcuts(items, title, color = 'cyan'):
    menu = TerminalMenu (
        items, 
        title = f"  {title}",
        menu_cursor = "❯ ",
        menu_cursor_style = (f"fg_{color}", "bold"),
        menu_highlight_style = ("fg_gray", f"fg_{color}"),
        shortcut_key_highlight_style = ("fg_green",),
        shortcut_brackets_highlight_style = ("fg_green",)
    )

    index = menu.show()
    return index
