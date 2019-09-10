from typing import List


class Solution:
    mem = {}
    target = 0
    res = []

    def possible_values(self, num, diff, val, op):
        """ diff changes from last round, val current value"""

        if len(num) == 0 and val == self.target:
            self.res.append(op)
            return

        for i in range(1, len(num)+1):
            if num[0] == '0':
                num1 = 0
                next_num = num[1:]
            else:
                num1 = int(num[0:i])
                next_num = num[i:]

            if len(op) == 0:
                self.possible_values(next_num, num1, num1, num[0:i])

            else:
                self.possible_values(next_num, num1, val + num1, op + '+' + num[0:i])
                self.possible_values(next_num, -num1, val - num1, op + '-' + num[0:i])
                self.possible_values(next_num, diff * num1, val - diff + diff * num1, op + '*' + num[0:i])

            if num[0] == '0':
                return
        pass

    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        self.target = target
        self.res = []
        self.possible_values(num, 0, 0, "")
        return self.res


if __name__ == '__main__':
    s = Solution()

    num = '123'
    target = 6

    num = "105"
    target = 5

    # num = "232"
    # target = 8

    print(s.addOperators(num, target))
