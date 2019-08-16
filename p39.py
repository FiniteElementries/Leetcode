from typing import List


class Solution:
    res = []

    def find_combination(self, canadiates, start_ind, combination, current_sum, target):
        if current_sum == target:
            self.res.append(combination[:])

        for i in range(start_ind, len(canadiates)):
            item = canadiates[i]
            new_sum = item + current_sum
            if new_sum > target:
                return
            else:
                combination.append(item)
                self.find_combination(canadiates, i, combination, new_sum, target)
                combination.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        self.find_combination(candidates, 0, [], 0, target)
        return self.res
