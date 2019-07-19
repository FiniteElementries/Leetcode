class Solution:

    def dosumsquare(self, n):
        s = str(n)
        total = 0
        for c in list(s):
            total += int(c) ** 2
        return total

    def isHappy(self, n: int) -> bool:

        seen = set([])
        while n not in seen:
            seen.add(n)
            n = self.dosumsquare(n)

        return n == 1


if __name__ == "__main__":
    s = Solution()

    n = 19

    print(s.isHappy(n))
