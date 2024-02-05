
# Import Statements
from Classes.Menu import Menu
from Classes.View import View

# Models
from Classes.Models.Hash import HashTable
from Classes.Models.Stack import Stack

# Utilities
from Classes.Utilities.IO import text_input
from Classes.Utilities.Class_Errors import Class_Errors
from Classes.Utilities.files import File_Manager
from Classes.Utilities.sort import Sort
from Classes.Utilities.search import Search

from Classes.evaluator import Evaluator
from Classes.buildParseTree import buildParseTree
from Classes.MathTree import global_hash_table
from Classes.binaryHash import BinaryHashTable

import re
import copy
# Alternative for importing all at once 

"""
import classes.models as Model
import classes.utilities as Utilities
"""

class Controller():
    def __init__(self):
        self.__view = View() # View Object (Don't want to allow users to create view object outside of Controller)
        self.__input = text_input() # IO Object (Don't want to allow users to create IO object outside of Controller)
        self.__storehashtable= global_hash_table
        self.__sort = Sort()
        self.__search = Search()
        self.__sortedKeys = []
        # self.__sortedKeys = self.__sort.bubbleSort(list(self.__storehashtable.getkeys()))

    # Run Function
    def run(self, folder_path, credits_file, menufile):

        # Instantiate Menu Object that contains the credits and menu options
        menu = Menu(folder_path, credits_file, menufile)

        # Display Credits
        menu.display_credits()
        
        # Create a Hastable to store the menu options
        hashtable_menu = HashTable()
        length = menu.load_menu()
        for i in range(length):
            if i == 0 or i == length-1:
                continue
            hashtable_menu[str(i)] = getattr(self, f'selection{i}')
        
        
        # Display Menu and get user selection till user quits
        while True:
            menu.display_menu()
            regex = f"^[1-{length-1}]$"
            selection = self.__input.check_input(regex, "Enter your selection: ", "Invalid input, please enter a valid selection")
            if selection == str(length-1):
                break
            hashtable_menu[selection]() 
            input("Press any key to continue...")
            
    def selection1(self):
        # Add/Modify Assignment Statements
        # Check if the expression is valid regex for assigment statement can include operator, numbers and letters
        key, expression = self.__input.get_expression("Enter the assignment statement you want to add/modify: \n For example, a=(1+2)\n") # Check for double "="
        self.__storehashtable[key] = buildParseTree(expression, key)
        self.__sortedKeys.append(key)
        print(self.__storehashtable[key].fast_eval)
        return 
    
    def selection2(self):
        # Display Assignment Statements
        print(f"Current Assignments:\n{'*' * 20}")
        self.__view.display_assignments(self.__storehashtable, self.__sortedKeys)
        return 
    
    def selection3(self):
        # Evaluate Assignment Statements #Expression Tree
        var = self.__io.get_expression("Please enter the variable you want to evaluate: \n")
        print("\n")

        self.__view.display_evaluation(self.__storehashtable[var])
        return
    
    def selection4(self):
        # Read Assigment Statements from File
        self.__io.get_file_path("Please enter the input file: \n")
        self.__storehashtable = self.__file.read_file(self.__storehashtable)
        self.__view.display_assignments()
        return
    
    def selection5(self):
        # Sort Assignment Statements & Store Seperate File
        # Sort by Value 

        # self.__storehashtable  = self.__sort.bubble_sort_value(self.__storehashtable)
        self.__view.display_assignments()
        return
    
    def update_hash(self):
        existing_keys = re.findall(r'\b[^\d\W]+\b', expression)
        for key in existing_keys:
            try:
                # if key exists
                new_expression = self.__storehashtable[key] # expression + eval
                expression = expression.replace(key, str(new_expression[1]))
            except:
                expression = expression.replace(key, ' ')
    
    
            # # Search if the expression contains another variable(s)
        # dup_expression = copy.copy(expression)
        # # a = (1+2), expression is (1+2), 


        # expression = Evaluator(expression)
        # dup_expression = Evaluator(dup_expression)
        
        # self.__storehashtable[key] = [dup_expression, expression.evaluate()]
        
        # if self.__storehashtable[key][1] == '?':
        #     self.__storehashtable[key][1] = None
        # print(self.__storehashtable[key])
