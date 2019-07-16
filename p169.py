from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        c = Counter(nums)

        l = len(nums)/2

        for k, v in c.items():
            if v > l:
                return k
