from typing import List


class Solution:
    ret_val = [[]]

    def find_set(self, prefix, i, nums):
        if i >= len(nums):
            return
        self.ret_val.append(prefix)
        for j in range(i + 1, len(nums)):
            new_prefix = prefix + [nums[j]]
            self.find_set(new_prefix, j, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret_val = [[]]
        for i in range(0, len(nums)):
            self.find_set([nums[i]], i, nums)

        return self.ret_val


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))
