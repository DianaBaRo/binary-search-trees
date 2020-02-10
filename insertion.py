#Insertion: If the data we want to insert is greater than the root node we go to the right, if it is smaller, we go to the left.

#A utility function to insert a new nde with the given key

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)