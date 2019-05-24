from typing import List


class Solution:
    solutions = []

    def dfs(self, nums, p):
        if len(nums) == 1:
            p_copy = p[:]
            p_copy.append(nums[-1])
            self.solutions.append(p_copy)
            return

        for i in range(0, len(nums)):
            p_copy = p[:]
            p_copy.append(nums[i])

            if i == 0:
                n_copy = nums[1:]
            elif i == (len(nums) - 1):
                n_copy = nums[0:-1]
            else:
                n_copy = nums[0:i] + nums[i + 1:]

            self.dfs(n_copy, p_copy)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.solutions = []

        self.dfs(nums, [])

        return self.solutions


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3]

    print(s.permute(nums))
