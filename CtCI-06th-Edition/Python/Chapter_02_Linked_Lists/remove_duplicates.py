"""
R�mov� Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
Hints: #9, #40
"""
import pytest
from LinkList import LinkList, Node
def remove_duplicates(node:Node):
    if node is None:
        return node
        
    aux = node
    while node.next is not None:
        if node.value == node.next.value:
            node.next = node.next.next
        node = node.next
    return node

@pytest.mark.parametrize("value1, value2, expected",
    [([1,1,2,2,3,4,4,5],[1,2,3,4,5], True),
    ([1,2,3,4,5],[1,2,3,4,5], True),
    ([1,2,3,4,5,5,6],[1,2,3,4,5,5], False),
    ([],[1,2,3,4,5,5], False),
    ([1,2,3,4,5,5,6],[], False),
    ([],[], True)]
)
def test_remove_duplicates(value1, value2, expected):
    list1 = LinkList(values=value1)
    list2 = LinkList(values=value2)
    remove_duplicates(list1.head)
    print(str(list1))
    print(str(list2))
    assert list1.equals(list2) == expected
