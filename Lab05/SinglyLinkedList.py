
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return "(" + str(self.data) + ")"
    def getNext(self):
        return self.next
    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next
    def setData(self, data):
        self.data = data

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += str(temp) + "->"
            temp = temp.next
        return string_repr + "END"

    def addFront(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head # link new_node to head
        self.head = new_node # make new_node as head

    def addRear(self, data):
        if self.head is None:
            self.addFront(data)
        else:
            temp = self.head
            while temp.next: # traverse to last node
                temp = temp.next
            temp.next = Node(data, None) # create node & link to tail

    def getNodeAt(self, pos):
        if(pos < 0):
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.next
            pos -= 1
        return node

    def getDataAt(self, pos):
        node = self.getNodeAt(pos)
        if node == None:
            return None
        else:
            return node.data

    def findData(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def getSize(self):
        cnt = 0
        temp = self.head
        while temp:
            temp = temp.next
            cnt+=1
        return cnt

    def isEmpty(self) -> bool:
        return self.head == None

    def clear(self):
        self.head = None

    def addAt(self, pos ,elem):
        before = self.getNodeAt(pos -1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            new_node = Node(elem, before.next)
            before.next = new_node

    def deleteAtFront(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        return temp

    def deleteAtRear(self):
        temp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                second_last = temp # Second from the back
                temp = temp.next # last Node
                second_last.next = None
        return temp

    def deleteAt(self, pos):
        temp = None
        if not self.isEmpty() and (pos <= self.getSize()) :
            if pos == 0:
                temp = self.deleteAtFront()
            elif pos == self.getSize():
                temp = self.deleteAtRear()
            else:
                before = self.getNodeAt(pos - 1)
                temp = before.next # delete Node
                before.next = temp.next
                temp.next = None
        return temp

    def replaceDataAt(self, pos, data):
        node = self.getNodeAt(pos)
        if node != None:
            node.data = data


    def reverseList(self):
        before = None
        temp = self.head
        while temp:
            next_node = temp.next # Store the current node's next node.
            temp.next = before # Make the current node's next point backwards
            before = temp  # Make the previous node be the current node
            temp = next_node # Make the current node the next node

        self.head = before # Set before node in order to put the head  at the end

    def printList(self):
        print(str(self))






























