

class Solution:
    def singleNumber(self, nums) -> int:
        mininum = min(min(nums), 0)

        for i in range(len(nums)):
            nums[i] += (-mininum)

        maximum = max(nums) + 1

        arr = [0] * maximum

        for item in nums:
            arr[item] += 1

        for i in range(len(arr)):
            if arr[i]==1:
                return i + mininum


if __name__ == "__main__":

    s = Solution()
    print(s.singleNumber([2,2,-1]))