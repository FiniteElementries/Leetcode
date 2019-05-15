from typing import List


class Solution:
    rows = {}
    cols = {}
    grids = {}

    def add_to_row(self, val, row_num):
        if row_num not in self.rows:
            self.rows[row_num] = set()
        if val not in self.rows[row_num]:
            self.rows[row_num].add(val)
            return True
        else:
            return False

    def add_to_col(self, val, col_num):
        if col_num not in self.cols:
            self.cols[col_num] = set()
        if val not in self.cols[col_num]:
            self.cols[col_num].add(val)
            return True
        else:
            return False

    def add_to_grid(self, val, row_num, col_num):
        row_count = row_num // 3
        col_count = col_num // 3

        if row_count not in self.grids:
            self.grids[row_count] = {}

        if col_count not in self.grids[row_count]:
            self.grids[row_count][col_count] = set()

        if val not in self.grids[row_count][col_count]:
            self.grids[row_count][col_count].add(val)
            return True
        else:
            return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.rows = {}
        self.cols = {}
        self.grids = {}

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    if not self.add_to_row(board[i][j], i):
                        return False
                    if not self.add_to_col(board[i][j], j):
                        return False
                    if not self.add_to_grid(board[i][j], i, j):
                        return False
        return True


if __name__ == "__main__":
    s = Solution()

    # board = [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]
    #
    # board = [
    #     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]

    board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
             ["2", ".", ".", ".", ".", ".", ".", ".", "."],
             ["3", ".", ".", ".", ".", ".", ".", ".", "."],
             ["4", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", ".", "."],
             ["6", ".", ".", ".", ".", ".", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             ["8", ".", ".", ".", ".", ".", ".", ".", "."],
             ["9", ".", ".", ".", ".", ".", ".", ".", "."]]

    print(s.isValidSudoku(board))
