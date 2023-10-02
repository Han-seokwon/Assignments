class Stack:
    def __init__(self):
        self.top = []
    def __iter__(self):
        for i in reversed(self.top):
            yield  i
    def __str__(self):
        return str(self.top)
    def __len__(self):
        return len(self.top)
    def __contains__(self, item):
        return item in self.top
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack is empty....")
            exit()
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("Stack is empty....")
            exit()
    def size(self):
        return len(self.top)
    def isEmpty(self):
        return len(self.top) == 0
    def clear(self):
        self.top = []
    def display(self):
        return str(self.top[::1])



