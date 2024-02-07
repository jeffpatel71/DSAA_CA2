
# Import Statements
from Classes.Menu import Menu
from Classes.View import View


# Models/Data Structures
from Classes.Models.Hash import HashTable
from Classes.Models.binaryHash import BinaryHashTable
from Classes.Models.historyStack import historyStack


# Utilities
from Classes.Utilities.IO import text_input
from Classes.Utilities.files import File_Manager
from Classes.Utilities.sort import Sort
from Classes.Utilities.search import Search

# Binary Classes
from Classes.Models.buildParseTree import buildParseTree
from Classes.Models.MathTree import global_hash_table

from Classes.Models.randomex import random_expressions
# Python Libraries

import re
import copy
import math

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
        
        if length >=10:
            regex = f"^[1-9]|{length-1}$"
        else:
            regex = f"^[1-{length-1}]$"
        # Display Menu and get user selection till user quits
        while True:
            menu.display_menu()
            selection = self.__input.check_input(regex, "Enter choice: ", "Invalid input, please enter a valid selection")
            if selection == str(length-1):
                break
            hashtable_menu[selection]()
            input("\nPress any key to continue...")
            
    def selection1(self):
        # Add/Modify Assignment Statements
        # Check if the expression is valid regex for assigment statement can include operator, numbers and letters
        key, expression = self.__input.get_expression("Enter the assignment statement you want to add/modify: \nFor example, a=(1+2)\n") # Check for double "="
        if key == None or expression == None:
            return  
        self.__storehashtable[key] = buildParseTree(expression, key)

        evaluated_expression = self.__storehashtable[key].eval

        if key not in self.__sortedKeys:
            self.__historyStackTable[key] = historyStack()
            self.__sortedKeys.add(key)
        else:
            pass
        self.__historyStackTable[key].push((expression, evaluated_expression))
        return 
    
    def selection2(self):
        # Display Assignment Statements
        self.__view.display_assignments(self.__storehashtable, self.__sortedKeys)
        return 
    
    def selection3(self):
        # Evaluate Assignment Statements #Expression Tree
        var = self.__input.get_variable("Please enter the variable you want to evaluate: \n", keys = self.__sortedKeys)
        print("\n")
        if var:
            self.__view.display_evaluation(self.__storehashtable[var], key=var)
        return
    
    def selection4(self):
        # Read Assigment Statements from File
        file_name = self.__input.get_file_path("Please enter the input file: \n")
        file = File_Manager(folder_name="./", file_name=file_name)
        content = file.open_non_empty_file("Please enter the input file: \n")

        # Read by Line
        for line in content.split("\n"):
            if line == "":
                continue
            key, expression = self.__input.get_expression(input=False,expression_string=line)
            if expression == None or key == None:
                continue

            if key not in self.__sortedKeys:
                self.__historyStackTable[key] = historyStack()
            else:
                pass

            self.__storehashtable[key] = buildParseTree(expression, key)
            self.__historyStackTable[key].push((expression, self.__storehashtable[key].eval))
            self.__sortedKeys.add(key)

        # Display Assignment Statements
        
        self.__view.display_assignments(self.__storehashtable, self.__sortedKeys)
        return
    
    def selection5(self):
        # Sort assignment statement
        eval = []
        for i in self.__sortedKeys:
            if self.__storehashtable[i].eval == None:
                eval.append([-math.inf, i])
            else:
                eval.append([self.__storehashtable[i].eval, i])

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
        # View assignment history
        inp = self.__input.yes_no()
        if inp == 'y':
            if len(self.__sortedKeys) == 0:
                print('There are currently no assignments. Please add an assignment statement first.')
                return
            
            self.__view.display_variables(self.__sortedKeys)

            var = self.__input.get_variable("Please enter the name for which you would like to view its history: ", self.__sortedKeys)
            stack_contents = self.__historyStackTable[var]
            contents = copy.deepcopy(stack_contents)
            content_length = len(contents.list)

            print(f"\nVariable {var}\'s history (ordered in descending time of creation):\n{'*' * 70}")

            self.__view.display_stack_contents(contents, content_length)

            if content_length > 1:
                inp_overwrite = self.__input.yes_no("\nWould you like to replace the variable with one of its historical assignments?")
                if inp_overwrite == 'y':
                    regex = r"^(?!0)[1-9]\d{0,%s}$" % (content_length - 1)
                    inp_regex = self.__input.check_input(regex, \
                                                         "Please enter the index corresponding to the expression you wish to overwrite with: ", \
                                                                "Invalid index. Please re-enter with the correct format.")
                    
                    self.__storehashtable[var] = buildParseTree(stack_contents.subset(content_length - int(inp_regex))[0], var)
                    print("Overwrite successful")
                    self.__historyStackTable[var].push(\
                        (str(self.__storehashtable[var].expression.replace(' ', '')),\
                        self.__storehashtable[var].eval))
                    return
        else:
            return
        
    def selection7(self):
        # Visualize Dependencies
        dependencies = {} 
        for i in global_hash_table.items():
            dependencies[i[0]] = i[1].dependants

        # if bool(dependencies):
        #     try:
        #         self.__view.visualize_dependencies(dependencies)
        #     except:
        #         print('Due to turtle\'s Terminator, visualization can only be done once')
        # else:
        #     print('There are currently no variables with dependencies')

        dependency_analysis = {key: set() for key in self.__sortedKeys}

        for key in self.__sortedKeys:
            visited = set()
            Search().dfs(key, dependencies, visited, dependency_analysis)
        
        self.__view.display_visual_representation(dependency_analysis)
        return
    
    def selection8(self):
        # Purpose is to create a random variable to help the user understand the expression tree

        # Random Variable Creation
        var = self.__input.get_variable_new("Please enter the variable name you want to create: \n", keys=self.__sortedKeys)
        get_length = self.__input.get_length("Please enter the length of the expression: (1-5)  \n")

        # Generate the random expression
        expression = random_expressions().generate_random_expression(length=get_length)

        # Display the expression and store it in the hashtable
        print(f"Variable {var} has been created with the expression {expression}")
        self.__storehashtable[var] = buildParseTree(expression, var)
        self.__sortedKeys.add(var)     
        return
    
    def selection9(self):
        # Turtle Graphics, visualize the expression tree
        var = self.__input.get_variable("Please enter the variable you want to visualize: \n", keys = self.__sortedKeys)
        self.__view.treeTraversal(self.__storehashtable[var])
        return
