from Classes.Models.Stack import Stack
from Classes.Models.binaryHash import BinaryHashTable

class historyStack(Stack):
    def __init__(self):
        super().__init__()

    def subset(self, index):
        return self.list[index]
    
    def __str__(self):
        output = "["
        for i in range(len(self.list)):
            item = self.list[i]
            if i < len(self.list)-1:
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += ']'
        return output

    