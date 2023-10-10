from Node import Node2


class DoublyLinkedList:
    def __init__(self):
        self.head =None

    def __str__(self):
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += str(temp) + " <-> "
            temp = temp.next
        return string_repr + "END"

    def getNodeAt(self, pos):
        if(pos < 0 or pos > self.getSize()):
            print("Invalid position")
            return None
        temp = self.head
        while pos > 0 and temp != None:
            temp = temp.next
            pos -= 1
        return temp

    def getDataAt(self, pos):
        node = self.getNodeAt(pos)
        if node is None:
            return None
        else:
            return node.data

    def getSize(self):
        cnt = 0
        temp = self.head
        while temp:
            temp = temp.next
            cnt += 1
        return cnt

    def isEmpty(self) -> bool:
        return self.head == None

    def clear(self):
        self.head = None

    def addFront(self, data):
        new_node = Node2(None, data, None)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addRear(self, data):
        if self.head is None:
            self.addFront(data)
        else:
            temp = self.head
            while temp.next: # traverse to last node
                temp = temp.next
            temp.next = Node2(temp, data, None) # create node & link to tail

    def addAt(self, pos, data):
        if (pos < 0 or pos > self.getSize()):
            print("Invalid position")
            return None
        else:
            if pos == self.getSize() - 1:
                self.addRear(data)
            elif pos == 0:
                self.addFront(data)
            else:
                before = self.getNodeAt(pos -1)
                new_node = Node2(before, data, before.next)
                before.next = new_node
                if new_node is not None:
                    new_node.next.prev = new_node

    def deleteAtFront(self):
        if self.isEmpty():
            print("List is empty..")
            return None
        temp = self.head
        if self.head.next is None: # just one node in list
            self.head = None
        else:
            self.head = temp.next
            self.head.prev = None
        return temp

    def deleteAtRear(self):
        if self.isEmpty():
            print("List is empty..")
            return None
        else:
            temp = self.head
            if self.head.next is None:
                self.head = None
            else:
                while temp.next:
                    temp = temp.next
                temp.prev.next = None  # temp : last node
                temp.prev = None
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
                temp = before.next # temp : delete Node
                before.next = temp.next
                temp.next.prev = before
                temp.next = temp.prev = None
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
            temp.next = temp.prev # Make the current node's next point backwards
            temp.prev = next_node # Make the current node's prev point forwards
            before = temp  # Make the previous node be the current node
            temp = next_node # Make the current node be the next node

        self.head = before # Set before node(which was the last node) in order to put the head at the end

    def printList(self, msg="Doubly Linked List: ") -> None:
        print(msg, str(self))

    def findData(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None





























