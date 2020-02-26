from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        ts = []
        for i in range(0, len(nums)):
            ts.append((nums[i], i))
        ts.sort()

        for i in range(0, len(ts)):
            item, ind = ts[i]

            for j in range(i + 1, len(ts)):
                item2, ind2 = ts[j]
                if abs(ind2 - ind) > k and item2 - item > t:
                    break
                if abs(ind2 - ind) <= k and item2 - item <= t:
                    return True
        return False

if __name__ == '__main__':
    s = Solution()

    nums = [1, 2, 3, 1]
    k = 3
    t = 0

    # nums = [1, 0, 1, 1]
    k = 1
    t = 2

    # nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3

    nums = [0, 10, 22, 15, 0, 5, 22, 12, 1, 5]
    k = 3
    t = 3

    nums = [1,3,6,2]
    k = 1
    t = 2
    print(s.containsNearbyAlmostDuplicate(nums, k, t))
