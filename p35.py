from typing import List
from bisect import bisect_left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


if __name__ == '__main__':
    s = Solution()

    nums = [1, 2, 3, 5]

    target = 4

    print(s.searchInsert(nums, target))
