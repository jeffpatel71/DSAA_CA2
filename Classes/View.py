class View():
    def __init__(self):
        return
    
    def display_assignments(self, hashtable, sorted_keys):
        print('Assignments:')
        for key in sorted_keys:
            if hashtable[key].fast_eval is not None:
                print(f'{key}={str(hashtable[key].expression)}=>{hashtable[key].fast_eval}')

    