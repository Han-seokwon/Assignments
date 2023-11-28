from Graph import Graph
from queue import PriorityQueue

class DisjointSet:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def makeSet(self, vtx):
        self.parent[vtx] = vtx
        self.rank[vtx] = 0

    def find(self, vtx):
        parent = self.parent[vtx]
        if parent != vtx: # not root node
            parent = self.find(parent)
        return parent # parent == vtx -> vtx is root node

    def union(self, vtx1, vtx2):
        root1 = self.find(vtx1)
        root2 = self.find(vtx2)
        if root1 != root2: # both vtx are not in same set
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1


class MST:
    def mstKruskal(self, G):
        T = Graph(G.isDirected())
        for v in G.getVertexList():
            T.addVertex(v)

        ds = DisjointSet()
        for v in G.getVertexList():
            ds.makeSet(v)

        pq = PriorityQueue()
        for e in G.getEdges():
            pq.put(e)

        while not pq.empty():
            e = pq.get()
            p1 = ds.find(e.getU())
            p2 = ds.find(e.getV())
            if p1 != p2:
                T.addEdge(e)
                ds.union(p1, p2) # ds.union(e.getU(), e.getV())

        return T # graph





