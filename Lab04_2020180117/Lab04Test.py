from QueueADT import *
from TCS import *
from Maze import *

def useCircularQueue():
    print("\n<< Test CircularQueue >>")
    que = CircularQueue()
    for i in range(9):
        que.enqueue(i)
    print("str(que) : " , que)
    print("que.print() : ", end ="")
    que.print()
    print("len(que) : ", len(que))

    print("que.peek() : " ,que.peek())
    print("que.dequque() : ", que.dequeue())
    print("que.dequque() : ", que.dequeue())
    que.enqueue(20)
    print("que.enqueue(20) ->  ", que)
    que.clear()
    print("que.clear() ->  ", que)

def useCircularDequeue():
    print("\n<< Test CircularDequeue >>")
    deque = CircularDequeue()
    for i in range(9):
        deque.addRear(i)

    print("str(deque) : " , deque)
    print("deque.print() : ", end ="")
    deque.print()
    print("len(deque) : ", len(deque))

    print("deque.getFront() : " ,deque.getFront())
    print("deque.getRear() : ", deque.getRear())
    print("deque.deleteFront() : ", deque.deleteFront())
    print("deque.deleteFront() : ", deque.deleteRear())
    print(deque)

    deque.addFront(20)
    print("deque.addFront(20)  ->  ", deque)
    deque.addFront(100)
    print("deque.addFront(100) -> ", deque)

    deque.clear()
    print("deque.clear() ->  ", deque)


def runSimulation():
    print("<< Test TicketCounterSimulation >>")
    numAgents = 3
    numMinutes = 10
    betweenTime = 1
    serviceTime = 3
    print("numAgents : {}, numMinutes: {}, betweenTime : {}, serviceTime : {} ".format(
        numAgents, numMinutes, betweenTime, serviceTime))
    simul = TicketCounterSimulation( numAgents, numMinutes, betweenTime, serviceTime)
    simul.run()
def useMaze():
    maze = Maze()
    maze.DFS1()
    maze.DFS2()
    maze.DFS3()

    maze.BFS1()
    maze.BFS2()


def main():
    # useCircularQueue()
    # useCircularDequeue()
    # runSimulation()
    useMaze()

if __name__ == "__main__":
    main()
