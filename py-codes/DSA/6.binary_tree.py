''''
I. Depth First Traversals:

                1
            /       \
            2        3
        /       \
        4       5
    Inorder (Left, Root, Right) : 4 2 5 1 3
    Preorder (Root, Left, Right) : 1 2 4 5 3
    Postorder (Left, Right, Root) : 4 5 2 3 1


2. Breadth-First or Level Order Traversal

'''
class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self, root) -> None:
        self.root = root

    def print_in_order(self, root):
        if root:
            self.print_in_order(root.left)
            print(root.val, end=' ')
            self.print_in_order(root.right)

    def print_pre_order(self, root):
        if root:
            print(root.val, end=' ')
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)

    def print_post_order(self, root):
        if root:
            self.print_post_order(root.left)
            self.print_post_order(root.right)
            print(root.val, end=' ')


root = Node(1)
''' following is the tree after above statement
        1
    / \
    None None'''

root.left     = Node(2)
root.right     = Node(3)

''' 2 and 3 become left and right children of 1
        1
        / \
        2     3
    / \ / \
None None None None'''


root.left.left = Node(4)
'''4 becomes left child of 2
        1
    /     \
    2         3
    / \     / \
4 None None None
/ \
None None'''

root.left.left = Node(4)
root.left.right = Node(5)

bt = BinaryTree(root)

bt.print_in_order(bt.root)  # Output: 4 2 5 1 3
print()

bt.print_pre_order(bt.root)  # Output: 4 2 5 1 3
print()

bt.print_post_order(bt.root)  # Output: 4 2 5 1 3
print()
