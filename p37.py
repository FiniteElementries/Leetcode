from typing import List


class Solution:

    def can_fit(self, board, i, j, n):
        for k in range(0, self.rows):
            if board[k][j] == n:
                return False
            if board[i][k] == n:
                return False

        quadra_x = i // 3 * 3
        quadra_y = j // 3 * 3

        for l in range(quadra_x, quadra_x + 3):
            for m in range(quadra_y, quadra_y + 3):
                if board[l][m] == n:
                    return False
        return True

    rows = 0
    cols = 0

    def solve(self, board, x, y):

        while True:
            if x >= self.rows or y >= self.cols:
                return True
            if board[x][y] == '.':
                break
            if y >= self.cols - 1:
                y = 0
                x += 1
            else:
                y += 1

        for n in range(1, 10):
            # check can fit
            if self.can_fit(board, x, y, str(n)):
                board[x][y] = str(n)
                if self.solve(board, x, y):
                    return True
                board[x][y] = '.'
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = len(board)
        self.cols = len(board[0])

        self.solve(board, 0, 0)


if __name__ == '__main__':
    s = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s.solveSudoku(board)

    print(board)
