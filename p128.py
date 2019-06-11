from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = {}

        for item in nums:
            visited[item] = 0

        max_count = 0
        for item in nums:
            count = 0
            l = item
            r = item
            while visited[l] == 0 or visited[r] == 0:
                if visited[l] == 0:
                    visited[l] = 1
                    count += 1
                if l-1 in visited:
                    l -= 1

                if visited[r] == 0:
                    visited[r] = 1
                    count += 1
                if r+1 in visited:
                    r += 1
            max_count = max(max_count, count)
        return max_count


if __name__ == "__main__":
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    nums=[-1,1,0]

    print(s.longestConsecutive(nums))
