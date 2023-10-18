import random
import sys

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

    def __str__(self):
        rowStrs = ["[{}]".format(', '.join(map(str, row))) for row in self.M]
        return ',\n'.join(rowStrs)

    def __repr__(self):
        rowStrs = ["[{}]".format(', '.join(map(str, row))) for row in self.M]
        return "[" + ','.join(rowStrs) + "]"

    def __add__(self, other):
        return self.matrixCal(other, "add")

    def __sub__(self, other):
        return self.matrixCal(other, "sub")

    def __mul__(self, other):
        return self.matrixCal(other, "mul")
    def matrixCal(self, other, calMethod):
        rowLen = len(self.M)
        colLen = len(self.M[0])
        if(rowLen == len(other.M) and colLen == len(other.M[0])):
            C = Matrix(rowLen, colLen, 'z')
            # calculate each self Matrix's element and other Matrix's element
            for row in range(rowLen):
                for col in range(colLen):
                    if(calMethod == "add"):
                        C.M[row][col] = self.M[row][col] + other.M[row][col]
                    elif(calMethod == "sub"):
                        C.M[row][col] = self.M[row][col] - other.M[row][col]
                    elif(calMethod == "mul"):
                        C.M[row][col] = self.M[row][col] * other.M[row][col]
            return C
        else:
            return ("Error :The length of rows and columns of Matrices"
                    " which you want to calculate does not match.")


    def transpose(self): # change matrix rows to cols, cols to rows
        rowLen = len(self.M)
        colLen = len(self.M[0])
        C = Matrix(colLen, rowLen, 'z')
        for row in range(rowLen):
            for col in range(colLen):
                C.M[col][row] = self.M[row][col]
        return C

class EightQueen:
    rnb = random.Random()
    def __init__(self):
        self.bd = list(range(8)) # chess board
    def runEQ(self, nos): # number of solutions we need
        found = 0 # number of solutions we found
        tries = 0 # how many times tried to get one solution
        while found < nos:
            EightQueen.rnb.shuffle(self.bd) # random position
            tries += 1
            if not self.has_clash(): # found a solution
                found += 1
                print("Solution {}, {}, {} ".format(found, self.bd, tries))
                tries = 0
    def has_clash(self):
        for x1 in range(len(self.bd)):
            for x2 in range(x1 + 1, len(self.bd)):
                # Check for diagonal clash
                if(abs(x1 - x2) == abs(self.bd[x1] - self.bd[x2])):
                    return True
        return False

class TicTacToe:
    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append(-1)

    def play_ttt(self):
        while True:
            self.runGame()
            if self.quit_game():
                print("Exit the game...")
                break
            else:
                print("Restart the game...")
                for i in range(9): # initializing the board
                    self.board[i] = -1

    def runGame(self):
        move = 0
        while True:
            if move % 2 == 0:
                turn = 'X'
            else:
                turn = 'O'
            print("\nTurn for player {} ".format(turn))
            pos = self.getInput()  # position entered by the user
            self.board[pos] = "O" if turn == "O" else "X"
            move += 1
            if move > 3:  # winner may be determined when moved at least three times
                winner = self.check_win()
                if winner != -1:  # The winner is determined
                    self.printBoard()
                    print("The winner is {}".format("X" if winner == 1 else "O"))
                    break
                elif(move >= 9):
                    self.printBoard()
                    print("Draw")
                    break

    def check_win(self):
        win_cord = ((1,2,3), (4,5,6), (7,8,9),
                    (1,4,7), (2,5,8), (3,6,9),
                    (1,5,9), (3,5,7))

        for each in win_cord:
            if (self.board[each[0] - 1] == self.board[each[1] - 1] and
                self.board[each[1] - 1] == self.board[each[2] - 1]):
                return self.board[each[0] - 1]
        return -1  # draw

    def getInput(self):
        while True:
            self.printBoard()
            try:
                pos = int(input("Please enter the position(0 ~ 8) : "))
            except ValueError:
                print("Invalid input")
                continue
            if not (0 <= pos <= 8):
                print("Please enter a value between 0 and 8 ")
            elif(self.board[pos] != -1):
                print("The position has already been selected")
            else: # Input is valid
                return pos

    def printBoard(self):
        for i in range(0, len(self.board), 3):
            print(self.board[i:i + 3])

    def quit_game(self):
        quitGame = input("Enter \'q\' if you want to end the game or press any key if you want to continue : ")
        return True if quitGame == 'q' else False











