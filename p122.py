from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        state = 'empty'
        entry_price = 0
        current_price = prices[0]
        total_profit = 0

        for i in range(1, len(prices)):
            future_price = prices[i]

            if state == 'empty':
                if future_price > current_price:
                    entry_price = current_price
                    state = 'hold'
            else:
                if future_price < current_price:
                    profit = current_price - entry_price
                    total_profit += profit
                    entry_price = 0
                    state = 'empty'

            current_price = future_price
        if state == 'hold':
            profit = current_price - entry_price
            total_profit += profit
        return total_profit
