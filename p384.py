
from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.orig_nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.orig_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = self.orig_nums[:]

        for i in range(0, len(nums)):
            ind = randint(i, len(nums)-1)

            tmp = nums[ind]
            nums[ind] = nums[i]
            nums[i] = tmp
        return nums
