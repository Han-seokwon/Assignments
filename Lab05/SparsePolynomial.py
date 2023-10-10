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


    def add(self, B):
        result_Poly = copy.deepcopy(self) # copy self Poly to result Poly
        aNode = result_Poly.head
        bNode = B.head
        idx = 0
        while bNode is not None:
            aTerm = aNode.data
            bTerm = bNode.data
            if(aTerm.expon < bTerm.expon):
                aNode = aNode.next
                idx += 1
                continue
            elif(aTerm.expon > bTerm.expon):
                result_Poly.addAt(idx, bTerm)
            else: # aTerm.expon == bTerm.expon
                coeff = float(aTerm.sign + str(aTerm.coeff)) + float(bTerm.sign + str(bTerm.coeff))
                if coeff == 0:
                    result_Poly.deleteAt(idx) # delete node if coeff is 0
                else:
                    aNode.data.coeff = coeff
            bNode = bNode.next
        return result_Poly

    def sub(self, B):
        B_temp = copy.deepcopy(B) # copy B Poly to temp Poly
        temp = B_temp.head
        while temp is not None:
            temp.data.sign = '+' if temp.data.sign == '-' else '-' # change sign
            temp = temp.next
        return self.add(B_temp)

    def getDegree(self): # return highest exponential
        temp = self.head
        max_degree = temp.data.expon
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
        while True:
            token = input("input term (syn coef expon): ").strip().split(" ")
            if token[0] == '-1':
                self.display("The Polynomial: ")
                return 0
            else:
                try:
                    self.addAt(self.getSize(), Term(token[0], float(token[1]), int(token[2])))
                except:
                    print("Invaild Input : " , token)






