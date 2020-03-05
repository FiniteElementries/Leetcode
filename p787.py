from typing import List
import math
from queue import Queue
from collections import defaultdict


class Solution:
    min_distance = math.inf

    def dfs(self, node, level, distance, graph):
        if level > self.K+1:
            return
        if distance > self.min_distance:
            return
        if node == self.dst:
            if distance < self.min_distance:
                self.min_distance = distance
            return

        for k, v in graph[node].items():
            self.dfs(k, level + 1, distance + v, graph)

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        self.dst = dst
        self.min_distance = math.inf
        self.K = K

        graph = defaultdict(dict)
        for flight in flights:
            graph[flight[0]][flight[1]] = flight[2]

        self.dfs(src, 0, 0, graph)

        if self.min_distance != math.inf:
            return self.min_distance
        else:
            return -1


if __name__ == '__main__':
    s = Solution()

    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    # n = 3
    # edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # src = 0
    # dst = 2
    # k = 0

    # n = 4
    # edges = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
    # src = 0
    # dst = 3
    # k = 1

    # n = 5
    # edges = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    # src = 0
    # dst = 2
    # k = 2

    print(s.findCheapestPrice(n, edges, src, dst, k))
