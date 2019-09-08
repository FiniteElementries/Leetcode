from typing import List


class Solution:

    def path_at(self, i, j, m, n, grid):

        if i >= m or j >= n:
            return 0

        if grid[i][j] == 1:
            return 0

        if self.mem[i][j] is not None:
            return self.mem[i][j]

        p = self.path_at(i + 1, j, m, n, grid) + self.path_at(i, j + 1, m, n, grid)
        self.mem[i][j] = p
        return p

    mem = None

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        self.mem = [[None] * n for _ in range(m)]
        self.mem[m - 1][n - 1] = 1

        return self.path_at(0, 0, m, n, obstacleGrid)


if __name__ == '__main__':
    s = Solution()

    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    print(s.uniquePathsWithObstacles(grid))
