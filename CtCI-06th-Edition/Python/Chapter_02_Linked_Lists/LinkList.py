import pytest
class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None

class LinkList:
    def __init__(self,value=None,values=None):
        self.head = Node()
        if value is not None:
            self.head = Node(value)
        
        if values is not None:
            self.add_multiple(values)

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

    def equals(self,lst):
        
        if len(self) != len(lst):
            return False
        aux = self.head
        node = lst.head

        while aux is not None and node is not None:
            if aux.value != node.value:
                return False
            aux = aux.next
            node = node.next

        return True
    
    def add_multiple(self, values):
        
        for v in values:
            self.add(v)
        self.head = self.head.next

@pytest.mark.parametrize(
    "value, expected",
    [
        ([1,2,3,4,5],"(1) > (2) > (3) > (4) > (5) > None"),
        ([5,4,3,2,1],"(5) > (4) > (3) > (2) > (1) > None"),
        ([5,4,3,2,1,5,3,4,1],"(5) > (4) > (3) > (2) > (1) > (5) > (3) > (4) > (1) > None")
    ]
)
def test_link_list(value,expected):
    assert str(LinkList(values=value)) == expected