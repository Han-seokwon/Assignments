
MAX_SIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_SIZE

    def __str__(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front + 1 : self.rear + 1]
        elif self.front > self.rear:
            out = self.items[(self.front + 1) % MAX_SIZE : MAX_SIZE] + self.items[0:self.rear + 1]
        return str(out)

    def __len__(self):
        return (self.rear - self.front + MAX_SIZE) % MAX_SIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_SIZE

    def clear(self):
        self.rear = self.front

    def print(self):
        print("[f={}, r={}] --> ".format(self.front, self.rear), self)

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



















