from typing import List


class Solution:

    def search_left(self, nums, i, j, target):
        if i==0 and nums[i] == target:
            return i
        if nums[i] < target and nums[j] == target and j-i==1:
            return j

        if j-i<=1:
            return -1

        mid = int((i + j) / 2)
        if nums[mid] < target:
            return self.search_left(nums, mid, j, target)
        else:
            return self.search_left(nums, i, mid, target)

    def search_right(self, nums, i, j, target):
        if j == len(nums)-1 and nums[j] == target:
            return j

        if nums[i] == target and nums[j] > target and j-i==1:
            return i

        if j-i<=1:
            return -1

        mid = int((i + j) / 2)
        if nums[mid] <= target:
            return self.search_right(nums, mid, j, target)
        else:
            return self.search_right(nums, i, mid, target)

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums)==0:
            return [-1, -1]

        return [self.search_left(nums, 0, len(nums) - 1, target), self.search_right(nums, 0, len(nums)-1, target)]


if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    nums = [5]
    print(s.searchRange(nums, 5))
