class Solution:

    def count(self, s, i):
        """ count how many occurrence in a row of ith element"""

        c = 0
        j = i

        while j < len(s):
            if s[j] != s[i]:
                break
            c += 1
            j += 1
        return c

    def read_s(self, s):

        ret = ''
        i = 0

        while i < len(s):
            counter = self.count(s, i)

            ret += (str(counter) + str(s[i]))
            i += counter

        return ret

    def countAndSay(self, n: int) -> str:
        s = '1'

        for i in range(n-1):
            s = self.read_s(s)

        return s


if __name__ == "__main__":
    s = Solution()
    n = 4
    print(s.countAndSay(4))
