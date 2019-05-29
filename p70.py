class Solution:
    mem = {}

    def step(self, n):
        if n in self.mem:
            return self.mem[n]
        else:
            if n == 0:
                ret_val = 1
            elif n < 0:
                ret_val = 0
            else:
                ret_val = self.step(n - 1) + self.step(n - 2)
            self.mem[n] = ret_val
            return ret_val

    def climbStairs(self, n: int) -> int:
        self.mem = {}
        return self.step(n)


if __name__ == "__main__":
    s = Solution()

    n = 3
    print(s.step(n))
