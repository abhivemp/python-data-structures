# Driver file 

print("main file contents")

from Trees.bst import BST, Node

# from folder.pythonfile import class name (make sure you don't add the .py at the end)

tree1 = BST(5)
tree1.root.left = Node(1)
tree1.root.right = Node(20)
tree1.root.right.left = Node(10)
tree1.root.right.left.left = Node(7)