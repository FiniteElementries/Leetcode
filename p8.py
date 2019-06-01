class Solution:

    def get_nums_string(self, st):
        i = 0
        while i < len(st):
            if st[i] == '-' or st[i].isdigit():
                break
            if st[i] == '+':
                break
            if st[i] != ' ':
                return "0"
            i+=1

        j = i + 1
        while j < len(st):
            if not st[j].isdigit():
                break
            j+=1
        return st[i:j]

    def myAtoi(self, str: str) -> int:

        num_str = self.get_nums_string(str)

        if len(num_str)==0:
            return 0
        if not num_str[-1].isdigit():
            return 0

        i = int(num_str)

        if i < -2147483648:
            return -2147483648
        elif i > 2147483647:
            return 2147483647
        else:
            return i


if __name__ == "__main__":
    s = Solution()

    st = "-91283472332"
    st = "   -42"
    st = "  +b12102370352"
    print(s.myAtoi(st))
