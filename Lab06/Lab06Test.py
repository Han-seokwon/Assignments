from BinaryNode import *
import random

# def createRandomTree(node_count, startValue , endValue):
#     root = BinaryNode(random.randrange(startValue, endValue))
#     for i in range(10): # creating random nodes and add to tree
#         randNum = random.randrange(startValue, endValue)
#         new_node = BinaryNode(randNum)
#         tempRoot = root
#         while True:
#             if tempRoot.left is None:
#                 tempRoot.setLeft(new_node)
#                 break
#             elif tempRoot.right is None:
#                 tempRoot.setRight(new_node)
#                 break
#             else:
#                 isLeft = random.choice([True, False])
#                 tempRoot = tempRoot.left if isLeft else tempRoot.right
#                 continue

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

def main():
    testBinaryNode()

if __name__ == "__main__":
    main()





