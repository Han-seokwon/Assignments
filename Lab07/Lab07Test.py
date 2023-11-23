from GetGraphs import *
from Graph import *
from SearchGraph import *
from  EightQueen import EightQueen
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



def main():
    # testGrapgh()
    testSearchGraph()

if __name__ == "__main__":
    main()