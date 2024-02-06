import re
import os

### 

class text_input:
    def __init__(self):
        pass 

    def check_input(self, options, msg, invalid_msg):
        inp = input(msg)
        while not re.match(options, inp):
            print(invalid_msg)
            inp = input(msg)
        return inp

    def enter_message(self):
        return input("Press any key to continue...")
    
    def yes_no(self, msg = "Would you like to view the history of variable assignments?"):
        inp = input(f'{msg} Type Y for yes and N for no: ')
        while True:
            if str(inp).lower() in ['y', 'n']:
                return inp
            else:
                inp = input("Invalid input. Please enter Y for yes and N for no: ")


    def get_variable(self, prompt, keys):
        while True:
            variable = self.check_input(
                "^[a-zA-Z][a-zA-Z0-9]*$", prompt, "Invalid input, please enter a valid variable"
            )
            if variable in keys:
                return variable
            else:
                print("\nVariable not found, please enter an existing variable\n")

    def get_expression(self, prompt="", input=True, expression_string="None"):
        while True:
            # Check for Valid Symbols
            if input == True:
                full_expression = self.check_input( # "^[a-zA-Z][a-zA-Z0-9]*=[a-zA-Z0-9\+\-\*\/\(\)]+$"
                    "^[a-zA-Z][a-zA-Z0-9\s]*=[a-zA-Z0-9\s\+\-\*\/\.(\)]+$", prompt, "Invalid input, please enter a valid assignment statement1"
                )
            elif input == False:
                reject = re.match("^[a-zA-Z][a-zA-Z0-9\s]*=[a-zA-Z0-9\s\+\-\*\/\.(\)]+$", expression_string)
                full_expression = expression_string
                if reject == False:
                     print("\nInvalid string:", expression_string, "skipping Line...\n")
                     return None, None

            full_expression = full_expression.replace(" ", "")
            
            # Check for two or more "="
            if full_expression.count("=") >= 2:
                if input == False:
                    print(expression_string, "Skipping Line")
                    return None, None
                print("Invalid input, please enter a valid assignment statement")
                continue

            # Check for "=" at the start or end
            if full_expression[0] == "=" or full_expression[-1] == "=":
                if input == False:
                    print(expression_string, "Skipping Line")
                    return None, None
                print("Invalid input, please enter a valid assignment statement")
                continue

            # Check for opertors at the end or two operators in a row
            operators = ["+", "-", "*", "/"]

            for i in range(len(full_expression) - 1):
                if full_expression[i] in operators and full_expression[i + 1] in operators:
                    if full_expression[i] == "*" and full_expression[i + 1] == "*":
                        continue
                    if input == False:
                        print(expression_string, "Skipping Line")
                        return None
                    print("Invalid input, please enter a valid assignment statement")
                    continue

            key, expression = full_expression.split("=")

            return key, expression
    
    def get_message(self, text):
        inp = input(text)
        print()
        return inp

    def get_file_path(self, prompt, nospacing = False):
        file_path = self.check_input(
            "^.+\.txt$", prompt, "Invalid input, please enter a valid file path"
        )
        if nospacing == True:
            return file_path
        print()
        return file_path

