import random

class Matrix:
    rnb = random.Random()
    def __init__(self, rows, cols, f):
        self.M = []
        if(f == 'r'):
            self.rMatriix(rows, cols)
        elif(f == 'z'):
            self.zMatriix(rows, cols)

    def mPrint(self):
        for rows in self.M:
            print([x for x in rows])

    def rMatriix(self, rows, cols): # random element
        self.M = []
        while len(self.M) < rows:
            self.M.append([])
            while len(self.M[-1]) < cols:
                self.M[-1].append(Matrix.rnb.randint(1, 10))

    def zMatriix(self, rows, cols):
        self.M = []
        while len(self.M) < rows:
            self.M.append([])
            while len(self.M[-1]) < cols:
                self.M[-1].append(0)

    def __str__(self): # return Matrix as String
        pass
    def __repr__(self):
        pass

    def __add__(self, other):
        rowA = len(self.M)
        colA = len(self.M[0])
        C = Matrix(rowA, colA, 'z')
        for row in range(rowA):
            for col in range(colA): # add self Matrix's element and other Matrix's element
                C.M[row][col] = self.M[row][col] + other.M[row][col]

        return C


    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def transpose(self): # change matrix rows to cols, cols to rows
        pass

class EightQueen:
    rnb = random.Random()

    def __init__(self):
        self.bd = list(range(8)) # chess board

    def runEQ(self, nos): # number of solutions we need
        found = 0
        tries = 0 # how many times tried to get a one solution
        while found < nos:
            EightQueen.rnb.shuffle(self.bd) # random position
            tries += 1
            if not self.has_clash():
                found += 1
                print("Solution {}, {}, {} ".format(found, self.bd, tries))
                tries = 0
    def has_clash(self):
        for col in range(1, len(self.bd)):
            if self.col_clashes(col):
                return True
            else:
                return False

    def col_clashes(self, col): # k is queen's col position
        # for i in range(col):
        #     if(self.diagonal_clashes(i, self.bd[i], k, self.bd[k])):
        #         return True
        #     else:
        #         return False

    def diagonal_clashes(self, x0, y0, x1, y1):
        d1 = abs(x0 - y0)
        d2 = abs(x1 - y1)
        return d1 == d2


class TicTacToe:
    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append(-1)

    def play_ttt(self):
        win = False
        move = 0
        while not win:
            self.printBoard()
            if move %2 == 0:
                turn = 'X'
            else:
                turn = 'O'
            print("Turn for player {} ".format(turn))

            user = self.getInput();
            while self.board[user] != -1:
                print("Invalid input")
                user = self.getInput()

            self.board[user] = 1 if turn == "O" else 0
            move += 1
            if move > 3: #
                winner = self.check_win()
                if winner != -1 : # 승자가 결정됨
                    print("The winner is {}".format("X" if winner == 1 else "O"))
    def check_win(self):
        win_cord = ((1,2,3), (4,5,6), (7,8,9),
                    (1,4,7), (2,5,8), (3,6,9),
                    (1,5,9), (3,5,7))

        for each in win_cord:
            if self.board[each[0] - 1] == self.board[each[1] - 1] and
                self.board[each[1] - 1] == self.board[each[2] - 1]:
                return self.board[each[0] - 1]
        return -1

    def getInput(self):
        pass

    def printBoard(self):
        pass

    def quit_game(self):
        pass











