from stack import Stack
class MyQueue:
    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()

    def _shift_stacks(self):
        if self.old_stack.is_empty():
            while not self.new_stack.is_empty():
                self.old_stack.push(self.new_stack.pop())

    def add(self, value):
        return self.new_stack.push(value)
    
    def peek(self):
        if self.is_empty():
            return False
        self._shift_stacks()
        return self.old_stack.peek()
    
    def remove(self):
        if self.is_empty():
            return False
        self._shift_stacks()
        return self.old_stack.pop()
    
    def is_empty(self):
        return self.old_stack.pop()
    

    def __len__(self):
        return len(self.new_stack) + len(self.old_stack)
    
    