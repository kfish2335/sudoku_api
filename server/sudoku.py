import copy
import json
from random import randrange, sample


class Board:
    def __init__(self):
        self.boardf = self.full_board()
        self.puzzle = self.make_puzzle()

    def full_board(self):
        base = 3
        side = base * base

        
        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side

        def shuffle(s):
            return sample(s, len(s))

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))
        
        return [[nums[pattern(r, c)] for c in cols] for r in rows]

    def change_board(self):
        self.boardf = self.full_board()

    def make_puzzle(self):
        board = copy.deepcopy(self.boardf)
        for x in range(9):
            i = sample(range(9), randrange(5, 6))
            for y in i:
                board[x][y] = 0
        return board

    def change_puzzle(self):
        self.puzzle = self.make_puzzle()


class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.ans = []
        self.count = 0

    def start_solver(self):
        self.ans = []
        self.solve()
        return self.count

    def set_ans(self):
        if self.ans == []:
            self.ans = copy.deepcopy(self.board)

    def possible(self, y, x, n):
        for i in range(0, 9):
            if self.board[y][i] == n:
                return False
        for i in range(0, 9):
            if self.board[i][x] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[y0 + i][x0 + j] == n:
                    return False
        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            self.set_ans()
            return True
        else:
            x, y = find

        for i in range(1, 10):
            if self.possible(x, y, i):
                self.board[x][y] = i

                if self.solve():
                    self.count += 1

                    self.board[x][y] = 0

            self.board[x][y] = 0
        return False

    def find_empty(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if self.board[x][y] == 0:
                    return (x, y)  # row, col

        return None


if __name__ == "__main__":
    print("hello")
