def merge(head1, head2):
    if head1 == None: return head2

    if head2 == None: return head1

    result = None

    if head1.data < head2.data:
        result = head1
        result.bottom = merge(head1.bottom, head2)
    else:
        result = head2
        result.bottom = merge(head1, head2.bottom)
    
    result.next = None
    return result


def flatten(root):
    if root == None or root.next == None: return root

    root.next = flatten(root.next)

    root = merge(root, root.next)

    return root
