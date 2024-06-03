import pytest
from collections import deque
def isValid(s: str) -> bool:
    stack= []
    map = {")":"(","]":"[", "}":"{" }
    for c in s:
        if c in map:
            top = stack.pop() if stack else "!"

            if map[c] != top:
                return False
        else:
            stack.append(c) 
    return not stack

def isValidII(s) -> bool:
    stack = []
    map = {")":"(","]":"[", "}":"{" }
    for c in s:
        if c in map:
            top = stack.pop() if stack else "@"
            if map[c] != top:
                return False
        else:
            stack.append(c)
    return  len(stack) == 0



@pytest.mark.parametrize(
    's,expected',
    [
        ("()",True),
        ("()[]{}",True),
        ("(]",False),
        ("{[]}",True),
        ("]",False),
        ("){",False),
        ("([({{[()]}})])",True),
        ("([({{[(]}})])",False),
        ("(){}}{",False),
    ]
)
def test_isvalid(s, expected):
    assert isValidII(s) == expected



s = "()"
print(f"the string:{s} is {isValid(s)}")
s = "()[]{}"
print(f"the string:{s} is {isValid(s)}")
s = "(]"
print(f"the string:{s} is {isValid(s)}")
s ="{[]}"
print(f"the string:{s} is {isValid(s)}")
s ="]"
print(f"the string:{s} is {isValid(s)}")
s ="){"
print(f"the string:{s} is {isValid(s)}")
s ="([({{[()]}})])"
print(f"the string:{s} is {isValid(s)}")
s ="([({{[(]}})])"
print(f"the string:{s} is {isValid(s)}")
s="(){}}{"
print(f"the string:{s} is {isValid(s)}")
s="(])"
print(f"the string:{s} is {isValid(s)}")
#q = deque()
#q.append("(")
#q.append(")")
#print(q)
#print(q[-1])
