"""
3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
    threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
    composed of several stacks and should create a new stack once the previous one exceeds capacity.
    SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
    (that is, pop () should return the same values as it would if there were just a single stack).
    FOLLOW UP
    Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
    Hints:#64, #87
"""

from stack import Stack
class SetOfStacks(Stack):
    def __init__(self, t = 0):
        super().__init__()
        stacks = [Stack]
        self.treshold = 0
        self.stack_in_use = 0
    
    def push(self, item):
        if self.treshold >= len(self.stacks[self.stack_in_use]):
            self.stack_in_use += 1
            self.stacks.append(self.items)
        super.push(item)
        

    def pop(self):
        self.popAt()

    def popAt(self):
        if self.stacks[self.stack_in_use].is_empty():
            return self.stacks.pop()
        else:
            return self.stacks[self.stack_in_use].pop()
        
    def __str__(self):
        pass