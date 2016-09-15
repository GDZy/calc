class Stack(object):
    """
    (numb or operand) -> list

    реализует стек
    
    """

    def __init__(self):
        self.items = []

    def push (self, item):
        self.items.append(item);        
    
    def pop (self, item):
        self.items.pop(item)            
    
    def size (self):
        return len(self.items)          
    
    def isEmpty (self):
        return self.items               
    
    def last (self):
        return self.items[-1]
        




