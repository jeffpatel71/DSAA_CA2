class View():
    def __init__(self):
        return
    
    def display_assignments(self, hashtable, sorted_keys):
        print('Assignments:')
        for key in sorted_keys:
            print(f'{key}={hashtable[key]}=>22')