from typing import List


class Solution:

    def notflip(self, i, j, connected_to_edge, board, rows, cols):
        if not (0 <= i < rows) or not (0 <= j < cols):
            return
        if board[i][j] == 'X':
            return
        if connected_to_edge[i][j] == 1:
            return
        connected_to_edge[i][j] = 1

        self.notflip(i + 1, j, connected_to_edge, board, rows, cols)
        self.notflip(i - 1, j, connected_to_edge, board, rows, cols)
        self.notflip(i, j + 1, connected_to_edge, board, rows, cols)
        self.notflip(i, j - 1, connected_to_edge, board, rows, cols)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return board

        rows = len(board)
        cols = len(board[0])

        connected_to_edge = [[0] * cols for _ in range(rows)]

        for j in range(0, cols):
            self.notflip(0, j, connected_to_edge, board, rows, cols)
            self.notflip(rows - 1, j, connected_to_edge, board, rows, cols)

        for i in range(0, rows):
            self.notflip(i, 0, connected_to_edge, board, rows, cols)
            self.notflip(i, cols - 1, connected_to_edge, board, rows, cols)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and connected_to_edge[i][j] == 0:
                    board[i][j] = 'X'


if __name__ == "__main__":
    s = Solution()
