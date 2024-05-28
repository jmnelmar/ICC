'''
3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
    an additional temporary stack, but you may not copy the elements into any other data structure
    (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
'''
#from stack import Stack
class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        stack_string = ""
        for i in reversed(self.stack):
            stack_string += f"({i})\n"
            stack_string += "===\n"
        return stack_string

    def __bool__(self):
        return bool(self.stack) 

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def to_list(self):
        return reversed(self.stack)

    
class Sorted_Stack(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()

    def push(self, item):
        if self.is_empty () or self.peek() > item:
            super().push(item)
        else:
            while self.peek() is not None and self.peek() < item:
                self.temp_stack.push(self.pop())
            super().push(item)
            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())
        



myStack = Stack()
myStack.push(5)
myStack.push(3)
myStack.push(4)
myStack.push(1)
myStack.push(2)

mySortedStack = Sorted_Stack()
mySortedStack.push(5)
mySortedStack.push(3)
mySortedStack.push(4)
mySortedStack.push(1)
mySortedStack.push(2)
print(myStack)
print("======================================================")
print(mySortedStack)

