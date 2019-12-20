# bst are going to make inserting, deleting and sorting very fast, with O(log N) time compleity. It is predictable
# Tress have nodes with the data and connection between the nodes.
# root node: we have a reference to this, all other nodes can be accessed via the root node.
# In a tree there must be only a single path from the root node to any other nodes in the tree.
# There are parent nodes, child nodes and leaf nodes when they don't have children.

# Binary search tree:
    # They are data structures
    # Keeps the keys in sorted order, we can use binary search.
    # every node can have at most two children: left and right child. Left child is smaller than the parent, and right child is greater than the parent.
    # with this display, in every decision we get rid of half of the data in which we are searching. O(logN), ordo logarithmic time complexity.
    # Height of a tree: the number of layers it contains. First layer has 1 node, and second layer has 2 nodes.
    # Height of the tree, h: the length of the path from the root to the deepest node in the tree.
    # We should keep the height of the tree at a minimun which is h=log n
    #if the tree is unbalanced, the h= log n relation is no more valid and the operation's running time is no more logarithmic.
