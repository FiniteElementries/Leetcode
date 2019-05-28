from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:

        j = 0
        for i in range(0, len(nums)):

            steps = nums[i]

            if j < i:
                return False

            steps = steps - (j - i)
            if steps > 0:
                j += steps
                if j >= len(nums) - 1:
                    return True

        return True


if __name__ == "__main__":
    s = Solution()

    nums = [2, 3, 1, 1, 4]

    nums = [3, 2, 1, 0, 4]
    nums = [0]
    print(s.canJump(nums))
