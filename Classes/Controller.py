from Classes.Models.Hash import HashTable 
from Classes.Utilities.IO import IO
from Classes.Menu import Menu
from Classes.View import View
import Classes.Models as Model
# from Classes.Models import *

class Controller():
    def __init__(self, io):
        self.__view = View() # View Object (Don't want to allow users to create view object outside of Controller)
        self.__model = Model # Model Object (Import all models in the folder)
        self.__io = IO()
        self.__hashtable()

    # Run Function
    def run(self, folder_path, credits_file, menufile):

        # Instantiate Menu Object that contains the credits and menu options
        menu = Menu(folder_path, credits_file, menufile)

        # Display Credits
        menu.display_credits()

        # Dynamically display the menu and adjust the menu options
        length = menu.display_menu()
        
        # Create a Hastable to store the menu options
        hashtable_menu = self.__model.HashTable()
        for i in range(length):
            hashtable_menu[str(i)] = getattr(self, f'selection{i}')

        # Display Menu and get user selection till user quits
        while True:
            menu.display_menu()
            selection = self.io.check_input("^[0-9]+$", "Enter your selection: ", "Invalid input, please enter a valid selection")
            hashtable_menu[selection] 
            if selection == str(length-1): 
                break
        
        # Alternate Method ; Ask Irfan for this part
        # menustack = self.__models.Stack()
        # menustack.push(self.__view.display_menu())
        # while True:
        #     if menustack.isEmpty():
        #         break
    
    def selection1(self):
        
        FileHandler = IO()
        expression = FileHandler.get_expression("Please type text you want to encrypt: \n")\
        
        return
    
    def selection2(self):
        return 
    
    def selection3(self):
        return
    
    def selection4(self):
        return
    
    def selection5(self):
        return
    
    def selection6(self):
        return
    
    
