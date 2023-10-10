from SinglyLinkedList import *

class LineEditor:
    def __init__(self):
        self.list = SinglyLinkedList()
    def runLineEditor(self):
        while True:
            command = input("i-insert, d-delete, r=replace, "
                            "p-print, l-loadfile, s-writefile, q-quit ->")
            if command == 'i':
                self.addLine()
            elif command == 'd':
                self.deleteLine()
            elif command == 'r':
                self.replaceLine()
            elif command == 'p':
                self.printByLine()
            elif command == 'l':
                self.loadFromFile()
            elif command == 's':
                self.writeToFile()
            elif command == 'q':
                return 0

    def addLine(self):
        pos = int(input("input line number : "))
        str = input("input line text : ")
        self.list.addAt(pos, str)

    def deleteLine(self):
        pos = int(input("input line number : "))
        self.list.deleteAt(pos)

    def replaceLine(self):
        pos = int(input("input line number : "))
        str = input("input modified text : ")
        self.list.replaceDataAt(pos, str)

    def printByLine(self):
        print("Line Editor")
        node = self.list.head
        line = 0
        while node is not None:
            print(f"[{line:2d}] {node}")
            node = node.next
            line+=1

    def loadFromFile(self):
        filename = "test.txt"
        with open(filename, "r") as inFile:
            lines = inFile.readlines()
            for l in lines:
                self.list.addAt(self.list.getSize(), l.rstrip('\n'))

    def writeToFile(self):
        filename = "test.txt"
        with open(filename, "w") as outFile:
            size = self.list.getSize()
            for i in range(size):
                outFile.write(self.list.getDataAt(i) + '\n')

