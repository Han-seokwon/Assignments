from Node import Node


class CircularLinkedList:
    def __init__(self):
        self.head =None

    def __str__(self):
        temp = self.head.next
        string_repr = ""
        if self.head is not None:
            while True:
                string_repr += str(temp) + " -> "
                temp = temp.next
                if temp == self.head.next:
                    break
        return string_repr

    def addFront(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.head.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node # front : head.next

    def addRear(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.head.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node # rear : self.head

    def addAt(self, pos ,data):
        if (pos < 0 or pos > self.getSize()):
            print("Invalid position")
            return None
        else:
            if pos == self.getSize() -1 :
                self.addRear(data)
            elif pos == 0:
                self.addFront(data)
            else:
                before = self.getNodeAt(pos -1)
                new_node = Node(data, before.next)
                before.next = new_node

    def deleteAtFront(self):
        if self.isEmpty():
            print("List is empty..")
            return None
        if self.head == self.head.next: # only one node in list
            self.head = None
            return self.head
        else:
            temp = self.head.next
            self.head.next = temp.next
            temp.next = None
            return temp

    def deleteAtRear(self):
        if self.isEmpty():
            print("List is empty..")
            return None
        if self.head == self.head.next: # only one node in list
            self.head = None
            return self.head
        else:
            temp = self.head
            before = self.getNodeAt(self.getSize() - 2 ) # second last, head before
            self.head = before
            before.next = temp.next
            temp.next = None
            return temp

    def deleteAt(self, pos):
        if pos < 0 or pos > self.getSize():
            print("Invalid position")
            return None
        elif self.isEmpty():
            print("List is empty..")
            return None
        else:
            if pos == 0:
                temp = self.deleteAtFront()
            elif pos == self.getSize() - 1:
                temp = self.deleteAtRear()
            else:
                before = self.getNodeAt(pos - 1)
                temp = before.next  # delete Node
                before.next = temp.next
                temp.next = None
            return temp


    def getSize(self):
        cnt = 0
        temp = self.head.next
        if self.head is not None:
            while True:
                temp = temp.next
                cnt+=1
                if temp == self.head.next:
                    break
        return cnt

    def getNodeAt(self, pos):
        if(pos < 0 or pos > self.getSize()):
            print("Invalid position")
            return None
        node = self.head.next
        if self.head.next is not None:
            while pos > 0:
                node = node.next
                pos -= 1
        return node

    def getDataAt(self, pos):
        node = self.getNodeAt(pos)
        if node is None:
            return None
        else:
            return node.data
    def printList(self, msg="Circularly Linked List: ") -> None:
        print(msg, str(self))

    def isEmpty(self) -> bool:
        return self.head == None

    def clear(self):
        self.head = None
    def replaceDataAt(self, pos, data):
        node = self.getNodeAt(pos)
        if node != None:
            node.data = data

    def findData(self, data):
        node = self.head
        if self.head is not None:
            while True:
                if node.data == data:
                    return node
                node = node.next
                if node == self.head:
                    return None
    def findPos(self, node): # head.next = 0
        temp = self.head.next
        pos = 0
        while True:
            if temp.data == node.data:
                return pos%self.getSize()
            temp = temp.next
            pos += 1
            if pos > self.getSize():
                return None
