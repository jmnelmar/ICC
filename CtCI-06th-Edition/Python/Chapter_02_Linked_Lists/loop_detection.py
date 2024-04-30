"""
2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
    beginning of the loop.
    DEFINITION
    Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
    as to make a loop in the linked list.
    EXAMPLE
    Input:
    Output:
    A -> B -> C -> D -> E -> C [the same C as earlier]
    C
    Hints: #50, #69, #83, #90
"""
from LinkList import LinkList, Node
def loop_detection(lst:Node):
    map = {}
    while lst is not None:
        if lst.value not in map:
            map[lst.value] = 1
        else:
            map[lst.value] += 1
        if map[lst.value] > 1:
            break
        lst = lst.next
    return lst

lst = LinkList(values=['A','B','C','D','E'])
lst.head.next.next.next.next.next = lst.head.next.next
print(loop_detection(lst.head).value)


#a b c d e c