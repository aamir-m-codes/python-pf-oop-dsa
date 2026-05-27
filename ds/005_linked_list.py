"""
Pending...
Linked List implementation in python
"""

class node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
head = node(5)
node1 = node(6)
node2 = node(7)


head.next = node1
node1.next = node2

curr = head

while curr:
    print(curr.data)
    curr = curr.next
