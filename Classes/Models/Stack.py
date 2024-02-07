class Stack:   
    def __init__(self): 
        self.__list= [] 
 
    @property
    def list(self):
        return self.__list
    
    def isEmpty(self): 
        return self.__list == [] 
     
    def size(self): 
        return len(self.__list) 
     
    def clear(self): 
        self.__list.clear()  
    
    def push(self, item):  
        self.__list.append(item)  
     
    def pop(self):   
        if self.isEmpty():  
            return None 
        else: 
            return self.__list.pop()    
     
    def get(self):  
        if self.isEmpty():  
            return None 
        else: 
            return self.__list[-1]  
     
    def __str__(self): 
        output = ""
        for i in range( len(self.__list) ): 
            item = self.__list[i] 
            if i < len(self.__list)-1   : 
                output += f'\n{str(item)},' 
            else: 
                output += f'\n{str(item)}'  
        return output 