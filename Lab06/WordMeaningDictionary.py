from BST import *
from queue import LifoQueue
class Record:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __eq__(self, other): return self.word == other.word
    def __ne__(self, other): return self.word != other.word
    def __lt__(self, other): return self.word < other.word
    def __gt__(self, other): return self.word > other.word
    def __str__(self):
        return "{} : {}".format(str(self.word), str(self.meaning))


class Dictionary(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def searchByWord(self, word):
        n = self.search(self.root, Record(word, None))
        if n is not None:
            print("Record is ---->> ", n)
        else:
            print("The " + word + " is not found.")

    def searchByMeaning(self, meaning):
        self.searchMeaning(self.root, meaning)

    def searchMeaning(self, node, meaning):
        s = LifoQueue()
        s.put(node)
        while not s.empty(): # preorder search
            node = s.get()
            if node is not None:
                if node.getData().meaning == meaning:
                    print("Record is ---->> ", node)
                    return
                else:
                    s.put(node.getRight())
                    s.put(node.getLeft())
        print("The " + meaning + " is not found.")

    def runDict(self):
        wdict = Dictionary()
        while True:
            command = input("i-insert, d-delete, p-print, s-search, m-search meaning, q-quit -> ")
            if command == "i":
                word = input("   > word : ").strip()
                meaning = input("   > meaning : ").strip()
                wdict.insert_bst(Record(word, meaning))

            elif command == 'd':
                word = input("  Inter word : ").strip()
                wdict.delete_bst(Record(word, None))

            elif command == 'p':
                print("  Dictionary : ")
                wdict.inOrder(wdict.root)
                print('\n')

            elif command == 's':
                word = input("   > word : ").strip()
                wdict.searchByWord(word)

            elif command == 'm':
                meaning = input("   > meaning : ").strip()
                wdict.searchByMeaning(meaning)

            elif command == 'q': return
