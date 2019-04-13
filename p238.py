class Solution:

    def productExceptSelf(self, nums):

        left_product = [0] * len(nums)
        left_product[0] = 1
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        right_product = [0] * len(nums)
        right_product[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        ret_val = [0] * len(nums)
        for i in range(0, len(nums)):
            ret_val[i] = left_product[i] * right_product[i]
        return ret_val


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
