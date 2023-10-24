class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        pass


    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root


class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data
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

