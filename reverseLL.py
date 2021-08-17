def reverseList(head):
    prev = None
    root = head
    next = None
    while root:
        next = root.next
        root.next = prev
        prev = root
        root = next
    return prev