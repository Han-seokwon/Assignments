
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return  str(self.data)
    def getNext(self):
        return self.next
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def setData(self, data):
        self.data = data


class Node2:
    def __init__(self, prev=None, data=None, next=None ):
        self.prev = prev
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def getPrev(self):
        return self.prev
    def getNext(self):
        return self.next
    def getData(self):
        return self.data

    def setPrev(self):
        return self.prev
    def setNext(self, next):
        self.next = next
    def setData(self, data):
        self.data = data