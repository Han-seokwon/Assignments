

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = []

    def __str__(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def peek(self):
        return self.items[0]

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)