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
    head1 = lst1.head
    head2 = lst2.head
    
    count = 0

    while 

    while lst1.head is not None:
        if lst1.head == head1:
            count+=1
        if count > 1:
            print(head1.value)
            return head1
    count = 0
    while lst2.head is not None:
        if lst2.head == head2:
            count+=1
        if count > 1:
            print(head2.value)
            return head2

    return None

def test_intersection(value1, expected):
    pass
    
lst = LinkList(values=[1,2,3,4])
lst2 = LinkList(0)

lst2.head.next = Node(2)
lst2.head.next.next = Node(3)
lst2.head.next.next.next = lst.head
#print(lst.head.next.next.next.value)
#print(lst2.head.next.next.next.value)
intersection(lst,lst2)
