import torch


class Game:
    def __init__(self):
        self.board = torch.zeros(3, 3, dtype=torch.int)

    def take_move(self, x, y, value):
        self.board[y, x] = value

    def clear(self):
        self.board = torch.zeros(3, 3, dtype=torch.int)

    def who_wins(self):
        s1 = self.board.sum(0)
        s2 = self.board.sum(1)
        if (s1 == 3).any() or (s2 == 3).any() or (self.board.diag().sum() == 3) or (self.board.flip(1).diag().sum() == 3):
            return 1
        if (s1 == -3).any() or (s2 == -3).any() or (self.board.diag().sum() == -3) or (self.board.flip(1).diag().sum() == -3):
            return -1
        if (self.board == 0).sum() == 0:
            return 2
        return 0

    @staticmethod
    def hash(board):
        H, W = board.shape
        s = ''
        for y in range(H):
            for x in range(W):
                if board[y, x] == 0:
                    s += '#'
                elif board[y, x] == 1:
                    s += 'o'
                else:
                    s += 'x'
            if y < H-1:
                s += '\n'
        s += '\n'
        return s

    def __str__(self):
        return self.hash(self.board)
