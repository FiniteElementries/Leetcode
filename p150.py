"""
postfix notation eval
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for item in tokens:
            if item.isdigit() or item.strip("-").isdigit():
                nums.append(int(item))
            else:
                num2 = nums.pop()
                num1 = nums.pop()

                if item == '+':
                    res = num1 + num2
                elif item == '-':
                    res = num1 - num2
                elif item == '*':
                    res = num1 * num2
                else:
                    res = int(num1 / num2)

                nums.append(res)
        return nums[-1]


if __name__ == "__main__":
    s = Solution()

    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    print(s.evalRPN(tokens))
