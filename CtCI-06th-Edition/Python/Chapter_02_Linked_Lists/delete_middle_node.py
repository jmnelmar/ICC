"""
2.3
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks likea->b->d->e- >f
Hints:#72
"""
import pytest
from LinkList import LinkList, Node

def delete_node(node:Node):
    if node.next is None:
        return
    
    node.value = node.next.value
    node.next = node.next.next
    
@pytest.mark.parametrize("value1, value2, value3, expected",
   [(LinkList(values=[1,2,3,4,5]),3,LinkList(values=[1,2,4,5]),True),
    (LinkList(values=[1,2,3,4,5]),3,LinkList(values=[1,2,3,4,5]),False),
    (LinkList(values=[1,2,3,4,5]),2,LinkList(values=[1,3,4,5]),True)]
)
def test_delete_node(value1, value2, value3, expected):
    i = 1
    node = value1.head
    for i in range(value2 - 1):
        node = node.next
    delete_node(node)
    print(value1)
    assert value1.equals(value3) == expected