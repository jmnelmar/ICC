"""
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
"""
from LinkList import LinkList, Node

def palindrome(lst:Node):
    map = {}
    allowed_pivot = 0

    while lst is not None:
        if lst.value not in map:
            map[lst.value] = 1
        else:
            map[lst.value] += 1
        lst = lst.next
        
    for n in map.keys():
        if map[n] == 1:
            allowed_pivot += 1
        elif map[n] > 2:
            return False

    if allowed_pivot > 2:
        return False

    return True


lst = LinkList(values=[0,1,2,1,0])
print(str(lst))
print(palindrome(lst.head))