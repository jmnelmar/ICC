"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""
import pytest
from LinkList import LinkList, Node
def return_kth(root:Node, kth):
    if root is None:
        return 0
    index = return_kth(root.next,kth) + 1 
    if index == kth: 
        print(root.value)

    return index 

@pytest.mark.parametrize( "value1, value2, value3, expected",
    [
        ([1,2,3,4,5],2, 4,True),
        ([1,2,3,4,5],3, 3,True),
        ([],2,3,False),
        ([1,1,1,1,1],2,2,False),
        ([1,2,3,4,5],2,1,False),
    ]
)

def test_return_kth(value1,value2, value3, expected):
    assert (return_kth(LinkList(values=value1).head,value2) == value3) ==expected
