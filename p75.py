from typing import List


class Solution:

    def sort(self, nums, nums_copy, lower, high):
        mid = (lower + high) // 2
        if high - lower <= 0:
            return
        else:
            self.sort(nums, nums_copy, lower, mid)
            self.sort(nums, nums_copy, mid + 1, high)

        for i in range(lower, high + 1):
            nums_copy[i] = nums[i]

        i = lower
        j = mid + 1
        for k in range(lower, high + 1):
            if i > mid:
                nums[k] = nums_copy[j]
                j += 1
            elif j > high:
                nums[k] = nums_copy[i]
                i += 1
            else:
                if nums_copy[i] > nums_copy[j]:
                    nums[k] = nums_copy[j]
                    j += 1
                else:
                    nums[k] = nums_copy[i]
                    i += 1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_copy = nums[:]
        self.sort(nums, nums_copy, 0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()

    # nums = [2, 0, 2, 1, 1, 0]
    # nums = [2, 0, 1]
    # nums = [2, 2]
    # nums = [0, 2]
    # nums = [2, 0, 2]
    # nums = [1, 2, 0]
    # nums = [0,1,2,0,0,2,2,1]
    # nums = [2, 0, 0, 0, 0, 1, 2, 2]
    # nums = [0,1,2]
    nums = [1, 2, 0]
    s.sortColors(nums)
    print(nums)
