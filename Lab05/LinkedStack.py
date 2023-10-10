from Node import Node

class LinkedStack:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += str(temp) + "->"
            temp = temp.next
        return string_repr + "END"

    def push(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head  # link new_node to head
        self.head = new_node  # make new_node as head

    def pop(self):
        if self.isEmpty():
            print("Stack is empty..")
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp

    def peek(self):
        return self.head

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
