from Node import Node


class LinkedDeque:

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
            new_node.next = self.head  # link new_node to head
        self.head = new_node  # make new_node as head

    def addRear(self, data):
        if self.head is None:
            self.addFront(data)
        else:
            temp = self.head
            while temp.next:  # traverse to last node
                temp = temp.next
            temp.next = Node(data, None)  # create node & link to tail

    def deleteFront(self):
        if self.isEmpty():
            print("Dequeue is empty..")
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp

    def deleteRear(self):
        if self.isEmpty():
            print("Dequeue is empty..")
            return None
        else:
            temp = self.head
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                second_last = temp
                temp = temp.next  # temp : last node
                second_last.next = None
            return temp

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



