from typing import List
import math


class Solution:
    def path_at(self, i, j, m, n, grid):

        if i >= m or j >= n:
            return math.inf

        if self.mem[i][j] is not None:
            return self.mem[i][j]

        p = grid[i][j] + min(self.path_at(i + 1, j, m, n, grid), self.path_at(i, j + 1, m, n, grid))
        self.mem[i][j] = p
        return p

    mem = None

    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        self.mem = [[None] * n for _ in range(m)]
        self.mem[m - 1][n - 1] = grid[m - 1][n - 1]

        return self.path_at(0, 0, m, n, grid)


if __name__ == '__main__':
    s = Solution()

    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]

    print(s.minPathSum(grid))
