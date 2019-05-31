from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i1 = m - 1
        i2 = n - 1
        k = len(nums1) - 1
        while i1 >= 0 or i2 >= 0:
            if i1 < 0:
                nums1[k] = nums2[i2]
                k -= 1
                i2 -= 1
            elif i2 < 0:
                # i2 is empty, need to shift all num1 to ends
                nums1[k] = nums1[i1]
                k -= 1
                i1 -= 1
            else:
                if nums2[i2] > nums1[i1]:
                    nums1[k] = nums2[i2]
                    k -= 1
                    i2 -= 1
                else:
                    nums1[k] = nums1[i1]
                    k -= 1
                    i1 -= 1

        if k > 0:
            # shift all item to beginning
            for i in range(k, len(nums1)):
                nums1[i - k] = nums1[k]

            # set ending values to 0
            for i in range(m + n, len(nums1)):
                nums1[i] = 0


if __name__ == "__main__":
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    s.merge(nums1, m, nums2, n)

    print(nums1)
