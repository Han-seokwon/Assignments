from MinHeap import *
class HNode:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):
        return "({} : {})".format(self.char, self.freq)

    def __eq__(self, other): return self.freq == other.freq
    def __ne__(self, other): return self.freq != other.freq
    def __lt__(self, other): return self.freq < other.freq
    def __le__(self, other): return self.freq <= other.freq
    def __gt__(self, other): return self.freq > other.freq
    def __ge__(self, other): return self.freq >= other.freq

class HuffmanCodes:
    def __init__(self, txt=None):
        self.text = txt
        self.mheap = MinHeap()
        self.codes = {} # dictionary to find matching code via char
        self.decodes = {} # dictionary to find matching char via code

    def makeFrequencyDict(self):
        frequencies = {}
        for c in self.text:
            if not c in frequencies:
                frequencies[c] = 0
            frequencies[c] += 1
        return frequencies

    def makeHeap(self):
        frequencies = self.makeFrequencyDict()
        for key in frequencies:
            node = HNode(key, frequencies[key])
            self.mheap.insert(node)
    def makeHuffmanTree(self):
        self.makeHeap()
        while self.mheap.getSize() > 1: # until reach last node
            p = self.mheap.delete() # delete smallest frequency node
            q = self.mheap.delete() # delete next smallest frequency node
            r = HNode(None, p.freq + q.freq, p , q) # intermediate node doesn't have char
            self.mheap.insert(r)

        return self.mheap.delete() # root

    def makeCodes(self):
        root = self.makeHuffmanTree()
        current_code =""
        self.make_codes(root, current_code)

    def make_codes(self, root, current_code):
        if root is None:
            return

        if root.char != None: # not intermediate node
            self.codes[root.char] = current_code # add code to 'codes' data set
            self.decodes[current_code] = root.char # add char to 'decodes' data set
            return

        # root.char is intermediate node
        # complete the corresponding code by traversing each node, starting with the root node
        self.make_codes(root.left, current_code + "0")
        self.make_codes(root.right, current_code + "1")


    def getEncodedText(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char] # add matching code from code data set(dictionary)
        return encoded_text

    def printCodes(self):
        self.makeCodes()
        for key in self.codes:
            print("{} : {}".format(key, self.codes[key]))
        print("Reverse Coding")
        for key in self.decodes:
            print("{} : {}".format(key, self.decodes[key]))












