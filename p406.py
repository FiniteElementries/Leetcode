import heapq
from typing import List


class Solution:

    def insert_person(self, arr, p):
        count = 0

        i = 0
        while i < len(arr):
            if arr[i][0] >= p[0]:
                count += 1
            if count >= p[1]:
                i += 1
                break
            i += 1
        arr.insert(i, p)

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        h = []
        arr = []
        for p in people:
            heapq.heappush(h, (-p[0], p))

        while len(h) > 0:
            p = heapq.heappop(h)[1]
            self.insert_person(arr, p)

        return arr


if __name__ == '__main__':
    s = Solution()

    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

    print(s.reconstructQueue(people))
