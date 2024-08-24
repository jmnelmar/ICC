#addTwoNumbers in Python. 
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1:ListNode, l2:ListNode):
    result = ListNode()
    dummy = result
    carry = 0

    while l1 != None or l2 != None or carry != 0:

        digit1 = l1.val if l1 != None else 0
        digit2 = l2.val if l2 != None else 0
