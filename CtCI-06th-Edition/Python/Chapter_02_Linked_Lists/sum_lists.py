"""
2.5
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
Hints: #7, #30, #71, #95, #109
"""
from LinkList import LinkList, Node
def sum_lists(l1:Node, l2:Node):
    number1, number2, carry, total, val = 0, 0, 0, 0, Node()
    head = val


    while l1 is not None or l2 is not None or carry != 0:
        number1 = l1.value if l1 is not None else 0
        number2 = l2.value if l2 is not None else 0

        total = number1 + number2 + carry
        carry = total // 10
        total = total % 10
        val.next = Node(total)
        val = val.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    
    chain = ""
    head = head.next
    while head is not None:
        chain += f"({head.value}) > "
        head = head.next
    chain += "None"
    print(chain)

def sum_lists_floowup(lst1:Node, lst2:Node):
    pass
     
lst = LinkList(values=[7,1,6])
lst2 = LinkList(values=[5,9,2])
print(str(lst))
print(str(lst2))
sum_lists(lst.head,lst2.head)