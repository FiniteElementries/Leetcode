import heapq
from typing import List


class Building(object):

    def __init__(self, l, r, h):
        self.l = l
        self.r = r
        self.h = h

    def __lt__(self, other):
        return self.h > other.h


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # create heap by height, highest is at top of heap
        max_r = 0
        bs = []
        for b in buildings:
            if b[1] > max_r:
                max_r = b[1]
            bs.append(Building(b[0], b[1], b[2]))
        bs.append(Building(-1, max_r + 1, 0))
        heapq.heapify(bs)

        # pop heap one by one to create contour
        countour_buildings = []
        while bs:
            new_bs = [heapq.heappop(bs)]

            for c_building in countour_buildings:
                l = len(new_bs)

                # check new height overlapping with existing contour
                # and break new height down into fragments where non overlapping
                for i in range(l):
                    new_b = new_bs[i]
                    if new_b:
                        if c_building.l <= new_b.l < new_b.r <= c_building.r:
                            new_bs[i] = None
                            break
                        elif c_building.l <= new_b.l < c_building.r <= new_b.r:
                            new_b.l = c_building.r
                        elif new_b.l <= c_building.l < new_b.r <= c_building.r:
                            new_b.r = c_building.l
                        elif new_b.l < c_building.l < c_building.r < new_b.r:
                            new_bs.append(Building(c_building.r, new_b.r, new_b.h))
                            new_b.r = c_building.l

            for item in new_bs:
                if item:
                    countour_buildings.append(item)

        # get points
        t = [[x.l, x.h] for x in countour_buildings]

        contours = sorted(t, key=lambda x: x[0])[1:]
        cleaned = []
        for item in contours:  # clean same height
            if cleaned:
                if cleaned[-1][1] == item[1]:
                    continue
            cleaned.append(item)

        return cleaned


if __name__ == '__main__':
    s = Solution()

    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

    # buildings = [[0, 2147483647, 2147483647]]

    buildings = [[0, 1, 3]]

    buildings = [[0, 2, 3], [2, 5, 3]]

    print(s.getSkyline(buildings))
