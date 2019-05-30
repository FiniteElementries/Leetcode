import heapq
from typing import List


class Solution:

    def search_left(self, i, number, heights):
        """ search left boundary that are greater or equal to number """
        while heights[i] >= number:
            i = self.mem[i][0] - 1
            if i < 0:
                break
            self.marker[i] = 1
        if i>=0:
            self.marker[i] = 0
        return i + 1

    def search_right(self, i, number, heights):
        """ search left boundary that are greater or equal to number """

        while heights[i] >= number:
            i = self.mem[i][1] + 1
            if i >= len(heights):
                break
            self.marker[i] = 1
        if i < len(heights):
            self.marker[i] = 0
        return i - 1

    def search(self, i, heights):
        if self.marker[i] == 1:
            return

        if i > 0:
            left = self.search_left(i, heights[i], heights)
        else:
            left = 0

        if i < len(heights):
            right = self.search_right(i, heights[i], heights)
        else:
            right = len(heights) - 1

        self.mem[left] = [left, right]
        self.mem[right] = [left, right]

        area = (right - left + 1) * heights[i]
        if area > self.max_height:
            self.max_height = area

    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        heap = []
        self.mem = []
        self.map = {}
        self.marker = [0] * len(heights)
        self.max_height = heights[0]
        for i in range(0, len(heights)):
            item = heights[i]
            heap_val = -item
            if heap_val not in self.map:
                self.map[heap_val] = []
            self.map[heap_val].append(i)

            heapq.heappush(heap, -item)
            self.mem.append([i, i])

        while len(heap) > 0:
            item = heapq.heappop(heap)
            i = self.map[item][-1]
            del self.map[item][-1]
            self.search(i, heights)

        return self.max_height


if __name__ == "__main__":
    s = Solution()

    # heights = [2, 1, 5, 6, 2, 3]
    heights = [2]
    heights = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    print(s.largestRectangleArea(heights))
