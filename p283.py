from typing import List


class Solution:

    def merge(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        arr1 = self.merge(nums[0:mid])
        arr2 = self.merge(nums[mid:])

        i = 0
        j = 0
        k = 0

        while k < len(nums):
            if j >= len(nums)-mid:
                nums[k] = arr1[i]
                i += 1
            elif i >= mid:
                nums[k] = arr2[j]
                j += 1
            elif arr1[i] == 0:
                nums[k] = arr2[j]
                j += 1
            elif arr2[j] == 0:
                nums[k] = arr1[i]
                i += 1
            elif i < len(arr1):
                nums[k] = arr1[i]
                i += 1
            else:
                nums[k] = arr2[j]
                j += 1
            k += 1
        return nums

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.merge(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]

    print(s.moveZeroes(nums))
