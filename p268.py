from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        upper_limit = len(nums) + 1

        arr = [0] * (upper_limit + 1)

        for item in nums:
            arr[item] = 1

        for i in range(0, len(arr)):
            if arr[i] == 0:
                return i

if __name__ == '__main__':
    s = Solution()

    nums = [0]
    print(s.missingNumber(nums))