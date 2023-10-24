from BinaryNode import *
import random


def testBinaryNode():
    root = BinaryNode(14)
    for i in range(10): # creating random nodes and add to tree
        randNum = random.randrange(0, 20)
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

    binaryTree = BinaryTree(root)
    print(binaryTree)



def main():
    pass

if __name__ == " __main__":
    main()



