from queue import Queue, LifoQueue
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

