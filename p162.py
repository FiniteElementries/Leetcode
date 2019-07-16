class Solution(object):

    def findPeak(self, nums, l, r):
        if r - l <= 2:
            return None

        mid = (r + l) // 2
        ll = nums[mid - 1]
        rr = nums[mid + 1]
        m = nums[mid]

        if ll < m and m > rr:
            return mid

        res = None
        if ll > m:
            res = self.findPeak(nums, l, mid + 1)

        if res:
            return res

        if rr > m:
            res = self.findPeak(nums, mid, r)

        if res:
            return res

        return None

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        ret = self.findPeak(nums, 0, len(nums))

        return ret


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3, 1]

    # nums = [-26, 2, 9, 30, 25, 10, -60, 95, -91, 91, -43, 46, -17, 27, 21, -39, 66, 74, -21, -86, 39, -66, -64, -49, 40,
    #         34, 69, -97, -24, 42, 18, -15, 80, 76, -78, 92, -44, 83, 88, 67, -70, 73, -79, 90, 41, -77, -61, 28, 19, 45]

    # nums = [1, 2, 1, 3, 5, 6, 4]
    nums = [3, 2, 1]
    print(s.findPeakElement(nums))
