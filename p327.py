from typing import List


class Solution:

    def count_sums(self, sums, lower, upper):
        if len(sums) == 0:
            return 0, sums
        if len(sums) == 1:
            if lower <= sums[0] <= upper:
                return 1, sums
            else:
                return 0, sums
        mid = int(len(sums) / 2)
        count = 0
        count1, left = self.count_sums(sums[0:mid], lower, upper)
        count2, right = self.count_sums(sums[mid:], lower, upper)

        count += (count1 + count2)

        i = 0
        j = 0
        while i < mid and j < len(right):
            while i < mid and right[j] - left[i] > upper:
                i += 1
            count += (len(left) - i)
            j += 1

        i = 0
        j = 0
        while i < mid and j < len(right):
            while i < mid and right[j] - left[i] >= lower:
                i += 1
            count -= (len(left) - i)
            j += 1

        # merge
        i = 0
        j = 0
        k = 0
        while i < len(left) or j < len(right):
            if j >= len(right):
                sums[k] = left[i]
                i += 1
                k += 1
            elif i >= len(left):
                sums[k] = right[j]
                j += 1
                k += 1
            else:
                if left[i] < right[j]:
                    sums[k] = left[i]
                    i += 1
                    k += 1
                else:
                    sums[k] = right[j]
                    j += 1
                    k += 1
        return count, sums

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if len(nums) == 0:
            return 0
        prefix_sums = [nums[0]]
        for item in nums[1:]:
            prefix_sums.append(prefix_sums[-1] + item)

        return self.count_sums(prefix_sums, lower, upper)[0]


if __name__ == '__main__':
    s = Solution()

    nums = [-2, 5, -1]
    lower = -2
    upper = 2

    # nums = [-3, 1, 2, -2, 2, -1]
    # lower = -3
    # upper = -1
    #
    # nums = [0]
    # lower = 0
    # upper = 0

    # nums = [2147483647, -2147483648, -1, 0]
    # lower = -1
    # upper = 0

    print(s.countRangeSum(nums, lower, upper))
