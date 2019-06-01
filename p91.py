class Solution:
    mem = {}

    def decode_way(self, s, i):
        if i in self.mem:
            return self.mem[i]

        if i > len(s):
            return 0

        if i == len(s):
            return 1

        if s[i] == '0':
            return 0

        total = 0

        # single digit
        next_val = self.decode_way(s, i + 1)
        if next_val != 0:
            total += next_val

        # double digit
        next_val = 0
        if i + 1 < len(s):
            if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                next_val = self.decode_way(s, i + 2)
        if next_val != 0:
            total += next_val

        self.mem[i] = total
        return total

    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0

        self.mem = {}
        total = self.decode_way(s, 0)
        return max(total, 0)


if __name__ == "__main__":
    s = Solution()

    st = "226"
    # st = '1100'
    # st = '10'
    # st = '100'
    # st = '101'
    st = '27'
    st = '12'
    print(s.numDecodings(st))
