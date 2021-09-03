def getNthFromLast(head,n):
    count = 0
    temp = head

    while temp:
        count += 1
        temp = temp.next

    if n > count: return -1

    diff = count - n
    count = 0
    while count < diff:
        head = head.next
    
    return head.data