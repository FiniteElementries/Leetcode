import heapq
from typing import List


class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ret_val = [-1] * len(nums)

        h = []

        for _ in range(2):
            for i in range(0, len(nums)):
                while len(h) > 0 and nums[i] > h[0][0]:
                    item = heapq.heappop(h)
                    ret_val[item[1]] = nums[i]
                heapq.heappush(h, (nums[i], i))
        return ret_val


if __name__ == '__main__':
    s = Solution()

    nums = [1, 2, 1]
    print(s.nextGreaterElements(nums))
