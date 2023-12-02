from collections import OrderedDict

class Edge:
    def __init__(self, u=None, v=None, weight=None):
        self.u = u
        self.v = v
        self.weight = weight
    def getU(self):
        return self.u
    def getV(self):
        return self.v
    def getWeight(self):
        return self.weight
    def __str__(self):
        return "({}, {}) -> {} ".format(self.u, self.v, self.weight)
    def __repr__(self):
        return "({}, {}) -> {} ".format(self.u, self.v, self.weight)
    def __hash__(self):
        return hash(self.weight)
    def __eq__(self, other):
        return self.weight == other.weight
    def __ne__(self, other):
        return self.weight != other.weight
    def __lt__(self, other):
        return self.weight < other.weight
    def __le__(self, other):
        return self.weight <= other.weight
    def __gt__(self, other):
        return self.weight > other.weight
    def __ge__(self, other):
        return self.weight >= other.weight


class Vertex: # Node
    def __init__(self, key=None):
        self.key = key
    def __str__(self):
        return str(self.key)
    def __repr__(self):
        return str(self.key)
    def setData(self, key):
        self.key = key
    def getData(self, key):
        return self.key
    def __hash__(self):
        return hash(self.key)
    def __eq__(self, other):
        return self.key == other.key
    def __ne__(self, other):
        return self.key != other.key
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self, other):
        return self.key <= other.key
    def __gt__(self, other):
        return self.key > other.key
    def __ge__(self, other):
        return self.key >= other.key

class Graph:
    def __init__(self, directed=False, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        self.directed = directed
        self.keyIndex = {} # vertex list

    def __repr__(self):
        gs = ""
        for vtx in self.gdict:
            gs += "{} : {}\n".format(vtx, self.gdict[vtx])
        return gs

    def __str__(self):
        gs = ""
        for vtx in self.gdict:
            gs += "{} : {}\n".format(vtx, self.gdict[vtx])
        return gs

    def isDirected(self):
        return self.directed

    def addVertex(self, vtx):
        if vtx in self.gdict:
            print("Vertex is already addedd...")
        else:
            self.gdict[vtx] = []  # vtx is key of gdict
            self.keyIndex[vtx] = len(self.keyIndex) + 1

    def addEdge(self, edge):
        if edge.getU() in self.gdict:
            self.gdict[edge.getU()].append(edge)  # add edge to vtx
        if not self.directed:
            edge2 = Edge(edge.getV(), edge.getU(), edge.getWeight())
            self.gdict[edge2.getU()].append(edge2)
        # else:
        #     print("matching vertex not found...")

    def getNeighborVertices(self, vtx):
        edgeList = self.gdict.get(vtx)
        nlist = []  # neighbor vtx list
        for edge in edgeList:
            nlist.append(edge.getV())
        return nlist

    def getNeighborEdges(self, vtx):
        return self.gdict[vtx]

    def getVertexList(self):
        orderedVertexList = OrderedDict(sorted(self.keyIndex.items()))
        return list(orderedVertexList.keys())

    def getEdgeList(self):
        edgeList = []
        for vtx in self.gdict:
            for edge in self.gdict[vtx]:
                edgeList.append(edge)
        return edgeList

    def getAdjList(self):
        alist = {}
        for vtx in self.gdict:
            alist[vtx] = set(self.getNeighborVertices(vtx))
        return alist

    def printAdjList(self):
        print("\nAdjacency List")
        alist = self.getAdjList()  # actually it's set not list
        for vtx in alist:
            print("{} : {}".format(vtx, alist[vtx]))

    def getAdjMatrix(self):
        vtxCnt = len(self.keyIndex)
        adjMat = [[0 for x in range(vtxCnt)] for y in range(vtxCnt)]
        for edge in self.getEdgeList():
            uIdx = self.keyIndex[edge.getU()] - 1
            vIdx = self.keyIndex[edge.getV()] - 1
            adjMat[uIdx][vIdx] = edge.getWeight()
        return adjMat

    def printAdjMatrix(self):
        print("\nAdjacency Matrix")
        adjMatrix = self.getAdjMatrix()
        for i in range(0, len(self.keyIndex)):
            print()
            for j in range(0, len(self.keyIndex)):
                print(" {0:>2d}".format(adjMatrix[i][j]), end="")
        print("\n")


    def getOrder(self): # number of vertices
        return len(self.keyIndex)

    def getSize(self): # number of edges
        size = len(self.getEdgeList())
        if not self.isDirected():
            size = size // 2
        return size

    def getDegree(self, vtx):
        return self.getOutDegree(vtx) + self.getInDegree(vtx)
    def getOutDegree(self, vtx):
        return len(self.gdict[vtx])
    def printOutDegree(self):
        for vtx in self.gdict:
            print("Out degree of vertex {} = {}".format(vtx, self.getOutDegree(vtx)))
    def getInDegree(self, vtx):
        return len(self.getInwardEdges(vtx))

    def getInwardEdges(self, vtx):
        edgeList = []
        for edge in self.getEdgeList():
            if vtx == edge.getV():
                edgeList.append(edge)
        return edgeList

    def printInDegree(self):
        for vtx in self.gdict:
            print("In degree of vertex {} = {}".format(vtx, self.getInDegree(vtx)))

    def getWeight(self):
        totalWeight = 0
        for edge in self.getEdgeList():
            totalWeight += edge.getWeight()

        if not self.isDirected():
            totalWeight = totalWeight // 2
        return totalWeight

    def isCycle(self):
        ds = DisjointSet()
        for vtx in self.getVertexList():
            ds.makeSet(vtx)

        for edge in self.getEdgeList():
            x = ds.find(edge.getU())
            y = ds.find(edge.getV())
            if(x != y):
                ds.union(x, y)
            else:
                return True
        return False


















