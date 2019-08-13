import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        smallest = math.inf
        closest_sums = 0

        for i in range(0, len(nums)-2):
            two_target = target - nums[i]
            small_diff, sums = self.twoSumClosest(nums, i + 1, len(nums) - 1, two_target)
            if abs(small_diff) < abs(smallest):
                closest_sums = sums + nums[i]
                smallest = small_diff
        return closest_sums

    def twoSumClosest(self, nums, i, j, target):
        x = i
        y = j

        small_diff = nums[x] + nums[y] - target
        sums = nums[x] + nums[y]
        while x < y:
            diff = nums[x] + nums[y] - target
            if abs(diff) < abs(small_diff):
                small_diff = diff
                sums = nums[x] + nums[y]
            if diff > 0:
                y -= 1
            elif diff <= 0:
                x += 1

        return small_diff, sums


if __name__ == '__main__':
    s = Solution()

    nums = [-1, 2, 1, -4]
    target = 1

    print(s.threeSumClosest(nums, target))