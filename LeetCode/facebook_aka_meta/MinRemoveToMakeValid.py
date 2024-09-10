import pytest

def mminRemoveToMakeValid(s:str) -> str:
    index_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if not c in "()":
            continue    
        
        if c == "(": #adding open parenthesis to the stack
            stack.append(i)
        elif not stack: #if is closing and there no openning parenthesis in the stack add to indexes to remove
            index_to_remove.add(i)
        else: # if the character is closing removing from the stack
            stack.pop()

    index_to_remove = index_to_remove.union(set(stack)) #in case that were any opening tag without closing tag lets add it to the indexes to remove
    string_builder = [] #creating the variable which will hold the string to return.

    for i,c in enumerate(s):
        if i not in index_to_remove:
            string_builder.append(c)

    return "".join(string_builder)


s = "lee(t(c)o)de)"
print(mminRemoveToMakeValid(s))



