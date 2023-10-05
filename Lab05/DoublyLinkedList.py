class Node2:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
    def getPrev(self):
        return self.prev
    def getNext(self):
        return self.next
    def getData(self):
        return self.data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += str(temp) + "->"
            temp = temp.next
        return string_repr + "END"






