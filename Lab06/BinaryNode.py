from Queue import CircularQueue
from Stack import Stack

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def printInOrder(self, msg="In-order : "):
        print()
        print(msg, end = "")
        self.inOrder(self.getRoot())
        print()

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.getLeft())
            print(node, end=" -> ")
            self.inOrder(node.getRight())

    def printPreOrder(self, msg="Pre-order : "):
        print()
        print(msg, end = "")
        self.preOrder(self.getRoot())
        print()

    def preOrder(self, node):
        if node is not None:
            print(node, end=" -> ")
            self.inOrder(node.getLeft())
            self.inOrder(node.getRight())


    def printPostOrder(self, msg="Post-order : "):
        print()
        print(msg, end = "")
        self.postOrder(self.getRoot())
        print()

    def postOrder(self, node):
        if node is not None:
            self.inOrder(node.getLeft())
            self.inOrder(node.getRight())
            print(node, end=" -> ")

    def preOrder2(self, node):
        s = Stack()
        s.push(node)
        while not s.isEmpty():
            temp_node = s.pop() # BinaryNode
            if temp_node is not None:
                print(temp_node, end=" ")
                s.push(temp_node.getRight())
                s.push(temp_node.getLeft())

    def levelOrder(self, node):
        que = CircularQueue()
        que.enqueue(node)
        while not que.isEmpty():
            temp_node = que.dequeue() # BinaryNode
            if temp_node is not None:
                print(temp_node, end=" ")
                que.enqueue(temp_node.getLeft())
                que.enqueue(temp_node.getRight())


    def countNode(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.countNode(node.getLeft()) + self.countNode(node.getRight())
            # same
            # return 1 + self.countNode(node.getLeft() + node.getRight())

    def isLeaf(self, node):
        return (node.getLeft() is None) and (node.getRight() is None)

    def count_leaf(self, node):
        if node is None:
            return 0
        elif self.isLeaf(node) :
            return 1
        else:
            return self.count_leaf(node.getLeft()) + self.count_leaf(node.getRight())

    def get_height(self, node):
        if node is None:
            return -1 # if there is no Node in tree height is 0
        hleft = self.get_height(node.getLeft())
        hright = self.get_height(node.getRight)
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1

    def get_levels(self, node):
        if node is None:
            return -1 # if there is no Node in tree height is 0
        hleft = self.get_levels(node.getLeft())
        hright = self.get_levels(node.getRight)
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1


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

