import pytest
class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None

class LinkList:
    def __init__(self,value=None):
        self.head = Node(value)

    def add(self, value):
        aux = self.head
        if aux is None:
            aux = Node(value)
            return

        while aux.next is not None:
             aux = aux.next
        aux.next = Node(value)

    def __str__(self):
        s = ""
        aux = self.head 
        while aux is not None:
            s += f"({aux.value}) > "
            aux = aux.next
        s += "None"
        return s
    
    def __len__(self):
        count = 0
        aux= self.head
        while aux is not None:
            count += 1
            aux = aux.next
        return count

link_list = LinkList(5)
link_list.add(4)
link_list.add(3)
link_list.add(2)
link_list.add(1)

print(str(link_list))