'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
import pytest
class  ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def create_from_list(arr):
    head = ListNode()
    result = head
    for i in arr:
        head.next = ListNode(i)
        head = head.next
    return result.next

def to_list(head):
    res = []
    while head is not None:
        res.append(head.data)
        head.next
    return res

def print_list(head):
    s =""
    while head is not None:
        s += f"({head.data})->"
        head = head.next
    s += "None"
    return s
    

def add_two_numbers(l1,l2):
    digit1, digit2, carry, summ = 0, 0, 0, 0
    dumy = ListNode()
    result = dumy
    while l1 is not None or l2 is not None or carry > 0:
        digit1 = l1.data if l1 is not None else 0
        digit2 = l2.data if l2 is not None else 0

        summ = digit1 + digit2 + carry
        carry = summ // 10
        summ %= 10

        dumy.next = ListNode(summ)
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
        dumy = dumy.next
    return result.next


head1 = create_from_list([2,4,3])
print( print_list(head1) )
head2 = create_from_list([5,6,4])
print( print_list(head2) )
result = add_two_numbers(head1, head2)
print( print_list(result) )

