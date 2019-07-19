from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums[:] + nums[:]
        k = k % len(nums)

        start = len(nums)-k
        end = len(nums) + start
        tmp = tmp[start:end]

        for i in range(len(nums)):
            nums[i] = tmp[i]


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    # nums = [1, 2, 3, 4, 5, 6]
    # k = 2

    # nums = [1, 2]
    # k = 2

    s.rotate(nums, k)

    print(nums)
