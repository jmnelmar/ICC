"""
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
"""
from LinkList import LinkList, Node

def palindrome(lst:Node):
    reversed_list = LinkList(0)
    head = reversed_list.head
    aux = lst
    while aux is not None:
        head.next = Node(aux.value)
        head = head.next
        aux = aux.next
    reversed_list.head = reversed_list.head.next
    print(str(reversed_list))

    aux = reversed_list.head
    while lst is not None:
        if lst.value != aux.value:
            return False
        lst = lst.next
        aux = aux.next
    
    return True


lst = LinkList(values=[0,1,2,1,0])
print(str(lst))
print(palindrome(lst.head))

lst = LinkList(values=[1,2,3,4,5])
print(str(lst))
print(palindrome(lst.head))

lst = LinkList(values=[2,1,1,2,1,1,2])
print(str(lst))
print(palindrome(lst.head))