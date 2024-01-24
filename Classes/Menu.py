from Classes.Models.Stack import Stack
from Classes.Utilities.IO import IO
from Classes.Utilities.Class_Errors import errors

class Menu():
    ## Constructor Function
    def __init__(self, folder_path = None, creditfile = None, menuFile = None):
        self.__folder_path = folder_path
        self.__creditfile = creditfile
        self.__menuFile = menuFile

    ## Display Credits
    def display_credits(self):
        content = IO.open_non_empty_file(f"{self.__folder_path}/{self.__creditfile}", prompt = f"Please enter a real file name:")
        # Raise Error if file is empty/invalid don't ask for re-prompt
        print(content)
    
    ## Display Selection Menu
    def display_menu(self):
        menu_stack = Stack()
        raw_menu = IO.open_non_empty_file(f"{self.__folder_path}/{self.__menuFile}", prompt = f"Please enter a real file name:")
        raw_menu = raw_menu.split("\n")
        for line in raw_menu:
            menu_stack.push(line)
        print(menu_stack)
        return len(menu_stack)
        
        

        