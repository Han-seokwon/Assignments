from Lab03 import Stack, StackApp
"""
Name : Han Seokwon
Student ID : 2020180117
Description :  This module test the Classes defined in Lab03 Module
"""
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
    print("Even Stack peek() : ", even.peek())
    print("Even Stack pop() : ", even.pop())
    print("Even Stack len() : ", len(odd))

    print("Odd Stack peek() : ", odd.peek())
    print("Odd Stack pop() : ", odd.pop())
    print("Odd Stack size() : ", odd.size())
    print("Odd Stack iter() Test: ", end="")
    for i in odd: # __iter__ test
        print(i, end=", ")

def useStackApp():
    sa = StackApp()

    # convertBase() test
    sa.convertBase(26)


    # checkBrakets() test
    expr = "sadad(as{f[]sa}f)asf{asf}asfa[aw]"
    print(expr)
    print("Are brakets balanced? ", sa.checkBrakets(expr))

    # infix2Postfix() test
    expr =  "2+(4+3*2+1)/3" # =  2432+*1+3/+
    print("Postfix Expression = ", sa.infix2Postfix(expr))

    # evalPostfix() test
    expr = "2432*+1+3/+"
    print("Postfix Evaluation = {:.2f}".format(sa.evalPostfix(expr)))


def main():
    # useStack()
    useStackApp()

if __name__ == "__main__":
    main()