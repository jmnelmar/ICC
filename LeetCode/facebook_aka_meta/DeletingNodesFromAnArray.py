class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def modifiedList( nums, head):
    values_to_remove = set(nums)
    while head and head.val in values_to_remove: #handlig duplicates
        head = head.next
        if not head: #in case head were null then return null
            return None

        current = head #making a shadow copy to tleft head in the first node
        while current.next:
            if current.next.val in values_to_remove:
                current.next = current.next.next
            else:
                current = current.next
        return head

