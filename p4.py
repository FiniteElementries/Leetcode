"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

# todo solve this problem
"""


class Median:
    def __init__(self, arr, left, right):
        self.arr = arr
        self.left = left
        self.right = right

        if left < 0 or right < 0 or left >= len(arr) or right >= len(arr):
            self.mid = None
            self.mid_left = None
            self.mid_right = None
            return

        if (right - left) % 2 == 1:
            i = (right + left) // 2
            j = i + 1
            self.mid = (arr[i] + arr[j]) / 2
            self.mid_left = i
            self.mid_right = j
        else:
            i = (right + left) // 2
            self.mid = arr[i]
            self.mid_left = i - 1
            self.mid_right = i + 1

    def squeezed(self):
        return self.mid_left == self.left and self.right == self.mid_right

    def get(self, i):
        return self.arr[i]


class Divde:

    def __init__(self, arr, left, right):
        self.arr = arr
        self.left = left
        self.right = right

    def less_count(self):
        if self.left == self.right:
            return self.left
        else:
            return self.left + 1

    def more_count(self):
        if self.left == self.right:
            return len(self.arr) - self.less_count() - 1
        else:
            return len(self.arr) - self.less_count()


# print(Divde([1,2,3,4], 2, 2).more_count())

class Solution:

    def findMedianSortedArrays(self, nums1, nums2):

        l1 = len(nums1)
        l2 = len(nums2)

        expect_cut = (l1 + l2) // 2

        cut1a = 0
        cut1b = cut1a + 1
        cut2a = 0
        cut2b = cut2a + 1

        div1 = Divde(nums1, cut1a, cut1b)
        div2 = Divde(nums2, cut2a, cut2b)

        less = div1.less_count() + div2.less_count()

        # make sure div1 and div2 cut half
        while (div1.less_count() + div2.less_count()) != expect_cut:
            if less > expect_cut:
                if nums2[cut2a] > nums1[cut1a]:
                    tmp = cut2a
                    cuta = tmp % 2
                    cutb = (tmp + 1) % 2
                    div2 = Divde(nums2, cuta, cutb)
                else:
                    tmp = cut1a
                    cuta = tmp % 2
                    cutb = (tmp + 1) % 2
                    div1 = Divde(nums1, cuta, cutb)
            else:
                if nums2[cut2a] < nums1[cut1a]:
                    tmp = (cut2b + l2)//2
                    cuta = tmp % 2
                    cutb = (tmp + 1) % 2
                    div2 = Divde(nums2, cuta, cutb)
                else:
                    tmp = (cut1b + l1) // 2
                    cuta = tmp % 2
                    cutb = (tmp + 1) % 2
                    div1 = Divde(nums1, cuta, cutb)


        # find median between div1 and div2
        print(div1.left, div1.right)
        print(div2.left, div2.right)
        print("here")


# nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# m = Median(nums1, 1, 4)
# print(m.mid, m.cut)
#
# m = Median(nums1, 1, 5)
# print(m.mid, m.cut)
#
# m = Median(nums1, 0, 0)
# print(m.mid, m.cut)
#
# m = Median(nums1, 8, 8)
# print(m.mid, m.cut)
#
# m = Median(nums1, 4, 4)
# print(m.mid, m.cut)
#
# m = Median(nums1, -1, -1)
# print(m.mid, m.cut)
#
# m = Median(nums1, 9, 9)
# print(m.mid, m.cut)

s = Solution()

nums1 = [1, 3]
nums2 = [2]

# # print(s.find_median(nums1, 0, 1))
# # print(s.find_median(nums2, 0, 0))
# # print(s.find_median(nums2, -1, 0))
# # print(s.find_median(nums1, 1, 1))
#
print(s.findMedianSortedArrays(nums1, nums2))
#
nums1 = [1, 2]
nums2 = [3, 4]
print(s.findMedianSortedArrays(nums1, nums2))
#
nums1 = []
nums2 = [1]
# print (s.findMedianSortedArrays(nums1, nums2))
# #
# #
nums1 = [3]
nums2 = [-2, -1]
# print(s.findMedianSortedArrays(nums1, nums2))

#
nums1 = [1, 2]
nums2 = [-1, 3]
# print (s.findMedianSortedArrays(nums1, nums2))
