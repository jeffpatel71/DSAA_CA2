### Names : Hazem Bin Ryaz Patel (2200550) & Tan Yue Feng (2214621)
### Class : DAAA/FT/2B/07

# Imports
from Classes.Controller import Controller   
from Classes.View import View

# Main Function
if __name__ == "__main__":
    print()
    controller = Controller()
    controller.run(folder_path="Text_Files", 
                    credits_file="Credits.txt",
                    menufile= "Menu.txt")
