class Solution:

    def uw(self, i, j):
        if self.mapping[i][j] > 0:
            return self.mapping[i][j]

        if i < 0 or j < 0:
            ret_val = 0
        elif i == 0 and j == 0:
            ret_val = 1
        else:
            ret_val = self.uw(i - 1, j) + self.uw(i, j - 1)

        self.mapping[i][j] = ret_val
        return ret_val

    def uniquePaths(self, m: int, n: int) -> int:

        self.mapping = [[-1] * n for _ in range(m)]
        return self.uw(m - 1, n - 1)


if __name__ == "__main__":
    s = Solution()

    m = 3
    n = 2

    m = 7
    n = 3
    print(s.uniquePaths(m, n))
