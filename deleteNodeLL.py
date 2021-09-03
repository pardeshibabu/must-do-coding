def deleteNode(self,curr_node):
    if curr_node.next:
        return
    
    q = curr_node.next
    curr_node.data = q.data
    curr_node.next = q.next
    q.next = None