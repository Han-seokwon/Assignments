from Lab02 import Matrix, EightQueen, TicTacToe

def useMatrix():
    print("m1")
    m1 = Matrix(5, 5, "r")

    print("str() : \n" , m1)
    print("repr() : " , repr(m1))

    print("\nm2")
    m2 = Matrix(5, 5, "r")
    print(m2)

    print("\nm1+m2 :\n" ,m1+m2)
    print("\nm1-m2 :\n", m1 - m2)
    print("\nm1*m2 :\n", m1 * m2)

    m3 = Matrix(8, 5, "r")
    print("\n If length of Matrix doesn't match m1(5*5) + m3(8*5) : \n",  m1 + m3)

    print("transpose() :\n", m1.transpose())

def useEightQueen():
    e1 = EightQueen()
    e1.runEQ(5) # we need 5 solution

def useTicTacToe():
    tic = TicTacToe()
    tic.play_ttt()


def main():
    # useMatrix()
    # useEightQueen()
    useTicTacToe()
if __name__ == "__main__":
    main()