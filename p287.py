from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for item in nums:
            if item not in s:
                s.add(item)
            else:
                return item


if __name__ == '__main__':
    s = Solution()

    nums = [1, 3, 4, 2, 2]

    nums = [2, 2, 2, 2, 2]

    nums = [1, 4, 4, 2, 4]

    nums = [2, 1, 1, 1, 4]

    nums = [3, 1, 3, 4, 2]

    print(s.findDuplicate(nums))
