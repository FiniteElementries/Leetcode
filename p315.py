from typing import List

import bisect


class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = []
        aux = []
        for i in range(len(nums) - 1, -1, -1):
            loc = bisect.bisect_left(aux, nums[i])
            aux.insert(loc, nums[i])
            res.append(loc)
        res.reverse()

        return res


if __name__ == '__main__':
    s = Solution()

    nums = [5, 2, 6, 1]

    # nums = [0, 1, 2]
    #
    # # nums = [2, 0, 1]
    #
    # nums = [84, 66, 65, 36, 100, 41]
    #
    # res = [4, 3, 2, 0, 1, 0]
    print(s.countSmaller(nums))
