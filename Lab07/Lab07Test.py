
from GetGraphs import *
from Graph import *

def testGrapgh():
    gg = GetGraphs()
    graph = gg.getG1()
    print(graph)
    print(graph.getEdges())
    matrix = graph.getAdjMat()
    for row in matrix:
        print(row)

def main():
    testGrapgh()

if __name__ == "__main__":
    main()