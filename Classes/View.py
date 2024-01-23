from Classes.Models.Stack import Stack
from Classes.Utilities.IO import IO
from Classes.Utilities.Class_Errors import Class_Errors

class View():
    def __init__(self, stack_class, io_class, class_errors):
        self.__stack = stack_class
        self.__io = io_class
        self.__errors = class_errors

    def display_credits(self, file_name= "text_files/credits.txt"):
        content = self.__io.open_non_empty_file(file_name)
        print(content)

    def display_menu(self):
        
        menu_stack = self.__stack
        for line in self.__io.open_non_empty_file("text_files/menu.txt"):
            menu_stack.push(line)
        print(menu_stack)
        return len(menu_stack)

    
        ## i need to make it as easy for the controller to push and pop from the stack 
        ## i want to loop through the menu.txt per line and push it to the stack, but i have to make it to dynamic
        ## i have to make it so that the stack can be pushed and popped from the controller
        ## wait stop finishing stop github copilot please stop

        
        

        