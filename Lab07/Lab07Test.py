
from GetGraphs import *
from Graph import *
from SearchGraph import *

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
    adjList = graph.getAdjList()
    start = graph.getVertexList()[0]
    sg = SearchGraph()
    sg.dfs_recursive(adjList, start)
    sg.dfs_loop(adjList, start)
    sg.bfs(adjList, start)


def main():
    # testGrapgh()
    testSearchGraph()

if __name__ == "__main__":
    main()