# Class file to run binary search trees.

class Node:

    def __init__(self, data):
        self.left = -1 # pointer to the left child
        self.right = -1 # pointer to the right child
        self.data = data # store data in the node itself




# Binary Search Tree class componses of a root node

class BST:

    def __init__(self, data):
        self.root = Node(data) # COnstructing root node with data
    


