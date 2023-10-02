from QueueADT import CircularQueue

def useCircularQueue():
    que = CircularQueue()
    for i in range(9):
        que.enqueue(i)
    print("str(queue) : " , que)
    print("que.print() : ", end ="")
    que.print()

    print("que.peek() : " ,que.peek())
    print("que.dequque() : ", que.dequeue())
    print("que.dequque() : ", que.dequeue())
    que.enqueue(20)
    print("que.enqueue(20) ->  ", que)
    que.clear()
    print("que.clear() ->  ", que)

def main():
    useCircularQueue()

if __name__ == "__main__":
    main()
