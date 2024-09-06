def modifiedList( nums, head):
    while head and head.value in nums:
        head = head.next

    if not head:
        return None
    
    current = head

    while current.next:
        if current.next.value in nums:
            current.next = current.next.next
        else:
            current = current.next

    return head