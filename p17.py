from typing import List

class Solution:
    mapping = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
    }

    def dfs(self, digits, combination, i):
        if len(digits)==0:
            return []

        if i>=len(digits):
            self.combinations.append(combination)
            return

        cs = self.mapping[digits[i]]
        for c in cs:
            self.dfs(digits, combination + c, i+1)


    def letterCombinations(self, digits: str) -> List[str]:

        self.combinations = []

        self.dfs(digits, '', 0)

        return self.combinations


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
