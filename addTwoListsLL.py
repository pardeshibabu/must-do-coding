class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def reverse(self, head):
    prev = None
    Next = None
    while head:
        Next = head.next
        head.next = prev
        prev = head
        head = Next
    return prev




def addTwoLists(self, first, second):
    result = None
    prev = None

    c = 0
    Sum = 0

    while first != None or second != None:
        firstData = first.data or 0
        secondData = second.data or 0
        Sum = c + firstData + secondData
        c = 1 if Sum >= 10 else 0
        Sum = Sum % 10
        temp = Node(Sum)

        if result == None:
            result = temp
        else:
            prev.next = temp
        
        prev = temp
    return result
