class Solution(object):
    cache = {0: 1}

    def orderAtPos(self, i):
        if i in self.cache:
            return self.cache[i]
        val = 26 * self.orderAtPos(i - 1)
        self.cache[i] = val
        return val

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        total = 0
        for i in range(0, len(s)):
            j = len(s) - i - 1
            item = s[j]
            order = ord(item) - ord('A') + 1
            total += order * self.orderAtPos(i)
        return total


if __name__ == '__main__':
    s = Solution()

    st = "AB"

    print(s.titleToNumber(st))
