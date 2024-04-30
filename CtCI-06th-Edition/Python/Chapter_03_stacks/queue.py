"""
A queue implements FIFO (first-in first-out) ordering. As in a line or queue at a ticket stand, items are
removed from the data structure in the same order that they are added.
It uses the operations:
* add ( i tern): Add an item to the end of the list.
* remove (): Remove the first item in the list.
* peek ( ) : Return the top of the queue.
* is Empty(): Return true if and only if the queue is empty.

A queue can also be implemented with a linked list. In fact, they are essentially the same thing, as long as
items are added and removed from opposite sides.
"""
import pytest
class QueueNode:
    def __init__(self, _data = None, _next = None):
        self.data = _data
        self.next = _next

class MyQueue:
    def __init__(self):
        self.first = QueueNode()
        self.last = QueueNode()
    
    def add(self, item):
        node = QueueNode(_data=item)
        if self.last is not None:
            self.last.next = node
        self.last = node
        if self.first is None:
            self.first = self.last
    
    def remove(self):
        if self.first is not None:
            data = self.first.data
            self.first = self.first.next
        if self.first is None:
            self.last = None
        return data

    def peek(self):
        if self.first is not None:
            return self.first

    def isEmpty(self):
        if self.first is None:
            return True
        return False

@pytest.mark.parametrize(
    "value1, value2, expected",
    [
        ('A','A', True)
    ]
)
def test_MyQueue(value1, value2, expected):
    queue = MyQueue()
    queue.add(value1)

    assert (queue.peek().data == value2) == expected
    

    
    

