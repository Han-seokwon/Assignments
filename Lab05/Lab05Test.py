from SinglyLinkedList import *

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
    print(list)

    list.addAt(4, 55)
    list.addAt(list.getSize(), 1)
    list.addRear(0)
    print(list)

    print("list.deleteAtFront() : ", list.deleteAtFront())
    print("list.deleteAtRear() : ", list.deleteAtRear())
    print("list.deleteAt(4) : ", list.deleteAt(4))
    print(list)

    print("list.getNodeAt(3) : ", list.getNodeAt(3))
    print("list.getDataAt(3) : ", list.getDataAt(3))
    print("findData(40) : ", list.findData(40))

    list.replaceDataAt(2, 500)
    print("replaceDataAt(2, 500) -> ", list)

    list.reverseList()
    print("reverseList() -> ", list)



def main():
    # testNodes()
    testSinglyLinkedList()

if __name__ == "__main__":
    main()