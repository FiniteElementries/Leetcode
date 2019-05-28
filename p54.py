from typing import List


class Solution:

    def move_right(self, i, j):
        direction = 'right'
        if j < self.n - 1:
            if self.marker[i][j + 1] == 0:
                return i, j + 1, direction
        direction = 'down'
        if self.marker[i + 1][j] == 1:
            return -1, -1, None
        return i + 1, j, direction

    def move_down(self, i, j):
        direction = 'down'
        if i < self.m - 1:
            if self.marker[i + 1][j] == 0:
                return i + 1, j, direction

        direction = 'left'
        if self.marker[i][j - 1] == 1:
            return -1, -1, None
        return i, j - 1, direction

    def move_left(self, i, j):
        direction = 'left'
        if j > 0:
            if self.marker[i][j - 1] == 0:
                return i, j - 1, direction
        direction = 'up'
        if self.marker[i - 1][j] == 1:
            return -1, -1, None
        return i - 1, j, direction

    def move_up(self, i, j):
        direction = 'up'
        if i > 0:
            if self.marker[i - 1][j] == 0:
                return i - 1, j, direction
        direction = 'right'
        if self.marker[i][j + 1] == 1:
            return -1, -1, None
        return i, j + 1, direction

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.m = len(matrix)

        if self.m == 0:
            return []

        if self.m == 1:
            return matrix[0]

        self.n = len(matrix[0])

        self.marker = [[0] * self.n for _ in range(0, self.m)]

        i = 0
        j = 0
        ret_val = []
        dir = 'right'

        while (i >= 0 and j >= 0):
            self.marker[i][j] = 1
            ret_val.append(matrix[i][j])

            if dir == 'right':
                i, j, dir = self.move_right(i, j)
            elif dir == 'down':
                i, j, dir = self.move_down(i, j)
            elif dir == 'left':
                i, j, dir = self.move_left(i, j)
            elif dir == 'up':
                i, j, dir = self.move_up(i, j)

        return ret_val


if __name__ == "__main__":
    s = Solution()

    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    #
    # matrix = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12]
    # ]

    # matrix = [[1]]
    matrix = [[1] ,[2]]
    print(s.spiralOrder(matrix))
