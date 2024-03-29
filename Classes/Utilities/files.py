import os
import re
class File_Manager:
    def __init__(self, folder_name = os.getcwd, file_name = None):
        self.__folder_name = folder_name    
        self.__file_name = file_name
        self.file_path = os.path.join(self.__folder_name, self.__file_name)

    def open_non_empty_file(self, prompt):
        while True:
            file_contents = self.openfile(self.file_path, prompt)
            if file_contents != "":
                return file_contents
            else:
                print(f"The file '{file_path}' is empty.")
                file_path = self.get_file_path(prompt)

    def writefile(self, content_to_write):
        while True:
            try:
                with open(self.file_path, "w") as file:
                    file.write(content_to_write)
                    print(f'File written successfully\n')
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
    
    def openfile(self, file_path, input_message):
        while True: 
            try:
                with open(file_path, "r") as file:
                    file_contents = file.read()                    
                    break
            except FileNotFoundError:
                print(f"The file '{file_path}' was not found.")
                print("")
                file_path = self.check_input(
                "^.+\.txt$",
                (input_message),
                "Invalid input, please enter a valid file path",
            )
            except Exception as e:
                print(f"An error occurred: {e}")
        return file_contents
    
    def check_folder(self):
        folder_name = self.check_input(
            "^[a-zA-Z0-9_\-\s]+$",
            "Enter the folder name: ",
            "Invalid input, please enter a valid folder name",
        )
        while True:
            try:
                if os.path.exists(folder_name):
                    break
                else:
                    print(f"The folder '{folder_name}' does not exist.\n")
                    folder_name = self.check_input(
                        "^[a-zA-Z0-9_\-\s]+$",
                        "Enter the folder name: ",
                        "Invalid input, please enter a valid folder name",
                    )
            except Exception as e:
                print(f"An error occurred: {e}")
                print("")
        return folder_name

    def get_files_folder(self, folder_path):
        files_folder = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".txt"):
                file_path = os.path.join(folder_path, file_name)
                file_contents = self.openfile(file_path, input_message="none")
                if file_contents == "":
                    print(f"The file '{file_path}' is empty, and won't be processed.")
                    continue
                files_folder.append(file_name)
        return files_folder
    
    def check_input(self, options, msg, invalid_msg):
        inp = input(msg)
        while not re.match(options, inp):
            print(invalid_msg)
            inp = input(msg)
        return inp