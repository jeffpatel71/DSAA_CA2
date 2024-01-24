### Names : Hazem Bin Ryaz Patel (2200550) & Tan Yue Feng (2214621)
### Class : DAAA/FT/2B/07

# Imports
from Classes.Controller import Controller   
from Classes.View import View

# Main Function
if __name__ == "__main__":
    print()
    Controller().run(folder_path="TextFiles", 
                    credits_file="title.txt",
                    menufile= "options.txt")


