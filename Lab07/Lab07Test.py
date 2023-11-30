from GetGraphs import *
from Graph import *
from SearchGraph import *
from  EightQueen import EightQueen
from MinimumSpanningTree import *

def testGrapgh():
    gg = GetGraphs()
    graph = gg.getG1()
    print(graph)
    print(graph.getEdges())
    matrix = graph.getAdjMat()
    for row in matrix:
        print(row)
    graph.printAdjList()


def testSearchGraph():

    graph = GetGraphs().getG1()
    graph.printAdjList()
    adjList = graph.getAdjList()
    start = graph.getVertexList()[0]

    sg = SearchGraph()
    sg.dfs_recursive(adjList, start)
    sg.dfs_loop(adjList, start)
    sg.bfs(adjList, start)

    # EightQueen
    print()
    # eq = EightQueen(8)
    # eq.solve()

    # dfsTS
    print()
    # graph = GetGraphs().getG3()
    # sg.doTS(graph)

    # sg.findCC(adjList)
    GetGraphs().getG4_TestConnectedComponents()

def testMST():
    graph = GetGraphs().getG5()
    print(graph)
    print("graph.getEdges(): ", graph.getEdges())
    print("graph.getSize():" , graph.getSize())

    print("\n========== < Kruskal mst > ==========\n")
    mst =  MST()
    T = mst.mstKruskal(graph)
    print(T)
    print("T.getEdges(): ", T.getEdges())
    print("T.getSize():" , T.getSize())


    print("\n========== < Prim mst > ==========\n")
    g = GetGraphs().getG6()
    startVertex = g.getVertexList()[0]
    T2 = mst.runPrim(g, startVertex)
    print(T2)
    print("T2.getEdges(): ",T2.getEdges())
    print("T2.getSize(): ",T2.getSize())



def testDijstra():
    g = GetGraphs().getG6()
    print(g)
    startVertex = g.getVertexList()[0]
    dk = Dijkstra()
    dk.runDijkstra(g, startVertex)


def main():
    # testGrapgh()
    # testSearchGraph()
    testMST()
    # testDijstra()

if __name__ == "__main__":
    main()