
# Import Statements
from Classes.Menu import Menu
from Classes.View import View
# Models
from Classes.Models.Hash import HashTable

# Utilities
from Classes.Utilities.IO import text_input
from Classes.Utilities.files import File_Manager

from Classes.buildParseTree import buildParseTree
from Classes.MathTree import global_hash_table
import random2 
import re
import copy
import math
# Alternative for importing all at once 

class Controller():
    def __init__(self):
        self.__view = View() # View Object (Don't want to allow users to create view object outside of Controller)
        self.__input = text_input() # IO Object (Don't want to allow users to create IO object outside of Controller)
        self.__storehashtable = global_hash_table # Import the global hashtable from MathTree (Can't be instantiated outside of MathTree)
        self.__sortedKeys = set() # Set to store the sorted keys, handles duplicates

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
        
        # Add to the hashtable
        self.__storehashtable[key] = buildParseTree(expression, key)
        return 
    
    def selection2(self):
        # Display Assignment Statements
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

        # Instantiate File_Manager
        file = File_Manager(folder_name="./", file_name=file_name)
        content = file.open_non_empty_file("Please enter the input file: \n")

        # Read content for each line
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
        # Purpose is to create a random variable to help the user understand the expression tree

        # Random Variable Creation
        var = self.__input.get_variable("Please enter the variable name you want to create: \n")
        get_length = self.__input.get_number("Please enter the length of the expression: \n")

        # Generate the random expression
        expression = random2.generate_random_expression(get_length)

        # Display the expression and store it in the hashtable
        print(f"Variable {var} has been created with the expression {expression}")
        self.__storehashtable[var] = buildParseTree(expression, var)
        self.__sortedKeys.add(var)     
        return
        
    def selection7(self):
        # Turtle Graphics, visualize the expression tree
        var = self.__input.get_variable("Please enter the variable you want to visualize: \n", keys = self.__sortedKeys)
        menu = Menu(menuFile="expression_tree")
        menu.load_menu()
        menu.display_menu()
        di = self.__input.check_input("^[1-3]$", "Enter your selection: ", "Invalid input, please enter a valid selection")
        if di =="4":
            # Exit out of the sub-menu
            return
        self.__view.display_evaluation_turtle(self.__storehashtable[var], di)
        return
        


