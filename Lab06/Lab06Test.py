from BinaryTree import *
from BST import BinarySearchTree
from BTree import BTree
def testBST():
    bst1 = BinarySearchTree();
    eleList = [3, 7, 12, 18 , 26, 27, 31]
    for n in eleList:
        bst1.insert_bts(n)
    bst1.printInOrder()

def testBinaryNode():
    # create test tree
    root = BinaryNode(14)
    four = BinaryNode(4)
    root.setLeft(four)
    three = BinaryNode(3)
    nine = BinaryNode(9)
    four.setLeft(three)
    four.setRight(nine)
    seven = BinaryNode(7)
    nine.setLeft(seven)
    five = BinaryNode(5)
    seven.setLeft(five)

    fifteen = BinaryNode(15)
    root.setRight(fifteen)
    eighteen = BinaryNode(18)
    fifteen.setRight(eighteen)
    sixteen = BinaryNode(16)
    eighteen.setLeft(sixteen)
    seventeen = BinaryNode(17)
    sixteen.setRight(seventeen)
    twenty = BinaryNode(20)
    eighteen.setRight(twenty)

    bt = BinaryTree()
    bt.setRoot(root)

    print("\n< in-order >")
    bt.inOrder(bt.getRoot())
    bt.printInOrder()

    print("\n< pre-order >")
    bt.preOrder(bt.getRoot())
    bt.printPreOrder()
    bt.preOrder2(bt.getRoot())
    print()

    print("\n< post-order >")
    bt.postOrder(bt.getRoot())
    bt.printPostOrder()

    print("\nlevelOrder() : ", end="")
    bt.levelOrder(bt.getRoot())

    print()
    print("\ncountNode() : ", bt.countNode(bt.getRoot()))

    print()
    print("count_leaf() : ", bt.count_leaf(bt.getRoot()))

    print()
    print("get_height() : ", bt.get_height(bt.getRoot()))



def useBTree():
    print("Btree")
    btree = BTree(3)
    keys = [10, 20, 34, 21, 90, 56, 62]
    for key in keys:
        btree.insert(key)
        print()
        btree.display()


def main():
    # testBinaryNode()
    # testBST()
    useBTree()

if __name__ == "__main__":
    main()





