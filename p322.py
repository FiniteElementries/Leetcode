from typing import List


class Solution:
    mem = {}

    def find_min_combination(self, coins, amount):
        if amount == 0:
            return [0]

        if amount < 0:
            return []

        if not amount in self.mem:
            candidiate = []

            for item in coins:
                arr = self.find_min_combination(coins, amount - item)
                if arr:
                    arr = [item] + arr
                    if not candidiate:
                        candidiate = arr
                    else:
                        if len(arr) < len(candidiate):
                            candidiate = arr
            self.mem[amount] = candidiate

        return self.mem[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.mem = {}
        return len(self.find_min_combination(coins, amount))-1


if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 11

    print(s.coinChange(coins, amount))
