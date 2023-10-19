from DoublyLinkedList import *
import copy

class Term:
    def __init__(self, sign=None, coeff=None,  expon=None):
        self.sign = sign
        self.coeff = coeff
        self.expon = expon
    def __str__(self):
        return str(self.sign) + str(self.coeff) + "x^"+ str(self.expon) + ' '
    def getCoeff(self):
        return self.coeff
    def getExpon(self):
        return self.expon
    def getSign(self):
        return self.sign


class SparsePolynomial(DoublyLinkedList):
    def __init__(self):
        super().__init__()
    def getDegree(self): # return highest exponential
        max_degree = self.head.expon
        temp = self.head
        while temp is not None:
            if temp.data.expon > max_degree:
                max_degree = temp.data.expon
            temp = temp.next
        return max_degree

    def display(self, msg=""):
        print("\t", msg, end="")
        node = self.head
        while node is not None:
            print(node, end="")
            node = node.getNext()
        print()

    def read(self):
        self.clear()
        tokenList = []
        while True:
            token = input("input term (syn coef expon): ").strip().split(" ")
            if token[0] == '-1':
                # Sorted by exponent in case the user entered by mixing the exponent
                tokenList = sorted(tokenList, key=lambda term : term.expon, reverse=True)
                for i in range(len(tokenList)):
                    self.addFront(tokenList[i])
                self.display("The Polynomial: ")
                return 0
            else:
                try:
                    tokenList.append(Term(token[0], float(token[1]), int(token[2])))
                except:
                    print("Invaild Input : " , token)

    def add(self, B):
        # Each term in A and B is arranged in ascending order by exponent
        # Added term of A and B to "result_Poly" according to exponential order
        result_Poly = SparsePolynomial()
        aNode = self.head
        bNode = B.head
        while aNode is not None or bNode is not None:
            if aNode is None: # Add all remaining nodes in B to 'result_Poly'
                while bNode:
                    result_Poly.addRear(bNode.data)
                    bNode = bNode.next
                break
            if bNode is None: # Add all remaining nodes in A to 'result_Poly'
                while aNode:
                    result_Poly.addRear(aNode.data)
                    aNode = aNode.next
                break
            a_term = aNode.data
            b_term = bNode.data
            # Add data of Node with smaller exponent to 'result_Poly'
            if a_term.expon < b_term.expon:
                result_Poly.addRear(aNode.data)
                aNode = aNode.next
            elif a_term.expon > b_term.expon:
                result_Poly.addRear(bNode.data)
                bNode = bNode.next
            else: # a_term.expon == b_term.expon
                result_coeff = float(a_term.sign + str(a_term.coeff)) + float(b_term.sign + str(b_term.coeff))
                if result_coeff > 0 : # positive
                    result_Poly.addRear(Term("+" , result_coeff, a_term.expon))
                elif result_coeff < 0 : # negative
                    result_Poly.addRear(Term("-" , abs(result_coeff), a_term.expon))
                # If the coefficient is zero, do not add it to 'result_Poly'
                aNode = aNode.next
                bNode = bNode.next
        return result_Poly


    def sub(self, B):
        B_temp = copy.deepcopy(B) # copy B Poly to temp Poly
        temp = B_temp.head
        while temp is not None:
            temp.data.sign = '+' if temp.data.sign == '-' else '-' # change sign
            temp = temp.next
        return self.add(B_temp)








