"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline/
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):

        max_row = [max(item) for item in grid]
        max_col = [max(item) for item in zip(*grid)]

        room = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                room_left = min(max_row[i], max_col[j]) - grid[i][j]
                room += room_left
        return room

s = Solution()

gridNew = [ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
print(s.maxIncreaseKeepingSkyline(gridNew))


