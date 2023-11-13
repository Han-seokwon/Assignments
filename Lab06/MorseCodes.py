from BinaryTree import *
class MorseCodes:
    def __init__(self):
        self.root = BinaryNode()
        self.table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'),
                        ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
                        ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
                        ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
                        ('Y', '-.--'), ('Z', '--..')]

    def makeMorseTree(self):
        for tp in self.table:
            code = tp[1]
            node = self.root
            for c in code: # move to the node corresponding to the code
                if c == '.':
                    if node.getLeft() is None:
                        node.setLeft(BinaryNode())
                    node = node.getLeft()
                elif c == '-':
                    if node.getRight() is None:
                        node.setRight(BinaryNode())
                    node = node.getRight()
            node.setData(tp[0]) # matching alphabet

    def printMorseTree(self): # BFS
        n = self.root
        queue = Queue()
        queue.put(n)
        while not queue.empty():
            n = queue.get()
            if n is not None:
                print(n , end=' -> ')
                queue.put(n.getLeft())
                queue.put(n.getRight())
        print()

    def decode(self, code):
        n = self.root
        for c in code:
            if c == '.':
                n = n.getLeft()
            elif c == '-':
                n = n.getRight()
        return n.getData()

    def encode(self, ch):
        idx = ord(ch) - ord('A')
        return self.table[idx][1]

