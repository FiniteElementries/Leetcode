from typing import List

import heapq

class HeightHeap(object):

    def __init__(self, height, ind):
        self.height = 1.0/(height+0.001)
        self.ind = ind

    def __lt__(self, other):
        return self.height < other.height

class Solution:

    def calc_volume(self, i, j):
        min_level = min(self.height[i], self.height[j])
        vol = 0
        for m in range(i, j+1):
            if min_level > self.height[m]:
                vol += (min_level - self.height[m])
        return vol

    def scan_left(self, i, j):
        for m in range(j-1, i-1, -1):
            if self.has_water[m] == 1:
                for n in range(m, j):
                    self.has_water[n] = 1
                return self.calc_volume(m, j)
        return 0

    def scan_right(self, i, j):
        for m in range(i+1, j+1):
            if self.has_water[m] == 1:
                for n in range(i, m):
                    self.has_water[n] = 1
                return self.calc_volume(i, m)
        return 0


    def trap(self, height: List[int]) -> int:
        heap = []

        self.has_water = [0] * len(height)
        self.height = height

        for i in range(0, len(height)):
            heapq.heappush(heap, HeightHeap(height[i], i))

        vol = 0
        while len(heap)>0:
            h = heapq.heappop(heap)
            self.has_water[h.ind] = 1
            vol += self.scan_left(0, h.ind)
            vol += self.scan_right(h.ind, len(height)-1)

        return vol



if __name__ == "__main__":
    s = Solution()
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]

    height = [2, 0, 2]

    # height = [5, 4, 1, 2]

    print(s.trap(height))
