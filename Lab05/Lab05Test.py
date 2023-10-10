from SinglyLinkedList import *
from DoublyLinkedList import *
from LineEditor import *
from SparsePolynomial import *
def testNodes():

    d = Node(100, None)
    c = Node(99, d)
    b = Node(23, c)
    a = Node(None, b)
    print( a, a.getNext(), b.getNext(), c.getNext())
    print(a, a.getNext(), a.getNext().getNext(), a.getNext().getNext().getNext())
    print( a, a.next, a.next.next, a.next.next.next)

def testSinglyLinkedList():
    list = SinglyLinkedList()
    for i in range(1, 10):
        list.addFront(i*10)
    list.printList()

    list.addAt(4, 55)
    print("list.addAt(4, 55) : ", list)
    list.addAt(list.getSize(), 1)
    print("list.addAt(list.getSize(), 1) : ", list)
    list.addRear(0)
    print("list.addRear(0) : ", list)

    print("list.deleteAtFront() : ", list.deleteAtFront())
    print("list.deleteAtRear() : ", list.deleteAtRear())
    print("list.deleteAt(4) : ", list.deleteAt(4))
    print(list)

    print("list.getNodeAt(3) : ", list.getNodeAt(3))
    print("list.getDataAt(3) : ", list.getDataAt(3))
    print("findData(40) : ", list.findData(40))

    list.replaceDataAt(2, 500)
    print("replaceDataAt(2, 500) : ", list)

    list.reverseList()
    print("reverseList() : ", list)

def testLineEditor():
    le = LineEditor()
    le.runLineEditor()

def testDoublyLinkedList():
    dList = DoublyLinkedList()
    for i in range(1, 10):
        dList.addFront(i*10)
    dList.printList()

    dList.addAt(4, 55)
    print("dList.addAt(4, 55) : ", dList)
    dList.addAt(dList.getSize(), 1)
    print("dList.addAt(dList.getSize(), 1) : ", dList)
    dList.addRear(0)
    print("dList.addRear(0) : ", dList)

    print("dList.deleteAtFront() : ", dList.deleteAtFront())
    print("dList.deleteAtRear() : ", dList.deleteAtRear())
    print("dList.deleteAt(4) : ", dList.deleteAt(4))
    print(dList)

    print("dList.getNodeAt(3) : ", dList.getNodeAt(3))
    print("dList.getDataAt(3) : ", dList.getDataAt(3))
    print("findData(40) : ", dList.findData(40))

    dList.replaceDataAt(2, 500)
    print("replaceDataAt(2, 500) : ", dList)

    dList.reverseList()
    print("reverseList() : ", dList)


def testPoly():

    a = SparsePolynomial()
    a.read()
    b = SparsePolynomial()
    b.read()
    a.display(" A = ")
    b.display(" B = ")

    c = a.add(b)
    c.display(" A + B = ")
    d = a.sub(b)
    d.display(" A - B = ")

def main():
    # testNodes()
    # testSinglyLinkedList()
    # testLineEditor()
    # testDoublyLinkedList()
    testPoly()

if __name__ == "__main__":
    main()