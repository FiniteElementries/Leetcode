from typing import List


class Solution:
    res = set()

    def find_combination(self, canadiates, start_ind, combination, current_sum, target):
        if current_sum == target:
            self.res.add(tuple(combination[:]))

        for i in range(start_ind, len(canadiates)):
            item = canadiates[i]
            new_sum = item + current_sum
            if new_sum > target:
                return
            else:
                combination.append(item)
                self.find_combination(canadiates, i+1, combination, new_sum, target)
                combination.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = set()
        self.find_combination(candidates, 0, [], 0, target)
        return [list(x) for x in self.res]
