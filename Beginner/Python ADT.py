class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root_index = inorder.index(root_val)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]
    left_preorder = preorder[1:root_index+1]
    right_preorder = preorder[root_index+1:]

    root = Node(root_val)
    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root

def preorder_traversal(root): 
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Given preorder and inorder traversals
preorder = "EXAMFUN"
inorder = "MAFXUEN"

# Building the binary tree
root = build_tree(preorder, inorder)

# Print the preorder and inorder traversals 
print("Preorder traversal:")
preorder_traversal(root)
print()
print("Inorder traversal:")
inorder_traversal(root)