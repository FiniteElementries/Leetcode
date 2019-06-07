from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxp = prices[0]
        minp = prices[0]

        max_profit = 0

        for i in range(0, len(prices)):
            if prices[i] < minp:
                max_profit = max(max_profit, maxp - minp)
                minp = prices[i]
                maxp = minp

            elif prices[i] > maxp:
                maxp = prices[i]
        max_profit = max(max_profit, maxp - minp)
        return max_profit
