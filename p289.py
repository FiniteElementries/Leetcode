from typing import List


class Solution:

    def is_live(self, i, j, board):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return 0
        return board[i][j]

    def dfs(self, board, i, j, visited):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return
        if visited[i][j] == 1:
            return

        live_neighbor_count = self.is_live(i - 1, j - 1, board) + \
                              self.is_live(i - 1, j, board) + \
                              self.is_live(i - 1, j + 1, board) + \
                              self.is_live(i, j - 1, board) + \
                              self.is_live(i, j + 1, board) + \
                              self.is_live(i + 1, j - 1, board) + \
                              self.is_live(i + 1, j, board) + \
                              self.is_live(i + 1, j + 1, board)

        if board[i][j] == 1:
            if 2 <= live_neighbor_count <= 3:
                board_next = 1
            else:
                board_next = 0
        else:
            if live_neighbor_count == 3:
                board_next = 1
            else:
                board_next = 0

        visited[i][j] = 1
        self.dfs(board, i - 1, j - 1, visited)
        self.dfs(board, i - 1, j, visited)
        self.dfs(board, i - 1, j + 1, visited)
        self.dfs(board, i, j - 1, visited)
        self.dfs(board, i, j + 1, visited)
        self.dfs(board, i + 1, j - 1, visited)
        self.dfs(board, i + 1, j, visited)
        self.dfs(board, i + 1, j + 1, visited)

        board[i][j] = board_next

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[0] * len(board[0]) for _ in range(len(board))]

        self.dfs(board, 0, 0, visited)


if __name__ == '__main__':
    s = Solution()

    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

    print(s.gameOfLife(board))
