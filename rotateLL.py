def rotate(head, k):
        # code here
        if not head: return head
        
        root = head
        count = 1
        while count < k and root:
            count += 1
            root=root.next
        
        if root is None:
            return head
        
        kthnode = root
        
        while root.next:
            root=root.next
        
        root.next = head
        head = kthnode.next
        kthnode.next = None
        
        return head
        
    
