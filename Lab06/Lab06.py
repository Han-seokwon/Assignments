from BinaryNode import *
import random

def createRandomTree(node_count, startValue , endValue):
    root = BinaryNode(random.randrange(startValue, endValue))
    for i in range(10): # creating random nodes and add to tree
        randNum = random.randrange(startValue, endValue)
        new_node = BinaryNode(randNum)
        tempRoot = root
        while True:
            if tempRoot.left is None:
                tempRoot.setLeft(new_node)
                break
            elif tempRoot.right is None:
                tempRoot.setRight(new_node)
                break
            else:
                isLeft = random.choice([True, False])
                tempRoot = tempRoot.left if isLeft else tempRoot.right
                continue

def testBinaryNode():
    root = BinaryNode(14)

    bt = BinaryTree()
    bt.setRoot(root)

    print()
    bt.inOrder(bt.getRoot())
    bt.printInOrder()

    print()
    bt.preOrder(bt.getRoot())
    bt.printPreOrder()
    bt.preOrder2(bt.getRoot())
    print()

    print()
    bt.postOrder(bt.getRoot())
    bt.printPostOrder()

    bt.levelOrder(bt.getRoot())

    print()
    print(bt.countNode(bt.getRoot()))

    print()
    print(bt.count_leaf(bt.getRoot()))

    print()
    print(bt.get_height(bt.getRoot()))

def main():
    testBinaryNode()

if __name__ == "__main__":
    main()





