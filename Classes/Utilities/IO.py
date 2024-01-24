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

