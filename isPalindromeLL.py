def reverse(self, head):
    prev = None
    Next = None
    while head:
        Next = head.next
        head.next = prev
        prev = head
        head = Next
    return prev

def compare(first, second):
    while first and second:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
    
    return True

def isPalindrome(self, head):
    slow = head
    fast = head
    prev = head
    res = False

    while fast != None and fast.next != None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    if fast != None:
        prev.next = None
        slow = slow.next
    
    slow = reversed(slow)

    return compare(head, slow)