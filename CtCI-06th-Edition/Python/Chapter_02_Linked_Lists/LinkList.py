import pytest
class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None

class LinkList:
    def __init__(self,value=None):
        self.head = Node(value)

    def add(self, value):
        while self.head.next is not None:
             self.head = self.head.next
        self.head.next = Node(value)

    def __str__(self):
        s = ""
        while head is not None:
            s += f"({head.vale}) > "
        s += "None"
    
    def __len__(self):
        count = 0
        while head is not None:
            count += 1
        return count

link_list = LinkList(5)
link_list.__append__