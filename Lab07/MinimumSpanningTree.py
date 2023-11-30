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


    def runPrim(self, graph, startVertex):
        T = Graph(graph.isDirected())
        eList = []
        PQ = PriorityQueue()

        for edge in graph.getNeighborEdges(startVertex):
            PQ.put(edge)
        T.addVertex(startVertex)

        while T.getOrder() != graph.getOrder(): # number of vertices
            minEdge = PQ.get()
            vtxV = minEdge.getV()
            if vtxV in T.getVertexList():
                continue
            #else
            T.addVertex(vtxV)
            eList.append(minEdge)
            for edge in graph.getNeighborEdges(vtxV):
                PQ.put(edge)

        # for edge in eList:
        #     print(edge)
        return T



class Dijkstra:
    def runDijkstra(self, graph, startVertex):
        known = {}
        Dv = {} # distance between start node
        Pv ={}
        for vtx in graph.getVertexList(): # initialize
            known[vtx] = False
            Dv[vtx] = float("inf")
            Pv[vtx] = None
        known[startVertex] = True
        Dv[startVertex] = 0.0

        PQ = PriorityQueue()
        PQ.put((0, startVertex)) # 튜플( 거리, vertex )

        while not PQ.empty():
            self.printConfiguration(known, Dv, Pv)
            emin = PQ.get()[1]
            for e in graph.getNeighborEdges(emin) :
                EdgeDistance = e.getWeight()
                newDistance = Dv[e.getU()] + EdgeDistance
                # 아직 추가가 안 된 vertex이고, 저장된 거리보다 새로운 거리가 가까운 경우
                if( not known[e.getV()]) and (Dv[e.getV()] > newDistance) :
                    Dv[e.getV()] = newDistance # 더 가까운 거리로 바꿈
                    Pv[e.getV()] = e.getU()  # 부모 노드를 바꿈 U : start node
                    PQ.put(newDistance, e.getV()) # 튜플 업데이트

                known[e.getU] = True

    def printConfiguration(self, known, Dv, Pv):
        print("Configuration")
        print("vtx, known, Dv, Pv")
        for vtx in known:
            print("{}, {}, {}, {}".format(vtx, known[vtx], Dv[vtx], Pv[vtx]))

    def printConfiguration(self, known, Dv, Pv):
        pass\




