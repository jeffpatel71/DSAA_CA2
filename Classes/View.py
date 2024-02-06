class View():
    def __init__(self):
        return
    
    def display_assignments(self, hashtable, sorted_keys):
        print('Assignments:')
        for key in sorted_keys:
            expression_string = str(hashtable[key].expression)
            expression_string = expression_string.replace(' ', '')
            print(f'{key}={expression_string}=>{hashtable[key].fast_eval}')

    def display_evaluation(self, tree):
        print("Expression Tree:")
        print(tree.root.printInorder(0))
        print(f'Value for variable: {tree.fast_eval}')