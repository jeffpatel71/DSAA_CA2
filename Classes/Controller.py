from Models import *

class Controller():
    def __init__(self, view, models, utilities):
        self.__view = view
        self.__models = models
        self.__utilities = utilities
        self.__options = hashtable()    
        print(self.__menustack[0]) #print the inital menu

    def run(self):
        # Dynamically display the menu and adjust the menu options
        _, length = self.__view.display_menu()
        hashtable_menu = hashtable() 
        for i in range(length):
            hashtable_menu[str(i)] = getattr(self, f'selection{i}')

        while True:
            self.__view.display_menu()
            selection = self.__utilities.check_input("^[0-9]+$", "Enter your selection: ", "Invalid input, please enter a valid selection")
            hashtable_menu[selection] # hashtable
            if selection == str(length-1): 
                break
        
        # Alternate Method ; Ask Irfan for this part
        # menustack = self.__models.Stack()
        # menustack.push(self.__view.display_menu())
        # while True:
        #     if menustack.isEmpty():
        #         break
    
    def selection1(self):
        
        expression = self.__utilities.get_expression("Please type text you want to encrypt: \n")


        return