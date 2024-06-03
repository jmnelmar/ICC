# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ""
        while self.next:
            s += f"({self.val})->"
            self = self.next
        s += f"({self.val})->"
        return s

def reverseList( head:[ListNode]) -> [ListNode]:
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
print(root)
print(reverseList(root))