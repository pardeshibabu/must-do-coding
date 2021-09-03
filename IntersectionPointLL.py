def intersetPoint(head1,head2):
    count1 = 0
    count2 = 0

    root1 = head1
    root2 = head2

    while root1:
        count1 += 1
        root1 = root1.next
    
    while root2:
        count2 += 1
        root2 = root2.next
    
    diff = abs(count1- count2)
    root1 = head1
    root2 = head2

    if count1 > count2:
        for i in range(diff):
            root1 = root1.next
    else:
        for i in range(diff):
            root2 = root2.next
    
    while root1 and root2:
        if root1 == root2:
            return root1.data
        root1 = root1.next
        root2 = root2.next
    return -1
