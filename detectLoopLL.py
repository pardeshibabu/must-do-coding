def detectLoop(self, head):
    tortoise = head
    hare = head

    while tortoise and hare and hare.next:
        if tortoise == hare:
            return True
        tortoise = tortoise.next
        hare = hare.next.next
    
    return False
