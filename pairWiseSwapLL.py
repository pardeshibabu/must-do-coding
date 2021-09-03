def pairWiseSwap(self, head):
        # code here
        if head == None or head.next == None: return head
        
        newHead = head.next

        p = head
        q = None

        while(True):
            q = p.next
            temp = q.next
            q.next = p

            if temp == None or temp.next==None:
                p.next = temp
                break

            p.next = temp.next
            p = temp
        
        return newHead