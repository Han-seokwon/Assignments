from CircularLinkedList import *


class JosephusProblem:
    def __init__(self, n =10, m=3):
        self.list = CircularLinkedList()
        self.n = n
        self.m = m
        for i in range(1, n+1):
            self.list.addFront(i)

    def runJosephus(self):
        print(self.list)
        temp = self.list.head.next
        count = 0
        while True:
            temp = temp.next
            count += 1
            if count == self.m:
                nextStartNode = temp.next
                pos = self.list.findPos(temp)
                print("Eliminated -> ", self.list.deleteAt(pos))
                temp = nextStartNode
                print(self.list)
                count = 0

            if temp == temp.next: # The last one left
                print("Selected -> ", temp)
                break