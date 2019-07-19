class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        for i in range(len(nums) - 3, -1, -1):
            orig = nums[i]
            nums[i] = max(nums[i + 1], nums[i + 2] + nums[i])
            if i+3 <= len(nums)-1:
                nums[i] = max(nums[i], nums[i + 3] + orig)

        return max(nums[0:2])


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3, 1]

    nums = [2, 7, 9, 3, 1]

    nums = [2, 1, 1, 2]
    print(s.rob(nums))
