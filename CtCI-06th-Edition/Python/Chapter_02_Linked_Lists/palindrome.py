"""
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
"""
from LinkList import LinkList, Node
import pytest

def palindrome(lst:Node):
    reversed_list = LinkList(0)
    head = reversed_list.head
    aux = lst
    while aux is not None:
        n = Node(aux.value)
        n.next = head
        head = n
        aux = aux.next
    reversed_list.head = head
    print(str(reversed_list))

    while lst is not None:
        if lst.value != head.value:
            return False        
        lst = lst.next
        head = head.next

    return True

@pytest.mark.parametrize(
    "value1, expected",
    [
        ([1,0,1], True),
        ([0,1,2,1,0], True),
        ([1,2,3,4,5], False),
        ([2,1,1,2,1,1,2], True)
    ]
)
def test_palindrome(value1, expected):
    lst = LinkList(values=value1)
    assert palindrome(lst.head) == expected
"""
lst = LinkList(values=[0,1,2,1,0])
print(str(lst))
print(palindrome(lst.head))

lst = LinkList(values=[1,2,3,4,5])
print(str(lst))
print(palindrome(lst.head))

lst = LinkList(values=[2,1,1,2,1,1,2])
print(str(lst))
print(palindrome(lst.head))
"""