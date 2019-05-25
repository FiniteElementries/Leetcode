class Solution:
    map = {}

    def pow(self, x, n):
        if n in self.map:
            return self.map[n]
        else:
            if n == 1:
                ret_val = x
            else:
                i = n // 2
                j = n - i
                ret_val = self.pow(x, i) * self.pow(x, j)

        self.map[n] = ret_val
        return ret_val

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        self.map = {}
        m = abs(n)

        y = self.pow(x, m)

        if n < 0:
            return 1 / y
        else:
            return y


if __name__ == "__main__":
    s = Solution()

    x = 2.0000
    n = 10
    print(s.myPow(x, n))
