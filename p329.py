from typing import List


class Solution:
    max_path = 0

    def dfs(self, i, j, matrix, visited, mem, last_val):

        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]): return 0
        if visited[i][j] == 1: return 0
        if matrix[i][j] <= last_val: return 0

        if mem[i][j] is not None:
            return mem[i][j]

        visited[i][j] = 1
        count = 1
        last_val = matrix[i][j]

        max_count = max(0, self.dfs(i + 1, j, matrix, visited, mem, last_val))
        max_count = max(max_count, self.dfs(i - 1, j, matrix, visited, mem, last_val))
        max_count = max(max_count, self.dfs(i, j + 1, matrix, visited, mem, last_val))
        max_count = max(max_count, self.dfs(i, j - 1, matrix, visited, mem, last_val))

        mem[i][j] = max_count + count
        self.max_path = max(self.max_path, mem[i][j])
        visited[i][j] = 0

        return mem[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        mem = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        self.max_path = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                self.dfs(i, j, matrix, visited, mem, -1)

        return self.max_path


if __name__ == '__main__':
    s = Solution()

    m = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

    m = [[3, 4, 5],
         [3, 2, 6],
         [2, 2, 1]]

    m = [[7, 7, 5],
         [2, 4, 6],
         [8, 2, 0]]

    print(s.longestIncreasingPath(m))
