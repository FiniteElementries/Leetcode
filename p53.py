from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        max_overall = nums[0]
        max_sofar = nums[0]

        for i in range(1, len(nums)):
            tmp = nums[i] + max_sofar
            if nums[i] > tmp:
                max_sofar = nums[i]
            else:
                max_sofar = tmp
            max_overall = max(max_sofar, max_overall)
        return max_overall


if __name__ == "__main__":
    s = Solution()

    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    # nums = [-2, 1]
    # nums = [-1, 0, -2]
    # nums = [1, -1, -2]
    # nums = [-1, -2, -2, -2, 3, 2, -2, 0]
    nums = [1, 2]
    # nums = [-2, -1]

    print(s.maxSubArray(nums))
