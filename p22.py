from typing import List



class Solution:

    combinations = []

    def dfs(self, s, n, step, count):
        if step==n:
            if count==0:
                self.combinations.append(s)
            return

        if count>0:
            self.dfs(s + ')', n, step + 1, count - 1)
        if count<n/2:
            self.dfs(s + '(', n, step + 1, count + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.combinations = []
        self.dfs('', n*2, 0, 0)
        return self.combinations


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))