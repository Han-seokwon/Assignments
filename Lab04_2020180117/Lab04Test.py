MAX_SIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0;
        self.items = [] * MAX_SIZE
    def __str__(self):
        pass
    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_SIZE

    def size(self):
        return (self.rear - self.front + MAX_SIZE) % MAX_SIZE

    def display(self):
        out = []
        if self.front < self.row:
            out = self.items[self.front + 1 : self.rear + 1]
        else:
            out = self.items[(self.front + 1)%MAX_SIZE  : MAX_SIZE]

    def peek(self):
        return self.items[(self.front+1)%MAX_SIZE]
    def enqueue(self, item):
        if not self.isEmpty():
            self.rear = (self.rear + 1)%self.MAX_SIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_SIZE
            return self.items[self.front]

    def clear(self):
        self.rear = self.front

class CircularDequeue(CircularQueue):
    def __init__(self):
        super().__init__()



















