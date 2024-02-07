from Classes.Models.Stack import Stack
from Classes.Utilities.files import File_Manager 
# from Classes.Utilities.errors import Class_Errors

class Menu():
    ## Constructor Function
    def __init__(self, folder_path = None, creditfile = None, menuFile = None):
        self.__folder_path = folder_path
        self.__creditfile = creditfile
        self.__menuFile = menuFile
        self.__menu_stack = Stack()

    ## Display Credits
    def display_credits(self):
        file = File_Manager(file_name=self.__creditfile, folder_name=self.__folder_path)
        content = file.open_non_empty_file(prompt = f"Please enter a real file name:")        
        print(content)
    
    ## Display Selection Menu
    def load_menu(self):
        self.__menu_stack = Stack()
        raw_menu = File_Manager(file_name=self.__menuFile, folder_name=self.__folder_path)
        raw_menu = raw_menu.open_non_empty_file(prompt = f"Please enter a real file name:")
        raw_menu = raw_menu.split("\n")
        for line in raw_menu:
            self.__menu_stack.push(line)
        return self.__menu_stack.size()
    
    def display_menu(self):
        print(self.__menu_stack)
    
    

        

        