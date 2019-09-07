class Solution:
    mem = None

    def open_brackets_count(self, i, j, s):

        if self.mem[i][j] is not None:
            return self.mem[i][j]
        elif s[i] == ')':
            res = -1
        elif i == j:
            res = 1
        else:
            t = self.open_brackets_count(i, j - 1, s)
            if t < 0:
                res = -1
            else:
                if s[j] == '(':
                    res = t + 1
                else:
                    res = t - 1

        if res == 0:
            self.max_l = max(self.max_l, j - i + 1)

        self.mem[i][j] = res
        return res

    def longestValidParentheses(self, s: str) -> int:
        l = len(s)

        self.mem = [[None] * l for _ in range(l)]
        self.max_l = 0

        for i in range(0, l):
            for j in range(i, l):
                self.open_brackets_count(i, j, s)

        return self.max_l


if __name__ == '__main__':
    s = Solution()

    st = "()()"

    # st = ')('

    print(s.longestValidParentheses(st))
