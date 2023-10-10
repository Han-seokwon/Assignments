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
        result_Poly = copy.deepcopy(self) # copy this Poly to result Poly
        aNode = result_Poly.head
        bNode = B.head
        idx = 0 # result_Poly index
        while bNode is not None:
            aTerm = aNode.data
            bTerm = bNode.data
            if(aTerm.expon < bTerm.expon):
                aNode = aNode.next
                idx += 1
            elif(aTerm.expon > bTerm.expon):
                result_Poly.addAt(idx, bTerm)
                bNode = bNode.next
                idx += 1
            else: # aTerm.expon == bTerm.expon
                result = float(aTerm.sign + str(aTerm.coeff)) + float(bTerm.sign + str(bTerm.coeff))
                if result > 0 : # positive
                    aTerm.sign = '+'  # change sign
                    aTerm.coeff = result
                elif result < 0 : # negative
                    aTerm.sign = '-' # change sign
                    aTerm.coeff = abs(result)
                else: # delete node if coeff is 0
                    result_Poly.deleteAt(idx)
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






