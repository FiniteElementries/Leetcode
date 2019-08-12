from typing import List
import math

class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:

        i = math.inf
        j = math.inf

        for k in nums:
            if k < i:
                i = k
            elif k < j:
                j = k
            else:
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    nums = [2, 5, 3, 4, 5]
    nums = [2, 1, 5, 0, 3]

    print(s.increasingTriplet(nums))
