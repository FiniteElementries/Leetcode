from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if k == 0:
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        left_sums = []
        right_sums = []

        left_sum = 0
        for i in nums:
            left_sum += i
            left_sums.append(left_sum)

        right_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            right_sum += nums[i]
            right_sums.append(right_sum)

        right_sums.reverse()

        total = left_sums[-1]

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                s = left_sums[j] + right_sums[i] - total
                if (s / k).is_integer():
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [23, 2, 6, 4, 7]
    k = 6

    nums = [0, 0]
    k = 0

    nums = [0, 1, 0]
    k = 0

    nums = [23, 6, 9]
    k = 6
    print(s.checkSubarraySum(nums, k))
