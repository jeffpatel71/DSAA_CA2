from Models import *

class Controller():
    def __init__(self, view, models, utilities):
        self.__view = view
        self.__models = models
        
        self.__utilities = utilities    
        self.__menu = self.__utilities.get_menu()
        self.__menustack = self.__models.Stack()
        self.__menustack.push(self.__menu)

        self.__choices = {
            "1": self.selection1,
            "2": self.selection2,
            "3": self.selection3,
            "4": self.selection4,
            "5": self.selection5,
            "6": self.selection6,
            "7": self.selection7,
            "8": self.goodbye,
        } ### Hashtable for the menu options
        # wait how tf do i do this again



        print(self.__menustack[0]) #print the inital menu

    def selections():
        return 2
        
    def run(self):
        while True:
            selection = self.__view.display_menu() # Change this

            self.__choices[selection]() # hashtable
            if selection == "8": #this kinda remains the same
                break
        return