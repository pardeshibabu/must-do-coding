# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def sortedMerge(head1, head2):
    if head1 == None: return head2
    if head2 == None: return head1

    result = Node(0)
    temp = result
    while head1 and head2:
        if head1.data < head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
    
    if head1:
        temp.next = head1
    if head2:
        temp.next = head2
    
    return result.next

