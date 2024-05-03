"""
3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
    which returns the minimum element? Push, pop and min should all operate in 0(1) time.
    Hints:#27, #59, #78
"""
from stack import Stack
import pytest

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min  = None
        self.min_stack = Stack()
        
    
    def push(self, value):
        if self.items is None:
            self.min = value
            self.min_stack.push(value)
            super().push(value)
            
        else:
            super().push(value)
            if self.min is None:
                self.min = value
                self.min_stack.push(value)
            if self.min >= value:
                self.min = value
                self.min_stack.push(value)
    
    def pop(self):
        value = super().pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()
        return value
    
    def stack_min(self):
        return self.min_stack.peek()
    
@pytest.mark.parametrize(
        "value1, value2, value3, expected",
        [
            ([5,3,6,5,1,4],3,1,True),
            ([1,3,4,5,6,1],3,1,True),
            ([9,3,2,4,5,6,2,1],3,1,False),
            ([-9,3,2,4,5,6,2,1],3,1,False),
            ([-9,3,2,4,5,6,2,1],3,-9,True)
        ]
)
def test_min_stack(value1, value2, value3, expected):
    my_minstack = MinStack()
    for n in value1:
        my_minstack.push(n)
    
    for i in range(value3):
        my_minstack.pop()

    assert (my_minstack.stack_min() == value3) == expected


mystack = MinStack()
mystack.push(5)
mystack.push(3)
mystack.push(6)
mystack.push(5)
mystack.push(1)
mystack.push(4)

print(mystack.stack_min())
print(str(mystack))

mystack.pop()
mystack.pop()
mystack.pop()
print(mystack.stack_min())
print(str(mystack))


