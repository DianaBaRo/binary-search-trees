"""
We need to think about three possible scenarios:

The node we want to remove is a leaf nod, that means it doesn't have children.
The node has a single child. 
Or it has 2 children. We have to 2 options: look for the largest item (predecessor) in the left subtree or for the smallest item in the right subtree(successor)
"""

class BSTreeNode
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def delete(self, key):
        """ delete the node with the given key and return the 
        root node of the tree """

        if self.key == key:
            # found the node we need to delete

            if self.right and self.left: 

                # get the successor node and its parent 
                [psucc, succ] = self.right._findMin(self)

                # splice out the successor
                # (we need the parent to do this) 

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                # reset the left and right children of the successor

                succ.left = self.left
                succ.right = self.right

                return succ                

            else:
                # "easier" case
                if self.left:
                    return self.left    # promote the left subtree
                else:
                    return self.right   # promote the right subtree 
        else:
            if self.key > key:          # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                # else the key is not in the tree 

            else:                       # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)

        return self

def _findMin(self, parent):
    """ return the minimum node in the current tree and its parent """

    # we use an ugly trick: the parent node is passed in as an argument
    # so that eventually when the leftmost child is reached, the 
    # call can return both the parent to the successor and the successor

    if self.left:
        return self.left._findMin(self)
    else:
        return [parent, self]