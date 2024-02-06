
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

from Classes.buildParseTree import buildParseTree
from Classes.MathTree import global_hash_table
from Classes.Models.binaryHash import BinaryHashTable
from Classes.Models.historyStack import historyStack

import re
import copy
import math
# Alternative for importing all at once 

class Controller():
    def __init__(self):
        self.__view = View() # View Object (Don't want to allow users to create view object outside of Controller)
        self.__input = text_input() # IO Object (Don't want to allow users to create IO object outside of Controller)
        self.__storehashtable = global_hash_table
        self.__historyStackTable = BinaryHashTable()
        self.__sortedKeys = set()

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
        key, expression = self.__input.get_expression("Enter the assignment statement you want to add/modify: \n For example, a=(1+2)\n") # Check for double "="
        self.__storehashtable[key] = buildParseTree(expression, key)
        return 
    
    def selection2(self):
        # Display Assignment Statements
        print(f"Current Assignments:\n{'*' * 20}")
        self.__view.display_assignments(self.__storehashtable, self.__sortedKeys)
        return 
    
    def selection3(self):
        # Evaluate Assignment Statements #Expression Tree
        var = self.__input.get_variable("Please enter the variable you want to evaluate: \n", keys = self.__sortedKeys)
        
        self.__view.display_evaluation(self.__storehashtable[var])
        return
    
    def selection4(self):
        # Read Assigment Statements from File
        file_name = self.__input.get_file_path("Please enter the input file: \n")
        file = File_Manager(folder_name="./", file_name=file_name)
        content = file.open_non_empty_file("Please enter the input file: \n")

        for line in content.split("\n"):
            key, expression = self.__input.get_expression(input=False,expression_string=line)
            self.__storehashtable[key] = buildParseTree(expression, key)
            self.__sortedKeys.add(key)
        return
    
    def selection5(self):
        # Sort assignment statement
        eval = []
        for i in self.__sortedKeys:
            if self.__storehashtable[i].fast_eval == None:
                eval.append([-math.inf, i])
            else:
                eval.append([self.__storehashtable[i].fast_eval, i])

        sorted_eval = sorted(eval, key=lambda x: x[0], reverse=True)

        # Group items with the same value
        grouped_eval = {}
        for value, key in eval:
            if value not in grouped_eval:
                grouped_eval[value] = []
            grouped_eval[value].append(key)

        # Sort the groups in descending order of value
        sorted_eval = sorted(grouped_eval.items(), key=lambda x: x[0], reverse=True)

        # Convert each group to a string
        grouped_strings = []
        for value, keys in sorted_eval:
            if value == -math.inf:
                value = 'None'
            grouped_strings.append(f"Statements with Value ==> {value}")
            for i in keys:
                expression_string = str(self.__storehashtable[i].expression)
                expression_string = expression_string.replace(' ', '')
                grouped_strings.append(f"{i}={expression_string}")
            grouped_strings.append("")

        # Join all the strings together
        result = "\n".join(grouped_strings)
        file_name= self.__input.get_file_path("Please enter the output file: \n")
        tofile = File_Manager(folder_name="./", file_name=file_name)
        tofile.writefile(result)
        return
    
    def selection6(self):
        return
        
    def selection7(self):
        return
        


