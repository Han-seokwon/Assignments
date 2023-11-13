from BinaryTree import *
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def search_bst(self, key):
        node = self.search(self.getRoot(), key)
        if node is not None:
            print("Item found : ", str(node.getData()))
        else:
            print("Item not found --> ", str(key))

    def search(self, node, key): # recursive version
        if node is None:
            return None
        elif key == node.getData():
            return node
        elif key < node.getData():
            return self.search(node.getLeft(), key)
        else:
            return self.search(node.getRight(), key)

    def search_max_bst(self, node):
        while node is not None and node.getRight() is not None:
            node = node.getRight()
        return node

    def search_min_bst(self, node):
        while node is not None and node.getLeft() is not None:
            node = node.getLeft()
        return node

    def insert_bst(self, key):
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
                return self.insert(root.getLeft(), node)
        elif node > root:
            if root.getRight() is None:
                root.setRight(node)
                return True  # successfully inserted
            else:
                return self.insert(root.getRight(), node)
        else: # node == root
            # do not insert, if there is same one in tree
            return False

    def delete_bst(self, key):
        if not super().isEmpty():
            parent = None
            node = self.root
            while node is not None and node.getData() != key:
                parent = node
                if key < node.getData() :
                    node = node.getLeft()
                else:
                    node = node.getRight()
            if node is None: #  key not found
                return None

            #case 1: node to be deleted is leaf
            if node.left is None and node.right is None :
                self.delete_bts_case1(parent, node)
            # case 2: node to be deleted has one child
            elif node.left is None or node.right is None :
                self.delete_bts_case2(parent, node)
            # case 3: node to be deleted has both child
            else:
                self.delete_bts_case3(parent, node)


    def delete_bts_case1(self, parent, node): # node to be deleted is leaf
        if parent is None:
            root = None
        else:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None

    def delete_bts_case2(self, parent, node): # node to be deleted has one child
        if node.left is not None:
            child = node.getLeft()
        else:
            child = node.getRight()

        if node == self.root:
            self.root = child
        else:
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child

    def delete_bts_case3(self, parent, node): # node to be deleted has both child
        succParent = node # inorder successor's parent
        succ = node.right # inorder successor
        # find left most child of succ
        while succ.left is not None:
            succParent = succ
            succ = succ.left

        # succ is left most so succ.left is None
        if succParent.left == succ:
            succParent.left = succ.right
        else:
            succParent.right = succ.right

        node.setData(succ.getData()) # copy data
        node = succ













