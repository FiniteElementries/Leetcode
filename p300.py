from typing import List


class Solution:
    mem = {}

    def longest_at(self, i, nums):
        if i not in self.mem:
            longest = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    longest = max(longest, 1 + self.longest_at(j, nums))

            self.mem[i] = longest
        longest = self.mem[i]

        return longest

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.mem = {}

        m = 0

        for i in range(0, len(nums)):
            m = max(m, self.longest_at(i, nums))
        return m

if __name__ == '__main__':

    s = Solution()

    st = [10,9,2,5,3,7,101,18]

    print(s.lengthOfLIS(st))
