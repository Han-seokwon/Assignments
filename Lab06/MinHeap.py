class MinHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)
    def __str__(self):
        return str(self.heap)

    def getParent(self, i): return self.heap[i//2]
    def getLeft(self, i ): return self.heap[i*2]
    def getRight(self, i): return self.heap[i*2+1]
    def getSize(self): return len(self.heap) - 1
    def isEmpty(self): return self.getSize() == 0

    def insert(self, n):
        self.heap.append(n)
        i = self.getSize()
        while i > 1 and n < self.getParent(i): # min heap, smaller node should go up
            self.heap[i] = self.getParent(i) # precolate up (switch pos with parent)
            i = i//2
        self.heap[i] = n

    def delete(self): # delete root node
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.getSize()]
            while child <= self.getSize() : # precolate down
                if child < self.getSize() and self.getLeft(parent) > self.getRight(parent) :
                    # if current node(child) == size == last node there is no left, right child
                    child += 1 # move to smaller(right) node
                if last <= self.heap[child]: # last is smaller than child(comparing) node stop
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2 # move to child
            self.heap[parent] = last # last node is moved to parent position
            self.heap.pop(-1)
            return hroot # delete hroot

    def printHeap(self):
        level = 1
        for i in range(1, self.getSize() + 1):
            if i == level:
                print('') # line break for each level
                level *= 2
            print(str(self.heap[i]), end =' ')
        print("\n-------------------")
