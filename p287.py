from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        while True:
            ind = nums[0]
            tmp = nums[ind]

            if ind == tmp:
                return ind

            nums[ind] = ind
            nums[0] = tmp



if __name__ == '__main__':
    s = Solution()

    nums = [1, 3, 4, 2, 2]

    # nums = [2, 2, 2, 2, 2]
    #
    # nums = [1, 4, 4, 2, 4]
    #
    # nums = [2, 1, 1, 1, 4]
    #
    # nums = [3, 1, 3, 4, 2]

    print(s.findDuplicate(nums))
