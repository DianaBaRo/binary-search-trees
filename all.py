"""
We need to think about three possible scenarios:

The node we want to remove is a leaf nod, that means it doesn't have children.
The node has a single child. 
Or it has 2 children. We have to 2 options: look for the largest item (predecessor) in the left subtree or for the smallest item in the right subtree(successor)
olakase
"""

class Node(object):
    #Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):

    def __init__(self):
        self.root = None

    #O(logN) if the tree is balanced.  Otherwise it can reduce to O(N)
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node, leftChild)
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print(node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)
    
    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node")
                del node 
                return None
            if not node.leftChild:
                print("Removing node with right child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing node with a single left child")
                tempNode = node.leftChild
                del node
                return tempNode
    print("Removing node with 2 children")
    tempNode = self.getPredecessor(node.leftChild)
    node.data = tempNode.data
    leftChild = self.removeNode(tempNode.data, node.leftChild)

    return node

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node

    def remove(self.data):
        if self.root:
            self.root =self.removeNode(data, self.root)


    #Other tutorial
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


            


            
