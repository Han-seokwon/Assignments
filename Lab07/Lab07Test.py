from GetGraphs import *
from SearchGraph import *
from EightQueen import EightQueen
from MinimumSpanningTree import MST, Dijkstra

def testGrapgh():
    gg = GetGraphs()

    print("\n<Graph01>")
    graph1 = gg.getG1()
    print(graph1)
    graph1.printAdjList()
    graph1.printAdjMatrix()
    print("Graph01 size : " , graph1.getSize())
    print("Graph01 order : ", graph1.getOrder())
    A = graph1.getVertexList()[0]
    print("Graph01 degree of A : ", graph1.getDegree(A))

    print("\n<Graph02>")
    graph2 = gg.getG2()
    print(graph2)
    graph2.printAdjList()
    graph2.printAdjMatrix()
    print("Graph02 size : " , graph2.getSize())
    print("Graph02 order : ", graph2.getOrder())
    v1 = graph2.getVertexList()[0]
    print("Graph02 degree of v1: ", graph2.getDegree(v1))

    print("\n<Graph03>")
    graph3 = gg.getG3()
    print(graph3)
    graph3.printAdjList()
    graph3.printAdjMatrix()
    print("Graph03 size : " , graph3.getSize())
    print("Graph03 order : ", graph3.getOrder())
    v1 = graph3.getVertexList()[0]
    print("Graph03 degree of v1: ", graph3.getDegree(v1))


def testSearchGraph():
    sg = SearchGraph()

    print("\n<Graph01>")
    graph1 = GetGraphs().getG1()
    adjList = graph1.getAdjList()
    start = graph1.getVertexList()[0]
    print("DFS(recursive) start with Vertex ", start)
    sg.dfs_recursive(adjList, start, set())
    sg.dfs_loop(adjList, start)
    sg.bfs(adjList, start)


    print("\n\n<Graph02>")
    graph2 = GetGraphs().getG2()
    adjList = graph2.getAdjList()
    start = graph2.getVertexList()[0]
    print("DFS(recursive) start with Vertex ", start)
    sg.dfs_recursive(adjList, start, set())
    sg.dfs_loop(adjList, start)
    sg.bfs(adjList, start)


    print("\n\n<Graph03>")
    graph3 = GetGraphs().getG3()
    adjList = graph3.getAdjList()
    start = graph3.getVertexList()[0]
    print("DFS(recursive) start with Vertex ", start)
    sg.dfs_recursive(adjList, start, set())
    sg.dfs_loop(adjList, start)
    sg.bfs(adjList, start)

    GetGraphs().getG4_TestConnectedComponents()

    # dfsTS
    print("\n<Graph03 Topological Sort >")
    graph3 = GetGraphs().getG3()
    sg.doTS(graph3)

    print("\n<Graph05 Topological Sort>")
    graph5 = GetGraphs().getG5()
    sg.doTS(graph5)

    # EightQueen
    print()
    eq = EightQueen(6)
    eq.solve()


def testMST():
    graph = GetGraphs().getG2()
    print(graph)
    # print("graph.getEdges(): ", graph.getEdgeList())
    print("graph.getSize():" , graph.getSize())

    print("\n========== < Kruskal mst > ==========\n")
    mst =  MST()
    T = mst.mstKruskal(graph)
    print(T)
    T.printAdjList()
    print("T.getSize():" , T.getSize())


    print("\n========== < Prim mst > ==========\n")
    g = GetGraphs().getG2()
    startVertex = g.getVertexList()[0]
    T2 = mst.runPrim(g, startVertex)
    print(T2)
    T2.printAdjList()
    print("T2.getSize(): ",T2.getSize())



def testDijstra():
    g = GetGraphs().getG3()
    print(g)
    startVertex = g.getVertexList()[0]
    dk = Dijkstra()
    dk.runDijkstra(g, startVertex)


def main():
    testGrapgh()
    # testSearchGraph()
    # testMST()
    # testDijstra()

if __name__ == "__main__":
    main()