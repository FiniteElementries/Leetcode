from typing import List


class Solution:

    def twoSum(self, nums, i, target):
        x = i
        y = len(nums) - 1

        res = set()
        while x < y:
            if nums[x] + nums[y] < target:
                x += 1
            elif nums[x] + nums[y] > target:
                y -= 1
            else:
                res.add((nums[x], nums[y]))
                x += 1
        return res

    def threeSum(self, nums, start, target):

        res = set()

        for i in range(start, len(nums) - 1):
            twoSum = self.twoSum(nums, i + 1, target - nums[i])
            for item in twoSum:
                res.add((nums[i], item[0], item[1]))
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = set()
        for i in range(len(nums)):
            threeSum = self.threeSum(nums, i + 1, target - nums[i])
            for item in threeSum:
                res.add((nums[i], item[0], item[1], item[2]))
        return [[x[0], x[1], x[2], x[3]] for x in res]
