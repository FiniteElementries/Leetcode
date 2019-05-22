from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:

        positives = [x for x in nums if x > 0]

        ma = len(positives)

        if ma == 0:
            return 1

        arr = [0 for _ in range(ma + 1)]

        for item in positives:
            # if a integer is out of bound, just ignore it
            if item <= ma:
                arr[item] = 1

        for i in range(1, len(arr)):
            if arr[i] == 0:
                return i
        return max(positives) + 1


if __name__ == "__main__":
    s = Solution()

    # nums = [3, 4, -1, 1]
    # nums = [2189, 2147483647]
    # nums = [7, 8, 1, 3, 12]
    nums = [1, 2, 0]
    # nums = [2, 3, 4, 1, 2, 3, 6]

    print(s.firstMissingPositive(nums))
