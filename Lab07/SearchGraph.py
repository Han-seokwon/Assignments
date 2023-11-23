from queue import Queue, LifoQueue
from Graph import Graph
from collections import defaultdict

class SearchGraph:
    def dfs_recursive(self, adjList, start, visited=set()):
        if start not in visited:
            visited.add(start)
            print(start, end=" -> ")
            for next in adjList[start] - visited:
                self.dfs_recursive(adjList, next, visited)

    def dfs_loop(self, adjList, start):
        visited = set()
        print("\nDFS(loop) start with Vertex ", start)
        visited.add(start)
        stack = LifoQueue()
        stack.put(start)
        while not stack.empty():
            v = stack.get()
            print(v, end = " -> ")
            neighbors  = adjList[v]
            for u in neighbors:
                if u not in visited:
                    visited.add(u)
                    stack.put(u)


    def bfs(self, adjList, start):
        visited = set()
        print("\nBFS start with Vertex ", start)
        visited.add(start)
        queue = Queue()
        queue.put(start)
        while not queue.empty():
            v = queue.get()
            print(v, end = " -> ")
            neighbors = adjList[v]
            for u in neighbors:
                if u not in visited:
                    visited.add(u)
                    queue.put(u)

    def doTS(self, g):
        adjList = g.getAdjList()
        visited = defaultdict() # { key : vtx, value : bool }
        for vtx in adjList:
            visited[vtx] = False

        result = []
        for v in visited:
            self.dfsTS(v, adjList, visited, result)
        print(result)

    def dfsTS(self, v, adjList, visited, result):
        if not visited[v]:
            visited[v] = True
            for neighbor in adjList[v]:
                self.dfsTS(neighbor,  adjList, visited, result)
            result.insert(0, v)
    def findCC(self, adjList): # Connected Components
        visited = set()
        colorList = []
        for vtx in adjList:
            if vtx not in visited:
                color = self.dfsCC(adjList, [], vtx, visited)
                colorList.append(color)
        print("Connected Components = {}".format(len(colorList)))
        print("colorList : " , colorList)

    def dfsCC(self, adjList, color, vtx, visited ):
        if vtx not in visited:
            visited.add(vtx)
            color.append(vtx)
            neighbor = adjList[vtx]
            for vtx in neighbor:
                if vtx not in visited:
                    self.dfsCC(adjList, color, vtx, visited )
        return color