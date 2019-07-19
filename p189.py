from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        starter = nums[0+k]
        for i in range(0, k):
            val = nums[i+k]
            nums[i+k] = nums[i]



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
