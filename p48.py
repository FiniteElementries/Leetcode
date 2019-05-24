from typing import List


class Solution:

    def rotate_m(self, matrix, m, n):

        i = 0
        while m + i < n - m:
            tmp = matrix[m][m + i]
            matrix[m][m + i] = matrix[n - m - i][m]
            matrix[n - m - i][m] = matrix[n - m][n - m - i]
            matrix[n - m][n - m - i] = matrix[m + i][n - m]
            matrix[m + i][n - m] = tmp
            i += 1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(0, n // 2):
            self.rotate_m(matrix, i, n-1)

        print(matrix)


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(s.rotate(matrix))
