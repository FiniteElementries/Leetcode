"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums==[]):
            return []

        count = 1

        for i in range(0, len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[count]=nums[i+1]
                count+=1


        return count


if __name__=="__main__":

    nums = [1,1,2]

    solution = Solution()
    print(solution.removeDuplicates(nums))
    print(nums)