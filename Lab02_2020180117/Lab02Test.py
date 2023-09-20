from Lab02 import Matrix, EightQueen, TicTacToe

def useMatrix():
    print("m1")
    m1 = Matrix(5, 5, "r")
    m1.mPrint()

    print("m2")
    m2 = Matrix(5, 5, "r")
    m2.mPrint()

    print("m1+m2")
    m = m1+m2
    m.mPrint()

def useEightQueen():
    e1 = EightQueen()
    e1.runEQ(5) # we need 5 solution

def useTicTacToe():
    pass


def main():
    # useMatrix()
    useEightQueen()

if __name__ == "__main__":
    main()