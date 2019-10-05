from typing import List
from bisect import bisect_left


class Solution:

    def find_row(self, target, matrix, row_num_start, row_num_end):

        if target >= matrix[row_num_end][0]:
            return row_num_end

        if row_num_end - row_num_start <=1:
            return row_num_start

        mid = (row_num_start + row_num_end) // 2

        if matrix[mid][0] > target:
            return self.find_row(target, matrix, row_num_start, mid)
        elif matrix[mid][0] < target:
            return self.find_row(target, matrix, mid, row_num_end)
        else:
            return mid

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix) == 1:
            row = 0
        else:
            row = self.find_row(target, matrix, 0, len(matrix)-1)

        col = bisect_left(matrix[row], target)

        if col == len(matrix[row]):
            return False

        return matrix[row][col] == target


if __name__ == '__main__':
    s = Solution()

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 20

    matrix = [[1]]
    target = 1

    print(s.searchMatrix(matrix, target))
