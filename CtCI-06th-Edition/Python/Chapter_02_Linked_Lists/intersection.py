"""
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter­
    secting node. Note that the intersection is defined based on reference, not value.That is, if the kth
    node of the first linked list is the exact same node (by reference) as the jth node of the second
    linked list, then they are intersecting.
    Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129
"""
from LinkList import LinkList, Node
import pytest
def intersection(lst1:LinkList, lst2:LinkList):
    map = {}
    head1 = lst1.head
    head2 = lst2.head

    while head1 is not None or head2 is not None:
        if head1 is not None and head1  not in map:
            map[head1] = 1
        elif head1 is not None:
            map[head1] += 1
        if head2 is not None and head2 not in map:
            map[head2] = 1
        elif head2 is not None:
            map[head2] +=1

        if head1 is not None and map[head1] > 1: 
            return head1
        if head2 is not None and map[head2] > 1:
            return head2

        head1 = head1.next if head1 is not None else None
        head2 = head2.next if head2 is not None else None
    
    return None


@pytest.mark.parametrize(
    "value1, value2, value3, value4, expected",
    [
        (['A','B','C','D','E','F'],['A','E','I'],3,'D', True),
        (['A','B','C','D','E','F'],['A','E','I'],3,'E', False),
        (['A','B','C','D','E','F'],['A','E','I'],2,'C', True),
        (['A','B','C','D','E','F'],['A','E','I'],4,'E', True),
        (['A','B','C','D','E','F'],['A','E','I'],5,'E', False)
    ]
)
def test_intersection(value1, value2, value3, value4, expected):
    lst1 = LinkList(values=value1)
    lst2 = LinkList(values=value2)

    head1= lst1.head
    aux = lst2.head

    for _ in range(value3):
        head1 = head1.next
    
    while aux.next is not None:
        aux = aux.next
    
    aux.next = head1

    assert (intersection(lst1, lst2).value == value4) == expected 

