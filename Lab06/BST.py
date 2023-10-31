from BinaryTree import *
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()


    def search_bst(self, key):
        node = self.search(self.getRoot(), key)
        if node is not None:
            print("Item found : ", str(node.getData()))
        else:
            print("Item not found")

    def search(self, node, key): # recursive version
        if node is None:
            return None
        elif key == node.getData():
            return node
        elif key < node.getData():
            return self.search(node.getLeft(), key)
        else:
            return self.search(node.getRight(), key)


    def insert_bts(self, key):
        node = BinaryNode(key) # left, right None default
        if super().isEmpty():
            self.root = node
        else:
            self.insert(self.root, node)


    def insert(self, root, node):
        if node < root:
            if root.getLeft() is None:
                root.setLeft(node)
                return True # successfully inserted
            else:
                self.insert(root.getLeft(), node)
        elif node > root:
            if root.getRight() is None:
                root.setRight(node)
                return True  # successfully inserted
            else:
                self.insert(root.getRight(), node)
        else: # node == root
            # do not insert, if there is same one in tree
            return False

    def delete_bts(self, key):
        pass













