from typing import List


class Solution:

    mem = {}
    def perform_ops(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2

    def diffWaysToCompute(self, input: str) -> List[int]:
        if input in self.mem:
            return self.mem[input]
        try:
            res = int(input)
            self.mem[input] = [res]
            return [res]
        except:
            pass
        res = []
        ops = {'+', '-', '*'}
        for i in range(0, len(input)):
            if input[i] in ops:
                lefts = self.diffWaysToCompute(input[0:i])
                rights = self.diffWaysToCompute(input[i + 1:])
                for l in lefts:
                    for r in rights:
                        res.append(self.perform_ops(l, r, input[i]))
        self.mem[input] = res
        return self.mem[input]
