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
    
    def get_expression(self, prompt):
        while True:
            # Check for Valid Symbols
            full_expression = self.check_input(
                "^[a-zA-Z][a-zA-Z0-9]*=[a-zA-Z0-9\+\-\*\/\(\)]+$", prompt, "Invalid input, please enter a valid assignment statement"
            )
            
            # Check for two or more "="
            if full_expression.count("=") >= 2:
                print("Invalid input, please enter a valid assignment statement")
                continue

            # Check for "=" at the start or end
            if full_expression[0] == "=" or full_expression[-1] == "=":
                print("Invalid input, please enter a valid assignment statement")
                continue

            # Check for opertors at the end or two operators in a row
            operators = ["+", "-", "*", "/"]

            for i in range(len(full_expression) - 1):
                if full_expression[i] in operators and full_expression[i + 1] in operators:
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

