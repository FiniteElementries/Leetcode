import heapq


class MyStr(object):

    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        for i in range(0, max(len(self.val), len(other.val))):
            if i > len(self.val) - 1 or i > len(other.val) - 1:
                return self.val + other.val < other.val + self.val

            self_val = self.val[i]
            other_val = other.val[i]
            if self_val != other_val:
                return self_val < other_val


class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        strs = []

        for item in nums:
            st = str(item)
            strs.append(MyStr(st))

        heapq.heapify(strs)

        ret_val = ""

        while len(strs) > 0:
            item = heapq.heappop(strs)
            ret_val = item.val + ret_val

        for i in range(len(ret_val)):
            if ret_val[i] != '0':
                return ret_val[i:]

        return '0'


if __name__ == "__main__":
    s = Solution()

    nums = [10, 2]
    nums = [3, 30, 34, 5, 9]
    # nums = [0, 0]
    nums = [824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]
    # nums = [121,12]
    print(s.largestNumber(nums))
