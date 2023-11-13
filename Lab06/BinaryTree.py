# from Queue import Queue
from queue import Queue, LifoQueue # using built-in-class

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def printInOrder(self, msg="In-order : "):
        print(msg, end = "")
        self.inOrder(self.getRoot())
        print()

    def inOrder(self, node):
        # left -> node -> right
        if node is not None:
            self.inOrder(node.getLeft())
            print(node, end=" -> ")
            self.inOrder(node.getRight())

    def printPreOrder(self, msg="Pre-order : "):
        print(msg, end = "")
        self.preOrder(self.getRoot())
        print()

    def preOrder(self, node): # DFS
        # node -> left -> right
        if node is not None:
            print(node, end=" -> ")
            self.preOrder(node.getLeft())
            self.preOrder(node.getRight())

    def preOrder2(self, node): # using stack not recursive
        s = LifoQueue()
        s.put(node)
        while not s.empty():
            temp_node = s.get()
            if temp_node is not None:
                print(temp_node, end=" -> ")
                # push right first then left in order to pop left first (LIFO)
                s.put(temp_node.getRight())
                s.put(temp_node.getLeft())


    def printPostOrder(self, msg="Post-order : "):
        print(msg, end = "")
        self.postOrder(self.getRoot())
        print()

    def postOrder(self, node): # DFS
        # left -> right -> node
        if node is not None:
            self.postOrder(node.getLeft())
            self.postOrder(node.getRight())
            print(node, end=" -> ")

    def printLevelOrder(self, msg="Level-Order : "):
        print(msg, end="")
        self.levelOrder(self.root)
        print()

    def levelOrder(self, node): # BFS
        que = Queue() # FIFO
        que.put(node)
        while not que.empty():
            temp_node = que.get()
            if temp_node is not None:
                print(temp_node, end=" -> ")
                que.put(temp_node.getLeft())
                que.put(temp_node.getRight())

    def calcHeight(self, node):
        if node is None:
            return -1 # if there is no Node in tree height is -1
        hleft = self.calcHeight(node.getLeft())
        hright = self.calcHeight(node.getRight())
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1

    def calcLevels(self, node):
        if node is None:
            return -1 # if there is no Node in tree level is -1
        hleft = self.calcLevels(node.getLeft())
        hright = self.calcLevels(node.getRight())
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1

    def countNodes(self, node):
        if node is None:
            return 0
        else: # node + left subtree nodes + right subtree nodes
            return 1 + self.countNodes(node.getLeft()) + self.countNodes(node.getRight())


    def isLeaf(self, node):
        return (node.getLeft() is None) and (node.getRight() is None)

    def countLeaf(self, node):
        if node is None:
            return 0
        elif self.isLeaf(node) :
            return 1
        else: # leaf node of left subtree + leaf node of right subtree
            return self.countLeaf(node.getLeft()) + self.countLeaf(node.getRight())


class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    def __gt__(self, other):
        return self.data > other.data
    def __lt__(self, other):
        return self.data < other.data
    def __eq__(self, other):
        return self.data == other.data
    def __ne__(self, other):
        return self.data != other.data

    def getData(self):
        return self.data
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data
    def setLeft(self, node):
        self.left = node
    def setRight(self, node):
        self.right = node

