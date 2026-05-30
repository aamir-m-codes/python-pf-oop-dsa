"""
BST Tree implementation in python
"""

class node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = node(5)
leftnode = node(4)
rightnode = node(7)


root.left = leftnode
root.right = rightnode

print(root.data)
print(leftnode.data, rightnode.data)