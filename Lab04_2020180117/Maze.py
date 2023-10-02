from QueueADT import *
from Stack import Stack

class Cell:
    def __init__(self, r, c):
        self.row = r
        self.col = c
    def __str__(self):
        return '(' + str(self.row) + ", "+ str(self.col) + ")"

class Maze:
    MAZE_SIZE = 6
    def getMap(self):
        map = [['e', '1', '1', '1', '1', '1'],
               ['0', '1', '1', '0', '0', '0'],
               ['0', '1', '1', '0', '1', '1'],
               ['0', '0', '0', '0', '1', '1'],
               ['1', '0', '1', '0', '0', '0'],
               ['1', '0', '1', '1', '1', 'x']]
        return map

    def printMap(self, map):
        print()
        for row in map:
            print(row)

    def isValidPos(self, x, y, map):
        if(x < 0 or y < 0 or x >= self.MAZE_SIZE or y >= self.MAZE_SIZE):
            return False
        else:
            # not blocked or 'x' goal point
            return map[y][x] == '0' or map[y][x] == 'x'



    def DFS1(self): # Using CircularDequeue as a Stack (front end operations)
        map = self.getMap()
        deq = CircularDequeue()
        entry = Cell(0,0)
        deq.addFront(entry)
        print("\n DFS1 : using Dequeue Data Structure: ")

        while not deq.isEmpty():
            here = deq.deleteFront()
            print(here, end=" -> ")
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): # Finished
                self.printMap(map)
                return True
            else:
                map[y][x] = '.' # point that we passed
                if self.isValidPos(x, y - 1, map): deq.addFront(Cell(x, y - 1))  # up
                if self.isValidPos(x, y + 1, map): deq.addFront(Cell(x, y + 1)) # down
                if self.isValidPos(x - 1, y, map): deq.addFront(Cell(x - 1, y)) # left
                if self.isValidPos(x + 1, y, map): deq.addFront(Cell(x + 1 , y)) # right

        # There are no path to exit
        self.printMap(map)
        return False

    def DFS2(self): # Using  Stack
        map = self.getMap()
        stack = Stack()
        entry = Cell(0,0)
        stack.push(entry)
        print("\n DFS2 : using Stack Data Structure: ")

        while not stack.isEmpty():
            here = stack.pop()
            print(here, end=" -> ")
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): # Finished
                self.printMap(map)
                return True
            else:
                map[y][x] = '.' # point that we passed
                if self.isValidPos(x, y - 1, map): stack.push(Cell(x, y - 1))  # up
                if self.isValidPos(x, y + 1, map): stack.push(Cell(x, y + 1)) # down
                if self.isValidPos(x - 1, y, map): stack.push(Cell(x - 1, y)) # left
                if self.isValidPos(x + 1, y, map): stack.push(Cell(x + 1 , y)) # right

        # There are no path to exit
        self.printMap(map)
        return False

    def DFS3(self): # Using CircularDequeue as a Stack (rear end operations)
        map = self.getMap()
        deq = CircularDequeue()
        entry = Cell(0,0)
        deq.addRear(entry)
        print("\n DFS1 : using Dequeue Data Structure: ")

        while not deq.isEmpty():
            here = deq.deleteRear()
            print(here, end=" -> ")
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): # Finished
                self.printMap(map)
                return True
            else:
                map[y][x] = '.' # point that we passed
                if self.isValidPos(x, y - 1, map): deq.addRear(Cell(x, y - 1))  # up
                if self.isValidPos(x, y + 1, map): deq.addRear(Cell(x, y + 1)) # down
                if self.isValidPos(x - 1, y, map): deq.addRear(Cell(x - 1, y)) # left
                if self.isValidPos(x + 1, y, map): deq.addRear(Cell(x + 1 , y)) # right

        # There are no path to exit
        self.printMap(map)
        return False

    def BFS1(self): # Using CircularDequeue
        map = self.getMap()
        deq = CircularDequeue()
        entry = Cell(0,0)
        deq.addRear(entry)
        print("\n BFS1 : using Dequeue Data Structure: ")

        while not deq.isEmpty():
            here = deq.deleteFront()
            print(here, end=" -> ")
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): # Finished
                self.printMap(map)
                return True
            else:
                map[y][x] = '.' # point that we passed
                if self.isValidPos(x, y - 1, map): deq.addRear(Cell(x, y - 1))  # up
                if self.isValidPos(x, y + 1, map): deq.addRear(Cell(x, y + 1)) # down
                if self.isValidPos(x - 1, y, map): deq.addRear(Cell(x - 1, y)) # left
                if self.isValidPos(x + 1, y, map): deq.addRear(Cell(x + 1 , y)) # right

        # There are no path to exit
        self.printMap(map)
        return False


    def BFS2(self): # Using CircularQueue
        map = self.getMap()
        deq = CircularQueue()
        entry = Cell(0,0)
        deq.enqueue(entry)
        print("\n BFS2 : using Queue Data Structure: ")

        while not deq.isEmpty():
            here = deq.dequeue()
            print(here, end=" -> ")
            x = here.row
            y = here.col
            if(map[y][x] == 'x'): # Finished
                self.printMap(map)
                return True
            else:
                map[y][x] = '.' # point that we passed
                if self.isValidPos(x, y - 1, map): deq.enqueue(Cell(x, y - 1))  # up
                if self.isValidPos(x, y + 1, map): deq.enqueue(Cell(x, y + 1)) # down
                if self.isValidPos(x - 1, y, map): deq.enqueue(Cell(x - 1, y)) # left
                if self.isValidPos(x + 1, y, map): deq.enqueue(Cell(x + 1 , y)) # right

        # There are no path to exit
        self.printMap(map)
        return False