from typing import List
from collections import defaultdict


class Solution:
    cache = {}

    def put(self, i, j, size):
        if i not in self.cache:
            self.cache[i] = {}

        self.cache[i][j] = size

    def get(self, i, j):
        if i not in self.cache:
            return -1
        if j not in self.cache[i]:
            return -1
        return self.cache[i][j]

    def largest_square_at(self, i, j, matrix):
        if i >= len(matrix) or j >= len(matrix[0]):
            return 0
        if matrix[i][j] == '0':
            return 0

        if self.get(i, j) > -1:
            return self.get(i, j)

        contained_size = self.largest_square_at(i + 1, j + 1, matrix)
        if contained_size > 0:
            can_expand = True
            for expand in range(1, contained_size + 1):
                if matrix[i][j + expand] == '0' or matrix[i + expand][j] == '0':
                    can_expand = False
                    break
            if can_expand:
                contained_size += 1
                self.put(i, j, contained_size)
                return contained_size

        potential_size = 1
        while potential_size + i < len(matrix) and potential_size + j < len(matrix[0]):
            has_zero = False
            for ii in range(i, i + potential_size + 1):
                if matrix[ii][j + potential_size] == '0':
                    has_zero = True
                    break
            if not has_zero:
                for jj in range(j, j + potential_size + 1):
                    if matrix[i + potential_size][jj] == '0':
                        has_zero = True
                        break

            if has_zero:
                break
            potential_size += 1
        self.put(i, j, potential_size)
        return potential_size

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.cache = {}
        max_size = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                max_size = max(self.largest_square_at(i, j, matrix), max_size)
        return max_size ** 2


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 0, 1, 0],
              ]

    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    matrix = [["0", "1"]]

    matrix = [["0", "0", "0", "1", "0", "1", "1", "1"],
              ["0", "1", "1", "0", "0", "1", "0", "1"],
              ["1", "0", "1", "1", "1", "1", "0", "1"],
              ["0", "0", "0", "1", "0", "0", "0", "0"],
              ["0", "0", "1", "0", "0", "0", "1", "0"],
              ["1", "1", "1", "0", "0", "1", "1", "1"],
              ["1", "0", "0", "1", "1", "0", "0", "1"],
              ["0", "1", "0", "0", "1", "1", "0", "0"],
              ["1", "0", "0", "1", "0", "0", "0", "0"]]
    print(s.maximalSquare(matrix))
