class EightQueen:
    def __init__(self, NQ):
        self.NQ = NQ
        self.solutions = 0
        self.nn = 0

    def solve(self):
        board = [-1] * self.NQ
        self.dfsPQ(board, 0)
        print("Found " , self.solutions, " solutions.")
        print("Number of nodes ", self.nn )

    def dfsPQ(self, board, row):
        if row == self.NQ:
            print(board)
            self.solutions += 1
        else:
            for col in range(self.NQ):
                if not self.isAttack(board, row, col):
                    self.nn += 1
                    board[row] = col
                    self.dfsPQ(board, row + 1)

    def isAttack(self, board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return True
        return False





