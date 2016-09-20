class Stack(object):
    """
    (numb or operand) -> list

    реализует стек
    
    """

    def __init__(self):
        self.items = []

    def push (self, item):
        self.items.append(item);        
    
    def pop (self):
        return self.items.pop()            
    
    def size (self):
        return len(self.items)          
    
    def isEmpty (self):
        return self.items == []   
    
    def isNotEmpty (self):
        return self.items != []           
    
    def last (self):
        return self.items[-1]
        




