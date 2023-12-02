from queue import PriorityQueue
from Graph import Graph

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
        for edge in G.getEdgeList():
            pq.put(edge)

        while not pq.empty():
            edge = pq.get()
            p1 = ds.find(edge.getU())
            p2 = ds.find(edge.getV())
            if p1 != p2:
                T.addEdge(edge)
                ds.union(p1, p2)
        return T


    def runPrim(self, graph, startVertex):
        T = Graph(graph.isDirected())
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
            T.addEdge(minEdge)
            for edge in graph.getNeighborEdges(vtxV):
                PQ.put(edge)

        return T



class Dijkstra:
    def runDijkstra(self, graph, startVertex):
        known = {} # visited
        Dv = {} # Distance between start Vertex(node)
        Pv ={} # Parent Vertex
        for vtx in graph.getVertexList(): # initialize
            known[vtx] = False
            Dv[vtx] = float("inf")
            Pv[vtx] = None
        known[startVertex] = True
        Dv[startVertex] = 0.0

        PQ = PriorityQueue()
        PQ.put((0, startVertex)) # tuple( distance between start Vertex, current vertex )

        while not PQ.empty():
            self.printConfiguration(known, Dv, Pv)
            edgeMin = PQ.get()[1] # get vertex
            for edge in graph.getNeighborEdges(edgeMin) :
                edgeDistance = edge.getWeight()
                newDistance = Dv[edge.getU()] + edgeDistance
                # 아직 추가가 안 된 vertex이고, 저장된 거리보다 새로운 거리가 가까운 경우
                if( not known[edge.getV()]) and (Dv[edge.getV()] > newDistance) :
                    Dv[edge.getV()] = newDistance # 더 가까운 거리로 바꿈
                    Pv[edge.getV()] = edge.getU()  # 부모 노드를 바꿈 U : start node
                    PQ.put((newDistance, edge.getV())) # 해당 경로 추가
                known[edge.getU()] = True
        self.printConfiguration(known, Dv, Pv)

    def printConfiguration(self, known, Dv, Pv):
        print("\n<Configuration>")
        print("vtx | known | Dv | Pv")
        for vtx in known:
            print("{} | {} | {} | {}".format(vtx, known[vtx], Dv[vtx], Pv[vtx]))






