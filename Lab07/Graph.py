
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
        if gdict == None:
            gdict = {}
        self.gdict = gdict
        self.Directed = directed # 방향이 있는 그래프인지 정하는 필드
        self.keyIndex = {}

    def __str__(self):
        gs = ""
        for vtx in self.gdict:
            gs += "{} : {}\n".format(vtx, self.gdict[vtx])
        return gs

    def getOrder(self):
        pass
    def getSize(self): # use number of edges
        pass
    def getVertexDegree(self):
        pass
    def getDegree(self):
        pass

    def getNeighbors(self, vtx):
        nlist = [] # neighbor list
        edgeList = self.gdict.get(vtx)
        for e in edgeList:
            nlist.append(e.getV)
        return nlist

    def getAdjList(self):
        alist = {}
        for vtx in self.gdict:
            alist[vtx] = set( self.getNeighbors(vtx))
        return alist

    def printAdjList(self):
        alist = self.getAdjList() # actually it's set not list
        for vtx in alist:
            print("{} : {}".format(vtx, alist[vtx]))

    def addVertex(self, vtx):
        if vtx in self.gdict:
            print("Vertex is already addedd...")
        else:
            self.gdict[vtx] = [] # vtx is key of dict
            self.keyIndex[vtx] = len(self.keyIndex) + 1

    def addEdge(self, edge):
        # if edge.getU() in self.gdict:
        self.gdict[edge.getU()].append(edge)
        if not self.Directed:
            edge2 = Edge(edge.getV(), edge.getU(), edge.getWeight())
            self.gdict[edge.getV()].append(edge2)
            # self.gdict[e2.getU()].append(e2)

    def getAdjMat(self):
        length = len(self.keyIndex)
        adjMat = [[0 for x in range(length)] for y in range(length)]
        for e in self.getEdges():
            uIdx = self.keyIndex[e.getU()] - 1
            vIdx = self.keyIndex[e.getV()] - 1
            adjMat[uIdx][vIdx] = e.getWeight()
        return adjMat

    def getEdges(self):
        edgeList = []
        for vtx in self.gdict:
            for e in self.gdict[vtx]:
                edgeList.append(e)
        return edgeList




















