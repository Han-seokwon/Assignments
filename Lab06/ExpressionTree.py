from BinaryTree import *
from queue import LifoQueue
class ExpressionTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root=root)

    def isOperator(self, c):
        if( c == '+' or c == '-' or c == '*' or
            c == '/' or c == '^' ):
            return True
        else:
            return False

    def constructTree(self, postfix):
        stack = LifoQueue()

        # Traverse through every character of input expression
        for char in postfix:
            # if operand, simply push into stack
            if not self.isOperator(char):
                n = BinaryNode(char)
                stack.put(n)
            else: # operator
                n = BinaryNode(char)# operator

                # pop two top nodes
                n1 = stack.get()
                n2 = stack.get()

                # make them children
                n.setRight(n1)
                n.setLeft(n2)

                # add this subexpression to stack
                stack.put(n)

        # only element will be the root of expression tree
        root = stack.get()
        return root

    def evaluateExpressionTree(self, node):
        if node is not None:
            t = node.data
            if not self.isOperator(t):
                return t
            else:
                a = int(self.evaluateExpressionTree(node.getLeft()))
                b = int(self.evaluateExpressionTree(node.getRight()))
                if t == "+":
                    return a + b
                elif t == '-':
                    return a - b
                elif t == '*':
                    return a * b
                elif t == '/':
                    return a / b







