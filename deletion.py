"""
We need to think about three possible scenarios:

The node we want to remove is a leaf nod, that means it doesn't have children.
The node has a single child. 
Or it has 2 children. We have to 2 options: look for the largest item (predecessor) in the left subtree or for the smallest item in the right subtree(successor)
"""

class BSTreeNode

    #Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def minValueNode(node):
        current = node

        #loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
        return current
    
    #Some places use self in other root. I am going to use root.
    #Recursion!
    """ Utility function to delete the node with the given key and return the 
        root node of the tree """
    
    def delete(root, key):
        #Base case
        if root is None:
            return root

        if key < root.key:
            root.left = delete(roo.left, key)

        elif key > root.key:
            root.right = delete(root.right, key)

        #If key is same as root' key, then this is the node to be deleted
        else:

            #Node with only one child or no child, leaf node
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            #Node with two children: get the inorder sucessor (smallest in the right tree)
            temp = minValueNode(root.right)

            #Copy the inorder sucessor's content to this node
            root.key = temp.key

            #Delete the inorder successor
            root.right = delete(root.right, temp.key)

        return root


            