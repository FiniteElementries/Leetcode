from typing import List
from collections import Counter


class Solution:

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        AB = []
        for item1 in A:
            for item2 in B:
                AB.append(item1 + item2)
        cAB = Counter(AB)

        CD = []
        for item1 in C:
            for item2 in D:
                CD.append(item1 + item2)
        cCD = Counter(CD)

        total = 0

        for k, v in cAB.items():
            if -k in cCD:
                total += v * cCD[-k]

        return total


if __name__ == '__main__':
    s = Solution()

    A = [-1, -1]
    B = [-1, 1]
    C = [-1, 1]
    D = [1, -1]

    print(s.fourSumCount(A, B, C, D))
