
class StackApp:
    def convertBase(self, num):
        s = Stack()
        print(num, "is converted into Base 2 : ", end="")
        while(num != 0):
            r = num%2
            s.push(r)
            num = num//2

        while not s.isEmpty():
            print(s.pop(), end="")
        print()

    def checkBrakets(self, expr):
        s = Stack()
        for ch in expr:
            if ch in ("(", "{", "["):
                s.push(ch)
            elif ch in (")", "}", "]"):
                if s.isEmpty():
                    return False
                else:
                    ob = s.pop()
                    # if parentheses do not fit together
                    if (ch == ")" and ob != "(") or (ch == "}"
                        and ob != "{") or (ch == "]" and ob != "["):
                        return False
        return s.isEmpty()
    def infix2Postfix(self, expr):
        s = Stack()
        output =[]

        for term in expr:
            if term == '(':
                s.push(term)
            elif term == ')':
                while not s.isEmpty():
                    op = s.pop()
                    if(op == '('):
                        break
                    output.append(op)
            elif term in "+-*/":
                while not s.isEmpty():
                    op = s.peek()
                    #  if an operator with a higher priority
                    #  than the current operator is at the top of the stack
                    if (self.precedence(term) <= self.precedence(op)):
                        output.append(s.pop())
                    else:
                        break
                s.push(term)
            else: # nums
                output.append(term)
        # Append all remaining elements to output
        while not s.isEmpty():
            output.append(s.pop())

        return output

    def precedence(self, op):
        if op == '(' or op == ')':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return -1

    def evalPostfix(self, expr):
        s = Stack()
        for term in expr:
            if term in "+-*/":
                value1 = s.pop()
                value2 = s.pop()
                if term == '+':
                    s.push(value2 + value1)
                elif term == '-':
                    s.push(value2 - value1)
                elif term == '*':
                    s.push(value2 * value1)
                elif term == '/':
                    s.push(value2 / value1)
            else:
                s.push(float(term))
        return s.pop()

class Stack:
    def __init__(self):
        self.top = []
    def __iter__(self):
        for i in reversed(self.top):
            yield  i
    def __str__(self):
        return str(self.top)
    def __len__(self):
        return len(self.top)
    def __contains__(self, item):
        return item in self.top
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack is empty....")
            exit()
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("Stack is empty....")
            exit()
    def size(self):
        return len(self.top)
    def isEmpty(self):
        return len(self.top) == 0
    def clear(self):
        self.top = []
    def display(self):
        return str(self.top[::1])



