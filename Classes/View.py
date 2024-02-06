import turtle as turtle
import math
from Classes.Models.sort import Sort
class View():
    def __init__(self):
        return
    
    def display_assignments(self, hashtable, sorted_keys):
        print('Assignments:')
        sorted_keys = Sort().quick_sort(set_of_items=sorted_keys)
        for key in sorted_keys:
            expression_string = str(hashtable[key].expression)
            expression_string = expression_string.replace(' ', '')
            print(f'{key}={expression_string}=>{hashtable[key].fast_eval}')

    def display_evaluation(self, tree):
        print("\n Expression Tree:")
        print(tree.root.printInorder(0))
        print(f'Value for variable: {tree.fast_eval}')

    
    
    