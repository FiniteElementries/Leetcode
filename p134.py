from typing import List


class Solution:

    def explore(self, i, gas, cost):

        tank = 0
        for j in range(0, len(gas)):
            k = (i + j) % len(gas)
            tank += (gas[k] - cost[k])
            if tank < 0:
                return False, k + 1
        return True, i

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        i = 0

        while i < len(gas):
            res, j = self.explore(i, gas, cost)
            if res:
                return i
            if j <= i:
                return -1
            else:
                i = j

        return -1


if __name__ == "__main__":
    s = Solution()

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    # gas = [2, 3, 4]
    # cost = [3, 4, 3]

    print(s.canCompleteCircuit(gas, cost))
