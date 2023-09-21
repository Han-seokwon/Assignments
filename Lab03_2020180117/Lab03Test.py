from Lab03 import Stack, StackApp

def useStack():
    odd = Stack()
    even = Stack()
    for i in range(20):
        if i%2 == 0:
            even.push(i)
        else:
            odd.push(i)
    print("Even Stack : " , even)
    print("Odd Stack : " ,odd)
    print(even.peek())
    print(even.pop())
    print(odd.peek())
    print(odd.pop())
    print("Even Stack : " , even)
    print("Odd Stack : " ,odd)
    print(odd.size())
    print(len(odd))

    for i in odd:
        print(i)

def useStackApp():
    sa = StackApp()
    # converBase()
    # sa.converBase(26)

    # checkBrakets()
    # expr = "sadad(as{f[]sa}f)asf{asf}asfa[aw]"
    # print("Are brakets balanced? ", sa.checkBrakets(expr))

    expr =  "2+(4+3*2+1)/3" #  -> 2432+*1+3/+
    print("Postfix Expression = ", sa.infix2Postfix(expr))

    expr = "2432*+1+3/+"
    print("Postfix Evaluation = ",sa.evalPostfix(expr))


def main():
    # useStack()
    useStackApp()

if __name__ == "__main__":
    main()