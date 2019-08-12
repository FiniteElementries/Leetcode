from typing import List
import math

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = math.ceil(len(nums)/2)
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]




if __name__ == '__main__':
    s = Solution()

    nums = [1, 1, 2, 1, 2, 2, 1]

    # nums = [1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2]

    # nums = [1,3,2,2,3,1]

    nums = [4, 5, 5, 6,  1]
    s.wiggleSort(nums)

    print(nums)
