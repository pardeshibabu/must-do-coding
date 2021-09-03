def removeLoop(self, head):
    if head is None: return
    if head.next is None: return
        
    slow_p = head
    fast_p = head
            
    while(slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        # If slow_p and fast_p meet at some point then
        # there is a loop
        if slow_p == fast_p:
            slow_p = head
            # Finding the begining of the loop
            
            if slow_p == fast_p:
                while fast_p.next != slow_p:
                    fast_p = fast_p.next
            else:
                while (slow_p.next != fast_p.next):
                    slow_p = slow_p.next
                    fast_p = fast_p.next
                    # Sinc fast.next is the looping point
                
            fast_p.next = None  # Remove loop