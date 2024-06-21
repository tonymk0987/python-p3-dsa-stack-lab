class Stack:
    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        if not self.full():
            self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None  # or raise an exception for an empty stack
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None  # or raise an exception for an empty stack
    
    def size(self):
        return len(self.items)
    
    def full(self):
        return len(self.items) >= self.limit
    
    def search(self, target):
        try:
            index = self.items.index(target)
            return self.size() - index - 1  # Distance from the top of the stack (0-based index)
        except ValueError:
            return -1  # or handle the case where target is not found
