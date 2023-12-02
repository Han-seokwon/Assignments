from BinaryTree import *
from queue import Queue, LifoQueue
from BST import BinarySearchTree
from BinaryTree import *
from MorseCodes import MorseCodes
from ExpressionTree import  *
from WordMeaningDictionary import *
from MinHeap import *
from HuffmanCodes import *

def BFS01(n):
    queue = Queue()
    queue.put(n)
    while not queue.empty():
        n = queue.get()
        if n is not None:
            print(n, end=" -> ")
            queue.put(n.getLeft())
            queue.put(n.getRight())
def DFS01(n):
    stack = LifoQueue()
    stack.put(n)
    while not stack.empty():
        n = stack.get()
        if n is not None:
            print(n, end=" -> ")
            stack.put(n.getRight())
            stack.put(n.getLeft())


def testBinaryTree():
    # create test nodes
    root = BinaryNode(14)
    n2 = BinaryNode(4); n3 = BinaryNode(15); n4 = BinaryNode(3); n5 = BinaryNode(9)
    n6 = BinaryNode(18); n7 = BinaryNode(7); n8 = BinaryNode(16); n9 = BinaryNode(20)
    n10 = BinaryNode(5); n11 = BinaryNode(17)

    root.setLeft(n2); root.setRight(n3)
    n2.setLeft(n4); n2.setRight(n5)
    n3.setRight(n6)
    n5.setLeft(n7)
    n6.setLeft(n8); n6.setRight(n9)
    n7.setLeft(n10)
    n8.setRight(n11)

    print("\n\nBreadth First Search :")
    BFS01(root)
    print("\n\nDepth First Search :")
    DFS01(root)

    # create test tree
    print("\n\n< Binary Tree Test >")
    bt = BinaryTree()
    bt.setRoot(root)

    bt.printInOrder()

    bt.printPreOrder()
    print("preOrder2(): ", end="")
    bt.preOrder2(bt.getRoot())
    print()

    bt.printPostOrder()
    print()

    bt.printLevelOrder()

    print()
    print("Tree Height : ", bt.calcHeight(bt.getRoot()))

    print()
    print("Tree Level : ", bt.calcLevels(bt.getRoot()))

    print()
    print("Leaf count : ", bt.countLeaf(bt.getRoot()))

    print()
    print("Size of the Tree : ", bt.countNodes(bt.getRoot()))


def testMorseCodes():
    mc = MorseCodes()
    mc.makeMorseTree()
    mc.printMorseTree()

    str01 = "MUHAMMADTARIQMAHMOOD"
    mlist = []
    for ch in str01:
        code = mc.encode(ch)
        mlist.append(code)
    print("\nMorse Code : ", mlist)
    print("\nDecodinge : ", end="")
    for code in mlist:
        ch = mc.decode(code)
        print(ch, end="")
    print()

    # mcbt = BinaryTree(mc.root)
    # mcbt.printInOrder()
    # mcbt.printPreOrder()
    # mcbt.printPostOrder()
    # mcbt.printLevelOrder()
    # print("Tree Height : ", mcbt.calcHeight(mcbt.getRoot()))
    # print("Leaf count : ", mcbt.countLeaf(mcbt.getRoot()))
    # print("Size of the Tree : ", mcbt.countNodes(mcbt.getRoot()))

def testBST():
    tree = BinarySearchTree()
    eleList = [35,18,7,26,12,3,68,22,30,99]
    for n in eleList:
        tree.insert_bst(n)
        tree.printInOrder()
    tree.printPreOrder()
    tree.printPostOrder()
    tree.printLevelOrder()
    print("Nodes = %d"% tree.countNodes(tree.getRoot()))
    print("Leaf Nodes = %d" % tree.countLeaf(tree.getRoot()))
    print("Height = %d" % tree.calcHeight(tree.getRoot()))
    print("Maximum = %d" % tree.search_max_bst(tree.getRoot()).getData())
    print("Minimum = %d" % tree.search_min_bst(tree.getRoot()).getData())

    tree.search_bst(12)
    tree.search_bst(2000)

    tree.printLevelOrder("Original : LevelOrder : ")
    tree.delete_bst(3)
    tree.printLevelOrder(" case1 : < 3> LevelOrder : ")
    tree.delete_bst(68)
    tree.printLevelOrder(" case2 : <68> LevelOrder : ")
    tree.delete_bst(18)
    tree.printLevelOrder(" case3 : <18> LevelOrder : ")
    tree.delete_bst(35)
    tree.printLevelOrder(" case3 : <35> LevelOrder : ")

    print("Nodes = %d"% tree.countNodes(tree.getRoot()))
    print("Leaf Nodes = %d" % tree.countLeaf(tree.getRoot()))
    print("Height = %d" % tree.calcHeight(tree.getRoot()))
    print("Maximum = %d" % tree.search_max_bst(tree.getRoot()).getData())
    print("Minimum = %d" % tree.search_min_bst(tree.getRoot()).getData())

def testExpressionTree():
    et = ExpressionTree()
    postfix = "ab+ef*g*-" # (a+b)-((e*f)*g)
    root = et.constructTree(postfix)
    print("\nInorder (infix) : ", end="")
    et.inOrder(root)
    print("\nPreorder (prefix) : ", end="")
    et.preOrder(root)
    print("\nPostorder (postfix) : ", end="")
    et.postOrder(root)

    et = ExpressionTree()
    postfix = "24+45*8*-"  # (2+4)-((4*5)*8) = -154
    root = et.constructTree(postfix)
    print("\nevaluateExpressionTree() : 24+45*8*- = " , et.evaluateExpressionTree(root))


def testWMDic():
    wmd = Dictionary()
    wmd.runDict()


def testMinHeap():
    print("\n Heap Test")
    heap = MinHeap()
    data = [2, 5, 4, 8, 9, 3, 7, 3]
    print("Data elements : " + str(data))

    for elem in data:
        heap.insert(elem)
    heap.printHeap()

    print("\ndelete() : " , heap.delete())
    heap.printHeap()
    print(heap)

    print("\ndelete() : " , heap.delete())
    heap.printHeap()
    print(heap)


def testHuffmanCodes():
    HuffmanCodes()
    text = "kjalklkkjaklkllkfkljsdkl"
    # with open("License.txt") as txt_file:
    #     text = txt_file.read()
    hc = HuffmanCodes(text)
    freq = hc.makeFrequencyDict()
    for key in freq:
        print("{} : {} ".format(key, freq[key]))
    print()
    hc.printCodes()

def main():
    # testBinaryTree()
    # testMorseCodes()
    # testBST()
    # testExpressionTree()
    # testWMDic()
    # testMinHeap()
    testHuffmanCodes()




if __name__ == "__main__":
    main()





