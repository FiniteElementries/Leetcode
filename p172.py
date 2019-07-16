class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        f = n // 5
        while f > 0:
            count += f
            f = f // 5
        return count


if __name__ == "__main__":

    s = Solution()

    n = 3
    n = 5
    n = 10
    n = 30
    print(s.trailingZeroes(n))
