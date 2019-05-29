from typing import List


class Solution:

    def setNone(self, i, j, matrix, m, n):
        matrix[i][j] = None
        for k in range(0, m):
            if matrix[k][j] != 0:
                matrix[k][j] = None

        for k in range(0, n):
            if matrix[i][k] != 0:
                matrix[i][k] = None

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    self.setNone(i, j, matrix, m, n)

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


if __name__ == "__main__":
    s = Solution()

    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    s.setZeroes(matrix)
    print(matrix)
