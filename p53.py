from typing import List


class Solution:

    def find_max(self, nums):
        sums1 = []
        sums1.append(nums[0])
        for i in range(1, len(nums)):
            sums1.append(sums1[-1] + nums[i])

        minimum = sums1[0]
        max_dis = max(nums + sums1)

        for i in range(1, len(sums1)):
            if sums1[i] - minimum > max_dis:
                max_dis = sums1[i] - minimum
            if sums1[i] < minimum:
                minimum = sums1[i]

        return max_dis

    def maxSubArray(self, nums: List[int]) -> int:

        return self.find_max(nums)


if __name__ == "__main__":
    s = Solution()

    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [1]
    # nums = [-2, 1]
    # nums = [-1, 0, -2]
    # nums = [1, -1, -2]
    # nums = [-1, -2, -2, -2, 3, 2, -2, 0]
    # nums = [1, 2]
    print(s.maxSubArray(nums))
