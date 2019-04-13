class Solution:
    def reverse(self, x: int) -> int:

        text = str(x)

        if text[0] == "-":
            new_text = "-"
            text = text[1:]
        else:
            new_text = ""

        for i in range(0, len(text)):
            new_text += text[len(text) - i - 1]

        ret_val = int(new_text)

        if ret_val > 2 ** 31 - 1 or ret_val < -2 ** 31:
            return 0
        else:
            return ret_val


s = Solution()
print(s.reverse(1534236469))
print(s.reverse(-123))
