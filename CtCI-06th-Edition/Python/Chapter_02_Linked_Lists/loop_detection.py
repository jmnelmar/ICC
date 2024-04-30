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
import pytest
from LinkList import LinkList, Node
def loop_detection(lst:Node):
    map = {}
    while lst is not None:
        if lst not in map:
            map[lst] = 1
        else:
            map[lst] += 1
        if map[lst] > 1:
            break
        lst = lst.next
    return lst

lst = LinkList(values=['A','B','C','D','E'])
lst.head.next.next.next.next.next = lst.head.next.next
print(loop_detection(lst.head).value)

@pytest.mark.parametrize(
    "value1, value2, value3, expected",
    [
        ( ['A','B','C','D','E'], 2,'C', True ),
        ( ['A','B','C','D','E'], 2,'F', False ),
        ( ['A','B','C','C','D','E'], 1,'B', True ),
        ( ['A','B','C','C','D','E'], 0,'B', False ),
        ( ['A','B','C','C','D','E'], 1,'B', True )
    ]
)
def test_loop_detection(value1, value2, value3, expected):
    lst = LinkList(values=value1)
    root = lst.head
    tail = lst.head
    for _ in range(value2):
        root = root.next

    while tail.next is not None:
        tail = tail.next
    tail.next = root

    assert (loop_detection(lst.head).value == value3) == expected

#a b c d e c