"""
2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input:3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
    Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    Hints: #3, #24
"""
from LinkList import LinkList,Node
#Mergin 2 linklists
def partition(lst:LinkList, x:int):
    lst_greater = LinkList(0)
    lst_lesser = LinkList(0)
    greater_node = lst_greater.head
    lesser_node = lst_lesser.head


    node = lst.head
    while node is not None:
        if node.value < x:
            lesser_node.next = Node(node.value)
            lesser_node = lesser_node.next
        else:
            greater_node.next = Node(node.value)
            greater_node = greater_node.next
        node = node.next
    
    lesser_node.next = lst_greater.head.next
    lst_lesser.head = lst_lesser.head.next
    print(lst_lesser)
    return lst_lesser

#Recursive method
def partition_II(lst:LinkList, x:int):
    head = lst.head
    tail = lst.head

    node = lst.head

    while node is not None:
        next = node.next
        if node.value < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node

        node = next
    tail.next = None
    chain = ""
    while head is not None:
        chain += f"({head.value}) > "
        head = head.next
    chain += "None"
    print(chain)
    
lst = LinkList(values=[3,5,8,5,10,2,1])
print(str(lst))
partition_II(lst,5)
