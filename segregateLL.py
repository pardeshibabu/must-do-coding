def segregate(self, head):
    zero = 0
    one = 0
    two = 0
    root = head

    while root:
        if root.data == 0:
            zero += 1
        elif root.data == 1:
            one += 1
        elif root.data == 2:
            two += 1
        root = root.next
    
    root = head
    while zero:
        root.data = 0
        root = root.next
        zero -= 1

    while one:
        root.data = 1
        root = root.next

    while two:
        root.data = 2
        root = root.next    
