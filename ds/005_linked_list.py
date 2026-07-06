"""
Linked List implementation in python
Changelog:
- [26-June-2026]: Added 'delete_node' function to allow removal of nodes by value.
"""

class node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():

    def __init__(self):
        self.head = None

    def add_node(self, data):
        curr = self.head
        if self.head:
            while curr.next:
                print('hello')
                curr = curr.next
                print(curr.data)
            curr.next = node(data)
        else:
            self.head = node(data)
            
    def delete_node(self, key):
        curr = self.head
        
        if curr is None:
            print("Linked list is empty")
            return
        
        if curr.data == key:
            self.head = curr.next
            curr = None
            return
        
        previous = None
        while curr is not None and curr.data != key:
            previous = curr
            curr = curr.next
        
        if curr is None:
            print(f"{key} not found in this linked list")
            return
        
        previous.next = curr.next
        curr = None

    def print_list(self):
        curr = self.head

        while curr:
            print(f'{curr.data}', end=' -> ' if curr.next else '\n')
            curr=curr.next


linkedlist_obj = linkedlist()

linkedlist_obj.add_node(5)
linkedlist_obj.add_node(6)
linkedlist_obj.add_node(7)
linkedlist_obj.add_node(8)
linkedlist_obj.add_node(9)

linkedlist_obj.print_list()
linkedlist_obj.delete_node(8)
linkedlist_obj.print_list()
linkedlist_obj.delete_node(4)