"""
2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter­
    secting node. Note that the intersection is defined based on reference, not value.That is, if the kth
    node of the first linked list is the exact same node (by reference) as the jth node of the second
    linked list, then they are intersecting.
    Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129
"""
from LinkList import LinkList, Node

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
        
        if map[head1] > 1 or map[head2] > 1:
            return head1

        head1 = head1.next if head1 is not None else None
        head2 = head2.next if head2 is not None else None
    
    return None

lst1 = LinkList(values=['A','B','C','D','E','F'])
lst2 = LinkList(values=['A','E','I'])

lst2.head.next.next.next = lst1.head.next.next.next

print(intersection(lst1,lst2).value)