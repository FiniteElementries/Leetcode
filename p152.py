from typing import List


class Solution:

    def max_p(self, nums):
        if len(nums) == 1:
            return nums[0]
        p = 1
        first_neg = 1
        last_pos = 1

        for i, item in enumerate(nums):
            p *= item
            if p < 0 < first_neg:
                first_neg = p
            if p > 0:
                last_pos = p

        return max(p / first_neg, last_pos)

    def maxProduct(self, nums: List[int]) -> int:

        i = 0
        ret_val = nums[0]

        has_zero = False
        while i < len(nums):
            if nums[i] == 0:
                has_zero = True
                i += 1
                continue
            j = i + 1
            while j < len(nums):
                if nums[j] == 0:
                    has_zero = True
                    break
                j += 1
            p = self.max_p(nums[i:j])
            ret_val = max(p, ret_val)
            i = j + 1
        if has_zero:
            ret_val = max(0, ret_val)
        return int(ret_val)


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, -2, 4]

    nums = [0, 2]

    nums = [-2, -1, 0, -1, -3]

    print(s.maxProduct(nums))
