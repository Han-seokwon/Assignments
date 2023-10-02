
MAX_SIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_SIZE

    def __str__(self):
        out = []
        front = (self.front + 1) % MAX_SIZE
        rear =  (self.rear + 1) % MAX_SIZE
        if front < rear:
            out = self.items[front : rear]
        elif front > rear:
            out = self.items[front : MAX_SIZE] + self.items[0:rear]
        return "[f={}, r={}] --> ".format(self.front, self.rear) + str(out)

    def __len__(self):
        return (self.rear - self.front + MAX_SIZE) % MAX_SIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_SIZE

    def clear(self):
        self.rear = self.front

    def print(self):
        print(self)

    def peek(self):
        return self.items[(self.front + 1) % MAX_SIZE]

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_SIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_SIZE
            return self.items[self.front]


class CircularDequeue(CircularQueue):
    def __init__(self):
        super().__init__()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front - 1 + MAX_SIZE) % MAX_SIZE

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = ((self.rear - 1) + MAX_SIZE) % MAX_SIZE
            return item
    def getFront(self):
        return self.peek()

    def getRear(self):
        return self.items[self.rear]


















