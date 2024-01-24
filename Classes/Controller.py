from Classes.Models.Hash import HashTable 
from Classes.Utilities.IO import IO
from Classes.Menu import Menu
from Classes.View import View


import Classes.Models as Model


class Controller():
    def __init__(self):
        self.__view = View() # View Object (Don't want to allow users to create view object outside of Controller)
        self.__model = Model # Model Object (Import all models in the folder)
        self.__io = IO()
        self.__storehashtable= Model.HashTable()
        self.enter_message = input("\n Press enter key, to continue...")


    # Run Function
    def run(self, folder_path, credits_file, menufile):

        # Instantiate Menu Object that contains the credits and menu options
        menu = Menu(folder_path, credits_file, menufile)

        # Display Credits
        menu.display_credits()

        # Dynamically display the menu and adjust the menu options
        length = menu.getlength() 
        
        # Create a Hastable to store the menu options
        hashtable_menu = self.__model.HashTable()
        for i in range(length):
            hashtable_menu[str(i)] = getattr(self, f'selection{i}')

        # Display Menu and get user selection till user quits
        while True:
            menu.display_menu()
            regex = f"^[0-{length-1}]$"
            selection = self.io.check_input(regex, "Enter your selection: ", "Invalid input, please enter a valid selection")
            if selection == str(length-1):
                break
            hashtable_menu[selection]
            self.enter_message() 
            
    def selection1(self):
        # Add/Modify Assignment Statements
        expression = self.__io.get_expression("Enter the assignment statement you want to add/modify: \n For example, a=(1+2)\n")
        
        return
    
    def selection2(self):
        # Display Assignment Statements
        print(f"Current Assignments:\n{'*' * 20}")
        self.__view.display_assignments()
        
        return 
    
    def selection3(self):
        # Evaluate Assignment Statements
        self.__io.get_expression("Please enter the variable you want to evaluate: \n")
        print("\n")

        self.__view.display_evaluation()
        return
    
    def selection4(self):
        # Read Assigment Statements from File
        self.__io.get_file_path("Please enter the input file: \n")

        self.__view.display_assignments()
        return
    
    def selection5(self):
        # Sort Assignment Statements
        self.__storehashtable  = self.__sort.bubble_sort(self.__storehashtable)
        self.__view.display_assignments()
        return
    
    
    
